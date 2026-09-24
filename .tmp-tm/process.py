import json, math

with open('.tmp-tm/markets.json') as f:
    markets = json.load(f)
with open('.tmp-tm/trending.json') as f:
    trending_raw = json.load(f)

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','ethena-usde','usdt0'}
def is_stable(c):
    sym = (c.get('symbol') or '').upper()
    name = (c.get('name') or '').lower()
    cid = (c.get('id') or '').lower()
    if cid in STABLE_IDS:
        return True
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'):
        return True
    if 'stablecoin' in name:
        return True
    return False

filtered = []
for c in markets:
    if c.get('total_volume') is None or c.get('current_price') is None:
        continue
    if is_stable(c):
        continue
    if c['total_volume'] < 1_000_000:
        continue
    filtered.append(c)

print(f"Total fetched: {len(markets)}, after filter: {len(filtered)}")

# dedupe wrapped tokens - keep highest mcap rep among known wrapped dupes
WRAPPED_GROUPS = [
    {'wrapped-bitcoin','bitcoin'},
    {'weth','ethereum'},
    {'staked-ether','ethereum'},
]
# skip complex wrapped dedupe for now, not many typically appear in winners/losers top10 anyway

filtered_sorted_desc = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h_in_currency') or c.get('price_change_percentage_24h') or -9999, reverse=True)
def chg24(c):
    return c.get('price_change_percentage_24h_in_currency', c.get('price_change_percentage_24h'))

filtered_valid = [c for c in filtered if chg24(c) is not None]
winners = sorted(filtered_valid, key=chg24, reverse=True)[:10]
losers = sorted(filtered_valid, key=chg24)[:10]

trending_coins = trending_raw.get('coins', [])[:7]

# Market pulse: top100 by mcap (post-filter) - use full markets list top100 by market cap rank, excluding stables
top100 = [c for c in markets if not is_stable(c) and c.get('market_cap_rank') and c['market_cap_rank'] <= 100 and chg24(c) is not None]
pos = sum(1 for c in top100 if chg24(c) > 0)
top50 = sorted(top100, key=lambda c: c['market_cap_rank'])[:50]
med50 = sorted([chg24(c) for c in top50])
median_50 = med50[len(med50)//2] if med50 else 0

print(f"Top100 tracked: {len(top100)}, positive: {pos}, median top50 24h%: {median_50:.2f}")

trending_ids = set(t['item']['id'] for t in trending_coins)

def fmt_price(p):
    if p is None:
        return "n/a"
    if p < 0.01:
        return f"${p:.6f}"
    if p < 1:
        return f"${p:.4f}"
    return f"${p:,.2f}" if p >= 1000 else f"${p:.4g}" if p<1000 else f"${p:,.2f}"

def fmt_usd(v):
    if v is None:
        return "n/a"
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    if v >= 1e6:
        return f"${v/1e6:.0f}M"
    if v >= 1e3:
        return f"${v/1e3:.0f}K"
    return f"${v:.0f}"

def tags_for(c):
    tags = []
    chg = chg24(c)
    chg7d = c.get('price_change_percentage_7d_in_currency')
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 9999
    vol = c.get('total_volume') or 0
    in_trend = c['id'] in trending_ids
    is_winner = chg is not None and chg > 0
    is_loser = chg is not None and chg < 0
    if in_trend and is_winner:
        tags.append('TRENDING+UP')
    if in_trend and is_loser:
        tags.append('TRENDING+DOWN')
    if chg7d is not None:
        if chg is not None and chg > 15 and chg7d > 25:
            tags.append('BREAKOUT')
        if chg is not None and chg > 20 and chg7d < 0:
            tags.append('FADE')
    if chg is not None and chg < -10 and mcap>0 and (vol/mcap) > 0.25:
        tags.append('CAPITULATION')
    if chg is not None and rank > 150 and chg > 30:
        tags.append('PUMP-RISK')
    if mcap and mcap < 50_000_000:
        tags.append('MICROCAP')
    if rank <= 20:
        tags.append('MAJOR')
    return tags[:2]

print("\n=== WINNERS ===")
for c in winners:
    t = tags_for(c)
    print(f"{c['symbol'].upper()} ({c['name']}) rank#{c.get('market_cap_rank')} price={fmt_price(c['current_price'])} 24h={chg24(c):.1f}% 7d={c.get('price_change_percentage_7d_in_currency')} 1h={c.get('price_change_percentage_1h_in_currency')} vol={fmt_usd(c.get('total_volume'))} mcap={fmt_usd(c.get('market_cap'))} tags={t}")

print("\n=== LOSERS ===")
for c in losers:
    t = tags_for(c)
    print(f"{c['symbol'].upper()} ({c['name']}) rank#{c.get('market_cap_rank')} price={fmt_price(c['current_price'])} 24h={chg24(c):.1f}% 7d={c.get('price_change_percentage_7d_in_currency')} 1h={c.get('price_change_percentage_1h_in_currency')} vol={fmt_usd(c.get('total_volume'))} mcap={fmt_usd(c.get('market_cap'))} tags={t}")

print("\n=== TRENDING ===")
for t in trending_coins:
    item = t['item']
    # find matching market entry for tags/chg
    match = next((c for c in markets if c['id']==item['id']), None)
    chg = chg24(match) if match else item.get('data',{}).get('price_change_percentage_24h',{}).get('usd')
    price = item.get('data',{}).get('price')
    tg = tags_for(match) if match else []
    print(f"{item['symbol'].upper()} ({item['name']}) rank#{item.get('market_cap_rank')} chg24={chg} price={price} tags={tg}")

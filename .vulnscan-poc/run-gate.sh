#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export VULN_POC_DIR="$(pwd)/.vulnscan-poc"
export VULN_POC_RESULTS_DIR="$(pwd)/.vulnscan-poc-results"
export VULN_POC_EXEC_LOG="$(pwd)/.vulnscan-poc-executions.log"
./scripts/vuln-poc-gate.sh command --finding .vulnscan-poc/finding-1.json --repo .vulnwork-cli-anything --script .vulnscan-poc/finding-1.sh

#!/bin/bash

set -euo pipefail

dnf -y builddep rust-afterburn.spec
spectool -g rust-afterburn.spec

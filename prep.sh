#!/bin/bash

set -euo pipefail

dnf -y install rpmdevtools rpm-build dnf-plugins-core
dnf -y builddep rust-afterburn.spec
spectool -g rust-afterburn.spec

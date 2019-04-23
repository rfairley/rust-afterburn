#!/bin/bash

set -euo pipefail

rpmbuild -ba \
    --define "_sourcedir $PWD" \
    --define "_specdir $PWD" \
    --define "_builddir $PWD/.build" \
    --define "_srcrpmdir $PWD/rpms" \
    --define "_rpmdir $PWD/rpms" \
    --define "_buildrootdir $PWD/.buildroot" rust-afterburn.spec
rm -rf "$PWD/.build"

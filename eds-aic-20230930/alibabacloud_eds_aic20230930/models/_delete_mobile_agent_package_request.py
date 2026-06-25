# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteMobileAgentPackageRequest(DaraModel):
    def __init__(
        self,
        package_ids: List[str] = None,
    ):
        # The list of packages.
        self.package_ids = package_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        return self


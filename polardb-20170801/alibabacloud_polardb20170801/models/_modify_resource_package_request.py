# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyResourcePackageRequest(DaraModel):
    def __init__(
        self,
        auto_quota: bool = None,
        resource_package_id: str = None,
    ):
        self.auto_quota = auto_quota
        # This parameter is required.
        self.resource_package_id = resource_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_quota is not None:
            result['AutoQuota'] = self.auto_quota

        if self.resource_package_id is not None:
            result['ResourcePackageId'] = self.resource_package_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoQuota') is not None:
            self.auto_quota = m.get('AutoQuota')

        if m.get('ResourcePackageId') is not None:
            self.resource_package_id = m.get('ResourcePackageId')

        return self


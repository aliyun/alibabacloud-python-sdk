# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackAppCodeSnapshotRequest(DaraModel):
    def __init__(
        self,
        site_id: str = None,
        target_logical_number: int = None,
    ):
        self.site_id = site_id
        self.target_logical_number = target_logical_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.target_logical_number is not None:
            result['TargetLogicalNumber'] = self.target_logical_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TargetLogicalNumber') is not None:
            self.target_logical_number = m.get('TargetLogicalNumber')

        return self


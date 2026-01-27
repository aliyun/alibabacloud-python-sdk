# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostInfoByDbsInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        region_code: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        return self


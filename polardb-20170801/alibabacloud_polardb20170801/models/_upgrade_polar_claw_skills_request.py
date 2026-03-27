# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradePolarClawSkillsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        region_id: str = None,
        upgrade_method: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.application_type = application_type
        self.region_id = region_id
        self.upgrade_method = upgrade_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.upgrade_method is not None:
            result['UpgradeMethod'] = self.upgrade_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpgradeMethod') is not None:
            self.upgrade_method = m.get('UpgradeMethod')

        return self


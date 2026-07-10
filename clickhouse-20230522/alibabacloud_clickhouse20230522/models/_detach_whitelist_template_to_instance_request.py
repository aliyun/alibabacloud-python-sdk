# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachWhitelistTemplateToInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        template_id: str = None,
    ):
        # The IDs of the ClickHouse instances, separated by commas. You can specify up to 20 IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The whitelist template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


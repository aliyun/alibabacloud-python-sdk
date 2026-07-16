# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        config_value: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        # The configuration item to modify. For more information, see [Compute layer variables](https://help.aliyun.com/document_detail/316576.html).
        # 
        # This parameter is required.
        self.config_name = config_name
        # If configName is set to ENABLE_CONSISTENT_REPLICA_READ, the valid values are "true" and "false".
        # 
        # This parameter is required.
        self.config_value = config_value
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


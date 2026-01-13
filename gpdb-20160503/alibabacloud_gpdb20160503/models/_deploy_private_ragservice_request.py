# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployPrivateRAGServiceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The vSwitch ID.
        # 
        # >   The zone where the **vSwitch** resides must be the same as the zone that is specified by **ZoneId**.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The zone ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the available regions and zones.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


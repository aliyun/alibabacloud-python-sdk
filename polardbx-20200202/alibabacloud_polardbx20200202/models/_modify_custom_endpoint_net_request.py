# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomEndpointNetRequest(DaraModel):
    def __init__(
        self,
        conn_prefix: str = None,
        custom_endpoint_id: str = None,
        dbinstance_name: str = None,
        port: int = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.conn_prefix = conn_prefix
        # This parameter is required.
        self.custom_endpoint_id = custom_endpoint_id
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.port = port
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_prefix is not None:
            result['ConnPrefix'] = self.conn_prefix

        if self.custom_endpoint_id is not None:
            result['CustomEndpointId'] = self.custom_endpoint_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnPrefix') is not None:
            self.conn_prefix = m.get('ConnPrefix')

        if m.get('CustomEndpointId') is not None:
            self.custom_endpoint_id = m.get('CustomEndpointId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self


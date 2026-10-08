# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDBProxyEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_connect_string_net_type: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_engine_type: str = None,
        region_id: str = None,
    ):
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the database proxy endpoint to delete. Valid values:
        # * **Public**: Internet
        # * **VPC**: internal network (VPC)
        # * **Classic**: internal network (classic network)
        # 
        # Default value: **Classic**.
        # 
        # > - You cannot delete the internal endpoint that is created by default.
        # > - ApsaraDB RDS for PostgreSQL supports only **Public** and **VPC**.
        # 
        # This parameter is required.
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type
        # The ID of the database proxy endpoint. You can call DescribeDBProxyEndpoint to query the ID.
        # 
        # This parameter is required.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A deprecated parameter. You do not need to configure this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The region ID. You can call DescribeRegions to query the available regions.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_connect_string_net_type is not None:
            result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyConnectStringNetType') is not None:
            self.dbproxy_connect_string_net_type = m.get('DBProxyConnectStringNetType')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBProxyEndpointRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_connect_string: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_engine_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The proxy endpoint that you want to query. You can call the DescribeDBProxy interface to query the proxy endpoint.
        self.dbproxy_connect_string = dbproxy_connect_string
        # The name of the proxy terminal. You can call the DescribeDBProxy interface to query the name of the proxy terminal.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A reserved parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_connect_string is not None:
            result['DBProxyConnectString'] = self.dbproxy_connect_string

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyConnectString') is not None:
            self.dbproxy_connect_string = m.get('DBProxyConnectString')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self


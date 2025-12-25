# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBProxyEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_connect_string_net_type: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_new_connect_string: str = None,
        dbproxy_new_connect_string_port: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the database proxy endpoint. Valid values:
        # 
        # *   **Public**
        # *   **VPC** (default)
        # 
        # >  If the RDS instance runs MySQL, this parameter is required.
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type
        # The ID of the database proxy endpoint. You can call the DescribeDBProxyEndpoint operation to query the ID of the database proxy endpoint.
        # 
        # This parameter is required.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A deprecated parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The prefix of the new database proxy endpoint. A custom value is supported.
        # 
        # >  You must specify at least one of the **DBProxyNewConnectString** and **DBProxyNewConnectStringPort** parameters.
        self.dbproxy_new_connect_string = dbproxy_new_connect_string
        # The port number that is associated with the database proxy endpoint. A custom value is supported.
        # 
        # >  You must specify at least one of the **DBProxyNewConnectString** and **DBProxyNewConnectStringPort** parameters.
        self.dbproxy_new_connect_string_port = dbproxy_new_connect_string_port
        self.owner_id = owner_id
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

        if self.dbproxy_connect_string_net_type is not None:
            result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_new_connect_string is not None:
            result['DBProxyNewConnectString'] = self.dbproxy_new_connect_string

        if self.dbproxy_new_connect_string_port is not None:
            result['DBProxyNewConnectStringPort'] = self.dbproxy_new_connect_string_port

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('DBProxyNewConnectString') is not None:
            self.dbproxy_new_connect_string = m.get('DBProxyNewConnectString')

        if m.get('DBProxyNewConnectStringPort') is not None:
            self.dbproxy_new_connect_string_port = m.get('DBProxyNewConnectStringPort')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self


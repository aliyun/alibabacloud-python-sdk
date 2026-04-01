# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDbProxyInstanceSslRequest(DaraModel):
    def __init__(
        self,
        dbproxy_engine_type: str = None,
        db_instance_id: str = None,
        db_proxy_connect_string: str = None,
        db_proxy_endpoint_id: str = None,
        db_proxy_ssl_enabled: str = None,
        region_id: str = None,
    ):
        # A reserved parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The dedicated proxy endpoint of the instance.
        # 
        # This parameter is required.
        self.db_proxy_connect_string = db_proxy_connect_string
        # The ID of the proxy endpoint. You can call the DescribeDBProxyEndpoint operation to query the ID of the proxy endpoint.
        # 
        # This parameter is required.
        self.db_proxy_endpoint_id = db_proxy_endpoint_id
        # The SSL configuration setting that you want to apply on the instance. Valid values:
        # 
        # *   0: disables SSL encryption.
        # *   1: enables SSL encryption or modifies the endpoint that requires SSL encryption.
        # *   2: updates the validity period of the SSL certificate.
        # 
        # > This setting causes your instance to restart. Proceed with caution.
        # 
        # This parameter is required.
        self.db_proxy_ssl_enabled = db_proxy_ssl_enabled
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_proxy_connect_string is not None:
            result['DbProxyConnectString'] = self.db_proxy_connect_string

        if self.db_proxy_endpoint_id is not None:
            result['DbProxyEndpointId'] = self.db_proxy_endpoint_id

        if self.db_proxy_ssl_enabled is not None:
            result['DbProxySslEnabled'] = self.db_proxy_ssl_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbProxyConnectString') is not None:
            self.db_proxy_connect_string = m.get('DbProxyConnectString')

        if m.get('DbProxyEndpointId') is not None:
            self.db_proxy_endpoint_id = m.get('DbProxyEndpointId')

        if m.get('DbProxySslEnabled') is not None:
            self.db_proxy_ssl_enabled = m.get('DbProxySslEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSslVpnClientCertResponseBody(DaraModel):
    def __init__(
        self,
        ca_cert: str = None,
        client_cert: str = None,
        client_config: str = None,
        client_key: str = None,
        create_time: int = None,
        end_time: int = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        ssl_vpn_client_cert_id: str = None,
        ssl_vpn_server_id: str = None,
        status: str = None,
    ):
        # The CA certificate.
        self.ca_cert = ca_cert
        # The client certificate.
        self.client_cert = client_cert
        # The client configuration.
        self.client_config = client_config
        # The client key.
        self.client_key = client_key
        # The timestamp that indicates when the SSL client certificate was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The timestamp that indicates when the SSL client certificate expires. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The name of the SSL client certificate.
        self.name = name
        # The ID of the region where the SSL client certificate is created.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the SSL client certificate belongs.
        # 
        # The SSL client certificate and the SSL server associated with the SSL client certificate belong to the same resource group. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The ID of the SSL client certificate.
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        # The ID of the SSL server.
        self.ssl_vpn_server_id = ssl_vpn_server_id
        # The status of the SSL client certificate. Valid values:
        # 
        # *   **expiring-soon**
        # *   **normal**
        # *   **expired**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert

        if self.client_cert is not None:
            result['ClientCert'] = self.client_cert

        if self.client_config is not None:
            result['ClientConfig'] = self.client_config

        if self.client_key is not None:
            result['ClientKey'] = self.client_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.ssl_vpn_client_cert_id is not None:
            result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id

        if self.ssl_vpn_server_id is not None:
            result['SslVpnServerId'] = self.ssl_vpn_server_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')

        if m.get('ClientCert') is not None:
            self.client_cert = m.get('ClientCert')

        if m.get('ClientConfig') is not None:
            self.client_config = m.get('ClientConfig')

        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SslVpnClientCertId') is not None:
            self.ssl_vpn_client_cert_id = m.get('SslVpnClientCertId')

        if m.get('SslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('SslVpnServerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


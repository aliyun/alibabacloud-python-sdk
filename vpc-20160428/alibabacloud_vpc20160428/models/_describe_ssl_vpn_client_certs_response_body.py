# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeSslVpnClientCertsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        ssl_vpn_client_cert_keys: main_models.DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeys = None,
        total_count: int = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the SSL client certificates.
        self.ssl_vpn_client_cert_keys = ssl_vpn_client_cert_keys
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ssl_vpn_client_cert_keys:
            self.ssl_vpn_client_cert_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ssl_vpn_client_cert_keys is not None:
            result['SslVpnClientCertKeys'] = self.ssl_vpn_client_cert_keys.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SslVpnClientCertKeys') is not None:
            temp_model = main_models.DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeys()
            self.ssl_vpn_client_cert_keys = temp_model.from_map(m.get('SslVpnClientCertKeys'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeys(DaraModel):
    def __init__(
        self,
        ssl_vpn_client_cert_key: List[main_models.DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeysSslVpnClientCertKey] = None,
    ):
        self.ssl_vpn_client_cert_key = ssl_vpn_client_cert_key

    def validate(self):
        if self.ssl_vpn_client_cert_key:
            for v1 in self.ssl_vpn_client_cert_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SslVpnClientCertKey'] = []
        if self.ssl_vpn_client_cert_key is not None:
            for k1 in self.ssl_vpn_client_cert_key:
                result['SslVpnClientCertKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ssl_vpn_client_cert_key = []
        if m.get('SslVpnClientCertKey') is not None:
            for k1 in m.get('SslVpnClientCertKey'):
                temp_model = main_models.DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeysSslVpnClientCertKey()
                self.ssl_vpn_client_cert_key.append(temp_model.from_map(k1))

        return self

class DescribeSslVpnClientCertsResponseBodySslVpnClientCertKeysSslVpnClientCertKey(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: int = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        ssl_vpn_client_cert_id: str = None,
        ssl_vpn_server_id: str = None,
        status: str = None,
    ):
        # The timestamp generated when the SSL client certificate was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The timestamp generated when the SSL client certificate expires. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The name of the SSL client certificate.
        self.name = name
        # The region ID of the SSL client certificate.
        self.region_id = region_id
        # The ID of the resource group to which the SSL client certificate belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The ID of the SSL client certificate.
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        # The ID of the SSL server.
        self.ssl_vpn_server_id = ssl_vpn_server_id
        # The status of the SSL client certificate. Valid values:
        # 
        # *   **expiring-soon**: The certificate expires in one week.
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SslVpnClientCertId') is not None:
            self.ssl_vpn_client_cert_id = m.get('SslVpnClientCertId')

        if m.get('SslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('SslVpnServerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpnSslServerLogsRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        minute_period: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ssl_vpn_client_cert_id: str = None,
        to: int = None,
        vpn_ssl_server_id: str = None,
    ):
        # The beginning of the time range to query. The value must be a unix timestamp. For example, 1600738962 specifies 09:42:42 (UTC+8) on September 22, 2020.
        # 
        # >  If you specify **From**, you must also specify **To** or **MinutePeriod**.
        self.from_ = from_
        # The interval at which log data is queried. Unit: minutes.
        # 
        # >  If both **From** and **To** are not specified, you must specify **MinutePeriod**.
        self.minute_period = minute_period
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the SSL server is created. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SSL client certificate.
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        # The end of the time range to query. The value must be a unix timestamp. For example, 1600738962 specifies 09:42:42 (UTC+8) on September 22, 2020.
        # 
        # >  If you specify **To**, you must also specify **From** or **MinutePeriod**.
        self.to = to
        # The ID of the SSL server.
        # 
        # This parameter is required.
        self.vpn_ssl_server_id = vpn_ssl_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.minute_period is not None:
            result['MinutePeriod'] = self.minute_period

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ssl_vpn_client_cert_id is not None:
            result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id

        if self.to is not None:
            result['To'] = self.to

        if self.vpn_ssl_server_id is not None:
            result['VpnSslServerId'] = self.vpn_ssl_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('MinutePeriod') is not None:
            self.minute_period = m.get('MinutePeriod')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SslVpnClientCertId') is not None:
            self.ssl_vpn_client_cert_id = m.get('SslVpnClientCertId')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('VpnSslServerId') is not None:
            self.vpn_ssl_server_id = m.get('VpnSslServerId')

        return self


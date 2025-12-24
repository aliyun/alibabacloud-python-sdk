# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDevicesRequest(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        client_type: str = None,
        device_id: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        user_type: str = None,
    ):
        # The address of the Active Directory (AD) office network.
        self.ad_domain = ad_domain
        # The type of the client.
        # 
        # Valid values:
        # 
        # *   1: hardware client.
        # *   2: software client.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The ID of the device. The serial number (SN) of the hardware client or the UUID of the software client.
        self.device_id = device_id
        # The ID of the convenient office network.
        self.directory_id = directory_id
        # The ID of the bound user.
        self.end_user_id = end_user_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        self.region = region
        # The account type of the user.
        # 
        # Valid values:
        # 
        # *   AD: enterprise AD account.
        # *   SIMPLE: convenience account
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self


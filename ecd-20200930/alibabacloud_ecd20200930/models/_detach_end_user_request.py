# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachEndUserRequest(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        client_type: str = None,
        device_id: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        region: str = None,
    ):
        # The address of the Active Directory (AD) office network.
        self.ad_domain = ad_domain
        # The type of the client.
        # 
        # Valid values:
        # 
        # *   1: hardware client.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The serial number (SN) of the hardware client.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The ID of the convenient office network.
        self.directory_id = directory_id
        # The ID of the user that you want to unbind from the hardware client.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        self.region = region

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

        if self.region is not None:
            result['Region'] = self.region

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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self


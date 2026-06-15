# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrackListByMailFromAndTagNameRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        config_set_id: str = None,
        dedicated_ip: str = None,
        dedicated_ip_pool_id: str = None,
        end_time: str = None,
        esp: str = None,
        offset: str = None,
        offset_create_time: str = None,
        offset_create_time_desc: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
        total: str = None,
    ):
        # The sender address.
        # 
        # > If you leave this parameter empty, data for all addresses is returned. This parameter is required if you specify TagName.
        self.account_name = account_name
        # The configuration set ID.
        self.config_set_id = config_set_id
        # The dedicated IP address. This parameter is available only for users of dedicated IPs.
        # 
        # If you do not specify this parameter, data for all IPs is returned.
        self.dedicated_ip = dedicated_ip
        # The ID of the dedicated IP pool. This parameter is available only for users of dedicated IPs.
        # 
        # If you do not specify this parameter, data for all IP pools is returned.
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        # The end time. The time span between the start time and end time cannot exceed 15 days. The format is yyyy-MM-dd.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The Email Service Provider (ESP). This parameter is available only for users of dedicated IPs. Valid values:
        # 
        # - gmail.com
        # 
        # - yahoo.com
        # 
        # - outlook.com
        # 
        # - icloud.com
        # 
        # - others (data for ESPs other than the ones listed above)
        # 
        # If you do not specify this parameter, data for all ESPs is returned.
        self.esp = esp
        # The value is 0 for the first query and 1 for subsequent queries. A value of 1 indicates a paged query in chronological order. (This field is deprecated)
        self.offset = offset
        # Used for paging. Do not set this parameter for the first query. For subsequent queries, set this parameter to the OffsetCreateTime value from the previous response. (This field is deprecated)
        self.offset_create_time = offset_create_time
        # (This field is deprecated)
        self.offset_create_time_desc = offset_create_time_desc
        self.owner_id = owner_id
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time. The time cannot be earlier than 30 days ago. The format is yyyy-MM-dd.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The email tag. If you leave this parameter empty, data for all tags is returned.
        self.tag_name = tag_name
        # (This field is deprecated)
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.config_set_id is not None:
            result['ConfigSetId'] = self.config_set_id

        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip

        if self.dedicated_ip_pool_id is not None:
            result['DedicatedIpPoolId'] = self.dedicated_ip_pool_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.esp is not None:
            result['Esp'] = self.esp

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.offset_create_time is not None:
            result['OffsetCreateTime'] = self.offset_create_time

        if self.offset_create_time_desc is not None:
            result['OffsetCreateTimeDesc'] = self.offset_create_time_desc

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')

        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')

        if m.get('DedicatedIpPoolId') is not None:
            self.dedicated_ip_pool_id = m.get('DedicatedIpPoolId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Esp') is not None:
            self.esp = m.get('Esp')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OffsetCreateTime') is not None:
            self.offset_create_time = m.get('OffsetCreateTime')

        if m.get('OffsetCreateTimeDesc') is not None:
            self.offset_create_time_desc = m.get('OffsetCreateTimeDesc')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self


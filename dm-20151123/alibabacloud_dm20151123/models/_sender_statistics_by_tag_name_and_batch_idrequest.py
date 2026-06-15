# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SenderStatisticsByTagNameAndBatchIDRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dedicated_ip: str = None,
        dedicated_ip_pool_id: str = None,
        domain: str = None,
        end_time: str = None,
        esp: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
    ):
        # The sender address. If you do not specify this parameter, statistics for all sender addresses are returned.
        self.account_name = account_name
        # If you use Dedicated IPs, use this parameter to filter statistics by a specific Dedicated IP.
        # 
        # If you do not specify this parameter, statistics for all dedicated IPs that match the other criteria are returned.
        self.dedicated_ip = dedicated_ip
        # If you use Dedicated IPs, specify the ID of the dedicated IP pool to query.
        # 
        # If you do not specify this parameter, statistics for all resources are returned.
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        self.domain = domain
        # The end time for the query. The time range between `StartTime` and `EndTime` cannot exceed 7 days. The format must be `YYYY-MM-DD`.
        # 
        # This parameter is required.
        self.end_time = end_time
        # If you use Dedicated IPs, use this parameter to filter statistics by a specific Email Service Provider (ESP). Valid values are:
        # 
        # - `gmail.com`
        # 
        # - `yahoo.com`
        # 
        # - `outlook.com`
        # 
        # - `icloud.com`
        # 
        # - `others` (matches data for all other ESPs)
        # 
        # If you do not specify this parameter, statistics for all ESPs are returned.
        self.esp = esp
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time for the query. The date cannot be more than 30 days in the past. The format must be `YYYY-MM-DD`.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The email tag. If you do not specify this parameter, statistics for all tags are returned.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip

        if self.dedicated_ip_pool_id is not None:
            result['DedicatedIpPoolId'] = self.dedicated_ip_pool_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.esp is not None:
            result['Esp'] = self.esp

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')

        if m.get('DedicatedIpPoolId') is not None:
            self.dedicated_ip_pool_id = m.get('DedicatedIpPoolId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Esp') is not None:
            self.esp = m.get('Esp')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self


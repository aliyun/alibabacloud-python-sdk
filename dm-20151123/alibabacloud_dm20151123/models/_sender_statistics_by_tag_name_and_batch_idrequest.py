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
        end_time: str = None,
        esp: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        tag_name: str = None,
    ):
        # Sending address. If not filled, it represents all addresses.
        self.account_name = account_name
        self.dedicated_ip = dedicated_ip
        self.dedicated_ip_pool_id = dedicated_ip_pool_id
        # End time, which cannot exceed 7 days from the start time, in the format yyyy-MM-dd.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.esp = esp
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Start time, in the format yyyy-MM-dd.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Email tag. If not filled, it represents all tags.
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


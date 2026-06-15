# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SenderStatisticsDetailByParamRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        config_set_id: str = None,
        end_time: str = None,
        ip_pool_id: str = None,
        length: int = None,
        next_start: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        status: int = None,
        tag_name: str = None,
        to_address: str = None,
    ):
        # The sender address. If you leave this parameter empty, emails from all sender addresses are queried.
        # 
        # > You can leave **AccountName**, **TagName**, and **ToAddress** empty. You can specify a value for only one of these parameters at a time.
        self.account_name = account_name
        # The ID of the configuration set.
        self.config_set_id = config_set_id
        # The end time. The time range between the start time and the end time cannot exceed 30 days. The format is yyyy-MM-dd HH:mm.
        self.end_time = end_time
        # The ID of the independent IP address pool.
        self.ip_pool_id = ip_pool_id
        # The number of results to return. The value can range from 1 to 100.
        self.length = length
        # The offset for this request, used for paging. If more results are available, set the \\`NextStart\\` parameter in your next request to this return value.
        self.next_start = next_start
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time. The time range between the start time and the end time cannot exceed 30 days. The format is yyyy-MM-dd HH:mm.
        self.start_time = start_time
        # The delivery status. If you leave this parameter empty, emails in all delivery statuses are queried. Valid values:
        # 
        # - 0: delivered successfully
        # 
        # - 2: invalid address
        # 
        # - 3: spam
        # 
        # - 4: failed
        self.status = status
        # The email tag. If you leave this parameter empty, emails with all tags are queried.
        # When you send an email using SMTP, specify the \\`TagName\\` and its value for the \\`X-AliDM-Trace\\` field. For more information, see the examples for email tracking.
        self.tag_name = tag_name
        # The recipient address. If you leave this parameter empty, emails sent to all recipient addresses are queried.
        self.to_address = to_address

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.length is not None:
            result['Length'] = self.length

        if self.next_start is not None:
            result['NextStart'] = self.next_start

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.to_address is not None:
            result['ToAddress'] = self.to_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ConfigSetId') is not None:
            self.config_set_id = m.get('ConfigSetId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('NextStart') is not None:
            self.next_start = m.get('NextStart')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('ToAddress') is not None:
            self.to_address = m.get('ToAddress')

        return self


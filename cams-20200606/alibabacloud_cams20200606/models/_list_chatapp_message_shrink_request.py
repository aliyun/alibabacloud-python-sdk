# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatappMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        client_accept_status: str = None,
        cust_space_id: str = None,
        end_time: int = None,
        end_time_str: str = None,
        event_action: str = None,
        group_message_id: str = None,
        message_status: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: int = None,
        start_time_str: str = None,
        template_code: str = None,
        user_number: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        # This parameter is required.
        self.channel_type = channel_type
        self.client_accept_status = client_accept_status
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.end_time = end_time
        self.end_time_str = end_time_str
        self.event_action = event_action
        self.group_message_id = group_message_id
        self.message_status = message_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.start_time_str = start_time_str
        self.template_code = template_code
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.client_accept_status is not None:
            result['ClientAcceptStatus'] = self.client_accept_status

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_str is not None:
            result['EndTimeStr'] = self.end_time_str

        if self.event_action is not None:
            result['EventAction'] = self.event_action

        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id

        if self.message_status is not None:
            result['MessageStatus'] = self.message_status

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_str is not None:
            result['StartTimeStr'] = self.start_time_str

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.user_number is not None:
            result['UserNumber'] = self.user_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ClientAcceptStatus') is not None:
            self.client_accept_status = m.get('ClientAcceptStatus')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeStr') is not None:
            self.end_time_str = m.get('EndTimeStr')

        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')

        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')

        if m.get('MessageStatus') is not None:
            self.message_status = m.get('MessageStatus')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeStr') is not None:
            self.start_time_str = m.get('StartTimeStr')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')

        return self


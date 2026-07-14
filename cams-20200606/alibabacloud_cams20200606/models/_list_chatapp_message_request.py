# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListChatappMessageRequest(DaraModel):
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
        page: main_models.ListChatappMessageRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: int = None,
        start_time_str: str = None,
        template_code: str = None,
        user_number: str = None,
    ):
        # The business phone number.
        # 
        # - For WhatsApp channels, view the business phone number in the [**Channel Management**](https://chatapp.console.aliyun.com/CustomerList) > **Management** > **WABA Management** > **Phone Number Management** console.
        # 
        # <props="intl">- For Viber channels, view the Service ID in the [**Channel Management**](https://chatapp.console.aliyun.com/CustomerList) > **Management** > **Service Account Management** console.
        # 
        # This parameter is required.
        self.business_number = business_number
        # The channel type. Valid values:
        # 
        # - **whatsapp**
        # 
        # - **viber**
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The message receiving status of the user.
        self.client_accept_status = client_accept_status
        # The space ID of the ISV sub-customer or the instance ID of the direct customer. View the Space ID in the [Channel Management](https://chatapp.console.aliyun.com/CustomerList) console.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The end time. This value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        self.end_time_str = end_time_str
        # The message type. Valid values:
        # - DOWN: outbound message.
        # - UP: inbound message.
        self.event_action = event_action
        # The bulk message ID. View the bulk message ID in the [**Channel Management**](https://chatapp.console.alibabacloud.com/CustomerList) > **Management** > **Message List** > **Bulk Sending List** console.
        self.group_message_id = group_message_id
        # The message status.
        self.message_status = message_status
        self.owner_id = owner_id
        # The pagination object.
        # 
        # This parameter is required.
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time. This value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        self.start_time_str = start_time_str
        # The template code. View the template code in the [**Channel Management**](https://chatapp.console.aliyun.com/CustomerList) > **Management** > **Template Design** console.
        self.template_code = template_code
        # The user phone number. This is the phone number that you imported when sending messages in the [**Channel Management**](https://chatapp.console.aliyun.com/CustomerList) > **Management** > **Message Sending** console.
        self.user_number = user_number

    def validate(self):
        if self.page:
            self.page.validate()

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

        if self.page is not None:
            result['Page'] = self.page.to_map()

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
            temp_model = main_models.ListChatappMessageRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

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

class ListChatappMessageRequestPage(DaraModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.index = index
        # The number of entries per page.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self


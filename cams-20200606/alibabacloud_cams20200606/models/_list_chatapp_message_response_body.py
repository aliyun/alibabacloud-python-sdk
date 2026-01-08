# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListChatappMessageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListChatappMessageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListChatappMessageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListChatappMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        client_accept_status_name: str = None,
        client_read_status: str = None,
        client_read_status_name: str = None,
        conversation_id: str = None,
        event_action: str = None,
        event_action_name: str = None,
        fail_back_content: str = None,
        fail_back_flag: str = None,
        fail_reason: str = None,
        language_code: str = None,
        message: str = None,
        message_id: str = None,
        message_source: str = None,
        message_status: str = None,
        message_status_name: str = None,
        message_type: str = None,
        message_type_name: str = None,
        month: str = None,
        send_time: str = None,
        template_code: str = None,
        template_name: str = None,
        type: str = None,
        unique_message_id: str = None,
        user_number: str = None,
    ):
        self.business_number = business_number
        self.channel_type = channel_type
        self.client_accept_status_name = client_accept_status_name
        self.client_read_status = client_read_status
        self.client_read_status_name = client_read_status_name
        self.conversation_id = conversation_id
        self.event_action = event_action
        self.event_action_name = event_action_name
        self.fail_back_content = fail_back_content
        self.fail_back_flag = fail_back_flag
        self.fail_reason = fail_reason
        self.language_code = language_code
        self.message = message
        self.message_id = message_id
        self.message_source = message_source
        self.message_status = message_status
        self.message_status_name = message_status_name
        self.message_type = message_type
        self.message_type_name = message_type_name
        self.month = month
        self.send_time = send_time
        self.template_code = template_code
        self.template_name = template_name
        self.type = type
        self.unique_message_id = unique_message_id
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

        if self.client_accept_status_name is not None:
            result['ClientAcceptStatusName'] = self.client_accept_status_name

        if self.client_read_status is not None:
            result['ClientReadStatus'] = self.client_read_status

        if self.client_read_status_name is not None:
            result['ClientReadStatusName'] = self.client_read_status_name

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.event_action is not None:
            result['EventAction'] = self.event_action

        if self.event_action_name is not None:
            result['EventActionName'] = self.event_action_name

        if self.fail_back_content is not None:
            result['FailBackContent'] = self.fail_back_content

        if self.fail_back_flag is not None:
            result['FailBackFlag'] = self.fail_back_flag

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        if self.message is not None:
            result['Message'] = self.message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.message_source is not None:
            result['MessageSource'] = self.message_source

        if self.message_status is not None:
            result['MessageStatus'] = self.message_status

        if self.message_status_name is not None:
            result['MessageStatusName'] = self.message_status_name

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.message_type_name is not None:
            result['MessageTypeName'] = self.message_type_name

        if self.month is not None:
            result['Month'] = self.month

        if self.send_time is not None:
            result['SendTime'] = self.send_time

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.type is not None:
            result['Type'] = self.type

        if self.unique_message_id is not None:
            result['UniqueMessageId'] = self.unique_message_id

        if self.user_number is not None:
            result['UserNumber'] = self.user_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ClientAcceptStatusName') is not None:
            self.client_accept_status_name = m.get('ClientAcceptStatusName')

        if m.get('ClientReadStatus') is not None:
            self.client_read_status = m.get('ClientReadStatus')

        if m.get('ClientReadStatusName') is not None:
            self.client_read_status_name = m.get('ClientReadStatusName')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')

        if m.get('EventActionName') is not None:
            self.event_action_name = m.get('EventActionName')

        if m.get('FailBackContent') is not None:
            self.fail_back_content = m.get('FailBackContent')

        if m.get('FailBackFlag') is not None:
            self.fail_back_flag = m.get('FailBackFlag')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('MessageSource') is not None:
            self.message_source = m.get('MessageSource')

        if m.get('MessageStatus') is not None:
            self.message_status = m.get('MessageStatus')

        if m.get('MessageStatusName') is not None:
            self.message_status_name = m.get('MessageStatusName')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('MessageTypeName') is not None:
            self.message_type_name = m.get('MessageTypeName')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueMessageId') is not None:
            self.unique_message_id = m.get('UniqueMessageId')

        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')

        return self


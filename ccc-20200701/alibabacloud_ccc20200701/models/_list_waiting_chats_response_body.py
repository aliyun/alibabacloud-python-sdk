# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListWaitingChatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListWaitingChatsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListWaitingChatsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListWaitingChatsResponseBodyData(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        being_assigned: bool = None,
        chat_conversation_id: str = None,
        enqueue_time: int = None,
        job_id: str = None,
        messages: List[main_models.ListWaitingChatsResponseBodyDataMessages] = None,
        skill_group_id: str = None,
        user_list: List[main_models.ListWaitingChatsResponseBodyDataUserList] = None,
    ):
        self.access_channel_id = access_channel_id
        self.access_channel_type = access_channel_type
        self.being_assigned = being_assigned
        self.chat_conversation_id = chat_conversation_id
        self.enqueue_time = enqueue_time
        self.job_id = job_id
        self.messages = messages
        self.skill_group_id = skill_group_id
        self.user_list = user_list

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.being_assigned is not None:
            result['BeingAssigned'] = self.being_assigned

        if self.chat_conversation_id is not None:
            result['ChatConversationId'] = self.chat_conversation_id

        if self.enqueue_time is not None:
            result['EnqueueTime'] = self.enqueue_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('BeingAssigned') is not None:
            self.being_assigned = m.get('BeingAssigned')

        if m.get('ChatConversationId') is not None:
            self.chat_conversation_id = m.get('ChatConversationId')

        if m.get('EnqueueTime') is not None:
            self.enqueue_time = m.get('EnqueueTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ListWaitingChatsResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.ListWaitingChatsResponseBodyDataUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class ListWaitingChatsResponseBodyDataUserList(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.avatar_url = avatar_url
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

class ListWaitingChatsResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        sender_id: str = None,
        sender_type: str = None,
    ):
        self.content = content
        self.sender_id = sender_id
        self.sender_type = sender_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_type is not None:
            result['SenderType'] = self.sender_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CreateAIStaffChatRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        chat_id: str = None,
        conversation_id: str = None,
        messages: List[main_models.CreateAIStaffChatRequestMessages] = None,
        meta_data: Dict[str, str] = None,
    ):
        self.biz_id = biz_id
        self.chat_id = chat_id
        self.conversation_id = conversation_id
        self.messages = messages
        self.meta_data = meta_data

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.CreateAIStaffChatRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        return self

class CreateAIStaffChatRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        meta_data: Dict[str, str] = None,
        role: str = None,
        type: str = None,
    ):
        self.content = content
        self.content_type = content_type
        self.meta_data = meta_data
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


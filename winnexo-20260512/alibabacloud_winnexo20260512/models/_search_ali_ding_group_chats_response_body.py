# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SearchAliDingGroupChatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.SearchAliDingGroupChatsResponseBodyItems] = None,
        message: str = None,
        next_cursor: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # Indicates whether more pages are available.
        self.has_more = has_more
        # The user group tree node information.
        self.items = items
        # The description of the status code.
        self.message = message
        # The starting cursor for the next page.
        self.next_cursor = next_cursor
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.SearchAliDingGroupChatsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SearchAliDingGroupChatsResponseBodyItems(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        conversation_type: str = None,
        muted: bool = None,
        title: str = None,
    ):
        # The conversation ID. This ID is typically used for JSSDK.
        self.chat_id = chat_id
        # The conversation type. Valid values:
        # - **0**: one-on-one chat.
        # - **1**: group chat.
        # 
        # > For a one-on-one chat, you do not need to specify **openConversationId**. Specify the employee ID in **receiverUserIdList**. For a one-on-one chat between two users, specify the employee ID of either user. For a one-on-one chat between a user and a bot, specify the employee ID of the user.
        self.conversation_type = conversation_type
        # Indicates whether the current user has enabled the Do Not Disturb mode.
        self.muted = muted
        # The title of the scheduled meeting.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.conversation_type is not None:
            result['conversationType'] = self.conversation_type

        if self.muted is not None:
            result['muted'] = self.muted

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('conversationType') is not None:
            self.conversation_type = m.get('conversationType')

        if m.get('muted') is not None:
            self.muted = m.get('muted')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self


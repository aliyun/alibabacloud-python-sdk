# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAIStaffChatMessagesRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        conversation_id: str = None,
        page_size: int = None,
        start_create_time: str = None,
    ):
        self.biz_id = biz_id
        self.conversation_id = conversation_id
        self.page_size = page_size
        self.start_create_time = start_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_create_time is not None:
            result['StartCreateTime'] = self.start_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartCreateTime') is not None:
            self.start_create_time = m.get('StartCreateTime')

        return self


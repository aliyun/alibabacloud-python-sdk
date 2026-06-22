# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkakopilot20260414 import models as main_models
from darabonba.model import DaraModel

class KopilotListConversationsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.KopilotListConversationsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.KopilotListConversationsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class KopilotListConversationsResponseBodyData(DaraModel):
    def __init__(
        self,
        conversation_ids: List[str] = None,
        count: int = None,
        page: int = None,
        size: int = None,
        total: int = None,
        total_pages: int = None,
        user_id: str = None,
    ):
        self.conversation_ids = conversation_ids
        self.count = count
        self.page = page
        self.size = size
        self.total = total
        self.total_pages = total_pages
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_ids is not None:
            result['ConversationIds'] = self.conversation_ids

        if self.count is not None:
            result['Count'] = self.count

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationIds') is not None:
            self.conversation_ids = m.get('ConversationIds')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self


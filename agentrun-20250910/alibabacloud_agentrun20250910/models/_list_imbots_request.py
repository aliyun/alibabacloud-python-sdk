# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIMBotsRequest(DaraModel):
    def __init__(
        self,
        agent_runtime_id: str = None,
        bot_biz_type: str = None,
        bot_name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # The ID of the agent runtime.
        self.agent_runtime_id = agent_runtime_id
        # The business type of the bot.
        self.bot_biz_type = bot_biz_type
        # The name of the IM bot. The system performs a case-insensitive substring search.
        self.bot_name = bot_name
        # The page number. Must be greater than or equal to 1. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1–100. Default: 20.
        self.page_size = page_size
        # The status of the bot.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.bot_biz_type is not None:
            result['botBizType'] = self.bot_biz_type

        if self.bot_name is not None:
            result['botName'] = self.bot_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('botBizType') is not None:
            self.bot_biz_type = m.get('botBizType')

        if m.get('botName') is not None:
            self.bot_name = m.get('botName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


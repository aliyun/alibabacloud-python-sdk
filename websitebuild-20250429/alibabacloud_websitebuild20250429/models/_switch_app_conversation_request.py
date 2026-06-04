# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchAppConversationRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        bot_id: str = None,
        task_type: str = None,
    ):
        self.biz_id = biz_id
        self.bot_id = bot_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self


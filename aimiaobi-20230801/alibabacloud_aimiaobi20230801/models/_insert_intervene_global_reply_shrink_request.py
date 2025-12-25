# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertInterveneGlobalReplyShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        reply_messag_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reply_messag_list_shrink = reply_messag_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.reply_messag_list_shrink is not None:
            result['ReplyMessagList'] = self.reply_messag_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ReplyMessagList') is not None:
            self.reply_messag_list_shrink = m.get('ReplyMessagList')

        return self


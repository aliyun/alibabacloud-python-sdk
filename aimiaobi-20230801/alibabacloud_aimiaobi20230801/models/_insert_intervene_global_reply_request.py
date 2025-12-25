# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class InsertInterveneGlobalReplyRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        reply_messag_list: List[main_models.InsertInterveneGlobalReplyRequestReplyMessagList] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reply_messag_list = reply_messag_list

    def validate(self):
        if self.reply_messag_list:
            for v1 in self.reply_messag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k1 in self.reply_messag_list:
                result['ReplyMessagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k1 in m.get('ReplyMessagList'):
                temp_model = main_models.InsertInterveneGlobalReplyRequestReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k1))

        return self

class InsertInterveneGlobalReplyRequestReplyMessagList(DaraModel):
    def __init__(
        self,
        message: str = None,
        reply_type: str = None,
    ):
        self.message = message
        self.reply_type = reply_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')

        return self


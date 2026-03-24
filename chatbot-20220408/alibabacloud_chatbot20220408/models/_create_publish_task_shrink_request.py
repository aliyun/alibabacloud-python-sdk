# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePublishTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_type: str = None,
        data_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        self.biz_type = biz_type
        self.data_id_list_shrink = data_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.data_id_list_shrink is not None:
            result['DataIdList'] = self.data_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DataIdList') is not None:
            self.data_id_list_shrink = m.get('DataIdList')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePublishTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        biz_type: str = None,
        data_id_list: List[str] = None,
    ):
        # The key of the business space. If you omit this parameter, the default business space is used. You can obtain the key from the Business Management page of your main account.
        self.agent_key = agent_key
        # The type of content to publish. To publish a bot, use the `CreateInstancePublishTask` API.
        self.biz_type = biz_type
        # Specifies data to publish by ID. This parameter is used only when `BizType` is set to `faq`. In this case, provide one or more category IDs to publish knowledge exclusively from the specified categories.
        self.data_id_list = data_id_list

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

        if self.data_id_list is not None:
            result['DataIdList'] = self.data_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DataIdList') is not None:
            self.data_id_list = m.get('DataIdList')

        return self


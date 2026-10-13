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
        # The workspace key. If not specified, the default workspace is accessed. Obtain the key value from the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The publish unit type. To publish a chatbot, use the CreateInstancePublishTask API.
        self.biz_type = biz_type
        # Additional publish information. Currently supported: if BizType is faq, this field specifies category IDs, indicating that only knowledge under these categories is published.
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


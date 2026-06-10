# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLgfRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_id: int = None,
        lgf_text: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The key of the business space. If you do not specify this parameter, the default business space is used. You can obtain the key from the Business Management page of your main account.
        self.agent_key = agent_key
        # The ID of the chatbot.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the intent.
        # 
        # This parameter is required.
        self.intent_id = intent_id
        # The text used to filter the advanced semantic configurations.
        self.lgf_text = lgf_text
        # The number of the page to return. Defaults to 1.
        self.page_number = page_number
        # The number of entries to return on each page. Defaults to 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.lgf_text is not None:
            result['LgfText'] = self.lgf_text

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('LgfText') is not None:
            self.lgf_text = m.get('LgfText')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


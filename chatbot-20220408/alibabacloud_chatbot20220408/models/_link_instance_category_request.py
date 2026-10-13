# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LinkInstanceCategoryRequest(DaraModel):
    def __init__(
        self,
        ability_type: str = None,
        agent_key: str = None,
        category_ids: str = None,
        instance_id: str = None,
    ):
        # The capability type of the category. Valid values:
        # 
        # - FAQ: Frequently asked questions.
        # - MRC: Document-based machine reading comprehension.
        # 
        # Default value: FAQ.
        self.ability_type = ability_type
        # The business space key. If this parameter is not specified, the default business space is accessed. You can obtain the key on the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The array of FAQ category IDs to associate with the chatbot.
        self.category_ids = category_ids
        # The unique identifier of the chatbot.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability_type is not None:
            result['AbilityType'] = self.ability_type

        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbilityType') is not None:
            self.ability_type = m.get('AbilityType')

        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


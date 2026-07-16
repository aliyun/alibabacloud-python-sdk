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
        # The category\\"s ability type. Valid values: `FAQ` and `MRC` (machine reading comprehension). Defaults to `FAQ`.
        self.ability_type = ability_type
        # The key for the business space. If you do not specify this parameter, the default business space is used. You can obtain the key on the Business Management page of your primary account.
        self.agent_key = agent_key
        # An array of FAQ category IDs to link to the chatbot.
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


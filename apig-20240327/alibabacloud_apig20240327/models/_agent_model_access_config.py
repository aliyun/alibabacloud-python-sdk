# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AgentModelAccessConfig(DaraModel):
    def __init__(
        self,
        consumer_ids: List[str] = None,
        model_api_id: str = None,
    ):
        # The list of consumer IDs that represent the Agent to access the Model API. The Model API ID and consumer ID together identify the Agent identity, and the configuration takes effect for all current and future routes of the Model API. Specify at least one consumer. The consumer must be enabled and must have direct Consumer authorization for the Model API in the default environment of the target gateway, with the authorization publish status being Success. Different Agents cannot bind the same consumer to the same Model API. ConsumerGroup is not supported.
        # 
        # This parameter is required.
        self.consumer_ids = consumer_ids
        # The ID of the Model API to associate. The Model API must belong to the specified gateway.
        # 
        # This parameter is required.
        self.model_api_id = model_api_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_ids is not None:
            result['consumerIds'] = self.consumer_ids

        if self.model_api_id is not None:
            result['modelApiId'] = self.model_api_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerIds') is not None:
            self.consumer_ids = m.get('consumerIds')

        if m.get('modelApiId') is not None:
            self.model_api_id = m.get('modelApiId')

        return self


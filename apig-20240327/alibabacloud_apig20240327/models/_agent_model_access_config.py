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
        # This parameter is required.
        self.consumer_ids = consumer_ids
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


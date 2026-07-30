# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchRemoveConsumerGroupConsumersRequest(DaraModel):
    def __init__(
        self,
        consumer_ids: List[str] = None,
    ):
        # The list of consumer IDs to remove from the consumer group.
        self.consumer_ids = consumer_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_ids is not None:
            result['consumerIds'] = self.consumer_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerIds') is not None:
            self.consumer_ids = m.get('consumerIds')

        return self


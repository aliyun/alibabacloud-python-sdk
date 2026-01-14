# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumerGroupSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # The topic name. If you do not specify this parameter, all subscriptions of the consumer group are queried.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self


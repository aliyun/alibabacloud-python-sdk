# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsumerGroupLagRequest(DaraModel):
    def __init__(
        self,
        lite_topic_name: str = None,
        topic_name: str = None,
    ):
        self.lite_topic_name = lite_topic_name
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lite_topic_name is not None:
            result['liteTopicName'] = self.lite_topic_name

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liteTopicName') is not None:
            self.lite_topic_name = m.get('liteTopicName')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self


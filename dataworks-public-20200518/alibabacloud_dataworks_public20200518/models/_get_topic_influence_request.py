# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTopicInfluenceRequest(DaraModel):
    def __init__(
        self,
        topic_id: int = None,
    ):
        # The ID of the event.
        # 
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MNS(DaraModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # The SMQ topic. You can check topics within a region in the [SMQ console](https://mns.console.aliyun.com/). This parameter is required if you want to use SMQ for notifications.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self


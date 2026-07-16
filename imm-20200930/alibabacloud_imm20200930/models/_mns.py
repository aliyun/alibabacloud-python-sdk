# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MNS(DaraModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # Specifies the name of the ApsaraMQ for MNS topic, which can be found in the topic list for the current region in the left-side navigation pane of the [ApsaraMQ for MNS console](https://mns.console.aliyun.com/). This parameter is required for ApsaraMQ for MNS message notification.
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


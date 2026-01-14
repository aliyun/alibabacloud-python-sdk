# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTopicRequest(DaraModel):
    def __init__(
        self,
        lite_topic_expiration: int = None,
        max_send_tps: int = None,
        remark: str = None,
    ):
        self.lite_topic_expiration = lite_topic_expiration
        # Maximum send message tps
        self.max_send_tps = max_send_tps
        # Updated remarks for the topic.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lite_topic_expiration is not None:
            result['liteTopicExpiration'] = self.lite_topic_expiration

        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liteTopicExpiration') is not None:
            self.lite_topic_expiration = m.get('liteTopicExpiration')

        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteQueueRequest(DaraModel):
    def __init__(
        self,
        queue_name: str = None,
    ):
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        return self


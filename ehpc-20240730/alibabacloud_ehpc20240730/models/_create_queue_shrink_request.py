# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQueueShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The configurations of the queue to be created.
        self.queue_shrink = queue_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.queue_shrink is not None:
            result['Queue'] = self.queue_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Queue') is not None:
            self.queue_shrink = m.get('Queue')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueuesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue_names_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The names of the queues that you want to query. You can specify up to eight names.
        self.queue_names_shrink = queue_names_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')

        return self


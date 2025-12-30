# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class CreateQueueRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        queue: main_models.QueueTemplate = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The configurations of the queue to be created.
        self.queue = queue

    def validate(self):
        if self.queue:
            self.queue.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.queue is not None:
            result['Queue'] = self.queue.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Queue') is not None:
            temp_model = main_models.QueueTemplate()
            self.queue = temp_model.from_map(m.get('Queue'))

        return self


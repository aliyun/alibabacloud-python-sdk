# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSessionClusterRequest(DaraModel):
    def __init__(
        self,
        queue_name: str = None,
        session_cluster_id: str = None,
        region_id: str = None,
    ):
        # The queue name.
        self.queue_name = queue_name
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self


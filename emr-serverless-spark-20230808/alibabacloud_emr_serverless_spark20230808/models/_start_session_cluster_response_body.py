# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSessionClusterResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        session_cluster_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelSqlPreviewRequest(DaraModel):
    def __init__(
        self,
        query_id: str = None,
        session_cluster_name: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.query_id = query_id
        # This parameter is required.
        self.session_cluster_name = session_cluster_name
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_id is not None:
            result['queryId'] = self.query_id

        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')

        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self


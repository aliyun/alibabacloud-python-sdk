# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchSemanticViewsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        query_text: str = None,
        top_k: int = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The search query.
        self.query_text = query_text
        # The number of the most relevant semantic views to return.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self


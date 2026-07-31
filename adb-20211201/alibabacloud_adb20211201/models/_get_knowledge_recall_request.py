# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeRecallRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        question: str = None,
        topk: int = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The question for knowledge base recall.
        # 
        # This parameter is required.
        self.question = question
        # The top K number of related files to recall.
        self.topk = topk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.question is not None:
            result['Question'] = self.question

        if self.topk is not None:
            result['Topk'] = self.topk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Topk') is not None:
            self.topk = m.get('Topk')

        return self


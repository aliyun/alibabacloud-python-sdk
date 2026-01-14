# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBaseListResult(DaraModel):
    def __init__(
        self,
        knowledge_bases: List[main_models.KnowledgeBaseInfo] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.knowledge_bases = knowledge_bases
        self.request_id = request_id
        # This parameter is required.
        self.total = total

    def validate(self):
        if self.knowledge_bases:
            for v1 in self.knowledge_bases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['knowledgeBases'] = []
        if self.knowledge_bases is not None:
            for k1 in self.knowledge_bases:
                result['knowledgeBases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_bases = []
        if m.get('knowledgeBases') is not None:
            for k1 in m.get('knowledgeBases'):
                temp_model = main_models.KnowledgeBaseInfo()
                self.knowledge_bases.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self


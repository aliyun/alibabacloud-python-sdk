# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class GetQueryResponseBody(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        created_at: int = None,
        query_id: str = None,
        results: List[main_models.StatementResult] = None,
        sql: str = None,
        status: str = None,
        tier: str = None,
    ):
        self.completed_at = completed_at
        self.created_at = created_at
        self.query_id = query_id
        self.results = results
        self.sql = sql
        self.status = status
        self.tier = tier

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.query_id is not None:
            result['queryId'] = self.query_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.sql is not None:
            result['sql'] = self.sql

        if self.status is not None:
            result['status'] = self.status

        if self.tier is not None:
            result['tier'] = self.tier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.StatementResult()
                self.results.append(temp_model.from_map(k1))

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tier') is not None:
            self.tier = m.get('tier')

        return self


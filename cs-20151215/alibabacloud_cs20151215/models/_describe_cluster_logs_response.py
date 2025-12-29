# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterLogsResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeClusterLogsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeClusterLogsResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeClusterLogsResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        cluster_id: str = None,
        cluster_log: str = None,
        created: str = None,
        updated: str = None,
    ):
        # The ID of the log entry.
        self.id = id
        # The cluster ID.
        self.cluster_id = cluster_id
        # The log content.
        self.cluster_log = cluster_log
        # The time when the log entry was generated.
        self.created = created
        # The time when the log entry was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['ID'] = self.id

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_log is not None:
            result['cluster_log'] = self.cluster_log

        if self.created is not None:
            result['created'] = self.created

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_log') is not None:
            self.cluster_log = m.get('cluster_log')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self


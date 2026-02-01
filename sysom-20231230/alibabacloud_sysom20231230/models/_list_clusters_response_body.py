# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListClustersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[main_models.ListClustersResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListClustersResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_status: str = None,
        cluster_type: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        region: str = None,
        updated_at: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_status = cluster_status
        self.cluster_type = cluster_type
        self.created_at = created_at
        self.id = id
        self.name = name
        self.region = region
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_status is not None:
            result['cluster_status'] = self.cluster_status

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.region is not None:
            result['region'] = self.region

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_status') is not None:
            self.cluster_status = m.get('cluster_status')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self


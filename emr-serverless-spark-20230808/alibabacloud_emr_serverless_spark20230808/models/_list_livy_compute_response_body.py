# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListLivyComputeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListLivyComputeResponseBodyData(DaraModel):
    def __init__(
        self,
        livy_computes: List[main_models.ListLivyComputeResponseBodyDataLivyComputes] = None,
    ):
        self.livy_computes = livy_computes

    def validate(self):
        if self.livy_computes:
            for v1 in self.livy_computes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['livyComputes'] = []
        if self.livy_computes is not None:
            for k1 in self.livy_computes:
                result['livyComputes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.livy_computes = []
        if m.get('livyComputes') is not None:
            for k1 in m.get('livyComputes'):
                temp_model = main_models.ListLivyComputeResponseBodyDataLivyComputes()
                self.livy_computes.append(temp_model.from_map(k1))

        return self

class ListLivyComputeResponseBodyDataLivyComputes(DaraModel):
    def __init__(
        self,
        compute_id: str = None,
        created_by: str = None,
        endpoint: str = None,
        endpoint_inner: str = None,
        gmt_create: int = None,
        name: str = None,
        queue_name: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.compute_id = compute_id
        self.created_by = created_by
        self.endpoint = endpoint
        self.endpoint_inner = endpoint_inner
        self.gmt_create = gmt_create
        self.name = name
        self.queue_name = queue_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_id is not None:
            result['computeId'] = self.compute_id

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.endpoint_inner is not None:
            result['endpointInner'] = self.endpoint_inner

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.name is not None:
            result['name'] = self.name

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeId') is not None:
            self.compute_id = m.get('computeId')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('endpointInner') is not None:
            self.endpoint_inner = m.get('endpointInner')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


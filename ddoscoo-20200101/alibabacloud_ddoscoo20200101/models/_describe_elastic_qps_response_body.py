# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticQpsResponseBody(DaraModel):
    def __init__(
        self,
        elastic_qps: List[main_models.DescribeElasticQpsResponseBodyElasticQps] = None,
        request_id: str = None,
    ):
        # The information about the burstable QPS.
        self.elastic_qps = elastic_qps
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.elastic_qps:
            for v1 in self.elastic_qps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticQps'] = []
        if self.elastic_qps is not None:
            for k1 in self.elastic_qps:
                result['ElasticQps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elastic_qps = []
        if m.get('ElasticQps') is not None:
            for k1 in m.get('ElasticQps'):
                temp_model = main_models.DescribeElasticQpsResponseBodyElasticQps()
                self.elastic_qps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticQpsResponseBodyElasticQps(DaraModel):
    def __init__(
        self,
        index: int = None,
        max_normal_qps: int = None,
        max_qps: int = None,
        pv: int = None,
        status_2: int = None,
        status_3: int = None,
        status_4: int = None,
        status_5: int = None,
        ups: int = None,
    ):
        # The index number of the returned data.
        self.index = index
        # The peak QPS of the normal service.
        self.max_normal_qps = max_normal_qps
        # The peak inbound QPS.
        self.max_qps = max_qps
        # The total number of requests during the step size period.
        self.pv = pv
        # The total number of HTTP 2xx status codes during the step size period.
        self.status_2 = status_2
        # The total number of HTTP 3xx status codes during the step size period.
        self.status_3 = status_3
        # The total number of HTTP 4xx status codes during the step size period.
        self.status_4 = status_4
        # The total number of HTTP 5xx status codes during the step size period.
        self.status_5 = status_5
        # The total number of origin requests during the step size period.
        self.ups = ups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.pv is not None:
            result['Pv'] = self.pv

        if self.status_2 is not None:
            result['Status2'] = self.status_2

        if self.status_3 is not None:
            result['Status3'] = self.status_3

        if self.status_4 is not None:
            result['Status4'] = self.status_4

        if self.status_5 is not None:
            result['Status5'] = self.status_5

        if self.ups is not None:
            result['Ups'] = self.ups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        if m.get('Status2') is not None:
            self.status_2 = m.get('Status2')

        if m.get('Status3') is not None:
            self.status_3 = m.get('Status3')

        if m.get('Status4') is not None:
            self.status_4 = m.get('Status4')

        if m.get('Status5') is not None:
            self.status_5 = m.get('Status5')

        if m.get('Ups') is not None:
            self.ups = m.get('Ups')

        return self


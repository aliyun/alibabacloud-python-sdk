# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeConnectableClustersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeConnectableClustersResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeConnectableClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeConnectableClustersResponseBodyResult(DaraModel):
    def __init__(
        self,
        instances: str = None,
        network_type: str = None,
    ):
        self.instances = instances
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['instances'] = self.instances

        if self.network_type is not None:
            result['networkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        return self


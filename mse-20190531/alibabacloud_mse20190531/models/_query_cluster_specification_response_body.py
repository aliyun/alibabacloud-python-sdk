# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryClusterSpecificationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.QueryClusterSpecificationResponseBodyData] = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return value.
        self.code = code
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryClusterSpecificationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryClusterSpecificationResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_specification_name: str = None,
        cpu_capacity: str = None,
        memory_capacity: str = None,
    ):
        # The engine specifications that can be used.
        self.cluster_specification_name = cluster_specification_name
        # The number of vCPUs in the specifications.
        self.cpu_capacity = cpu_capacity
        # The memory size in the specifications. Unit: GB.
        self.memory_capacity = memory_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_specification_name is not None:
            result['ClusterSpecificationName'] = self.cluster_specification_name

        if self.cpu_capacity is not None:
            result['CpuCapacity'] = self.cpu_capacity

        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpecificationName') is not None:
            self.cluster_specification_name = m.get('ClusterSpecificationName')

        if m.get('CpuCapacity') is not None:
            self.cpu_capacity = m.get('CpuCapacity')

        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')

        return self


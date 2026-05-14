# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListInstanceModelResponseBody(DaraModel):
    def __init__(
        self,
        instance_model_list: List[main_models.ListInstanceModelResponseBodyInstanceModelList] = None,
        request_id: str = None,
    ):
        self.instance_model_list = instance_model_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.instance_model_list:
            for v1 in self.instance_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['instanceModelList'] = []
        if self.instance_model_list is not None:
            for k1 in self.instance_model_list:
                result['instanceModelList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_model_list = []
        if m.get('instanceModelList') is not None:
            for k1 in m.get('instanceModelList'):
                temp_model = main_models.ListInstanceModelResponseBodyInstanceModelList()
                self.instance_model_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListInstanceModelResponseBodyInstanceModelList(DaraModel):
    def __init__(
        self,
        ai_instance_id: str = None,
        ai_spec: str = None,
        auto_renewal: bool = None,
        charge_type: str = None,
        commodity_code: str = None,
        cpu: int = None,
        cpu_used: int = None,
        expiration_time: str = None,
        gpu: int = None,
        gpu_memory: int = None,
        gpu_memory_used: int = None,
        gpu_used: int = None,
        holo_instance_id: str = None,
        holo_instance_name: str = None,
        memory: int = None,
        memory_used: int = None,
        node_count: int = None,
        region_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        self.ai_instance_id = ai_instance_id
        self.ai_spec = ai_spec
        self.auto_renewal = auto_renewal
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.cpu = cpu
        self.cpu_used = cpu_used
        self.expiration_time = expiration_time
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.gpu_memory_used = gpu_memory_used
        self.gpu_used = gpu_used
        self.holo_instance_id = holo_instance_id
        self.holo_instance_name = holo_instance_name
        self.memory = memory
        self.memory_used = memory_used
        self.node_count = node_count
        self.region_id = region_id
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_instance_id is not None:
            result['aiInstanceId'] = self.ai_instance_id

        if self.ai_spec is not None:
            result['aiSpec'] = self.ai_spec

        if self.auto_renewal is not None:
            result['autoRenewal'] = self.auto_renewal

        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.cpu_used is not None:
            result['cpuUsed'] = self.cpu_used

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['gpuMemory'] = self.gpu_memory

        if self.gpu_memory_used is not None:
            result['gpuMemoryUsed'] = self.gpu_memory_used

        if self.gpu_used is not None:
            result['gpuUsed'] = self.gpu_used

        if self.holo_instance_id is not None:
            result['holoInstanceId'] = self.holo_instance_id

        if self.holo_instance_name is not None:
            result['holoInstanceName'] = self.holo_instance_name

        if self.memory is not None:
            result['memory'] = self.memory

        if self.memory_used is not None:
            result['memoryUsed'] = self.memory_used

        if self.node_count is not None:
            result['nodeCount'] = self.node_count

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiInstanceId') is not None:
            self.ai_instance_id = m.get('aiInstanceId')

        if m.get('aiSpec') is not None:
            self.ai_spec = m.get('aiSpec')

        if m.get('autoRenewal') is not None:
            self.auto_renewal = m.get('autoRenewal')

        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('cpuUsed') is not None:
            self.cpu_used = m.get('cpuUsed')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuMemory') is not None:
            self.gpu_memory = m.get('gpuMemory')

        if m.get('gpuMemoryUsed') is not None:
            self.gpu_memory_used = m.get('gpuMemoryUsed')

        if m.get('gpuUsed') is not None:
            self.gpu_used = m.get('gpuUsed')

        if m.get('holoInstanceId') is not None:
            self.holo_instance_id = m.get('holoInstanceId')

        if m.get('holoInstanceName') is not None:
            self.holo_instance_name = m.get('holoInstanceName')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('memoryUsed') is not None:
            self.memory_used = m.get('memoryUsed')

        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


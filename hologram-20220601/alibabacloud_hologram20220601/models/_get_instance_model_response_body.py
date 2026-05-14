# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetInstanceModelResponseBody(DaraModel):
    def __init__(
        self,
        ai_instance_id: str = None,
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
        memory: int = None,
        memory_used: int = None,
        model_service_list: List[main_models.GetInstanceModelResponseBodyModelServiceList] = None,
        node_count: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        self.ai_instance_id = ai_instance_id
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
        self.memory = memory
        self.memory_used = memory_used
        self.model_service_list = model_service_list
        self.node_count = node_count
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        if self.model_service_list:
            for v1 in self.model_service_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_instance_id is not None:
            result['aiInstanceId'] = self.ai_instance_id

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

        if self.memory is not None:
            result['memory'] = self.memory

        if self.memory_used is not None:
            result['memoryUsed'] = self.memory_used

        result['modelServiceList'] = []
        if self.model_service_list is not None:
            for k1 in self.model_service_list:
                result['modelServiceList'].append(k1.to_map() if k1 else None)

        if self.node_count is not None:
            result['nodeCount'] = self.node_count

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiInstanceId') is not None:
            self.ai_instance_id = m.get('aiInstanceId')

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

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('memoryUsed') is not None:
            self.memory_used = m.get('memoryUsed')

        self.model_service_list = []
        if m.get('modelServiceList') is not None:
            for k1 in m.get('modelServiceList'):
                temp_model = main_models.GetInstanceModelResponseBodyModelServiceList()
                self.model_service_list.append(temp_model.from_map(k1))

        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetInstanceModelResponseBodyModelServiceList(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        cpu: int = None,
        gpu: int = None,
        gpu_memory: int = None,
        instance_region: str = None,
        memory: int = None,
        message: str = None,
        model_name: str = None,
        model_params: str = None,
        model_type: str = None,
        provider: str = None,
        service_count: int = None,
        service_deploy_region: str = None,
        status: str = None,
        task_type: str = None,
        version: str = None,
    ):
        self.api_key = api_key
        self.cpu = cpu
        self.gpu = gpu
        self.gpu_memory = gpu_memory
        self.instance_region = instance_region
        self.memory = memory
        self.message = message
        self.model_name = model_name
        self.model_params = model_params
        self.model_type = model_type
        self.provider = provider
        self.service_count = service_count
        self.service_deploy_region = service_deploy_region
        self.status = status
        self.task_type = task_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['gpuMemory'] = self.gpu_memory

        if self.instance_region is not None:
            result['instanceRegion'] = self.instance_region

        if self.memory is not None:
            result['memory'] = self.memory

        if self.message is not None:
            result['message'] = self.message

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_params is not None:
            result['modelParams'] = self.model_params

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.provider is not None:
            result['provider'] = self.provider

        if self.service_count is not None:
            result['serviceCount'] = self.service_count

        if self.service_deploy_region is not None:
            result['serviceDeployRegion'] = self.service_deploy_region

        if self.status is not None:
            result['status'] = self.status

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuMemory') is not None:
            self.gpu_memory = m.get('gpuMemory')

        if m.get('instanceRegion') is not None:
            self.instance_region = m.get('instanceRegion')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelParams') is not None:
            self.model_params = m.get('modelParams')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('serviceCount') is not None:
            self.service_count = m.get('serviceCount')

        if m.get('serviceDeployRegion') is not None:
            self.service_deploy_region = m.get('serviceDeployRegion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceQueueRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        gpu_spec: List[str] = None,
        instance_id: str = None,
        payment_type: str = None,
        preheat: bool = None,
        queue_category: str = None,
        resource_spec: main_models.CreateWorkspaceQueueRequestResourceSpec = None,
        workspace_id: str = None,
        workspace_queue_name: str = None,
        region_id: str = None,
    ):
        # The description.
        self.description = description
        # The list of GPU models.
        self.gpu_spec = gpu_spec
        # The Ray cluster instance ID.
        self.instance_id = instance_id
        # The billing method of the instance. Valid values:
        # 
        # - PayAsYouGo: pay-as-you-go
        # - Pre: subscription
        self.payment_type = payment_type
        # Indicates whether resource prefetch is enabled.
        self.preheat = preheat
        # The queue type. Valid values: CPU and GPU.
        self.queue_category = queue_category
        # The resource specifications.
        self.resource_spec = resource_spec
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace queue name.
        self.workspace_queue_name = workspace_queue_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.preheat is not None:
            result['preheat'] = self.preheat

        if self.queue_category is not None:
            result['queueCategory'] = self.queue_category

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_queue_name is not None:
            result['workspaceQueueName'] = self.workspace_queue_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('preheat') is not None:
            self.preheat = m.get('preheat')

        if m.get('queueCategory') is not None:
            self.queue_category = m.get('queueCategory')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.CreateWorkspaceQueueRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceQueueName') is not None:
            self.workspace_queue_name = m.get('workspaceQueueName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class CreateWorkspaceQueueRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        gpu: int = None,
        gpu_machine_num: int = None,
        max_cu: int = None,
    ):
        # The maximum workspace resource capacity.
        self.cu = cu
        # The number of GPUs.
        self.gpu = gpu
        # The number of GPU machines. This parameter is valid only for subscription instances.
        self.gpu_machine_num = gpu_machine_num
        # The maximum number of CUs.
        self.max_cu = max_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_machine_num is not None:
            result['gpuMachineNum'] = self.gpu_machine_num

        if self.max_cu is not None:
            result['maxCu'] = self.max_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuMachineNum') is not None:
            self.gpu_machine_num = m.get('gpuMachineNum')

        if m.get('maxCu') is not None:
            self.max_cu = m.get('maxCu')

        return self


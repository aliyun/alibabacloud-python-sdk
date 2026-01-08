# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        accessibility: str = None,
        create_user_id: str = None,
        gpu_type: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        labels: Dict[str, Any] = None,
        max_cpu: str = None,
        max_gpu: str = None,
        max_gpu_memory: str = None,
        max_memory: str = None,
        min_cpu: str = None,
        min_gpu: str = None,
        min_gpu_memory: str = None,
        min_memory: str = None,
        order: str = None,
        oversold_info: str = None,
        oversold_type: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        resource_id: str = None,
        sort_by: str = None,
        status: str = None,
        tag: List[main_models.ListInstancesRequestTag] = None,
        workspace_id: str = None,
    ):
        # The accelerator type.
        # 
        # *   CPU: Only CPU computing is used.
        # *   GPU: GPUs are used to accelerate computing.
        self.accelerator_type = accelerator_type
        # The accessibility. Valid values:
        # 
        # *   PRIVATE (default): The instances are accessible only to you and the administrator of the workspace.
        # *   PUBLIC: The instances are accessible only to all members in the workspace.
        self.accessibility = accessibility
        # The UID of the creator.
        self.create_user_id = create_user_id
        # The GPU type.
        self.gpu_type = gpu_type
        # The image name.
        self.image_name = image_name
        # The instance ID. You can call [ListInstances](https://help.aliyun.com/document_detail/470439.html) to obtain the instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The labels. A maximum of four labels are supported.
        self.labels = labels
        # The maximum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.max_cpu = max_cpu
        # The maximum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.max_gpu = max_gpu
        # The maximum memory size per GPU card. Unit: GB.
        self.max_gpu_memory = max_gpu_memory
        # The maximum memory size. Unit: GB.
        self.max_memory = max_memory
        # The minimum number of CPUs. Unit: 0.001 CPU. The value 1000 indicates one CPU.
        self.min_cpu = min_cpu
        # The minimum number of GPUs. Unit: 0.001 GPU. The value 1000 indicates one GPU.
        self.min_gpu = min_gpu
        # The minimum memory size per GPU card. Unit: GB.
        self.min_gpu_memory = min_gpu_memory
        # The minimum memory size. Unit: GB.
        self.min_memory = min_memory
        # The order that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   ASC
        # *   DESC
        self.order = order
        self.oversold_info = oversold_info
        self.oversold_type = oversold_type
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo
        # *   Subscription
        self.payment_type = payment_type
        # The resource group ID. If you leave this parameter empty, the instances in the pay-as-you-go resource group are queried. If you set this parameter to ALL, all instances are queried.
        self.resource_id = resource_id
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   Priority
        # *   GmtCreateTime
        # *   GmtModifiedTime
        self.sort_by = sort_by
        # The instance status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   SaveFailed
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Queuing
        # *   Recovering
        # *   Starting
        # *   Running
        # *   Saved
        # *   Deleting
        # *   EnvPreparing
        self.status = status
        # The tags.
        self.tag = tag
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu

        if self.max_gpu is not None:
            result['MaxGpu'] = self.max_gpu

        if self.max_gpu_memory is not None:
            result['MaxGpuMemory'] = self.max_gpu_memory

        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory

        if self.min_cpu is not None:
            result['MinCpu'] = self.min_cpu

        if self.min_gpu is not None:
            result['MinGpu'] = self.min_gpu

        if self.min_gpu_memory is not None:
            result['MinGpuMemory'] = self.min_gpu_memory

        if self.min_memory is not None:
            result['MinMemory'] = self.min_memory

        if self.order is not None:
            result['Order'] = self.order

        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info

        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')

        if m.get('MaxGpu') is not None:
            self.max_gpu = m.get('MaxGpu')

        if m.get('MaxGpuMemory') is not None:
            self.max_gpu_memory = m.get('MaxGpuMemory')

        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')

        if m.get('MinCpu') is not None:
            self.min_cpu = m.get('MinCpu')

        if m.get('MinGpu') is not None:
            self.min_gpu = m.get('MinGpu')

        if m.get('MinGpuMemory') is not None:
            self.min_gpu_memory = m.get('MinGpuMemory')

        if m.get('MinMemory') is not None:
            self.min_memory = m.get('MinMemory')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')

        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workspace: main_models.GetWorkspaceResponseBodyWorkspace = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The workspace object.
        self.workspace = workspace

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('workspace') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m.get('workspace'))

        return self

class GetWorkspaceResponseBodyWorkspace(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        auto_renew_period_unit: str = None,
        create_time: int = None,
        dlf_catalog_id: str = None,
        dlf_type: str = None,
        duration: int = None,
        end_time: int = None,
        fail_reason: str = None,
        gpu_spec: List[str] = None,
        ip_white_list: List[str] = None,
        payment_duration_unit: str = None,
        payment_status: str = None,
        payment_type: str = None,
        pre_paid_quota: main_models.GetWorkspaceResponseBodyWorkspacePrePaidQuota = None,
        pre_paid_quota_gpu: List[main_models.GetWorkspaceResponseBodyWorkspacePrePaidQuotaGpu] = None,
        ram_role_name: str = None,
        region_id: str = None,
        release_type: str = None,
        resource_group_id: str = None,
        resource_owner_id: str = None,
        resource_spec: str = None,
        state_change_reason: main_models.GetWorkspaceResponseBodyWorkspaceStateChangeReason = None,
        storage: str = None,
        tags: List[main_models.GetWorkspaceResponseBodyWorkspaceTags] = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        # Specifies whether auto-renewal is enabled. This parameter is required for subscription workspaces.
        self.auto_renew = auto_renew
        # The auto-renewal period. This parameter is required for subscription workspaces.
        self.auto_renew_period = auto_renew_period
        # The auto-renewal cycle. This parameter is required for subscription workspaces.
        self.auto_renew_period_unit = auto_renew_period_unit
        # The time when the workspace was created. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The DLF catalog information.
        self.dlf_catalog_id = dlf_catalog_id
        # The bound DLF type.
        self.dlf_type = dlf_type
        # The subscription duration. This parameter is required for subscription workspaces.
        self.duration = duration
        # The time when the workspace is released.
        self.end_time = end_time
        # The reason for the failure.
        self.fail_reason = fail_reason
        # The list of GPU instance types.
        self.gpu_spec = gpu_spec
        # The IP whitelist of the workspace.
        self.ip_white_list = ip_white_list
        # The unit of the subscription period. This parameter is required for subscription workspaces.
        self.payment_duration_unit = payment_duration_unit
        # The payment status.
        self.payment_status = payment_status
        # The billing method.
        self.payment_type = payment_type
        # The information about the subscription resource quota.
        self.pre_paid_quota = pre_paid_quota
        # The list of GPU subscription quotas.
        self.pre_paid_quota_gpu = pre_paid_quota_gpu
        # The name of the RAM role used to execute Spark jobs.
        self.ram_role_name = ram_role_name
        # The region ID.
        self.region_id = region_id
        # The reason why the workspace is released.
        self.release_type = release_type
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The UID of the user who created the workspace.
        self.resource_owner_id = resource_owner_id
        # The resource specifications.
        self.resource_spec = resource_spec
        # The information about the workspace status change.
        self.state_change_reason = state_change_reason
        # The OSS path.
        self.storage = storage
        # The tag keys.
        self.tags = tags
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The workspace status.
        self.workspace_status = workspace_status

    def validate(self):
        if self.pre_paid_quota:
            self.pre_paid_quota.validate()
        if self.pre_paid_quota_gpu:
            for v1 in self.pre_paid_quota_gpu:
                 if v1:
                    v1.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dlf_catalog_id is not None:
            result['dlfCatalogId'] = self.dlf_catalog_id

        if self.dlf_type is not None:
            result['dlfType'] = self.dlf_type

        if self.duration is not None:
            result['duration'] = self.duration

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.pre_paid_quota is not None:
            result['prePaidQuota'] = self.pre_paid_quota.to_map()

        result['prePaidQuotaGpu'] = []
        if self.pre_paid_quota_gpu is not None:
            for k1 in self.pre_paid_quota_gpu:
                result['prePaidQuotaGpu'].append(k1.to_map() if k1 else None)

        if self.ram_role_name is not None:
            result['ramRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_type is not None:
            result['releaseType'] = self.release_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['resourceOwnerId'] = self.resource_owner_id

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.storage is not None:
            result['storage'] = self.storage

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.workspace_status is not None:
            result['workspaceStatus'] = self.workspace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dlfCatalogId') is not None:
            self.dlf_catalog_id = m.get('dlfCatalogId')

        if m.get('dlfType') is not None:
            self.dlf_type = m.get('dlfType')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('ipWhiteList') is not None:
            self.ip_white_list = m.get('ipWhiteList')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('prePaidQuota') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyWorkspacePrePaidQuota()
            self.pre_paid_quota = temp_model.from_map(m.get('prePaidQuota'))

        self.pre_paid_quota_gpu = []
        if m.get('prePaidQuotaGpu') is not None:
            for k1 in m.get('prePaidQuotaGpu'):
                temp_model = main_models.GetWorkspaceResponseBodyWorkspacePrePaidQuotaGpu()
                self.pre_paid_quota_gpu.append(temp_model.from_map(k1))

        if m.get('ramRoleName') is not None:
            self.ram_role_name = m.get('ramRoleName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceOwnerId') is not None:
            self.resource_owner_id = m.get('resourceOwnerId')

        if m.get('resourceSpec') is not None:
            self.resource_spec = m.get('resourceSpec')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyWorkspaceStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetWorkspaceResponseBodyWorkspaceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('workspaceStatus') is not None:
            self.workspace_status = m.get('workspaceStatus')

        return self

class GetWorkspaceResponseBodyWorkspaceTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag keys.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class GetWorkspaceResponseBodyWorkspaceStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The status information of the node pod.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class GetWorkspaceResponseBodyWorkspacePrePaidQuotaGpu(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        cpu_core_count: str = None,
        create_time: int = None,
        expire_time: int = None,
        gpu_amount: int = None,
        gpu_machine_num: int = None,
        gpu_memory_size: int = None,
        gpu_num: int = None,
        gpu_spec: str = None,
        instance_id: str = None,
        instance_type_family: str = None,
        instance_type_id: str = None,
        memory_size: str = None,
        order_id: str = None,
        payment_status: str = None,
    ):
        # Specifies whether auto-renewal is enabled.
        self.auto_renewal = auto_renewal
        # The number of CPU cores.
        self.cpu_core_count = cpu_core_count
        # The creation time.
        self.create_time = create_time
        # The expiration time.
        self.expire_time = expire_time
        # The number of GPUs.
        self.gpu_amount = gpu_amount
        # The number of GPU instances.
        self.gpu_machine_num = gpu_machine_num
        # The GPU memory size.
        self.gpu_memory_size = gpu_memory_size
        # The number of GPU instances.
        self.gpu_num = gpu_num
        # The GPU instance type.
        self.gpu_spec = gpu_spec
        # The instance ID.
        self.instance_id = instance_id
        # The instance family.
        self.instance_type_family = instance_type_family
        # The instance type ID.
        self.instance_type_id = instance_type_id
        # The memory size.
        self.memory_size = memory_size
        # The order ID.
        self.order_id = order_id
        # The order status.
        self.payment_status = payment_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['autoRenewal'] = self.auto_renewal

        if self.cpu_core_count is not None:
            result['cpuCoreCount'] = self.cpu_core_count

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gpu_amount is not None:
            result['gpuAmount'] = self.gpu_amount

        if self.gpu_machine_num is not None:
            result['gpuMachineNum'] = self.gpu_machine_num

        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size

        if self.gpu_num is not None:
            result['gpuNum'] = self.gpu_num

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type_family is not None:
            result['instanceTypeFamily'] = self.instance_type_family

        if self.instance_type_id is not None:
            result['instanceTypeId'] = self.instance_type_id

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenewal') is not None:
            self.auto_renewal = m.get('autoRenewal')

        if m.get('cpuCoreCount') is not None:
            self.cpu_core_count = m.get('cpuCoreCount')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gpuAmount') is not None:
            self.gpu_amount = m.get('gpuAmount')

        if m.get('gpuMachineNum') is not None:
            self.gpu_machine_num = m.get('gpuMachineNum')

        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')

        if m.get('gpuNum') is not None:
            self.gpu_num = m.get('gpuNum')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceTypeFamily') is not None:
            self.instance_type_family = m.get('instanceTypeFamily')

        if m.get('instanceTypeId') is not None:
            self.instance_type_id = m.get('instanceTypeId')

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')

        return self

class GetWorkspaceResponseBodyWorkspacePrePaidQuota(DaraModel):
    def __init__(
        self,
        allocated_resource: str = None,
        auto_renewal: bool = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        max_resource: str = None,
        order_id: str = None,
        payment_status: str = None,
        used_resource: str = None,
    ):
        # The amount of resources currently allocated.
        self.allocated_resource = allocated_resource
        # Specifies whether auto-renewal is enabled for the resource.
        # 
        # - true: Auto-renewal is enabled. The resource is automatically renewed upon expiration.
        # - false: Auto-renewal is disabled. The resource is stopped upon expiration.
        self.auto_renewal = auto_renewal
        # The time when the workspace was created. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The expiration time of the GPU subscription quota. The value is a UNIX timestamp in milliseconds.
        self.expire_time = expire_time
        # The instance ID.
        self.instance_id = instance_id
        # The maximum amount of resources that can be used.
        self.max_resource = max_resource
        # The order ID.
        self.order_id = order_id
        # The order status.
        self.payment_status = payment_status
        # The amount of resources currently used.
        self.used_resource = used_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_resource is not None:
            result['allocatedResource'] = self.allocated_resource

        if self.auto_renewal is not None:
            result['autoRenewal'] = self.auto_renewal

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.max_resource is not None:
            result['maxResource'] = self.max_resource

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status

        if self.used_resource is not None:
            result['usedResource'] = self.used_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocatedResource') is not None:
            self.allocated_resource = m.get('allocatedResource')

        if m.get('autoRenewal') is not None:
            self.auto_renewal = m.get('autoRenewal')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')

        if m.get('usedResource') is not None:
            self.used_resource = m.get('usedResource')

        return self


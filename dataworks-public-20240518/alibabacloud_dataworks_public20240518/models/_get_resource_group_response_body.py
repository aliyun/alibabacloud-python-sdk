# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: main_models.GetResourceGroupResponseBodyResourceGroup = None,
        success: bool = None,
    ):
        # The ID of the request, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # The detailed information of the resource group.
        self.resource_group = resource_group
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroup') is not None:
            temp_model = main_models.GetResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m.get('ResourceGroup'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResourceGroupResponseBodyResourceGroup(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[main_models.GetResourceGroupResponseBodyResourceGroupAliyunResourceTags] = None,
        create_time: int = None,
        create_user: str = None,
        default_vpc_id: str = None,
        default_vswitch_id: str = None,
        id: str = None,
        name: str = None,
        order_instance_id: str = None,
        payment_type: str = None,
        remark: str = None,
        resource_group_type: str = None,
        spec: main_models.GetResourceGroupResponseBodyResourceGroupSpec = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud resource group to which the resource group belongs.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The list of Alibaba Cloud tags.
        self.aliyun_resource_tags = aliyun_resource_tags
        # The creation time, represented as a 64-bit timestamp.
        self.create_time = create_time
        # The ID of the user who created the resource group.
        self.create_user = create_user
        # The ID of the default VPC bound to the resource group.
        self.default_vpc_id = default_vpc_id
        # The ID of the default vSwitch bound to the resource group.
        self.default_vswitch_id = default_vswitch_id
        # The unique identifier of the resource group.
        self.id = id
        # The name of the resource group.
        self.name = name
        # The order instance ID of the resource group.
        self.order_instance_id = order_instance_id
        # The billing method of the resource group. Valid values:
        # 
        # - PrePaid: subscription.
        # - PostPaid: pay-as-you-go.
        self.payment_type = payment_type
        # The remarks of the resource group.
        self.remark = remark
        # The type of the resource group. Valid values:
        # 
        # - CommonV2: new-version resource group.
        # - ExclusiveDataIntegration: exclusive data integration resource group.
        # - ExclusiveScheduler: exclusive scheduling resource group.
        # - ExclusiveDataService: exclusive data service resource group.
        self.resource_group_type = resource_group_type
        # The specifications of the resource group.
        self.spec = spec
        # The status of the resource group. Valid values:
        # 
        # - Normal: normal (running/in service).
        # - Stop: frozen (expired).
        # - Deleted: deleted (released/destroyed).
        # - Creating: being created.
        # - CreateFailed: creation failed.
        # - Updating: being updated (scaling out/scaling in/specification change in progress).
        # - UpdateFailed: update failed (scale-out failed/upgrade failed).
        # - Deleting: being deleted (being released/being destroyed).
        # - DeleteFailed: deletion failed (release failed/destruction failed).
        # - Timeout: operation timed out.
        # - Freezed: frozen.
        # - Starting: starting.
        self.status = status

    def validate(self):
        if self.aliyun_resource_tags:
            for v1 in self.aliyun_resource_tags:
                 if v1:
                    v1.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k1 in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.default_vpc_id is not None:
            result['DefaultVpcId'] = self.default_vpc_id

        if self.default_vswitch_id is not None:
            result['DefaultVswitchId'] = self.default_vswitch_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type

        if self.spec is not None:
            result['Spec'] = self.spec.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k1 in m.get('AliyunResourceTags'):
                temp_model = main_models.GetResourceGroupResponseBodyResourceGroupAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DefaultVpcId') is not None:
            self.default_vpc_id = m.get('DefaultVpcId')

        if m.get('DefaultVswitchId') is not None:
            self.default_vswitch_id = m.get('DefaultVswitchId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')

        if m.get('Spec') is not None:
            temp_model = main_models.GetResourceGroupResponseBodyResourceGroupSpec()
            self.spec = temp_model.from_map(m.get('Spec'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetResourceGroupResponseBodyResourceGroupSpec(DaraModel):
    def __init__(
        self,
        amount: int = None,
        standard: str = None,
    ):
        # The resource count.
        self.amount = amount
        # The specification details.
        self.standard = standard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.standard is not None:
            result['Standard'] = self.standard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Standard') is not None:
            self.standard = m.get('Standard')

        return self

class GetResourceGroupResponseBodyResourceGroupAliyunResourceTags(DaraModel):
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


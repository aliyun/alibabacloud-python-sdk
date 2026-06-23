# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListResourceGroupsResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListResourceGroupsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListResourceGroupsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_group_list: List[main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of resource groups.
        self.resource_group_list = resource_group_list
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.resource_group_list:
            for v1 in self.resource_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ResourceGroupList'] = []
        if self.resource_group_list is not None:
            for k1 in self.resource_group_list:
                result['ResourceGroupList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.resource_group_list = []
        if m.get('ResourceGroupList') is not None:
            for k1 in m.get('ResourceGroupList'):
                temp_model = main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupList()
                self.resource_group_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceGroupsResponseBodyPagingInfoResourceGroupList(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupListAliyunResourceTags] = None,
        create_time: int = None,
        create_user: str = None,
        default_vpc_id: str = None,
        default_vswicth_id: str = None,
        id: str = None,
        name: str = None,
        order_instance_id: str = None,
        payment_type: str = None,
        remark: str = None,
        resource_group_type: str = None,
        spec: main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupListSpec = None,
        status: str = None,
    ):
        # The Alibaba Cloud resource group ID.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # A list of Alibaba Cloud tags.
        self.aliyun_resource_tags = aliyun_resource_tags
        # The creation time of the resource group, as a 64-bit timestamp.
        self.create_time = create_time
        # The user ID of the creator.
        self.create_user = create_user
        # The ID of the default Virtual Private Cloud (VPC) bound to the general-purpose resource group.
        self.default_vpc_id = default_vpc_id
        # The ID of the default vSwitch bound to the general-purpose resource group.
        self.default_vswicth_id = default_vswicth_id
        # The unique identifier of the resource group.
        self.id = id
        # The name of the resource group.
        self.name = name
        # The ID of the order for the resource group.
        self.order_instance_id = order_instance_id
        # The billing method of the resource group. `PrePaid` indicates subscription and `PostPaid` indicates pay-as-you-go.
        self.payment_type = payment_type
        # The description of the resource group.
        self.remark = remark
        # The type of the resource group. Valid values:
        # 
        # - `CommonV2`: The new general-purpose resource group.
        # 
        # - `ExclusiveDataIntegration`: The exclusive resource group for data integration.
        # 
        # - `ExclusiveScheduler`: The exclusive resource group for scheduling.
        # 
        # - `ExclusiveDataService`: The exclusive resource group for data services.
        self.resource_group_type = resource_group_type
        # The specifications of the resource group.
        self.spec = spec
        # The status of the resource group. Valid values:
        # 
        # - `Normal`: Running.
        # 
        # - `Stop`: Frozen due to expiration.
        # 
        # - `Deleted`: Released.
        # 
        # - `Creating`: Creation in progress.
        # 
        # - `CreateFailed`: Creation failed.
        # 
        # - `Updating`: Update in progress.
        # 
        # - `UpdateFailed`: Update failed.
        # 
        # - `Deleting`: Release in progress.
        # 
        # - `DeleteFailed`: Release failed.
        # 
        # - `Timeout`: The operation timed out.
        # 
        # - `Freezed`: Frozen.
        # 
        # - `Starting`: Starting.
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

        if self.default_vswicth_id is not None:
            result['DefaultVswicthId'] = self.default_vswicth_id

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
                temp_model = main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupListAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DefaultVpcId') is not None:
            self.default_vpc_id = m.get('DefaultVpcId')

        if m.get('DefaultVswicthId') is not None:
            self.default_vswicth_id = m.get('DefaultVswicthId')

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
            temp_model = main_models.ListResourceGroupsResponseBodyPagingInfoResourceGroupListSpec()
            self.spec = temp_model.from_map(m.get('Spec'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListResourceGroupsResponseBodyPagingInfoResourceGroupListSpec(DaraModel):
    def __init__(
        self,
        amount: int = None,
        standard: str = None,
    ):
        # The number of resource units.
        self.amount = amount
        # The resource specifications.
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

class ListResourceGroupsResponseBodyPagingInfoResourceGroupListAliyunResourceTags(DaraModel):
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


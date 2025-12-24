# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceByCenterPolicyIdResponseBody(DaraModel):
    def __init__(
        self,
        count: str = None,
        next_token: str = None,
        request_id: str = None,
        resource_model_list: List[main_models.DescribeResourceByCenterPolicyIdResponseBodyResourceModelList] = None,
    ):
        # The total number of resources.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resource_model_list = resource_model_list

    def validate(self):
        if self.resource_model_list:
            for v1 in self.resource_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceModelList'] = []
        if self.resource_model_list is not None:
            for k1 in self.resource_model_list:
                result['ResourceModelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_model_list = []
        if m.get('ResourceModelList') is not None:
            for k1 in m.get('ResourceModelList'):
                temp_model = main_models.DescribeResourceByCenterPolicyIdResponseBodyResourceModelList()
                self.resource_model_list.append(temp_model.from_map(k1))

        return self

class DescribeResourceByCenterPolicyIdResponseBodyResourceModelList(DaraModel):
    def __init__(
        self,
        app_model_list: List[main_models.DescribeResourceByCenterPolicyIdResponseBodyResourceModelListAppModelList] = None,
        cpu: int = None,
        desktop_type: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        memory: int = None,
        os_type: str = None,
        pay_type: str = None,
        product_type: str = None,
        protocol_type: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        resource_group_rel_count: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The cloud applications.
        self.app_model_list = app_model_list
        # The number of vCPUs.
        self.cpu = cpu
        # The cloud computer type. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) operation to query the IDs of the cloud computer types supported by Alibaba Cloud Workspace.
        self.desktop_type = desktop_type
        # The number of GPUs.
        self.gpu_count = gpu_count
        # The GPU type.
        self.gpu_spec = gpu_spec
        # The memory size. Unit: MiB.
        self.memory = memory
        # The OS type.
        self.os_type = os_type
        # The billing method.
        self.pay_type = pay_type
        # The service type.
        self.product_type = product_type
        # The protocol type.
        self.protocol_type = protocol_type
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource group name.
        self.resource_group_name = resource_group_name
        # The number of associated resource groups
        self.resource_group_rel_count = resource_group_rel_count
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The resource type.
        self.resource_type = resource_type
        # The resource status.
        self.status = status

    def validate(self):
        if self.app_model_list:
            for v1 in self.app_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppModelList'] = []
        if self.app_model_list is not None:
            for k1 in self.app_model_list:
                result['AppModelList'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.resource_group_rel_count is not None:
            result['ResourceGroupRelCount'] = self.resource_group_rel_count

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_model_list = []
        if m.get('AppModelList') is not None:
            for k1 in m.get('AppModelList'):
                temp_model = main_models.DescribeResourceByCenterPolicyIdResponseBodyResourceModelListAppModelList()
                self.app_model_list.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ResourceGroupRelCount') is not None:
            self.resource_group_rel_count = m.get('ResourceGroupRelCount')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeResourceByCenterPolicyIdResponseBodyResourceModelListAppModelList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The application ID. This parameter is only applicable to cloud applications.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeApsResourceGroupsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The queried resource groups.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        # 
        # *   If the request was successful, a success message is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeApsResourceGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeApsResourceGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        resource_groups: List[main_models.DescribeApsResourceGroupsResponseBodyDataResourceGroups] = None,
        step: int = None,
    ):
        # The queried resource groups.
        self.resource_groups = resource_groups
        # The step size of resources. Unit: AnalyticDB compute units (ACUs).
        # 
        # *   If the value of GroupType is **Interactive**, 16 is returned.
        # *   If the value of GroupType is **Job**, 8 is returned.
        self.step = step

    def validate(self):
        if self.resource_groups:
            for v1 in self.resource_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k1 in self.resource_groups:
                result['ResourceGroups'].append(k1.to_map() if k1 else None)

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k1 in m.get('ResourceGroups'):
                temp_model = main_models.DescribeApsResourceGroupsResponseBodyDataResourceGroups()
                self.resource_groups.append(temp_model.from_map(k1))

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeApsResourceGroupsResponseBodyDataResourceGroups(DaraModel):
    def __init__(
        self,
        available: bool = None,
        cu_options: List[int] = None,
        group_name: str = None,
        group_type: str = None,
        left_compute_resource: int = None,
        max_compute_resource: int = None,
        min_compute_resource: int = None,
    ):
        # Indicates whether the resource group is available. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.available = available
        self.cu_options = cu_options
        # The name of the resource group.
        self.group_name = group_name
        # The type of the resource group. Valid values:
        # 
        # *   **Interactive**
        # *   **Job**
        # 
        # >  For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/428610.html).
        self.group_type = group_type
        # The amount of remaining computing resources. Unit: ACUs.
        self.left_compute_resource = left_compute_resource
        # The maximum amount of reserved computing resources. Unit: ACUs.
        # 
        # *   If the value of GroupType is **Interactive**, the amount of reserved computing resources that are not allocated in the cluster is returned in increments of 16 ACUs.
        # *   If the value of GroupType is **Job**, the amount of reserved computing resources that are not allocated in the cluster is returned in increments of 8 ACUs.
        self.max_compute_resource = max_compute_resource
        # The minimum amount of reserved computing resources. Unit: ACUs.
        # 
        # *   If the value of GroupType is **Interactive**, 16 is returned.
        # *   If the value of GroupType is **Job**, 0 is returned.
        self.min_compute_resource = min_compute_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.cu_options is not None:
            result['CuOptions'] = self.cu_options

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.left_compute_resource is not None:
            result['LeftComputeResource'] = self.left_compute_resource

        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource

        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('CuOptions') is not None:
            self.cu_options = m.get('CuOptions')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('LeftComputeResource') is not None:
            self.left_compute_resource = m.get('LeftComputeResource')

        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')

        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')

        return self


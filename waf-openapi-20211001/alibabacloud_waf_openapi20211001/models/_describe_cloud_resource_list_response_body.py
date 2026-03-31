# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudResourceListResponseBody(DaraModel):
    def __init__(
        self,
        cloud_resource_list: List[main_models.DescribeCloudResourceListResponseBodyCloudResourceList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cloud_resource_list = cloud_resource_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cloud_resource_list:
            for v1 in self.cloud_resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudResourceList'] = []
        if self.cloud_resource_list is not None:
            for k1 in self.cloud_resource_list:
                result['CloudResourceList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_resource_list = []
        if m.get('CloudResourceList') is not None:
            for k1 in m.get('CloudResourceList'):
                temp_model = main_models.DescribeCloudResourceListResponseBodyCloudResourceList()
                self.cloud_resource_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudResourceListResponseBodyCloudResourceList(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        port: int = None,
        protocol: str = None,
        resource_instance_id: str = None,
        resource_manager_resource_group_id: str = None,
        resource_product: str = None,
        resource_region_id: str = None,
    ):
        self.cloud_resource_id = cloud_resource_id
        self.port = port
        self.protocol = protocol
        self.resource_instance_id = resource_instance_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.resource_product = resource_product
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        return self


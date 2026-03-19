# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: List[main_models.DescribeContainerResourceResponseBodyResources] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.resources = resources
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeContainerResourceResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeContainerResourceResponseBodyResources(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_identifier: str = None,
        resource_id: str = None,
        resource_info: str = None,
        resource_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_identifier = cluster_identifier
        self.resource_id = resource_id
        self.resource_info = resource_info
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_identifier is not None:
            result['ClusterIdentifier'] = self.cluster_identifier

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterIdentifier') is not None:
            self.cluster_identifier = m.get('ClusterIdentifier')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceInfo') is not None:
            self.resource_info = m.get('ResourceInfo')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApisecExamplesRequest(DaraModel):
    def __init__(
        self,
        abnormal_tag: str = None,
        api_id: str = None,
        cluster_id: str = None,
        example_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        request_sensitive_type_list: List[str] = None,
        resource_manager_resource_group_id: str = None,
        response_sensitive_type_list: List[str] = None,
    ):
        self.abnormal_tag = abnormal_tag
        # This parameter is required.
        self.api_id = api_id
        self.cluster_id = cluster_id
        self.example_type = example_type
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.request_sensitive_type_list = request_sensitive_type_list
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        self.response_sensitive_type_list = response_sensitive_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_tag is not None:
            result['AbnormalTag'] = self.abnormal_tag

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.example_type is not None:
            result['ExampleType'] = self.example_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_sensitive_type_list is not None:
            result['RequestSensitiveTypeList'] = self.request_sensitive_type_list

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.response_sensitive_type_list is not None:
            result['ResponseSensitiveTypeList'] = self.response_sensitive_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalTag') is not None:
            self.abnormal_tag = m.get('AbnormalTag')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestSensitiveTypeList') is not None:
            self.request_sensitive_type_list = m.get('RequestSensitiveTypeList')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResponseSensitiveTypeList') is not None:
            self.response_sensitive_type_list = m.get('ResponseSensitiveTypeList')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        log_store_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeFlowLogsRequestTag] = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to only perform a dry run for this request. Valid values:
        # 
        # - **true**: send a check request and do not modify service resources.
        # 
        # - **false** (default): send a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The instance ID of the flow log instance.
        self.flow_log_id = flow_log_id
        # The name of the flow log. The name must be 0 to 128 characters in length.
        self.flow_log_name = flow_log_name
        # The instance ID of the VBR instance loaded on the Express Connect Router (ECR).
        self.instance_id = instance_id
        # The Simple Log Service Logstore used to capture traffic.
        # - If you have created a Logstore in the current region, you can enter the name of the existing Logstore.
        # - If you have not created a Logstore in the current region, you can specify a custom name for the Logstore, and the system automatically creates the Logstore. The naming rules are as follows:
        # 
        # - The Logstore name must be unique within the same project.
        # - It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # - It must start and end with a lowercase letter or a digit.
        # - It must be 3 to 63 characters in length.
        self.log_store_name = log_store_name
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If NextToken is empty, no next query is available.
        # - If NextToken has a return value, the value indicates the token for the next query.
        self.next_token = next_token
        # The Simple Log Service project used to capture traffic.
        # - If you have created a project in the current region, you can enter the name of the existing project.
        # - If you have not created a project in the current region, you can specify a custom name for the project, and the system automatically creates the project.
        # 
        # 
        # The project name must be globally unique within an Alibaba Cloud region and cannot be modified after creation. The naming rules are as follows:
        #    
        # - The project name must be globally unique.
        # - It can contain only lowercase
        # - letters, digits, and hyphens (-).
        # - It must start and end with a lowercase letter or a digit.
        # - It must be 3 to 63 characters in length.
        self.project_name = project_name
        # The ID of the resource group to which the flow log instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        # 
        # You can add up to 20 tags.
        self.tag = tag
        self.version = version

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFlowLogsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeFlowLogsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. Valid values of N: 1 to 20. If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length. It cannot start with `acs:`, and cannot contain `http://` or `https://`.
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


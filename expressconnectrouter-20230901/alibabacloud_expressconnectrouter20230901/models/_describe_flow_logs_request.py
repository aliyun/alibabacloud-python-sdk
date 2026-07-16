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
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The flow log name. The name must be 0 to 128 characters in length.
        self.flow_log_name = flow_log_name
        # The ID of the VBR associated with the ECR.
        self.instance_id = instance_id
        # The Logstore that stores the captured traffic data.
        # 
        # *   If a Logstore is already created in the selected region, enter the name of the Logstore.
        # *   If no Logstores are created in the selected region, enter a name and the system automatically creates a Logstore. The name of the Logstore. The name must meet the following requirements:
        # *   The name must be unique in a project.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.log_store_name = log_store_name
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # - You do not need to specify this parameter for the first request.
        # - You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The project that stores the captured traffic data.
        # 
        # *   If a project is already created in the selected region, enter the name of the project.
        # *   If no projects are created in the selected region, enter a name and the system automatically creates a project.
        # 
        # The project name must be unique in a region. You cannot change the name after the project is created. The name must meet the following requirements:
        # 
        # *   The name must be globally unique.
        # *   The name can contain only lowercase letters,
        # *   digits, and hyphens (-).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.project_name = project_name
        self.resource_group_id = resource_group_id
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
        self.key = key
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


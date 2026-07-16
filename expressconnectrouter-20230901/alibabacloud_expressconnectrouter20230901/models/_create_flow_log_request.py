# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class CreateFlowLogRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        interval: int = None,
        log_store_name: str = None,
        project_name: str = None,
        resource_group_id: str = None,
        sampling_rate: str = None,
        tag: List[main_models.CreateFlowLogRequestTag] = None,
        target_sls_region_id: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the flow log.
        # 
        # > The description can be empty or 1 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ID of the ECR.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The name of the flow log.
        # 
        # > The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.flow_log_name = flow_log_name
        # The VBR ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of network instance. Valid values:
        # 
        # *   **VBR**
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The time window for collecting log data. Unit: seconds. Valid values:
        # 
        # - **60**
        # - **600**
        # 
        # Default value: **600**.
        self.interval = interval
        # The Logstore that stores the captured traffic data.
        # 
        # *   If a Logstore is already created in the selected region, enter the name of the Logstore.
        # *   If no Logstores are created in the selected region, enter a name and the system automatically creates a Logstore. The name of the Logstore. The name must meet the following requirements:
        # *   The name must be unique in a project.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.log_store_name = log_store_name
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
        # 
        # This parameter is required.
        self.project_name = project_name
        self.resource_group_id = resource_group_id
        # The sampling proportion. Valid values:
        # 
        # - **1:4096**
        # - **1:2048**
        # - **1:1024**
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        self.tag = tag
        self.target_sls_region_id = target_sls_region_id
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

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_sls_region_id is not None:
            result['TargetSlsRegionId'] = self.target_sls_region_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFlowLogRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetSlsRegionId') is not None:
            self.target_sls_region_id = m.get('TargetSlsRegionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateFlowLogRequestTag(DaraModel):
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


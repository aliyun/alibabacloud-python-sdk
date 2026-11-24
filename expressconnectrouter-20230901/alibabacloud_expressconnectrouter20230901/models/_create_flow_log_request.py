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
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # The description of the flow log.
        # > The description can be empty or 0 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether the request is only a dry run. Valid values:
        # 
        # - **true**: Performs a dry run without modifying EPS resources.
        # 
        # - **false** (default): Sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The name of the flow log.
        # > The name can be empty or 0 to 128 characters in length. It cannot start with http:// or https://.
        self.flow_log_name = flow_log_name
        # The instance ID of the VBR.
        # 
        # >The VBR instance must be created by calling the CreateVirtualBorderRouter operation of the Vpc/2016-04-28 API version. The prerequisite is that a physical connection exists.
        # >The VBR instance must be mounted as a child instance to the Express Connect Router (ECR) corresponding to EcrId by calling AttachExpressConnectRouterChildInstance, and the mount status must be ACTIVE before you can create a flow log. You can call DescribeExpressConnectRouterChildInstance to query the mount status of the child instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the network instance. Valid values:
        # - **VBR**: virtual border router (VBR) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The duration of the capture window for traffic captured by the flow log. Unit: seconds. Valid values:
        # 
        # - **60** 
        # - **600**
        # 
        # Default value: **600**.
        self.interval = interval
        # The name of the Logstore used to store catch traffic.
        # - If you have already created a Logstore in the current region, you can enter the name of the existing Logstore.
        # - If you have not created a Logstore in the current region, you can specify a custom name for the Logstore, and the system will automatically create the Logstore. The naming rules for the Logstore name are as follows:
        # 
        # - The Logstore name must be unique within the same project.
        # - It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # - It must start and end with a lowercase letter or a digit.
        # - It must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.log_store_name = log_store_name
        # The name of the Simple Log Service project used to store catch traffic.
        # - If you have already created a project in the current region, you can enter the name of the existing project.
        # - If you have not created a project in the current region, you can specify a custom name for the project, and the system will automatically create the project.
        # 
        # 
        # The project name must be globally unique within an Alibaba Cloud region and cannot be modified after creation. The naming rules are as follows:
        #    
        # - The project name must be globally unique.
        # - It can contain only lowercase
        # - letters, digits, and hyphens (-).
        # - It must start and end with a lowercase letter or a digit.
        # - It must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The ID of the resource group to which the flow log instance belongs.
        self.resource_group_id = resource_group_id
        # The sampling ratio. Valid values:
        # 
        # - **1:4096**
        # - **1:2048**
        # - **1:1024**
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        # The tags.
        # 
        # You can add up to 20 tags.
        self.tag = tag
        # The region where the project to which logs are delivered resides. You only need to specify this parameter for cross-region log delivery. You do not need to specify this parameter for same-region log delivery.
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
        # The tag key of the resource. If you specify this parameter, it cannot be an empty string. It can be up to 128 characters in length, and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value. Valid values of N: 1 to 20. If you specify this parameter, it can be an empty string. It can be up to 128 characters in length, and cannot start with acs:. It cannot contain http:// or https://.
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


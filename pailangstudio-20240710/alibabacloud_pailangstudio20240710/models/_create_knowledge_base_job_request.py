# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class CreateKnowledgeBaseJobRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        description: str = None,
        ecs_specs: List[main_models.CreateKnowledgeBaseJobRequestEcsSpecs] = None,
        embedding_config: main_models.CreateKnowledgeBaseJobRequestEmbeddingConfig = None,
        job_action: str = None,
        max_running_time_in_seconds: int = None,
        resource_id: str = None,
        user_vpc: main_models.CreateKnowledgeBaseJobRequestUserVpc = None,
        workspace_id: str = None,
    ):
        # Workspace visibility. Possible values are:
        # 
        # *   PRIVATE: In this workspace, it is visible only to you and the administrator.
        # *   PUBLIC: This workspace is visible to all users.
        self.accessibility = accessibility
        # Knowledge base task description.
        self.description = description
        # Task Run Resource Configuration List Documentation and structured Knowledge Base contain only one Element and the Type is Worker. Images and Videos Knowledge Base contain two Elements and the Types are Head and Worker.
        self.ecs_specs = ecs_specs
        # Index Configuration.
        self.embedding_config = embedding_config
        # The type of the task operation.
        # 
        # *   SyncIndex: updates the knowledge base index
        self.job_action = job_action
        # The maximum running time for the task, in seconds.
        self.max_running_time_in_seconds = max_running_time_in_seconds
        # The resource group ID. This field being empty or public-cluster indicates a public resource.
        self.resource_id = resource_id
        # Task Run VPC Info.
        self.user_vpc = user_vpc
        # The ID of the workspace. For information on how to obtain the workspace ID, see ListWorkspaces.[](~~449124~~)
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ecs_specs:
            for v1 in self.ecs_specs:
                 if v1:
                    v1.validate()
        if self.embedding_config:
            self.embedding_config.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.description is not None:
            result['Description'] = self.description

        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k1 in self.ecs_specs:
                result['EcsSpecs'].append(k1.to_map() if k1 else None)

        if self.embedding_config is not None:
            result['EmbeddingConfig'] = self.embedding_config.to_map()

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k1 in m.get('EcsSpecs'):
                temp_model = main_models.CreateKnowledgeBaseJobRequestEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseJobRequestEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('EmbeddingConfig'))

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateKnowledgeBaseJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateKnowledgeBaseJobRequestUserVpc(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of a security group.
        self.security_group_id = security_group_id
        # The vSwitch IDs.
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateKnowledgeBaseJobRequestEmbeddingConfig(DaraModel):
    def __init__(
        self,
        batch_size: int = None,
        concurrency: int = None,
    ):
        # Index batch size. The knowledge base for documentation and structured data types is effective.
        self.batch_size = batch_size
        # Index concurrency. Image and video type knowledge base is valid.
        self.concurrency = concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        return self

class CreateKnowledgeBaseJobRequestEcsSpecs(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        driver: str = None,
        gpu: int = None,
        gputype: str = None,
        instance_type: str = None,
        memory: int = None,
        pod_count: int = None,
        shared_memory: int = None,
        type: str = None,
    ):
        # The number of CPU cores. You must specify the resource quota to use.
        self.cpu = cpu
        # The version of the GPU driver.
        self.driver = driver
        # The number of GPU cards. You must specify the resource quota to use.
        self.gpu = gpu
        # GPU Class
        self.gputype = gputype
        # The name of the instance type. Use of public resources must be filled in.
        self.instance_type = instance_type
        # The memory size, in GB. You must specify the resource quota to use.
        self.memory = memory
        # The number of replicas.
        self.pod_count = pod_count
        # The Shared Memory Capacity. Unit: GB. You must specify the resource quota to use.
        self.shared_memory = shared_memory
        # The type of the node. Possible values are Head and Worker.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.driver is not None:
            result['Driver'] = self.driver

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBaseJob(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        description: str = None,
        ecs_specs: List[main_models.KnowledgeBaseJobEcsSpecs] = None,
        embedding_config: main_models.KnowledgeBaseJobEmbeddingConfig = None,
        error_message: str = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modified_time: str = None,
        job_action: str = None,
        knowledge_base_id: str = None,
        knowledge_base_job_id: str = None,
        knowledge_base_job_result: main_models.KnowledgeBaseJobKnowledgeBaseJobResult = None,
        max_running_time_in_seconds: int = None,
        pipeline_run_info: main_models.KnowledgeBaseJobPipelineRunInfo = None,
        resource_id: str = None,
        status: str = None,
        user_vpc: main_models.KnowledgeBaseJobUserVpc = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.creator = creator
        self.description = description
        self.ecs_specs = ecs_specs
        self.embedding_config = embedding_config
        self.error_message = error_message
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_modified_time = gmt_modified_time
        self.job_action = job_action
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_base_job_id = knowledge_base_job_id
        self.knowledge_base_job_result = knowledge_base_job_result
        self.max_running_time_in_seconds = max_running_time_in_seconds
        self.pipeline_run_info = pipeline_run_info
        self.resource_id = resource_id
        self.status = status
        self.user_vpc = user_vpc
        self.workspace_id = workspace_id

    def validate(self):
        if self.ecs_specs:
            for v1 in self.ecs_specs:
                 if v1:
                    v1.validate()
        if self.embedding_config:
            self.embedding_config.validate()
        if self.knowledge_base_job_result:
            self.knowledge_base_job_result.validate()
        if self.pipeline_run_info:
            self.pipeline_run_info.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k1 in self.ecs_specs:
                result['EcsSpecs'].append(k1.to_map() if k1 else None)

        if self.embedding_config is not None:
            result['EmbeddingConfig'] = self.embedding_config.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_base_job_id is not None:
            result['KnowledgeBaseJobId'] = self.knowledge_base_job_id

        if self.knowledge_base_job_result is not None:
            result['KnowledgeBaseJobResult'] = self.knowledge_base_job_result.to_map()

        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds

        if self.pipeline_run_info is not None:
            result['PipelineRunInfo'] = self.pipeline_run_info.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k1 in m.get('EcsSpecs'):
                temp_model = main_models.KnowledgeBaseJobEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.KnowledgeBaseJobEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('EmbeddingConfig'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeBaseJobId') is not None:
            self.knowledge_base_job_id = m.get('KnowledgeBaseJobId')

        if m.get('KnowledgeBaseJobResult') is not None:
            temp_model = main_models.KnowledgeBaseJobKnowledgeBaseJobResult()
            self.knowledge_base_job_result = temp_model.from_map(m.get('KnowledgeBaseJobResult'))

        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')

        if m.get('PipelineRunInfo') is not None:
            temp_model = main_models.KnowledgeBaseJobPipelineRunInfo()
            self.pipeline_run_info = temp_model.from_map(m.get('PipelineRunInfo'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserVpc') is not None:
            temp_model = main_models.KnowledgeBaseJobUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class KnowledgeBaseJobUserVpc(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # 安全组ID
        self.security_group_id = security_group_id
        # 交换机ID
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

class KnowledgeBaseJobPipelineRunInfo(DaraModel):
    def __init__(
        self,
        pipeline_run_id: str = None,
    ):
        # PaiFlow工作流运行ID
        self.pipeline_run_id = pipeline_run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        return self

class KnowledgeBaseJobKnowledgeBaseJobResult(DaraModel):
    def __init__(
        self,
        add_chunk_count: int = None,
        delete_chunk_count: int = None,
        total_file_count: int = None,
    ):
        # 增加Chunk数量
        self.add_chunk_count = add_chunk_count
        # 删除Chunk数量
        self.delete_chunk_count = delete_chunk_count
        # 总处理文件数
        self.total_file_count = total_file_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_chunk_count is not None:
            result['AddChunkCount'] = self.add_chunk_count

        if self.delete_chunk_count is not None:
            result['DeleteChunkCount'] = self.delete_chunk_count

        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddChunkCount') is not None:
            self.add_chunk_count = m.get('AddChunkCount')

        if m.get('DeleteChunkCount') is not None:
            self.delete_chunk_count = m.get('DeleteChunkCount')

        if m.get('TotalFileCount') is not None:
            self.total_file_count = m.get('TotalFileCount')

        return self

class KnowledgeBaseJobEmbeddingConfig(DaraModel):
    def __init__(
        self,
        batch_size: int = None,
        concurrency: int = None,
    ):
        # Embedding分批大小
        self.batch_size = batch_size
        # Embedding并发数
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

class KnowledgeBaseJobEcsSpecs(DaraModel):
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
        # CPU核数
        self.cpu = cpu
        # 驱动版本
        self.driver = driver
        # GPU卡数
        self.gpu = gpu
        # GPU类型
        self.gputype = gputype
        # 机型名称
        self.instance_type = instance_type
        # 内存大小
        self.memory = memory
        # 副本数量
        self.pod_count = pod_count
        # 共享内存容量
        self.shared_memory = shared_memory
        # 节点类型
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


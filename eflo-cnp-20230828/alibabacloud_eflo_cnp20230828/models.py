# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class DataResultsTaskIndividualResultMapValue(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
        hostname: str = None,
        pod_name: str = None,
        gpu_num: int = None,
        gpu_name: str = None,
        warning_flag: bool = None,
        warning_msg: str = None,
        error_flag: bool = None,
        error_msg: str = None,
        tflops: float = None,
        samples_per_second: float = None,
    ):
        # Experiment ID
        self.experiment_id = experiment_id
        # Host IP
        self.hostname = hostname
        # Pod name
        self.pod_name = pod_name
        # GPU数量
        self.gpu_num = gpu_num
        # GPU名称
        self.gpu_name = gpu_name
        # Whether there is a warning
        self.warning_flag = warning_flag
        # Warning message
        self.warning_msg = warning_msg
        # Whether there is an error
        self.error_flag = error_flag
        # Error message
        self.error_msg = error_msg
        # TFLOPS value
        self.tflops = tflops
        # Throughput
        self.samples_per_second = samples_per_second

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # Region Id
        self.region_id = region_id
        # The resource group id.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource id.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request Id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentPlanRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateExperimentPlanRequest(TeaModel):
    def __init__(
        self,
        external_params: Dict[str, Any] = None,
        plan_template_name: str = None,
        resource_group_id: str = None,
        resource_id: int = None,
        tag: List[CreateExperimentPlanRequestTag] = None,
        template_id: int = None,
    ):
        # Additional parameters
        self.external_params = external_params
        # Plan Template Name
        self.plan_template_name = plan_template_name
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource ID
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource tags
        self.tag = tag
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_params is not None:
            result['ExternalParams'] = self.external_params
        if self.plan_template_name is not None:
            result['PlanTemplateName'] = self.plan_template_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalParams') is not None:
            self.external_params = m.get('ExternalParams')
        if m.get('PlanTemplateName') is not None:
            self.plan_template_name = m.get('PlanTemplateName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateExperimentPlanRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateExperimentPlanShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateExperimentPlanShrinkRequest(TeaModel):
    def __init__(
        self,
        external_params_shrink: str = None,
        plan_template_name: str = None,
        resource_group_id: str = None,
        resource_id: int = None,
        tag: List[CreateExperimentPlanShrinkRequestTag] = None,
        template_id: int = None,
    ):
        # Additional parameters
        self.external_params_shrink = external_params_shrink
        # Plan Template Name
        self.plan_template_name = plan_template_name
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource ID
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource tags
        self.tag = tag
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_params_shrink is not None:
            result['ExternalParams'] = self.external_params_shrink
        if self.plan_template_name is not None:
            result['PlanTemplateName'] = self.plan_template_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalParams') is not None:
            self.external_params_shrink = m.get('ExternalParams')
        if m.get('PlanTemplateName') is not None:
            self.plan_template_name = m.get('PlanTemplateName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateExperimentPlanShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateExperimentPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateExperimentPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentPlanTemplateRequestTemplatePipelineEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation count
        # 
        # This parameter is required.
        self.cpu_per_worker = cpu_per_worker
        # CUDA Version
        self.cuda_version = cuda_version
        # GPU Driver Version
        self.gpu_driver_version = gpu_driver_version
        # GPU allocation count
        # 
        # This parameter is required.
        self.gpu_per_worker = gpu_per_worker
        # Memory (GB) allocation count
        # 
        # This parameter is required.
        self.memory_per_worker = memory_per_worker
        # NCCL Version
        self.ncclversion = ncclversion
        # PyTorch Version
        self.py_torch_version = py_torch_version
        # Shared Memory (GB) allocation count
        # 
        # This parameter is required.
        self.share_memory = share_memory
        # Number of nodes
        # 
        # This parameter is required.
        self.worker_num = worker_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class CreateExperimentPlanTemplateRequestTemplatePipeline(TeaModel):
    def __init__(
        self,
        env_params: CreateExperimentPlanTemplateRequestTemplatePipelineEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured Environment Parameters
        # 
        # This parameter is required.
        self.env_params = env_params
        # Node Order Number
        # 
        # This parameter is required.
        self.pipeline_order = pipeline_order
        # Usage Scenario, e.g., "baseline"
        # 
        # This parameter is required.
        self.scene = scene
        # Configured Workload Parameters
        self.setting_params = setting_params
        # Workload ID
        # 
        # This parameter is required.
        self.workload_id = workload_id
        # Workload Name
        # 
        # This parameter is required.
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = CreateExperimentPlanTemplateRequestTemplatePipelineEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class CreateExperimentPlanTemplateRequest(TeaModel):
    def __init__(
        self,
        privacy_level: str = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline: List[CreateExperimentPlanTemplateRequestTemplatePipeline] = None,
    ):
        # Privacy Level
        # 
        # This parameter is required.
        self.privacy_level = privacy_level
        # Template Description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template Name
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template Pipeline
        # 
        # This parameter is required.
        self.template_pipeline = template_pipeline

    def validate(self):
        if self.template_pipeline:
            for k in self.template_pipeline:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['TemplatePipeline'] = []
        if self.template_pipeline is not None:
            for k in self.template_pipeline:
                result['TemplatePipeline'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.template_pipeline = []
        if m.get('TemplatePipeline') is not None:
            for k in m.get('TemplatePipeline'):
                temp_model = CreateExperimentPlanTemplateRequestTemplatePipeline()
                self.template_pipeline.append(temp_model.from_map(k))
        return self


class CreateExperimentPlanTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        privacy_level: str = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline_shrink: str = None,
    ):
        # Privacy Level
        # 
        # This parameter is required.
        self.privacy_level = privacy_level
        # Template Description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template Name
        # 
        # This parameter is required.
        self.template_name = template_name
        # Template Pipeline
        # 
        # This parameter is required.
        self.template_pipeline_shrink = template_pipeline_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_pipeline_shrink is not None:
            result['TemplatePipeline'] = self.template_pipeline_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplatePipeline') is not None:
            self.template_pipeline_shrink = m.get('TemplatePipeline')
        return self


class CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU Allocation
        self.cpu_per_worker = cpu_per_worker
        # cudaVersion
        self.cuda_version = cuda_version
        # GPU Driver Version
        self.gpu_driver_version = gpu_driver_version
        # GPU Allocation
        self.gpu_per_worker = gpu_per_worker
        # Memory (GB) Allocation
        self.memory_per_worker = memory_per_worker
        # NCCL Version
        self.ncclversion = ncclversion
        # PyTorch Version
        self.py_torch_version = py_torch_version
        # Shared Memory (GB) Allocation
        self.share_memory = share_memory
        # Number of Nodes
        self.worker_num = worker_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam(TeaModel):
    def __init__(
        self,
        env_params: CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured Environment Parameters
        self.env_params = env_params
        # Pipeline Order
        self.pipeline_order = pipeline_order
        # Usage Scenario, e.g., "baseline"
        self.scene = scene
        # Configured Workload Parameters
        self.setting_params = setting_params
        # Workload ID
        self.workload_id = workload_id
        # Workload Name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class CreateExperimentPlanTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_uid: int = None,
        is_delete: int = None,
        privacy_level: str = None,
        template_code: int = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline_param: List[CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam] = None,
        update_time: str = None,
        version_id: int = None,
    ):
        # Creation Time
        self.create_time = create_time
        # Primary Account UID
        self.creator_uid = creator_uid
        # Is Deleted
        self.is_delete = is_delete
        # Privacy Level
        self.privacy_level = privacy_level
        # Template Code
        self.template_code = template_code
        # Template Description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template Name
        self.template_name = template_name
        # Template Pipeline
        self.template_pipeline_param = template_pipeline_param
        # Update Time
        self.update_time = update_time
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.template_pipeline_param:
            for k in self.template_pipeline_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['TemplatePipelineParam'] = []
        if self.template_pipeline_param is not None:
            for k in self.template_pipeline_param:
                result['TemplatePipelineParam'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.template_pipeline_param = []
        if m.get('TemplatePipelineParam') is not None:
            for k in m.get('TemplatePipelineParam'):
                temp_model = CreateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam()
                self.template_pipeline_param.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateExperimentPlanTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: CreateExperimentPlanTemplateResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access Denied Detail
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # total
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = CreateExperimentPlanTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateExperimentPlanTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExperimentPlanTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentPlanTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequestMachineTypes(TeaModel):
    def __init__(
        self,
        bond_num: int = None,
        cpu_info: str = None,
        disk_info: str = None,
        gpu_info: str = None,
        memory_info: str = None,
        name: str = None,
        network_info: str = None,
        network_mode: str = None,
        node_count: int = None,
        type: str = None,
    ):
        # Number of Network Bonds
        self.bond_num = bond_num
        # CPU Information
        # 
        # This parameter is required.
        self.cpu_info = cpu_info
        # Disk Information
        self.disk_info = disk_info
        # GPU Information
        # 
        # This parameter is required.
        self.gpu_info = gpu_info
        # Memory Information
        self.memory_info = memory_info
        # Specification Name
        self.name = name
        # Network Information
        self.network_info = network_info
        # Network Mode
        self.network_mode = network_mode
        # Number of Nodes
        self.node_count = node_count
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num
        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info
        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info
        if self.name is not None:
            result['Name'] = self.name
        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNum') is not None:
            self.bond_num = m.get('BondNum')
        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')
        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateResourceRequestUserAccessParam(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        endpoint: str = None,
        workspace_id: str = None,
    ):
        # User ID
        # 
        # This parameter is required.
        self.access_id = access_id
        # User Key
        # 
        # This parameter is required.
        self.access_key = access_key
        # Endpoint
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # Workspace ID
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        cluster_desc: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        machine_types: CreateResourceRequestMachineTypes = None,
        user_access_param: CreateResourceRequestUserAccessParam = None,
    ):
        # Cluster Description
        self.cluster_desc = cluster_desc
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Cluster Name
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # Machine Types
        # 
        # This parameter is required.
        self.machine_types = machine_types
        # User Access Parameters
        # 
        # This parameter is required.
        self.user_access_param = user_access_param

    def validate(self):
        if self.machine_types:
            self.machine_types.validate()
        if self.user_access_param:
            self.user_access_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_desc is not None:
            result['ClusterDesc'] = self.cluster_desc
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types.to_map()
        if self.user_access_param is not None:
            result['UserAccessParam'] = self.user_access_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDesc') is not None:
            self.cluster_desc = m.get('ClusterDesc')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MachineTypes') is not None:
            temp_model = CreateResourceRequestMachineTypes()
            self.machine_types = temp_model.from_map(m['MachineTypes'])
        if m.get('UserAccessParam') is not None:
            temp_model = CreateResourceRequestUserAccessParam()
            self.user_access_param = temp_model.from_map(m['UserAccessParam'])
        return self


class CreateResourceShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_desc: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        machine_types_shrink: str = None,
        user_access_param_shrink: str = None,
    ):
        # Cluster Description
        self.cluster_desc = cluster_desc
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Cluster Name
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # Machine Types
        # 
        # This parameter is required.
        self.machine_types_shrink = machine_types_shrink
        # User Access Parameters
        # 
        # This parameter is required.
        self.user_access_param_shrink = user_access_param_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_desc is not None:
            result['ClusterDesc'] = self.cluster_desc
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.machine_types_shrink is not None:
            result['MachineTypes'] = self.machine_types_shrink
        if self.user_access_param_shrink is not None:
            result['UserAccessParam'] = self.user_access_param_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDesc') is not None:
            self.cluster_desc = m.get('ClusterDesc')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MachineTypes') is not None:
            self.machine_types_shrink = m.get('MachineTypes')
        if m.get('UserAccessParam') is not None:
            self.user_access_param_shrink = m.get('UserAccessParam')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total Count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
        resource_group_id: str = None,
    ):
        # Plan ID
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # Resource Group Id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteExperimentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total count of queries
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: int = None,
    ):
        # Plan ID
        # 
        # This parameter is required.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteExperimentPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteExperimentPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentPlanTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
    ):
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteExperimentPlanTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total Count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteExperimentPlanTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExperimentPlanTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentPlanTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
        resource_group_id: str = None,
    ):
        # Experiment ID
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # Resource Group Id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetExperimentResponseBodyDataEnvParamsResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
    ):
        # Node name
        self.node_name = node_name
        # Requested CPU
        self.request_cpu = request_cpu
        # Requested GPU
        self.request_gpu = request_gpu
        # Requested memory
        self.request_memory = request_memory
        # Total CPU
        self.total_cpu = total_cpu
        # Total GPU
        self.total_gpu = total_gpu
        # Total memory
        self.total_memory = total_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        return self


class GetExperimentResponseBodyDataEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        extend_param: Dict[str, str] = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        resource_nodes: List[GetExperimentResponseBodyDataEnvParamsResourceNodes] = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation number
        self.cpu_per_worker = cpu_per_worker
        # cudaVersion
        self.cuda_version = cuda_version
        # Additional parameters
        self.extend_param = extend_param
        # GPU driver version
        self.gpu_driver_version = gpu_driver_version
        # GPU allocation number
        self.gpu_per_worker = gpu_per_worker
        # Memory Per Worker
        self.memory_per_worker = memory_per_worker
        # NCCL version
        self.ncclversion = ncclversion
        # PyTorch version
        self.py_torch_version = py_torch_version
        # Specified nodes
        self.resource_nodes = resource_nodes
        # Share Memory
        self.share_memory = share_memory
        # Worker number
        self.worker_num = worker_num

    def validate(self):
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = GetExperimentResponseBodyDataEnvParamsResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class GetExperimentResponseBodyDataResourceMachineType(TeaModel):
    def __init__(
        self,
        bond_num: int = None,
        cpu_info: str = None,
        disk_info: str = None,
        gpu_info: str = None,
        memory_info: str = None,
        name: str = None,
        network_info: str = None,
        network_mode: str = None,
        node_count: int = None,
        type: str = None,
    ):
        # Number of network bonds
        self.bond_num = bond_num
        # CPU information
        self.cpu_info = cpu_info
        # Disk information
        self.disk_info = disk_info
        # GPU information
        self.gpu_info = gpu_info
        # Memory information
        self.memory_info = memory_info
        # Specification name
        self.name = name
        # Network information
        self.network_info = network_info
        # Network mode
        self.network_mode = network_mode
        # Number of nodes
        self.node_count = node_count
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num
        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info
        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info
        if self.name is not None:
            result['Name'] = self.name
        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNum') is not None:
            self.bond_num = m.get('BondNum')
        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')
        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExperimentResponseBodyDataResourceResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # Node name
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetExperimentResponseBodyDataResourceUserAccessParam(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        endpoint: str = None,
        workspace_id: str = None,
    ):
        # User ID
        self.access_id = access_id
        # User key
        self.access_key = access_key
        # Endpoint
        self.endpoint = endpoint
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetExperimentResponseBodyDataResource(TeaModel):
    def __init__(
        self,
        cpu_core_limit: int = None,
        gpu_limit: int = None,
        machine_type: GetExperimentResponseBodyDataResourceMachineType = None,
        max_cpu_core: int = None,
        max_gpu: int = None,
        max_memory: int = None,
        memory_limit: int = None,
        resource_id: int = None,
        resource_name: str = None,
        resource_nodes: List[GetExperimentResponseBodyDataResourceResourceNodes] = None,
        user_access_param: GetExperimentResponseBodyDataResourceUserAccessParam = None,
    ):
        # Used CPU
        self.cpu_core_limit = cpu_core_limit
        # Used GPU
        self.gpu_limit = gpu_limit
        # Instance type
        self.machine_type = machine_type
        # Used memory
        self.max_cpu_core = max_cpu_core
        # Used memory
        self.max_gpu = max_gpu
        # Used memory
        self.max_memory = max_memory
        # Used memory
        self.memory_limit = memory_limit
        # Cluster ID
        self.resource_id = resource_id
        # Cluster name
        self.resource_name = resource_name
        # Resource node list
        self.resource_nodes = resource_nodes
        # User authorization parameters
        self.user_access_param = user_access_param

    def validate(self):
        if self.machine_type:
            self.machine_type.validate()
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()
        if self.user_access_param:
            self.user_access_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['CpuCoreLimit'] = self.cpu_core_limit
        if self.gpu_limit is not None:
            result['GpuLimit'] = self.gpu_limit
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type.to_map()
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_gpu is not None:
            result['MaxGpu'] = self.max_gpu
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.user_access_param is not None:
            result['UserAccessParam'] = self.user_access_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('CpuCoreLimit')
        if m.get('GpuLimit') is not None:
            self.gpu_limit = m.get('GpuLimit')
        if m.get('MachineType') is not None:
            temp_model = GetExperimentResponseBodyDataResourceMachineType()
            self.machine_type = temp_model.from_map(m['MachineType'])
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxGpu') is not None:
            self.max_gpu = m.get('MaxGpu')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = GetExperimentResponseBodyDataResourceResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('UserAccessParam') is not None:
            temp_model = GetExperimentResponseBodyDataResourceUserAccessParam()
            self.user_access_param = temp_model.from_map(m['UserAccessParam'])
        return self


class GetExperimentResponseBodyDataResultsErrorWorker(TeaModel):
    def __init__(
        self,
        error_flag: bool = None,
        error_msg: str = None,
        experiment_id: int = None,
        gpu_name: str = None,
        gpu_num: int = None,
        hostname: str = None,
        pod_name: str = None,
        samples_per_second: float = None,
        tflops: float = None,
        warning_flag: bool = None,
        warning_msg: str = None,
    ):
        # error flag
        self.error_flag = error_flag
        # error message
        self.error_msg = error_msg
        # Experiment ID
        self.experiment_id = experiment_id
        # GPU name
        self.gpu_name = gpu_name
        # Number of GPUs
        self.gpu_num = gpu_num
        # Service address
        self.hostname = hostname
        # Pod name.
        self.pod_name = pod_name
        # Samples Per Second
        self.samples_per_second = samples_per_second
        # TFLOPS
        self.tflops = tflops
        # Whether there is a warning
        self.warning_flag = warning_flag
        # Warning message
        self.warning_msg = warning_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        return self


class GetExperimentResponseBodyDataResultsTaskIndividualResultList(TeaModel):
    def __init__(
        self,
        error_flag: bool = None,
        error_msg: str = None,
        experiment_id: int = None,
        gpu_name: str = None,
        gpu_num: int = None,
        hostname: str = None,
        pod_name: str = None,
        samples_per_second: float = None,
        tflops: float = None,
        warning_flag: bool = None,
        warning_msg: str = None,
    ):
        # Whether there is an error
        self.error_flag = error_flag
        # Error message
        self.error_msg = error_msg
        # 实验ID。
        self.experiment_id = experiment_id
        # GPU name
        self.gpu_name = gpu_name
        # Number of GPUs
        self.gpu_num = gpu_num
        # 节点主机名称。
        self.hostname = hostname
        # Pod名称。
        self.pod_name = pod_name
        # Throughput
        self.samples_per_second = samples_per_second
        # TFLOPS value
        self.tflops = tflops
        # Whether there is a warning
        self.warning_flag = warning_flag
        # Warning message
        self.warning_msg = warning_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        return self


class GetExperimentResponseBodyDataResultsWarningBoundList(TeaModel):
    def __init__(
        self,
        iteration: int = None,
        lower: float = None,
        upper: float = None,
    ):
        # Iteration
        self.iteration = iteration
        # LOWER
        self.lower = lower
        # UPPER
        self.upper = upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iteration is not None:
            result['Iteration'] = self.iteration
        if self.lower is not None:
            result['Lower'] = self.lower
        if self.upper is not None:
            result['Upper'] = self.upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iteration') is not None:
            self.iteration = m.get('Iteration')
        if m.get('Lower') is not None:
            self.lower = m.get('Lower')
        if m.get('Upper') is not None:
            self.upper = m.get('Upper')
        return self


class GetExperimentResponseBodyDataResultsWarningWorker(TeaModel):
    def __init__(
        self,
        error_flag: bool = None,
        error_msg: str = None,
        experiment_id: int = None,
        gpu_name: str = None,
        gpu_num: int = None,
        hostname: str = None,
        pod_name: str = None,
        samples_per_second: float = None,
        tflops: float = None,
        warning_flag: bool = None,
        warning_msg: str = None,
    ):
        # Whether there is an error
        self.error_flag = error_flag
        # Error message
        self.error_msg = error_msg
        # Experiment ID
        self.experiment_id = experiment_id
        # GPU name
        self.gpu_name = gpu_name
        # Number of GPUs
        self.gpu_num = gpu_num
        # Service address
        self.hostname = hostname
        # Pod name.
        self.pod_name = pod_name
        # Throughput
        self.samples_per_second = samples_per_second
        # TFLOPS value
        self.tflops = tflops
        # Whether there is an alarm
        self.warning_flag = warning_flag
        # Alarm message
        self.warning_msg = warning_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        return self


class GetExperimentResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        duration: float = None,
        error_worker: List[GetExperimentResponseBodyDataResultsErrorWorker] = None,
        experiment_id: int = None,
        mfu: float = None,
        samples_per_second: float = None,
        seconds_per_iteration: float = None,
        task_individual_result_list: List[GetExperimentResponseBodyDataResultsTaskIndividualResultList] = None,
        task_individual_result_map: Dict[str, List[DataResultsTaskIndividualResultMapValue]] = None,
        warning_bound_list: List[GetExperimentResponseBodyDataResultsWarningBoundList] = None,
        warning_worker: List[GetExperimentResponseBodyDataResultsWarningWorker] = None,
    ):
        # Duration
        self.duration = duration
        # Error node
        self.error_worker = error_worker
        # Parameter name
        self.experiment_id = experiment_id
        # MFU
        self.mfu = mfu
        # Samples Per Second
        self.samples_per_second = samples_per_second
        # Seconds per iteration
        self.seconds_per_iteration = seconds_per_iteration
        # Task individual result list
        self.task_individual_result_list = task_individual_result_list
        # Invalid task results
        self.task_individual_result_map = task_individual_result_map
        # Warning bound list
        self.warning_bound_list = warning_bound_list
        # Warning worker
        self.warning_worker = warning_worker

    def validate(self):
        if self.error_worker:
            for k in self.error_worker:
                if k:
                    k.validate()
        if self.task_individual_result_list:
            for k in self.task_individual_result_list:
                if k:
                    k.validate()
        if self.task_individual_result_map:
            for v in self.task_individual_result_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()
        if self.warning_bound_list:
            for k in self.warning_bound_list:
                if k:
                    k.validate()
        if self.warning_worker:
            for k in self.warning_worker:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        result['ErrorWorker'] = []
        if self.error_worker is not None:
            for k in self.error_worker:
                result['ErrorWorker'].append(k.to_map() if k else None)
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.mfu is not None:
            result['Mfu'] = self.mfu
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.seconds_per_iteration is not None:
            result['SecondsPerIteration'] = self.seconds_per_iteration
        result['TaskIndividualResultList'] = []
        if self.task_individual_result_list is not None:
            for k in self.task_individual_result_list:
                result['TaskIndividualResultList'].append(k.to_map() if k else None)
        result['TaskIndividualResultMap'] = {}
        if self.task_individual_result_map is not None:
            for k, v in self.task_individual_result_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['TaskIndividualResultMap'][k] = l1
        result['WarningBoundList'] = []
        if self.warning_bound_list is not None:
            for k in self.warning_bound_list:
                result['WarningBoundList'].append(k.to_map() if k else None)
        result['WarningWorker'] = []
        if self.warning_worker is not None:
            for k in self.warning_worker:
                result['WarningWorker'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.error_worker = []
        if m.get('ErrorWorker') is not None:
            for k in m.get('ErrorWorker'):
                temp_model = GetExperimentResponseBodyDataResultsErrorWorker()
                self.error_worker.append(temp_model.from_map(k))
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Mfu') is not None:
            self.mfu = m.get('Mfu')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('SecondsPerIteration') is not None:
            self.seconds_per_iteration = m.get('SecondsPerIteration')
        self.task_individual_result_list = []
        if m.get('TaskIndividualResultList') is not None:
            for k in m.get('TaskIndividualResultList'):
                temp_model = GetExperimentResponseBodyDataResultsTaskIndividualResultList()
                self.task_individual_result_list.append(temp_model.from_map(k))
        self.task_individual_result_map = {}
        if m.get('TaskIndividualResultMap') is not None:
            for k, v in m.get('TaskIndividualResultMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataResultsTaskIndividualResultMapValue()
                    l1.append(temp_model.from_map(k1))
                self.task_individual_result_map['k'] = l1
        self.warning_bound_list = []
        if m.get('WarningBoundList') is not None:
            for k in m.get('WarningBoundList'):
                temp_model = GetExperimentResponseBodyDataResultsWarningBoundList()
                self.warning_bound_list.append(temp_model.from_map(k))
        self.warning_worker = []
        if m.get('WarningWorker') is not None:
            for k in m.get('WarningWorker'):
                temp_model = GetExperimentResponseBodyDataResultsWarningWorker()
                self.warning_worker.append(temp_model.from_map(k))
        return self


class GetExperimentResponseBodyDataTask(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: int = None,
        params: Dict[str, str] = None,
        scene: str = None,
        start_time: int = None,
        status: str = None,
        task_id: int = None,
        update_time: int = None,
    ):
        # Creation time
        self.create_time = create_time
        # End time
        self.end_time = end_time
        # Experiment parameters
        self.params = params
        # Scene
        self.scene = scene
        # Start time
        self.start_time = start_time
        # Status
        self.status = status
        # Task ID
        self.task_id = task_id
        # Update time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.params is not None:
            result['Params'] = self.params
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetExperimentResponseBodyDataWorkloadParamSettings(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_regex: str = None,
        param_type: str = None,
        param_value: str = None,
    ):
        # Default parameter value
        self.default_value = default_value
        # Parameter description
        self.param_desc = param_desc
        # Parameter name
        self.param_name = param_name
        # Parameter regular expression
        self.param_regex = param_regex
        # Parameter type
        self.param_type = param_type
        # Parameter value
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_regex is not None:
            result['ParamRegex'] = self.param_regex
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamRegex') is not None:
            self.param_regex = m.get('ParamRegex')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class GetExperimentResponseBodyDataWorkloadStaticConfig(TeaModel):
    def __init__(
        self,
        frame_work: str = None,
        os: str = None,
        parameters: str = None,
        software_stack: str = None,
    ):
        # Framework
        self.frame_work = frame_work
        # Operating system
        self.os = os
        # Number of parameters
        self.parameters = parameters
        # Software stack
        self.software_stack = software_stack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_work is not None:
            result['FrameWork'] = self.frame_work
        if self.os is not None:
            result['Os'] = self.os
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.software_stack is not None:
            result['SoftwareStack'] = self.software_stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameWork') is not None:
            self.frame_work = m.get('FrameWork')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SoftwareStack') is not None:
            self.software_stack = m.get('SoftwareStack')
        return self


class GetExperimentResponseBodyDataWorkload(TeaModel):
    def __init__(
        self,
        default_cpu_per_worker: int = None,
        default_gpu_per_worker: int = None,
        default_memory_per_worker: int = None,
        default_share_memory: int = None,
        family: str = None,
        job_kind: str = None,
        param_settings: List[GetExperimentResponseBodyDataWorkloadParamSettings] = None,
        scene: str = None,
        scope: str = None,
        static_config: GetExperimentResponseBodyDataWorkloadStaticConfig = None,
        version_id: int = None,
        workload_description: str = None,
        workload_id: int = None,
        workload_name: str = None,
        workload_type: str = None,
    ):
        # Default CPU allocation
        self.default_cpu_per_worker = default_cpu_per_worker
        # Default GPU allocation
        self.default_gpu_per_worker = default_gpu_per_worker
        # Default memory (GB) allocation
        self.default_memory_per_worker = default_memory_per_worker
        # Default shared memory (GB) allocation
        self.default_share_memory = default_share_memory
        # Workload cluster, AI, GPU
        self.family = family
        # JobKind
        self.job_kind = job_kind
        # Parameter settings
        self.param_settings = param_settings
        # Workload usage scenario
        self.scene = scene
        # Scope
        self.scope = scope
        # Static configuration
        self.static_config = static_config
        # Version ID
        self.version_id = version_id
        # Workload description
        self.workload_description = workload_description
        # Workload ID
        self.workload_id = workload_id
        # Workload name
        self.workload_name = workload_name
        # Workload name
        self.workload_type = workload_type

    def validate(self):
        if self.param_settings:
            for k in self.param_settings:
                if k:
                    k.validate()
        if self.static_config:
            self.static_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_cpu_per_worker is not None:
            result['DefaultCpuPerWorker'] = self.default_cpu_per_worker
        if self.default_gpu_per_worker is not None:
            result['DefaultGpuPerWorker'] = self.default_gpu_per_worker
        if self.default_memory_per_worker is not None:
            result['DefaultMemoryPerWorker'] = self.default_memory_per_worker
        if self.default_share_memory is not None:
            result['DefaultShareMemory'] = self.default_share_memory
        if self.family is not None:
            result['Family'] = self.family
        if self.job_kind is not None:
            result['JobKind'] = self.job_kind
        result['ParamSettings'] = []
        if self.param_settings is not None:
            for k in self.param_settings:
                result['ParamSettings'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.static_config is not None:
            result['StaticConfig'] = self.static_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.workload_description is not None:
            result['WorkloadDescription'] = self.workload_description
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpuPerWorker') is not None:
            self.default_cpu_per_worker = m.get('DefaultCpuPerWorker')
        if m.get('DefaultGpuPerWorker') is not None:
            self.default_gpu_per_worker = m.get('DefaultGpuPerWorker')
        if m.get('DefaultMemoryPerWorker') is not None:
            self.default_memory_per_worker = m.get('DefaultMemoryPerWorker')
        if m.get('DefaultShareMemory') is not None:
            self.default_share_memory = m.get('DefaultShareMemory')
        if m.get('Family') is not None:
            self.family = m.get('Family')
        if m.get('JobKind') is not None:
            self.job_kind = m.get('JobKind')
        self.param_settings = []
        if m.get('ParamSettings') is not None:
            for k in m.get('ParamSettings'):
                temp_model = GetExperimentResponseBodyDataWorkloadParamSettings()
                self.param_settings.append(temp_model.from_map(k))
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('StaticConfig') is not None:
            temp_model = GetExperimentResponseBodyDataWorkloadStaticConfig()
            self.static_config = temp_model.from_map(m['StaticConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('WorkloadDescription') is not None:
            self.workload_description = m.get('WorkloadDescription')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')
        return self


class GetExperimentResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: str = None,
        env_params: GetExperimentResponseBodyDataEnvParams = None,
        experiment_id: int = None,
        experiment_name: str = None,
        experiment_type: str = None,
        get_params: Dict[str, str] = None,
        resource: GetExperimentResponseBodyDataResource = None,
        resource_name: str = None,
        results: GetExperimentResponseBodyDataResults = None,
        set_params: Dict[str, str] = None,
        start_time: str = None,
        status: str = None,
        task: GetExperimentResponseBodyDataTask = None,
        update_time: int = None,
        workload: GetExperimentResponseBodyDataWorkload = None,
        workload_name: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Task end time
        self.end_time = end_time
        # Running environment parameters
        self.env_params = env_params
        # Experiment ID
        self.experiment_id = experiment_id
        # Experiment name
        self.experiment_name = experiment_name
        # Experiment type
        self.experiment_type = experiment_type
        # Parsed workload parameters
        self.get_params = get_params
        # cluster info
        self.resource = resource
        # Resource name
        self.resource_name = resource_name
        # Task results
        self.results = results
        # Running workload parameters
        self.set_params = set_params
        # Task start time
        self.start_time = start_time
        # Status
        self.status = status
        # Experiment task
        self.task = task
        # Update time
        self.update_time = update_time
        # Workload information
        self.workload = workload
        # Workload name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()
        if self.resource:
            self.resource.validate()
        if self.results:
            self.results.validate()
        if self.task:
            self.task.validate()
        if self.workload:
            self.workload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.experiment_name is not None:
            result['ExperimentName'] = self.experiment_name
        if self.experiment_type is not None:
            result['ExperimentType'] = self.experiment_type
        if self.get_params is not None:
            result['GetParams'] = self.get_params
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.set_params is not None:
            result['SetParams'] = self.set_params
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task is not None:
            result['Task'] = self.task.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.workload is not None:
            result['Workload'] = self.workload.to_map()
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvParams') is not None:
            temp_model = GetExperimentResponseBodyDataEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ExperimentName') is not None:
            self.experiment_name = m.get('ExperimentName')
        if m.get('ExperimentType') is not None:
            self.experiment_type = m.get('ExperimentType')
        if m.get('GetParams') is not None:
            self.get_params = m.get('GetParams')
        if m.get('Resource') is not None:
            temp_model = GetExperimentResponseBodyDataResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Results') is not None:
            temp_model = GetExperimentResponseBodyDataResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('SetParams') is not None:
            self.set_params = m.get('SetParams')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Task') is not None:
            temp_model = GetExperimentResponseBodyDataTask()
            self.task = temp_model.from_map(m['Task'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Workload') is not None:
            temp_model = GetExperimentResponseBodyDataWorkload()
            self.workload = temp_model.from_map(m['Workload'])
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetExperimentResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied detail
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # RequestId
        self.request_id = request_id
        # total
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = GetExperimentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: int = None,
    ):
        # Plan ID
        # 
        # This parameter is required.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class GetExperimentPlanResponseBodyDataPlanPipelineEnvParamsResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
    ):
        # Node name
        self.node_name = node_name
        # Requested CPU
        self.request_cpu = request_cpu
        # Requested GPU
        self.request_gpu = request_gpu
        # Memory of the current request
        self.request_memory = request_memory
        # Total CPU
        self.total_cpu = total_cpu
        # Total GPU
        self.total_gpu = total_gpu
        # Total memory
        self.total_memory = total_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        return self


class GetExperimentPlanResponseBodyDataPlanPipelineEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        extend_param: Dict[str, str] = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        resource_nodes: List[GetExperimentPlanResponseBodyDataPlanPipelineEnvParamsResourceNodes] = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation
        self.cpu_per_worker = cpu_per_worker
        # CUDA version
        self.cuda_version = cuda_version
        # Additional parameters
        self.extend_param = extend_param
        # GPU driver version
        self.gpu_driver_version = gpu_driver_version
        # Number of GPUs allocated
        self.gpu_per_worker = gpu_per_worker
        # Memory GB allocation
        self.memory_per_worker = memory_per_worker
        # NCCL version
        self.ncclversion = ncclversion
        # PyTorch version
        self.py_torch_version = py_torch_version
        # Specified nodes
        self.resource_nodes = resource_nodes
        # Shared memory GB allocation
        self.share_memory = share_memory
        # Number of nodes
        self.worker_num = worker_num

    def validate(self):
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = GetExperimentPlanResponseBodyDataPlanPipelineEnvParamsResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class GetExperimentPlanResponseBodyDataPlanPipeline(TeaModel):
    def __init__(
        self,
        env_params: GetExperimentPlanResponseBodyDataPlanPipelineEnvParams = None,
        pipeline_order: int = None,
        resource_id: int = None,
        resource_name: str = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured environment parameters
        self.env_params = env_params
        # Node order number
        self.pipeline_order = pipeline_order
        # Resource ID
        self.resource_id = resource_id
        # Resource name
        self.resource_name = resource_name
        # Usage scenario, e.g., "baseline"
        self.scene = scene
        # Configured workload parameters
        self.setting_params = setting_params
        # Workload ID
        self.workload_id = workload_id
        # Workload name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = GetExperimentPlanResponseBodyDataPlanPipelineEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class GetExperimentPlanResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetExperimentPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        plan_id: int = None,
        plan_pipeline: List[GetExperimentPlanResponseBodyDataPlanPipeline] = None,
        resource_group_id: str = None,
        resource_id: int = None,
        tags: List[GetExperimentPlanResponseBodyDataTags] = None,
        template_id: int = None,
        template_name: str = None,
        update_time: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Plan ID
        self.plan_id = plan_id
        # Test plan pipeline
        self.plan_pipeline = plan_pipeline
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Associated resource ID
        self.resource_id = resource_id
        # The tag.
        self.tags = tags
        # Associated test plan template ID
        self.template_id = template_id
        # Associated test plan template name
        self.template_name = template_name
        # Update time
        self.update_time = update_time

    def validate(self):
        if self.plan_pipeline:
            for k in self.plan_pipeline:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        result['PlanPipeline'] = []
        if self.plan_pipeline is not None:
            for k in self.plan_pipeline:
                result['PlanPipeline'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        self.plan_pipeline = []
        if m.get('PlanPipeline') is not None:
            for k in m.get('PlanPipeline'):
                temp_model = GetExperimentPlanResponseBodyDataPlanPipeline()
                self.plan_pipeline.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetExperimentPlanResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetExperimentPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetExperimentPlanResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total count of the query
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = GetExperimentPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetExperimentPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentPlanTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
    ):
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
    ):
        # Node name
        self.node_name = node_name
        # 当前请求的cpu
        self.request_cpu = request_cpu
        # Requested GPU
        self.request_gpu = request_gpu
        # Requested memory
        self.request_memory = request_memory
        # Total CPU
        self.total_cpu = total_cpu
        # Total GPU
        self.total_gpu = total_gpu
        # Total memory
        self.total_memory = total_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        return self


class GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        extend_param: Dict[str, str] = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        resource_nodes: List[GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes] = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation
        self.cpu_per_worker = cpu_per_worker
        # CUDA version
        self.cuda_version = cuda_version
        # Additional parameters
        self.extend_param = extend_param
        # GPU driver version
        self.gpu_driver_version = gpu_driver_version
        # GPU allocation
        self.gpu_per_worker = gpu_per_worker
        # Allocated memory in GB
        self.memory_per_worker = memory_per_worker
        # NCCL version
        self.ncclversion = ncclversion
        # PyTorch version
        self.py_torch_version = py_torch_version
        # Specified nodes
        self.resource_nodes = resource_nodes
        # Shared memory in GB
        self.share_memory = share_memory
        # Number of nodes
        self.worker_num = worker_num

    def validate(self):
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParam(TeaModel):
    def __init__(
        self,
        env_params: GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured environment parameters
        self.env_params = env_params
        # Node sequence number
        self.pipeline_order = pipeline_order
        # Usage scenario, e.g., "baseline"
        self.scene = scene
        # Configured workload parameters
        self.setting_params = setting_params
        # Workload ID
        self.workload_id = workload_id
        # Workload Name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class GetExperimentPlanTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_uid: int = None,
        is_delete: int = None,
        privacy_level: str = None,
        template_code: int = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline_param: List[GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParam] = None,
        update_time: str = None,
        version_id: int = None,
    ):
        # Creation Time
        self.create_time = create_time
        # Primary account UID
        self.creator_uid = creator_uid
        # Whether deleted
        self.is_delete = is_delete
        # Privacy Level
        self.privacy_level = privacy_level
        # Template Code
        self.template_code = template_code
        # Template Description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template Name
        self.template_name = template_name
        # Template Pipeline
        self.template_pipeline_param = template_pipeline_param
        # Update Time
        self.update_time = update_time
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.template_pipeline_param:
            for k in self.template_pipeline_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['TemplatePipelineParam'] = []
        if self.template_pipeline_param is not None:
            for k in self.template_pipeline_param:
                result['TemplatePipelineParam'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.template_pipeline_param = []
        if m.get('TemplatePipelineParam') is not None:
            for k in m.get('TemplatePipelineParam'):
                temp_model = GetExperimentPlanTemplateResponseBodyDataTemplatePipelineParam()
                self.template_pipeline_param.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetExperimentPlanTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetExperimentPlanTemplateResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = GetExperimentPlanTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetExperimentPlanTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentPlanTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentPlanTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentResultDataRequest(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
        hostname: str = None,
        resource_group_id: str = None,
        workload_type: str = None,
    ):
        # Experiment ID
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # Hostname
        self.hostname = hostname
        # Resource Group Id
        self.resource_group_id = resource_group_id
        # Workload Type
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')
        return self


class GetExperimentResultDataResponseBodyDataMetricsInfos(TeaModel):
    def __init__(
        self,
        gpu_num: str = None,
        iteration: int = None,
        tflops: float = None,
        timestamp: int = None,
        value: float = None,
    ):
        # GPU
        self.gpu_num = gpu_num
        # Iteration
        self.iteration = iteration
        # TFLOPS
        self.tflops = tflops
        # Operation Timestamp
        self.timestamp = timestamp
        # Metric Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_num is not None:
            result['Gpu_num'] = self.gpu_num
        if self.iteration is not None:
            result['Iteration'] = self.iteration
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gpu_num') is not None:
            self.gpu_num = m.get('Gpu_num')
        if m.get('Iteration') is not None:
            self.iteration = m.get('Iteration')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetExperimentResultDataResponseBodyData(TeaModel):
    def __init__(
        self,
        gpu_num: str = None,
        hostname: str = None,
        metrics_infos: List[GetExperimentResultDataResponseBodyDataMetricsInfos] = None,
        pod_name: str = None,
    ):
        # Number of GPUs
        self.gpu_num = gpu_num
        # Host IP
        self.hostname = hostname
        # List of Metrics Information
        self.metrics_infos = metrics_infos
        # Pod Name
        self.pod_name = pod_name

    def validate(self):
        if self.metrics_infos:
            for k in self.metrics_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        result['MetricsInfos'] = []
        if self.metrics_infos is not None:
            for k in self.metrics_infos:
                result['MetricsInfos'].append(k.to_map() if k else None)
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        self.metrics_infos = []
        if m.get('MetricsInfos') is not None:
            for k in m.get('MetricsInfos'):
                temp_model = GetExperimentResultDataResponseBodyDataMetricsInfos()
                self.metrics_infos.append(temp_model.from_map(k))
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class GetExperimentResultDataResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[GetExperimentResultDataResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access Denied Details
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total Count of Queries
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetExperimentResultDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetExperimentResultDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExperimentResultDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentResultDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID of Lingjun
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetResourceResponseBodyDataMachineType(TeaModel):
    def __init__(
        self,
        bond_num: int = None,
        cpu_info: str = None,
        disk_info: str = None,
        gpu_info: str = None,
        memory_info: str = None,
        name: str = None,
        network_info: str = None,
        network_mode: str = None,
        node_count: int = None,
        type: str = None,
    ):
        # Number of network bonds
        self.bond_num = bond_num
        # CPU information
        self.cpu_info = cpu_info
        # Disk information
        self.disk_info = disk_info
        # GPU information
        self.gpu_info = gpu_info
        # Memory information
        self.memory_info = memory_info
        # Specification name
        self.name = name
        # Network information
        self.network_info = network_info
        # Network mode
        self.network_mode = network_mode
        # Number of nodes
        self.node_count = node_count
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num
        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info
        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info
        if self.name is not None:
            result['Name'] = self.name
        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNum') is not None:
            self.bond_num = m.get('BondNum')
        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')
        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResourceResponseBodyDataResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # Node name
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetResourceResponseBodyDataUserAccessParam(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        endpoint: str = None,
        workspace_id: str = None,
    ):
        # User ID
        self.access_id = access_id
        # User key
        self.access_key = access_key
        # Endpoint
        self.endpoint = endpoint
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_desc: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cpu_core_limit: int = None,
        gpu_limit: int = None,
        machine_type: GetResourceResponseBodyDataMachineType = None,
        max_cpu_core: int = None,
        max_gpu: int = None,
        max_memory: int = None,
        memory_limit: int = None,
        resource_id: int = None,
        resource_nodes: List[GetResourceResponseBodyDataResourceNodes] = None,
        user_access_param: GetResourceResponseBodyDataUserAccessParam = None,
    ):
        # Cluster description
        self.cluster_desc = cluster_desc
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Used CPU
        self.cpu_core_limit = cpu_core_limit
        # Used GPU
        self.gpu_limit = gpu_limit
        # Machine type
        self.machine_type = machine_type
        # Used memory
        self.max_cpu_core = max_cpu_core
        # Used memory
        self.max_gpu = max_gpu
        # Used memory
        self.max_memory = max_memory
        # Used memory
        self.memory_limit = memory_limit
        # Cluster ID
        self.resource_id = resource_id
        # List of resource nodes
        self.resource_nodes = resource_nodes
        # User authorization parameters
        self.user_access_param = user_access_param

    def validate(self):
        if self.machine_type:
            self.machine_type.validate()
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()
        if self.user_access_param:
            self.user_access_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_desc is not None:
            result['ClusterDesc'] = self.cluster_desc
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cpu_core_limit is not None:
            result['CpuCoreLimit'] = self.cpu_core_limit
        if self.gpu_limit is not None:
            result['GpuLimit'] = self.gpu_limit
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type.to_map()
        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core
        if self.max_gpu is not None:
            result['MaxGpu'] = self.max_gpu
        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.user_access_param is not None:
            result['UserAccessParam'] = self.user_access_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDesc') is not None:
            self.cluster_desc = m.get('ClusterDesc')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('CpuCoreLimit')
        if m.get('GpuLimit') is not None:
            self.gpu_limit = m.get('GpuLimit')
        if m.get('MachineType') is not None:
            temp_model = GetResourceResponseBodyDataMachineType()
            self.machine_type = temp_model.from_map(m['MachineType'])
        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')
        if m.get('MaxGpu') is not None:
            self.max_gpu = m.get('MaxGpu')
        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = GetResourceResponseBodyDataResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('UserAccessParam') is not None:
            temp_model = GetResourceResponseBodyDataUserAccessParam()
            self.user_access_param = temp_model.from_map(m['UserAccessParam'])
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetResourceResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total count of the query
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = GetResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePredictResultRequest(TeaModel):
    def __init__(
        self,
        resource_id: int = None,
        template_id: int = None,
    ):
        # Resource ID
        self.resource_id = resource_id
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetResourcePredictResultResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResourcePredictResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourcePredictResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourcePredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkloadRequest(TeaModel):
    def __init__(
        self,
        workload_id: int = None,
    ):
        # Workload ID
        # 
        # This parameter is required.
        self.workload_id = workload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        return self


class GetWorkloadResponseBodyDataParamSettings(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_regex: str = None,
        param_type: str = None,
        param_value: str = None,
    ):
        # Default Parameter Value
        self.default_value = default_value
        # Parameter Description
        self.param_desc = param_desc
        # Parameter Name
        self.param_name = param_name
        # Parameter Regular Expression
        self.param_regex = param_regex
        # Parameter type
        self.param_type = param_type
        # Parameter Value
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_regex is not None:
            result['ParamRegex'] = self.param_regex
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamRegex') is not None:
            self.param_regex = m.get('ParamRegex')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class GetWorkloadResponseBodyDataStaticConfig(TeaModel):
    def __init__(
        self,
        frame_work: str = None,
        os: str = None,
        parameters: str = None,
        software_stack: str = None,
    ):
        # Framework
        self.frame_work = frame_work
        # Operating System
        self.os = os
        # Parameter Volume
        self.parameters = parameters
        # Software Stack
        self.software_stack = software_stack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_work is not None:
            result['FrameWork'] = self.frame_work
        if self.os is not None:
            result['Os'] = self.os
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.software_stack is not None:
            result['SoftwareStack'] = self.software_stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameWork') is not None:
            self.frame_work = m.get('FrameWork')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SoftwareStack') is not None:
            self.software_stack = m.get('SoftwareStack')
        return self


class GetWorkloadResponseBodyData(TeaModel):
    def __init__(
        self,
        default_cpu_per_worker: int = None,
        default_gpu_per_worker: int = None,
        default_memory_per_worker: int = None,
        default_share_memory: int = None,
        family: str = None,
        job_kind: str = None,
        param_settings: List[GetWorkloadResponseBodyDataParamSettings] = None,
        scene: str = None,
        scope: str = None,
        static_config: GetWorkloadResponseBodyDataStaticConfig = None,
        version_id: int = None,
        workload_description: str = None,
        workload_id: int = None,
        workload_name: str = None,
        workload_type: str = None,
    ):
        # Default CPU Allocation per Worker
        self.default_cpu_per_worker = default_cpu_per_worker
        # Default GPU Allocation per Worker
        self.default_gpu_per_worker = default_gpu_per_worker
        # Default Memory (GB) Allocation per Worker
        self.default_memory_per_worker = default_memory_per_worker
        # Default Shared Memory (GB) Allocation
        self.default_share_memory = default_share_memory
        # Workload Cluster, e.g., AI, GPU
        self.family = family
        # Training Job Type
        self.job_kind = job_kind
        # Parameter Settings
        self.param_settings = param_settings
        # Workload Usage Scenario
        self.scene = scene
        # Scope Identifier for Workload Usage
        self.scope = scope
        # Static Configuration
        self.static_config = static_config
        # Version ID
        self.version_id = version_id
        # Workload Description
        self.workload_description = workload_description
        # Workload ID
        self.workload_id = workload_id
        # Workload Name
        self.workload_name = workload_name
        # Workload Type
        self.workload_type = workload_type

    def validate(self):
        if self.param_settings:
            for k in self.param_settings:
                if k:
                    k.validate()
        if self.static_config:
            self.static_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_cpu_per_worker is not None:
            result['DefaultCpuPerWorker'] = self.default_cpu_per_worker
        if self.default_gpu_per_worker is not None:
            result['DefaultGpuPerWorker'] = self.default_gpu_per_worker
        if self.default_memory_per_worker is not None:
            result['DefaultMemoryPerWorker'] = self.default_memory_per_worker
        if self.default_share_memory is not None:
            result['DefaultShareMemory'] = self.default_share_memory
        if self.family is not None:
            result['Family'] = self.family
        if self.job_kind is not None:
            result['JobKind'] = self.job_kind
        result['ParamSettings'] = []
        if self.param_settings is not None:
            for k in self.param_settings:
                result['ParamSettings'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.static_config is not None:
            result['StaticConfig'] = self.static_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.workload_description is not None:
            result['WorkloadDescription'] = self.workload_description
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpuPerWorker') is not None:
            self.default_cpu_per_worker = m.get('DefaultCpuPerWorker')
        if m.get('DefaultGpuPerWorker') is not None:
            self.default_gpu_per_worker = m.get('DefaultGpuPerWorker')
        if m.get('DefaultMemoryPerWorker') is not None:
            self.default_memory_per_worker = m.get('DefaultMemoryPerWorker')
        if m.get('DefaultShareMemory') is not None:
            self.default_share_memory = m.get('DefaultShareMemory')
        if m.get('Family') is not None:
            self.family = m.get('Family')
        if m.get('JobKind') is not None:
            self.job_kind = m.get('JobKind')
        self.param_settings = []
        if m.get('ParamSettings') is not None:
            for k in m.get('ParamSettings'):
                temp_model = GetWorkloadResponseBodyDataParamSettings()
                self.param_settings.append(temp_model.from_map(k))
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('StaticConfig') is not None:
            temp_model = GetWorkloadResponseBodyDataStaticConfig()
            self.static_config = temp_model.from_map(m['StaticConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('WorkloadDescription') is not None:
            self.workload_description = m.get('WorkloadDescription')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')
        return self


class GetWorkloadResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: GetWorkloadResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access Denied Information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # total
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = GetWorkloadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetWorkloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkloadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWorkloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentPlanTemplatesRequest(TeaModel):
    def __init__(
        self,
        privacy_level: str = None,
    ):
        # The sharing level of the template, default is private, options are public and private.
        self.privacy_level = privacy_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        return self


class ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParamEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation
        self.cpu_per_worker = cpu_per_worker
        # Cuda Version
        self.cuda_version = cuda_version
        # The version of the GPU driver.
        self.gpu_driver_version = gpu_driver_version
        # GPU allocation
        self.gpu_per_worker = gpu_per_worker
        # Allocated memory in GB
        self.memory_per_worker = memory_per_worker
        # NCCL Version
        self.ncclversion = ncclversion
        # PyTorch Version
        self.py_torch_version = py_torch_version
        # Allocated shared memory in GB
        self.share_memory = share_memory
        # Number of nodes
        self.worker_num = worker_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParam(TeaModel):
    def __init__(
        self,
        env_params: ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParamEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured environment parameters
        self.env_params = env_params
        # Node sequence number
        self.pipeline_order = pipeline_order
        # Usage scenario, e.g., "baseline"
        self.scene = scene
        # Configured workload parameters
        self.setting_params = setting_params
        # Workload ID
        self.workload_id = workload_id
        # Workload name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParamEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class ListExperimentPlanTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_uid: int = None,
        is_delete: int = None,
        privacy_level: str = None,
        template_code: int = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline_param: List[ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParam] = None,
        update_time: str = None,
        version_id: int = None,
    ):
        # Creation time
        self.create_time = create_time
        # Primary account UID
        self.creator_uid = creator_uid
        # Whether it is deleted
        self.is_delete = is_delete
        # Privacy level
        self.privacy_level = privacy_level
        # The template code.
        self.template_code = template_code
        # Template description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template name
        self.template_name = template_name
        # Template pipeline
        self.template_pipeline_param = template_pipeline_param
        # Update time
        self.update_time = update_time
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.template_pipeline_param:
            for k in self.template_pipeline_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['TemplatePipelineParam'] = []
        if self.template_pipeline_param is not None:
            for k in self.template_pipeline_param:
                result['TemplatePipelineParam'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.template_pipeline_param = []
        if m.get('TemplatePipelineParam') is not None:
            for k in m.get('TemplatePipelineParam'):
                temp_model = ListExperimentPlanTemplatesResponseBodyDataTemplatePipelineParam()
                self.template_pipeline_param.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListExperimentPlanTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListExperimentPlanTemplatesResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListExperimentPlanTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentPlanTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentPlanTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentPlanTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentPlansRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # Tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListExperimentPlansRequest(TeaModel):
    def __init__(
        self,
        creat_time_order: str = None,
        end_time_order: str = None,
        page: int = None,
        plan_task_status: List[str] = None,
        resource_group_id: str = None,
        resource_id: int = None,
        resource_name: List[str] = None,
        size: int = None,
        start_time_order: str = None,
        tag: List[ListExperimentPlansRequestTag] = None,
        template_id: int = None,
    ):
        # Creation Time Sorting Rule
        self.creat_time_order = creat_time_order
        # End Time Sorting Rule
        self.end_time_order = end_time_order
        # Page Number
        self.page = page
        # Execution Status
        self.plan_task_status = plan_task_status
        # Resource Group ID
        self.resource_group_id = resource_group_id
        # Resource ID
        self.resource_id = resource_id
        # Resource
        self.resource_name = resource_name
        # Number of Items
        self.size = size
        # Start Time Sorting Rule
        self.start_time_order = start_time_order
        # The tags.
        self.tag = tag
        # Template Id
        self.template_id = template_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creat_time_order is not None:
            result['CreatTimeOrder'] = self.creat_time_order
        if self.end_time_order is not None:
            result['EndTimeOrder'] = self.end_time_order
        if self.page is not None:
            result['Page'] = self.page
        if self.plan_task_status is not None:
            result['PlanTaskStatus'] = self.plan_task_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time_order is not None:
            result['StartTimeOrder'] = self.start_time_order
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatTimeOrder') is not None:
            self.creat_time_order = m.get('CreatTimeOrder')
        if m.get('EndTimeOrder') is not None:
            self.end_time_order = m.get('EndTimeOrder')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PlanTaskStatus') is not None:
            self.plan_task_status = m.get('PlanTaskStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTimeOrder') is not None:
            self.start_time_order = m.get('StartTimeOrder')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListExperimentPlansRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListExperimentPlansShrinkRequest(TeaModel):
    def __init__(
        self,
        creat_time_order: str = None,
        end_time_order: str = None,
        page: int = None,
        plan_task_status_shrink: str = None,
        resource_group_id: str = None,
        resource_id: int = None,
        resource_name_shrink: str = None,
        size: int = None,
        start_time_order: str = None,
        tag_shrink: str = None,
        template_id: int = None,
    ):
        # Creation Time Sorting Rule
        self.creat_time_order = creat_time_order
        # End Time Sorting Rule
        self.end_time_order = end_time_order
        # Page Number
        self.page = page
        # Execution Status
        self.plan_task_status_shrink = plan_task_status_shrink
        # Resource Group ID
        self.resource_group_id = resource_group_id
        # Resource ID
        self.resource_id = resource_id
        # Resource
        self.resource_name_shrink = resource_name_shrink
        # Number of Items
        self.size = size
        # Start Time Sorting Rule
        self.start_time_order = start_time_order
        # The tags.
        self.tag_shrink = tag_shrink
        # Template Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creat_time_order is not None:
            result['CreatTimeOrder'] = self.creat_time_order
        if self.end_time_order is not None:
            result['EndTimeOrder'] = self.end_time_order
        if self.page is not None:
            result['Page'] = self.page
        if self.plan_task_status_shrink is not None:
            result['PlanTaskStatus'] = self.plan_task_status_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name_shrink is not None:
            result['ResourceName'] = self.resource_name_shrink
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time_order is not None:
            result['StartTimeOrder'] = self.start_time_order
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatTimeOrder') is not None:
            self.creat_time_order = m.get('CreatTimeOrder')
        if m.get('EndTimeOrder') is not None:
            self.end_time_order = m.get('EndTimeOrder')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PlanTaskStatus') is not None:
            self.plan_task_status_shrink = m.get('PlanTaskStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name_shrink = m.get('ResourceName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTimeOrder') is not None:
            self.start_time_order = m.get('StartTimeOrder')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListExperimentPlansResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListExperimentPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        plan_id: int = None,
        plan_task_status: Dict[str, int] = None,
        resource_group_id: str = None,
        resource_id: int = None,
        resource_name: str = None,
        start_time: str = None,
        tags: List[ListExperimentPlansResponseBodyDataTags] = None,
        template_id: int = None,
        template_name: str = None,
        update_time: str = None,
    ):
        # Creation Time
        self.create_time = create_time
        # End Time
        self.end_time = end_time
        # Plan ID
        self.plan_id = plan_id
        # Test Plan Execution Status
        self.plan_task_status = plan_task_status
        # Resource Group ID
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # Associated Resource Name
        self.resource_name = resource_name
        # Start Time
        self.start_time = start_time
        # The tag.
        self.tags = tags
        # Associated Test Plan Template ID
        self.template_id = template_id
        # Associated Test Plan Template Name
        self.template_name = template_name
        # Update Time
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_task_status is not None:
            result['PlanTaskStatus'] = self.plan_task_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanTaskStatus') is not None:
            self.plan_task_status = m.get('PlanTaskStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListExperimentPlansResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListExperimentPlansResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[ListExperimentPlansResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access Denied Detail
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListExperimentPlansResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        order: int = None,
        plan_id: int = None,
        resource_group_id: str = None,
    ):
        # Order
        self.order = order
        # Plan ID
        self.plan_id = plan_id
        # 资源组id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListExperimentsResponseBodyDataEnvParamsResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
    ):
        # Node name
        self.node_name = node_name
        # Requested CPU
        self.request_cpu = request_cpu
        # Requested GPU
        self.request_gpu = request_gpu
        # Requested memory
        self.request_memory = request_memory
        # Total CPU
        self.total_cpu = total_cpu
        # Total GPU
        self.total_gpu = total_gpu
        # Total memory
        self.total_memory = total_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        return self


class ListExperimentsResponseBodyDataEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        extend_param: Dict[str, str] = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        resource_nodes: List[ListExperimentsResponseBodyDataEnvParamsResourceNodes] = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # Number of CPUs allocated
        self.cpu_per_worker = cpu_per_worker
        # CUDA version
        self.cuda_version = cuda_version
        # Additional parameters
        self.extend_param = extend_param
        # GPU driver version
        self.gpu_driver_version = gpu_driver_version
        # Number of GPUs allocated
        self.gpu_per_worker = gpu_per_worker
        # Amount of memory (GB) allocated
        self.memory_per_worker = memory_per_worker
        # NCCL version
        self.ncclversion = ncclversion
        # PyTorch version
        self.py_torch_version = py_torch_version
        # Specified nodes
        self.resource_nodes = resource_nodes
        # Amount of shared memory (GB) allocated
        self.share_memory = share_memory
        # Number of nodes
        self.worker_num = worker_num

    def validate(self):
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = ListExperimentsResponseBodyDataEnvParamsResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class ListExperimentsResponseBodyDataResultsErrorWorker(TeaModel):
    def __init__(
        self,
        error_flag: bool = None,
        error_msg: str = None,
        experiment_id: int = None,
        gpu_name: str = None,
        gpu_num: int = None,
        hostname: str = None,
        pod_name: str = None,
        samples_per_second: float = None,
        tflops: float = None,
        warning_flag: bool = None,
        warning_msg: str = None,
    ):
        # Whether there is an error
        self.error_flag = error_flag
        # Error information
        self.error_msg = error_msg
        # Experiment ID
        self.experiment_id = experiment_id
        # GPU name
        self.gpu_name = gpu_name
        # Number of GPUs
        self.gpu_num = gpu_num
        # Host IP
        self.hostname = hostname
        # Pod name
        self.pod_name = pod_name
        # Throughput
        self.samples_per_second = samples_per_second
        # TFLOPS value
        self.tflops = tflops
        # Whether there is an alarm
        self.warning_flag = warning_flag
        # Alarm information
        self.warning_msg = warning_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        return self


class ListExperimentsResponseBodyDataResultsWarningWorker(TeaModel):
    def __init__(
        self,
        error_flag: bool = None,
        error_msg: str = None,
        experiment_id: int = None,
        gpu_name: str = None,
        gpu_num: int = None,
        hostname: str = None,
        pod_name: str = None,
        samples_per_second: float = None,
        tflops: float = None,
        warning_flag: bool = None,
        warning_msg: str = None,
    ):
        # Whether there is an error
        self.error_flag = error_flag
        # Error message
        self.error_msg = error_msg
        # Experiment ID
        self.experiment_id = experiment_id
        # GPU name
        self.gpu_name = gpu_name
        # Number of GPUs
        self.gpu_num = gpu_num
        # Host IP
        self.hostname = hostname
        # Pod name
        self.pod_name = pod_name
        # Throughput
        self.samples_per_second = samples_per_second
        # TFLOPS value
        self.tflops = tflops
        # Whether there is an alarm
        self.warning_flag = warning_flag
        # Alarm message
        self.warning_msg = warning_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_flag is not None:
            result['ErrorFlag'] = self.error_flag
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.gpu_name is not None:
            result['GpuName'] = self.gpu_name
        if self.gpu_num is not None:
            result['GpuNum'] = self.gpu_num
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.tflops is not None:
            result['Tflops'] = self.tflops
        if self.warning_flag is not None:
            result['WarningFlag'] = self.warning_flag
        if self.warning_msg is not None:
            result['WarningMsg'] = self.warning_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorFlag') is not None:
            self.error_flag = m.get('ErrorFlag')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('GpuName') is not None:
            self.gpu_name = m.get('GpuName')
        if m.get('GpuNum') is not None:
            self.gpu_num = m.get('GpuNum')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('Tflops') is not None:
            self.tflops = m.get('Tflops')
        if m.get('WarningFlag') is not None:
            self.warning_flag = m.get('WarningFlag')
        if m.get('WarningMsg') is not None:
            self.warning_msg = m.get('WarningMsg')
        return self


class ListExperimentsResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        duration: float = None,
        error_worker: List[ListExperimentsResponseBodyDataResultsErrorWorker] = None,
        experiment_id: int = None,
        mfu: float = None,
        samples_per_second: float = None,
        seconds_per_iteration: float = None,
        warning_worker: List[ListExperimentsResponseBodyDataResultsWarningWorker] = None,
    ):
        # Duration
        self.duration = duration
        # Error nodes
        self.error_worker = error_worker
        # Parameter name
        self.experiment_id = experiment_id
        # MFU
        self.mfu = mfu
        # Samples per second
        self.samples_per_second = samples_per_second
        # Seconds per iteration
        self.seconds_per_iteration = seconds_per_iteration
        # Warning worker
        self.warning_worker = warning_worker

    def validate(self):
        if self.error_worker:
            for k in self.error_worker:
                if k:
                    k.validate()
        if self.warning_worker:
            for k in self.warning_worker:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        result['ErrorWorker'] = []
        if self.error_worker is not None:
            for k in self.error_worker:
                result['ErrorWorker'].append(k.to_map() if k else None)
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.mfu is not None:
            result['Mfu'] = self.mfu
        if self.samples_per_second is not None:
            result['SamplesPerSecond'] = self.samples_per_second
        if self.seconds_per_iteration is not None:
            result['SecondsPerIteration'] = self.seconds_per_iteration
        result['WarningWorker'] = []
        if self.warning_worker is not None:
            for k in self.warning_worker:
                result['WarningWorker'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.error_worker = []
        if m.get('ErrorWorker') is not None:
            for k in m.get('ErrorWorker'):
                temp_model = ListExperimentsResponseBodyDataResultsErrorWorker()
                self.error_worker.append(temp_model.from_map(k))
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('Mfu') is not None:
            self.mfu = m.get('Mfu')
        if m.get('SamplesPerSecond') is not None:
            self.samples_per_second = m.get('SamplesPerSecond')
        if m.get('SecondsPerIteration') is not None:
            self.seconds_per_iteration = m.get('SecondsPerIteration')
        self.warning_worker = []
        if m.get('WarningWorker') is not None:
            for k in m.get('WarningWorker'):
                temp_model = ListExperimentsResponseBodyDataResultsWarningWorker()
                self.warning_worker.append(temp_model.from_map(k))
        return self


class ListExperimentsResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        end_time: str = None,
        env_params: ListExperimentsResponseBodyDataEnvParams = None,
        experiment_id: int = None,
        experiment_name: str = None,
        experiment_type: str = None,
        get_params: Dict[str, str] = None,
        resource_name: str = None,
        results: ListExperimentsResponseBodyDataResults = None,
        set_params: Dict[str, str] = None,
        start_time: str = None,
        status: str = None,
        update_time: int = None,
        workload_name: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Task end time
        self.end_time = end_time
        # Environment parameters in operation
        self.env_params = env_params
        # Experiment ID
        self.experiment_id = experiment_id
        # Experiment name
        self.experiment_name = experiment_name
        # Experiment type
        self.experiment_type = experiment_type
        # Parsed load parameters
        self.get_params = get_params
        # Resource name
        self.resource_name = resource_name
        # Task results
        self.results = results
        # Load parameters in operation
        self.set_params = set_params
        # Task start time
        self.start_time = start_time
        # Status
        self.status = status
        # Update time
        self.update_time = update_time
        # Workload name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.experiment_name is not None:
            result['ExperimentName'] = self.experiment_name
        if self.experiment_type is not None:
            result['ExperimentType'] = self.experiment_type
        if self.get_params is not None:
            result['GetParams'] = self.get_params
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.set_params is not None:
            result['SetParams'] = self.set_params
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvParams') is not None:
            temp_model = ListExperimentsResponseBodyDataEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ExperimentName') is not None:
            self.experiment_name = m.get('ExperimentName')
        if m.get('ExperimentType') is not None:
            self.experiment_type = m.get('ExperimentType')
        if m.get('GetParams') is not None:
            self.get_params = m.get('GetParams')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Results') is not None:
            temp_model = ListExperimentsResponseBodyDataResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('SetParams') is not None:
            self.set_params = m.get('SetParams')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[ListExperimentsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListExperimentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key, with n in the range [1, 20].
        self.key = key
        # Tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # Next token for the next query
        self.next_token = next_token
        # ResourceId
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tags to be queried. The value range for N is 1~20.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # ResourceId
        self.resource_id = resource_id
        # Resource type
        self.resource_type = resource_type
        # Tag key
        self.tag_key = tag_key
        # Tag value
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Next token for the next query. An empty NextToken indicates there are no more results.
        self.next_token = next_token
        # Request ID
        self.request_id = request_id
        # List of resources
        self.tag_resources = tag_resources
        # Total
        self.total_count = total_count

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkloadsRequest(TeaModel):
    def __init__(
        self,
        scope: str = None,
    ):
        # Scope
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ListWorkloadsResponseBodyDataParamSettings(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        param_desc: str = None,
        param_name: str = None,
        param_regex: str = None,
        param_type: str = None,
        param_value: str = None,
    ):
        # Default Parameter Value
        self.default_value = default_value
        # Parameter Description
        self.param_desc = param_desc
        # Parameter Name
        self.param_name = param_name
        # Parameter Regular Expression
        self.param_regex = param_regex
        # Parameter type
        self.param_type = param_type
        # Parameter Value
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_regex is not None:
            result['ParamRegex'] = self.param_regex
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamRegex') is not None:
            self.param_regex = m.get('ParamRegex')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class ListWorkloadsResponseBodyDataStaticConfig(TeaModel):
    def __init__(
        self,
        frame_work: str = None,
        os: str = None,
        parameters: str = None,
        software_stack: str = None,
    ):
        # Framework
        self.frame_work = frame_work
        # Operating System
        self.os = os
        # Number of Parameters
        self.parameters = parameters
        # Software Stack
        self.software_stack = software_stack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_work is not None:
            result['FrameWork'] = self.frame_work
        if self.os is not None:
            result['Os'] = self.os
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.software_stack is not None:
            result['SoftwareStack'] = self.software_stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameWork') is not None:
            self.frame_work = m.get('FrameWork')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SoftwareStack') is not None:
            self.software_stack = m.get('SoftwareStack')
        return self


class ListWorkloadsResponseBodyData(TeaModel):
    def __init__(
        self,
        default_cpu_per_worker: int = None,
        default_gpu_per_worker: int = None,
        default_memory_per_worker: int = None,
        default_share_memory: int = None,
        family: str = None,
        job_kind: str = None,
        param_settings: List[ListWorkloadsResponseBodyDataParamSettings] = None,
        scene: str = None,
        scope: str = None,
        static_config: ListWorkloadsResponseBodyDataStaticConfig = None,
        version_id: int = None,
        workload_description: str = None,
        workload_id: int = None,
        workload_name: str = None,
        workload_type: str = None,
    ):
        # Default CPU Allocation
        self.default_cpu_per_worker = default_cpu_per_worker
        # Default GPU Allocation
        self.default_gpu_per_worker = default_gpu_per_worker
        # Default Memory (GB) Allocation
        self.default_memory_per_worker = default_memory_per_worker
        # Default Shared Memory (GB) Allocation
        self.default_share_memory = default_share_memory
        # Workload Cluster, AI, GPU
        self.family = family
        # Training Job Type
        self.job_kind = job_kind
        # Parameter Settings
        self.param_settings = param_settings
        # Workload Usage Scenario
        self.scene = scene
        # Scope Identifier for Workload Usage
        self.scope = scope
        # Static Configuration
        self.static_config = static_config
        # Version ID
        self.version_id = version_id
        # Workload Description
        self.workload_description = workload_description
        # Workload ID
        self.workload_id = workload_id
        # Workload Name
        self.workload_name = workload_name
        # Workload Type
        self.workload_type = workload_type

    def validate(self):
        if self.param_settings:
            for k in self.param_settings:
                if k:
                    k.validate()
        if self.static_config:
            self.static_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_cpu_per_worker is not None:
            result['DefaultCpuPerWorker'] = self.default_cpu_per_worker
        if self.default_gpu_per_worker is not None:
            result['DefaultGpuPerWorker'] = self.default_gpu_per_worker
        if self.default_memory_per_worker is not None:
            result['DefaultMemoryPerWorker'] = self.default_memory_per_worker
        if self.default_share_memory is not None:
            result['DefaultShareMemory'] = self.default_share_memory
        if self.family is not None:
            result['Family'] = self.family
        if self.job_kind is not None:
            result['JobKind'] = self.job_kind
        result['ParamSettings'] = []
        if self.param_settings is not None:
            for k in self.param_settings:
                result['ParamSettings'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.static_config is not None:
            result['StaticConfig'] = self.static_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.workload_description is not None:
            result['WorkloadDescription'] = self.workload_description
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpuPerWorker') is not None:
            self.default_cpu_per_worker = m.get('DefaultCpuPerWorker')
        if m.get('DefaultGpuPerWorker') is not None:
            self.default_gpu_per_worker = m.get('DefaultGpuPerWorker')
        if m.get('DefaultMemoryPerWorker') is not None:
            self.default_memory_per_worker = m.get('DefaultMemoryPerWorker')
        if m.get('DefaultShareMemory') is not None:
            self.default_share_memory = m.get('DefaultShareMemory')
        if m.get('Family') is not None:
            self.family = m.get('Family')
        if m.get('JobKind') is not None:
            self.job_kind = m.get('JobKind')
        self.param_settings = []
        if m.get('ParamSettings') is not None:
            for k in m.get('ParamSettings'):
                temp_model = ListWorkloadsResponseBodyDataParamSettings()
                self.param_settings.append(temp_model.from_map(k))
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('StaticConfig') is not None:
            temp_model = ListWorkloadsResponseBodyDataStaticConfig()
            self.static_config = temp_model.from_map(m['StaticConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('WorkloadDescription') is not None:
            self.workload_description = m.get('WorkloadDescription')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')
        return self


class ListWorkloadsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[ListWorkloadsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access Denied Information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # total
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWorkloadsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListWorkloadsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkloadsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkloadsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: int = None,
        resource_group_id: str = None,
    ):
        # Plan ID
        # 
        # This parameter is required.
        self.experiment_id = experiment_id
        # Resource Group Id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class StopExperimentResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total number of queries
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StopExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopExperimentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # ResourceId
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # List of tags, up to 20.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied details
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Whether to delete all, only effective when TagKey.N is empty. Allowed values: true, false, True, False. Default is false.
        self.all = all
        # Resource ID
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # Tag key group, up to 20 items
        # 
        # This parameter is required.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: int = None,
        plan_template_name: str = None,
    ):
        # Experiment plan ID
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # Experiment plan name
        # 
        # This parameter is required.
        self.plan_template_name = plan_template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_template_name is not None:
            result['PlanTemplateName'] = self.plan_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanTemplateName') is not None:
            self.plan_template_name = m.get('PlanTemplateName')
        return self


class UpdateExperimentPlanResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class UpdateExperimentPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentPlanTemplateRequestTemplatePipelineEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU allocation count
        # 
        # This parameter is required.
        self.cpu_per_worker = cpu_per_worker
        # CUDA version
        self.cuda_version = cuda_version
        # GPU driver version
        self.gpu_driver_version = gpu_driver_version
        # GPU allocation count
        # 
        # This parameter is required.
        self.gpu_per_worker = gpu_per_worker
        # Memory GB allocation count
        # 
        # This parameter is required.
        self.memory_per_worker = memory_per_worker
        # NCCL version
        self.ncclversion = ncclversion
        # PyTorch version
        self.py_torch_version = py_torch_version
        # Shared memory GB allocation count
        # 
        # This parameter is required.
        self.share_memory = share_memory
        # Number of nodes
        # 
        # This parameter is required.
        self.worker_num = worker_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class UpdateExperimentPlanTemplateRequestTemplatePipeline(TeaModel):
    def __init__(
        self,
        env_params: UpdateExperimentPlanTemplateRequestTemplatePipelineEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured environment parameters
        # 
        # This parameter is required.
        self.env_params = env_params
        # Node order number
        # 
        # This parameter is required.
        self.pipeline_order = pipeline_order
        # Usage scenario, e.g., "baseline"
        # 
        # This parameter is required.
        self.scene = scene
        # Configured workload parameters
        self.setting_params = setting_params
        # Workload ID
        # 
        # This parameter is required.
        self.workload_id = workload_id
        # Workload name
        # 
        # This parameter is required.
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = UpdateExperimentPlanTemplateRequestTemplatePipelineEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class UpdateExperimentPlanTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
        template_pipeline: List[UpdateExperimentPlanTemplateRequestTemplatePipeline] = None,
    ):
        # Template code
        # 
        # This parameter is required.
        self.template_id = template_id
        # Template pipeline
        # 
        # This parameter is required.
        self.template_pipeline = template_pipeline

    def validate(self):
        if self.template_pipeline:
            for k in self.template_pipeline:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TemplatePipeline'] = []
        if self.template_pipeline is not None:
            for k in self.template_pipeline:
                result['TemplatePipeline'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.template_pipeline = []
        if m.get('TemplatePipeline') is not None:
            for k in m.get('TemplatePipeline'):
                temp_model = UpdateExperimentPlanTemplateRequestTemplatePipeline()
                self.template_pipeline.append(temp_model.from_map(k))
        return self


class UpdateExperimentPlanTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
        template_pipeline_shrink: str = None,
    ):
        # Template code
        # 
        # This parameter is required.
        self.template_id = template_id
        # Template pipeline
        # 
        # This parameter is required.
        self.template_pipeline_shrink = template_pipeline_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_pipeline_shrink is not None:
            result['TemplatePipeline'] = self.template_pipeline_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplatePipeline') is not None:
            self.template_pipeline_shrink = m.get('TemplatePipeline')
        return self


class UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        request_cpu: int = None,
        request_gpu: int = None,
        request_memory: int = None,
        total_cpu: int = None,
        total_gpu: int = None,
        total_memory: int = None,
    ):
        # Node Name
        self.node_name = node_name
        # Requested CPU
        self.request_cpu = request_cpu
        # Requested GPU
        self.request_gpu = request_gpu
        # Requested Memory
        self.request_memory = request_memory
        # Total CPU
        self.total_cpu = total_cpu
        # Total GPU
        self.total_gpu = total_gpu
        # Total Memory
        self.total_memory = total_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.total_cpu is not None:
            result['TotalCPU'] = self.total_cpu
        if self.total_gpu is not None:
            result['TotalGPU'] = self.total_gpu
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('TotalCPU') is not None:
            self.total_cpu = m.get('TotalCPU')
        if m.get('TotalGPU') is not None:
            self.total_gpu = m.get('TotalGPU')
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        return self


class UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams(TeaModel):
    def __init__(
        self,
        cpu_per_worker: int = None,
        cuda_version: str = None,
        extend_param: Dict[str, str] = None,
        gpu_driver_version: str = None,
        gpu_per_worker: int = None,
        memory_per_worker: int = None,
        ncclversion: str = None,
        py_torch_version: str = None,
        resource_nodes: List[UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes] = None,
        share_memory: int = None,
        worker_num: int = None,
    ):
        # CPU Allocation
        self.cpu_per_worker = cpu_per_worker
        # CUDA Version
        self.cuda_version = cuda_version
        # Extend Param
        self.extend_param = extend_param
        # GPU Driver Version
        self.gpu_driver_version = gpu_driver_version
        # GPU Allocation
        self.gpu_per_worker = gpu_per_worker
        # Memory (GB) Allocation
        self.memory_per_worker = memory_per_worker
        # NCCL Version
        self.ncclversion = ncclversion
        # PyTorch Version
        self.py_torch_version = py_torch_version
        # Specified Nodes
        self.resource_nodes = resource_nodes
        # Shared Memory (GB) Allocation
        self.share_memory = share_memory
        # Number of Nodes
        self.worker_num = worker_num

    def validate(self):
        if self.resource_nodes:
            for k in self.resource_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_per_worker is not None:
            result['CpuPerWorker'] = self.cpu_per_worker
        if self.cuda_version is not None:
            result['CudaVersion'] = self.cuda_version
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_per_worker is not None:
            result['GpuPerWorker'] = self.gpu_per_worker
        if self.memory_per_worker is not None:
            result['MemoryPerWorker'] = self.memory_per_worker
        if self.ncclversion is not None:
            result['NCCLVersion'] = self.ncclversion
        if self.py_torch_version is not None:
            result['PyTorchVersion'] = self.py_torch_version
        result['ResourceNodes'] = []
        if self.resource_nodes is not None:
            for k in self.resource_nodes:
                result['ResourceNodes'].append(k.to_map() if k else None)
        if self.share_memory is not None:
            result['ShareMemory'] = self.share_memory
        if self.worker_num is not None:
            result['WorkerNum'] = self.worker_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuPerWorker') is not None:
            self.cpu_per_worker = m.get('CpuPerWorker')
        if m.get('CudaVersion') is not None:
            self.cuda_version = m.get('CudaVersion')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuPerWorker') is not None:
            self.gpu_per_worker = m.get('GpuPerWorker')
        if m.get('MemoryPerWorker') is not None:
            self.memory_per_worker = m.get('MemoryPerWorker')
        if m.get('NCCLVersion') is not None:
            self.ncclversion = m.get('NCCLVersion')
        if m.get('PyTorchVersion') is not None:
            self.py_torch_version = m.get('PyTorchVersion')
        self.resource_nodes = []
        if m.get('ResourceNodes') is not None:
            for k in m.get('ResourceNodes'):
                temp_model = UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParamsResourceNodes()
                self.resource_nodes.append(temp_model.from_map(k))
        if m.get('ShareMemory') is not None:
            self.share_memory = m.get('ShareMemory')
        if m.get('WorkerNum') is not None:
            self.worker_num = m.get('WorkerNum')
        return self


class UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam(TeaModel):
    def __init__(
        self,
        env_params: UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams = None,
        pipeline_order: int = None,
        scene: str = None,
        setting_params: Dict[str, str] = None,
        workload_id: int = None,
        workload_name: str = None,
    ):
        # Configured Environment Parameters
        self.env_params = env_params
        # Node sequence number
        self.pipeline_order = pipeline_order
        # Usage Scenario, e.g., "baseline"
        self.scene = scene
        # Configured Workload Parameters
        self.setting_params = setting_params
        # Workload ID
        self.workload_id = workload_id
        # Workload Name
        self.workload_name = workload_name

    def validate(self):
        if self.env_params:
            self.env_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['EnvParams'] = self.env_params.to_map()
        if self.pipeline_order is not None:
            result['PipelineOrder'] = self.pipeline_order
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.setting_params is not None:
            result['SettingParams'] = self.setting_params
        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id
        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvParams') is not None:
            temp_model = UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParamEnvParams()
            self.env_params = temp_model.from_map(m['EnvParams'])
        if m.get('PipelineOrder') is not None:
            self.pipeline_order = m.get('PipelineOrder')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SettingParams') is not None:
            self.setting_params = m.get('SettingParams')
        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')
        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')
        return self


class UpdateExperimentPlanTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        creator_uid: int = None,
        is_delete: int = None,
        privacy_level: str = None,
        template_code: int = None,
        template_description: str = None,
        template_id: int = None,
        template_name: str = None,
        template_pipeline_param: List[UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam] = None,
        update_time: str = None,
        version_id: int = None,
    ):
        # Create Time
        self.create_time = create_time
        # Primary account UID
        self.creator_uid = creator_uid
        # Whether it is deleted
        self.is_delete = is_delete
        # Privacy Level
        self.privacy_level = privacy_level
        # Template code
        self.template_code = template_code
        # Template Description
        self.template_description = template_description
        # Template ID
        self.template_id = template_id
        # Template Name
        self.template_name = template_name
        # Template Pipeline
        self.template_pipeline_param = template_pipeline_param
        # Update Time
        self.update_time = update_time
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.template_pipeline_param:
            for k in self.template_pipeline_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.privacy_level is not None:
            result['PrivacyLevel'] = self.privacy_level
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['TemplatePipelineParam'] = []
        if self.template_pipeline_param is not None:
            for k in self.template_pipeline_param:
                result['TemplatePipelineParam'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('PrivacyLevel') is not None:
            self.privacy_level = m.get('PrivacyLevel')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.template_pipeline_param = []
        if m.get('TemplatePipelineParam') is not None:
            for k in m.get('TemplatePipelineParam'):
                temp_model = UpdateExperimentPlanTemplateResponseBodyDataTemplatePipelineParam()
                self.template_pipeline_param.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class UpdateExperimentPlanTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: UpdateExperimentPlanTemplateResponseBodyData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Access denied information
        self.access_denied_detail = access_denied_detail
        # Data
        self.data = data
        # Request ID
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = UpdateExperimentPlanTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class UpdateExperimentPlanTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExperimentPlanTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentPlanTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateResourceRequestUserAccessParam(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        endpoint: str = None,
        workspace_id: str = None,
    ):
        # User ID
        self.access_id = access_id
        # User Key
        self.access_key = access_key
        # Endpoint
        self.endpoint = endpoint
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ValidateResourceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user_access_param: ValidateResourceRequestUserAccessParam = None,
    ):
        # Resource ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # User Authorization Parameters
        self.user_access_param = user_access_param

    def validate(self):
        if self.user_access_param:
            self.user_access_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_access_param is not None:
            result['UserAccessParam'] = self.user_access_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UserAccessParam') is not None:
            temp_model = ValidateResourceRequestUserAccessParam()
            self.user_access_param = temp_model.from_map(m['UserAccessParam'])
        return self


class ValidateResourceShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        user_access_param_shrink: str = None,
    ):
        # Resource ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # User Authorization Parameters
        self.user_access_param_shrink = user_access_param_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_access_param_shrink is not None:
            result['UserAccessParam'] = self.user_access_param_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UserAccessParam') is not None:
            self.user_access_param_shrink = m.get('UserAccessParam')
        return self


class ValidateResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Data
        self.data = data
        # Request Id
        self.request_id = request_id
        # Total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ValidateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



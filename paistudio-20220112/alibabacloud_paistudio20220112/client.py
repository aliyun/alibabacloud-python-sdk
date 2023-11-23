# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paistudio20220112 import models as pai_studio_20220112_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'pai.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'pai.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'pai.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'pai.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'pai.ap-southeast-5.aliyuncs.com',
            'us-west-1': 'pai.us-west-1.aliyuncs.com',
            'us-east-1': 'pai.us-east-1.aliyuncs.com',
            'eu-central-1': 'pai.eu-central-1.aliyuncs.com',
            'me-east-1': 'pai.me-east-1.aliyuncs.com',
            'ap-south-1': 'pai.ap-south-1.aliyuncs.com',
            'cn-qingdao': 'pai.cn-qingdao.aliyuncs.com',
            'cn-zhangjiakou': 'pai.cn-zhangjiakou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('paistudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_algorithm_with_options(
        self,
        request: pai_studio_20220112_models.CreateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateAlgorithmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not UtilClient.is_unset(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_algorithm_with_options_async(
        self,
        request: pai_studio_20220112_models.CreateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateAlgorithmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not UtilClient.is_unset(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_algorithm(
        self,
        request: pai_studio_20220112_models.CreateAlgorithmRequest,
    ) -> pai_studio_20220112_models.CreateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_algorithm_with_options(request, headers, runtime)

    async def create_algorithm_async(
        self,
        request: pai_studio_20220112_models.CreateAlgorithmRequest,
    ) -> pai_studio_20220112_models.CreateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_algorithm_with_options_async(request, headers, runtime)

    def create_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: pai_studio_20220112_models.CreateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateAlgorithmVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.CreateAlgorithmVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: pai_studio_20220112_models.CreateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateAlgorithmVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.CreateAlgorithmVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: pai_studio_20220112_models.CreateAlgorithmVersionRequest,
    ) -> pai_studio_20220112_models.CreateAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_algorithm_version_with_options(algorithm_id, algorithm_version, request, headers, runtime)

    async def create_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: pai_studio_20220112_models.CreateAlgorithmVersionRequest,
    ) -> pai_studio_20220112_models.CreateAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_algorithm_version_with_options_async(algorithm_id, algorithm_version, request, headers, runtime)

    def create_quota_with_options(
        self,
        request: pai_studio_20220112_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allocate_strategy):
            body['AllocateStrategy'] = request.allocate_strategy
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.parent_quota_id):
            body['ParentQuotaId'] = request.parent_quota_id
        if not UtilClient.is_unset(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not UtilClient.is_unset(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not UtilClient.is_unset(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_with_options_async(
        self,
        request: pai_studio_20220112_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allocate_strategy):
            body['AllocateStrategy'] = request.allocate_strategy
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.parent_quota_id):
            body['ParentQuotaId'] = request.parent_quota_id
        if not UtilClient.is_unset(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not UtilClient.is_unset(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not UtilClient.is_unset(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota(
        self,
        request: pai_studio_20220112_models.CreateQuotaRequest,
    ) -> pai_studio_20220112_models.CreateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_with_options(request, headers, runtime)

    async def create_quota_async(
        self,
        request: pai_studio_20220112_models.CreateQuotaRequest,
    ) -> pai_studio_20220112_models.CreateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_quota_with_options_async(request, headers, runtime)

    def create_resource_group_with_options(
        self,
        request: pai_studio_20220112_models.CreateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.computing_resource_provider):
            body['ComputingResourceProvider'] = request.computing_resource_provider
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: pai_studio_20220112_models.CreateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.computing_resource_provider):
            body['ComputingResourceProvider'] = request.computing_resource_provider
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: pai_studio_20220112_models.CreateResourceGroupRequest,
    ) -> pai_studio_20220112_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_group_with_options(request, headers, runtime)

    async def create_resource_group_async(
        self,
        request: pai_studio_20220112_models.CreateResourceGroupRequest,
    ) -> pai_studio_20220112_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_group_with_options_async(request, headers, runtime)

    def create_training_job_with_options(
        self,
        request: pai_studio_20220112_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateTrainingJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            body['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.algorithm_spec):
            body['AlgorithmSpec'] = request.algorithm_spec
        if not UtilClient.is_unset(request.algorithm_version):
            body['AlgorithmVersion'] = request.algorithm_version
        if not UtilClient.is_unset(request.code_dir):
            body['CodeDir'] = request.code_dir
        if not UtilClient.is_unset(request.compute_resource):
            body['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.hyper_parameters):
            body['HyperParameters'] = request.hyper_parameters
        if not UtilClient.is_unset(request.input_channels):
            body['InputChannels'] = request.input_channels
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.output_channels):
            body['OutputChannels'] = request.output_channels
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.training_job_description):
            body['TrainingJobDescription'] = request.training_job_description
        if not UtilClient.is_unset(request.training_job_name):
            body['TrainingJobName'] = request.training_job_name
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_training_job_with_options_async(
        self,
        request: pai_studio_20220112_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.CreateTrainingJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            body['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.algorithm_spec):
            body['AlgorithmSpec'] = request.algorithm_spec
        if not UtilClient.is_unset(request.algorithm_version):
            body['AlgorithmVersion'] = request.algorithm_version
        if not UtilClient.is_unset(request.code_dir):
            body['CodeDir'] = request.code_dir
        if not UtilClient.is_unset(request.compute_resource):
            body['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.hyper_parameters):
            body['HyperParameters'] = request.hyper_parameters
        if not UtilClient.is_unset(request.input_channels):
            body['InputChannels'] = request.input_channels
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.output_channels):
            body['OutputChannels'] = request.output_channels
        if not UtilClient.is_unset(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.training_job_description):
            body['TrainingJobDescription'] = request.training_job_description
        if not UtilClient.is_unset(request.training_job_name):
            body['TrainingJobName'] = request.training_job_name
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.CreateTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_training_job(
        self,
        request: pai_studio_20220112_models.CreateTrainingJobRequest,
    ) -> pai_studio_20220112_models.CreateTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_training_job_with_options(request, headers, runtime)

    async def create_training_job_async(
        self,
        request: pai_studio_20220112_models.CreateTrainingJobRequest,
    ) -> pai_studio_20220112_models.CreateTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_training_job_with_options_async(request, headers, runtime)

    def delete_machine_group_with_options(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_machine_group_with_options_async(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_machine_group(
        self,
        machine_group_id: str,
    ) -> pai_studio_20220112_models.DeleteMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(machine_group_id, headers, runtime)

    async def delete_machine_group_async(
        self,
        machine_group_id: str,
    ) -> pai_studio_20220112_models.DeleteMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_machine_group_with_options_async(machine_group_id, headers, runtime)

    def delete_quota_with_options(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_with_options_async(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota(
        self,
        quota_id: str,
    ) -> pai_studio_20220112_models.DeleteQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_with_options(quota_id, headers, runtime)

    async def delete_quota_async(
        self,
        quota_id: str,
    ) -> pai_studio_20220112_models.DeleteQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_quota_with_options_async(quota_id, headers, runtime)

    def delete_resource_group_with_options(
        self,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteResourceGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteResourceGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_group_with_options(resource_group_id, headers, runtime)

    async def delete_resource_group_async(
        self,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_group_with_options_async(resource_group_id, headers, runtime)

    def delete_resource_group_machine_group_with_options(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceGroupMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_machine_group_with_options_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceGroupMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group_machine_group(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_group_machine_group_with_options(machine_group_id, resource_group_id, headers, runtime)

    async def delete_resource_group_machine_group_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.DeleteResourceGroupMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_group_machine_group_with_options_async(machine_group_id, resource_group_id, headers, runtime)

    def get_algorithm_with_options(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_with_options_async(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetAlgorithmResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm(
        self,
        algorithm_id: str,
    ) -> pai_studio_20220112_models.GetAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_with_options(algorithm_id, headers, runtime)

    async def get_algorithm_async(
        self,
        algorithm_id: str,
    ) -> pai_studio_20220112_models.GetAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_with_options_async(algorithm_id, headers, runtime)

    def get_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetAlgorithmVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetAlgorithmVersionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> pai_studio_20220112_models.GetAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_version_with_options(algorithm_id, algorithm_version, headers, runtime)

    async def get_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> pai_studio_20220112_models.GetAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_version_with_options_async(algorithm_id, algorithm_version, headers, runtime)

    def get_machine_group_with_options(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_machine_group_with_options_async(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_machine_group(
        self,
        machine_group_id: str,
    ) -> pai_studio_20220112_models.GetMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(machine_group_id, headers, runtime)

    async def get_machine_group_async(
        self,
        machine_group_id: str,
    ) -> pai_studio_20220112_models.GetMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_machine_group_with_options_async(machine_group_id, headers, runtime)

    def get_node_metrics_with_options(
        self,
        resource_group_id: str,
        metric_type: str,
        request: pai_studio_20220112_models.GetNodeMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetNodeMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.gputype):
            query['GPUType'] = request.gputype
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/nodemetrics/{OpenApiUtilClient.get_encode_param(metric_type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetNodeMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_metrics_with_options_async(
        self,
        resource_group_id: str,
        metric_type: str,
        request: pai_studio_20220112_models.GetNodeMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetNodeMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.gputype):
            query['GPUType'] = request.gputype
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/nodemetrics/{OpenApiUtilClient.get_encode_param(metric_type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetNodeMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_metrics(
        self,
        resource_group_id: str,
        metric_type: str,
        request: pai_studio_20220112_models.GetNodeMetricsRequest,
    ) -> pai_studio_20220112_models.GetNodeMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_metrics_with_options(resource_group_id, metric_type, request, headers, runtime)

    async def get_node_metrics_async(
        self,
        resource_group_id: str,
        metric_type: str,
        request: pai_studio_20220112_models.GetNodeMetricsRequest,
    ) -> pai_studio_20220112_models.GetNodeMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_metrics_with_options_async(resource_group_id, metric_type, request, headers, runtime)

    def get_quota_with_options(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        quota_id: str,
    ) -> pai_studio_20220112_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(quota_id, headers, runtime)

    async def get_quota_async(
        self,
        quota_id: str,
    ) -> pai_studio_20220112_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(quota_id, headers, runtime)

    def get_resource_group_with_options(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetResourceGroupRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_group_with_options(resource_group_id, request, headers, runtime)

    async def get_resource_group_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetResourceGroupRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_group_with_options_async(resource_group_id, request, headers, runtime)

    def get_resource_group_machine_group_with_options(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResourceGroupMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_machine_group_with_options_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupMachineGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResourceGroupMachineGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups/{OpenApiUtilClient.get_encode_param(machine_group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_machine_group(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.GetResourceGroupMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_group_machine_group_with_options(machine_group_id, resource_group_id, headers, runtime)

    async def get_resource_group_machine_group_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> pai_studio_20220112_models.GetResourceGroupMachineGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_group_machine_group_with_options_async(machine_group_id, resource_group_id, headers, runtime)

    def get_resource_group_request_with_options(
        self,
        request: pai_studio_20220112_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupRequest',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/data/request',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_request_with_options_async(
        self,
        request: pai_studio_20220112_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupRequest',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/data/request',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_request(
        self,
        request: pai_studio_20220112_models.GetResourceGroupRequestRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_group_request_with_options(request, headers, runtime)

    async def get_resource_group_request_async(
        self,
        request: pai_studio_20220112_models.GetResourceGroupRequestRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupRequestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_group_request_with_options_async(request, headers, runtime)

    def get_resource_group_total_with_options(
        self,
        request: pai_studio_20220112_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupTotal',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/data/total',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_total_with_options_async(
        self,
        request: pai_studio_20220112_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetResourceGroupTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroupTotal',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/data/total',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetResourceGroupTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_total(
        self,
        request: pai_studio_20220112_models.GetResourceGroupTotalRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupTotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_group_total_with_options(request, headers, runtime)

    async def get_resource_group_total_async(
        self,
        request: pai_studio_20220112_models.GetResourceGroupTotalRequest,
    ) -> pai_studio_20220112_models.GetResourceGroupTotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_group_total_with_options_async(request, headers, runtime)

    def get_training_job_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_training_job_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_training_job(
        self,
        training_job_id: str,
    ) -> pai_studio_20220112_models.GetTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_training_job_with_options(training_job_id, headers, runtime)

    async def get_training_job_async(
        self,
        training_job_id: str,
    ) -> pai_studio_20220112_models.GetTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_training_job_with_options_async(training_job_id, headers, runtime)

    def get_user_view_metrics_with_options(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetUserViewMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserViewMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/usermetrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetUserViewMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_view_metrics_with_options_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.GetUserViewMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserViewMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/usermetrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.GetUserViewMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_view_metrics(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetUserViewMetricsRequest,
    ) -> pai_studio_20220112_models.GetUserViewMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_view_metrics_with_options(resource_group_id, request, headers, runtime)

    async def get_user_view_metrics_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.GetUserViewMetricsRequest,
    ) -> pai_studio_20220112_models.GetUserViewMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_view_metrics_with_options_async(resource_group_id, request, headers, runtime)

    def list_algorithm_versions_with_options(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.ListAlgorithmVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListAlgorithmVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithmVersions',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListAlgorithmVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithm_versions_with_options_async(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.ListAlgorithmVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListAlgorithmVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithmVersions',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListAlgorithmVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_algorithm_versions(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.ListAlgorithmVersionsRequest,
    ) -> pai_studio_20220112_models.ListAlgorithmVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algorithm_versions_with_options(algorithm_id, request, headers, runtime)

    async def list_algorithm_versions_async(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.ListAlgorithmVersionsRequest,
    ) -> pai_studio_20220112_models.ListAlgorithmVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_algorithm_versions_with_options_async(algorithm_id, request, headers, runtime)

    def list_algorithms_with_options(
        self,
        request: pai_studio_20220112_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListAlgorithmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithms',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithms_with_options_async(
        self,
        request: pai_studio_20220112_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListAlgorithmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithms',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_algorithms(
        self,
        request: pai_studio_20220112_models.ListAlgorithmsRequest,
    ) -> pai_studio_20220112_models.ListAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algorithms_with_options(request, headers, runtime)

    async def list_algorithms_async(
        self,
        request: pai_studio_20220112_models.ListAlgorithmsRequest,
    ) -> pai_studio_20220112_models.ListAlgorithmsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_algorithms_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: pai_studio_20220112_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not UtilClient.is_unset(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.statuses):
            query['Statuses'] = request.statuses
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: pai_studio_20220112_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListQuotasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not UtilClient.is_unset(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not UtilClient.is_unset(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.statuses):
            query['Statuses'] = request.statuses
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: pai_studio_20220112_models.ListQuotasRequest,
    ) -> pai_studio_20220112_models.ListQuotasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: pai_studio_20220112_models.ListQuotasRequest,
    ) -> pai_studio_20220112_models.ListQuotasResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_resource_group_machine_groups_with_options(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not UtilClient.is_unset(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroupMachineGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_machine_groups_with_options_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not UtilClient.is_unset(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroupMachineGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_machine_groups(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.ListResourceGroupMachineGroupsRequest,
    ) -> pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_group_machine_groups_with_options(resource_group_id, request, headers, runtime)

    async def list_resource_group_machine_groups_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.ListResourceGroupMachineGroupsRequest,
    ) -> pai_studio_20220112_models.ListResourceGroupMachineGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_group_machine_groups_with_options_async(resource_group_id, request, headers, runtime)

    def list_resource_groups_with_options(
        self,
        request: pai_studio_20220112_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.show_all):
            query['ShowAll'] = request.show_all
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: pai_studio_20220112_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.show_all):
            query['ShowAll'] = request.show_all
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: pai_studio_20220112_models.ListResourceGroupsRequest,
    ) -> pai_studio_20220112_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_groups_with_options(request, headers, runtime)

    async def list_resource_groups_async(
        self,
        request: pai_studio_20220112_models.ListResourceGroupsRequest,
    ) -> pai_studio_20220112_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_groups_with_options_async(request, headers, runtime)

    def list_training_job_logs_with_options(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobLogs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_logs_with_options_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobLogs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_logs(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobLogsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_training_job_logs_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_logs_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobLogsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_training_job_logs_with_options_async(training_job_id, request, headers, runtime)

    def list_training_job_metrics_with_options(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_metrics_with_options_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_metrics(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobMetricsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_training_job_metrics_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_metrics_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.ListTrainingJobMetricsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_training_job_metrics_with_options_async(training_job_id, request, headers, runtime)

    def list_training_jobs_with_options(
        self,
        tmp_req: pai_studio_20220112_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.ListTrainingJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_temp_algo):
            query['IsTempAlgo'] = request.is_temp_algo
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        if not UtilClient.is_unset(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_jobs_with_options_async(
        self,
        tmp_req: pai_studio_20220112_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ListTrainingJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.ListTrainingJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.labels):
            request.labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not UtilClient.is_unset(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_temp_algo):
            query['IsTempAlgo'] = request.is_temp_algo
        if not UtilClient.is_unset(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        if not UtilClient.is_unset(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ListTrainingJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_jobs(
        self,
        request: pai_studio_20220112_models.ListTrainingJobsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_training_jobs_with_options(request, headers, runtime)

    async def list_training_jobs_async(
        self,
        request: pai_studio_20220112_models.ListTrainingJobsRequest,
    ) -> pai_studio_20220112_models.ListTrainingJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_training_jobs_with_options_async(request, headers, runtime)

    def scale_quota_with_options(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.ScaleQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ScaleQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}/action/scale',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ScaleQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_quota_with_options_async(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.ScaleQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.ScaleQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.min):
            body['Min'] = request.min
        if not UtilClient.is_unset(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}/action/scale',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.ScaleQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_quota(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.ScaleQuotaRequest,
    ) -> pai_studio_20220112_models.ScaleQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_quota_with_options(quota_id, request, headers, runtime)

    async def scale_quota_async(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.ScaleQuotaRequest,
    ) -> pai_studio_20220112_models.ScaleQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_quota_with_options_async(quota_id, request, headers, runtime)

    def stop_training_job_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.StopTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.StopTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_training_job_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.StopTrainingJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.StopTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_training_job(
        self,
        training_job_id: str,
    ) -> pai_studio_20220112_models.StopTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_training_job_with_options(training_job_id, headers, runtime)

    async def stop_training_job_async(
        self,
        training_job_id: str,
    ) -> pai_studio_20220112_models.StopTrainingJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_training_job_with_options_async(training_job_id, headers, runtime)

    def update_algorithm_with_options(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.UpdateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateAlgorithmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_algorithm_with_options_async(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.UpdateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateAlgorithmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_algorithm(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.UpdateAlgorithmRequest,
    ) -> pai_studio_20220112_models.UpdateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_algorithm_with_options(algorithm_id, request, headers, runtime)

    async def update_algorithm_async(
        self,
        algorithm_id: str,
        request: pai_studio_20220112_models.UpdateAlgorithmRequest,
    ) -> pai_studio_20220112_models.UpdateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_algorithm_with_options_async(algorithm_id, request, headers, runtime)

    def update_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: pai_studio_20220112_models.UpdateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateAlgorithmVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.UpdateAlgorithmVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: pai_studio_20220112_models.UpdateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateAlgorithmVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_studio_20220112_models.UpdateAlgorithmVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlgorithmVersion',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/algorithms/{OpenApiUtilClient.get_encode_param(algorithm_id)}/versions/{OpenApiUtilClient.get_encode_param(algorithm_version)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: pai_studio_20220112_models.UpdateAlgorithmVersionRequest,
    ) -> pai_studio_20220112_models.UpdateAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_algorithm_version_with_options(algorithm_id, algorithm_version, request, headers, runtime)

    async def update_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: pai_studio_20220112_models.UpdateAlgorithmVersionRequest,
    ) -> pai_studio_20220112_models.UpdateAlgorithmVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_algorithm_version_with_options_async(algorithm_id, algorithm_version, request, headers, runtime)

    def update_quota_with_options(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_with_options_async(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateQuotaResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuota',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(quota_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.UpdateQuotaRequest,
    ) -> pai_studio_20220112_models.UpdateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(quota_id, request, headers, runtime)

    async def update_quota_async(
        self,
        quota_id: str,
        request: pai_studio_20220112_models.UpdateQuotaRequest,
    ) -> pai_studio_20220112_models.UpdateQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_with_options_async(quota_id, request, headers, runtime)

    def update_resource_group_with_options(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.UpdateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.unbind):
            body['Unbind'] = request.unbind
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.UpdateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.unbind):
            body['Unbind'] = request.unbind
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/{OpenApiUtilClient.get_encode_param(resource_group_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.UpdateResourceGroupRequest,
    ) -> pai_studio_20220112_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_group_with_options(resource_group_id, request, headers, runtime)

    async def update_resource_group_async(
        self,
        resource_group_id: str,
        request: pai_studio_20220112_models.UpdateResourceGroupRequest,
    ) -> pai_studio_20220112_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_group_with_options_async(resource_group_id, request, headers, runtime)

    def update_training_job_labels_with_options(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.UpdateTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateTrainingJobLabelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrainingJobLabels',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateTrainingJobLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_training_job_labels_with_options_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.UpdateTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20220112_models.UpdateTrainingJobLabelsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrainingJobLabels',
            version='2022-01-12',
            protocol='HTTPS',
            pathname=f'/api/v1/trainingjobs/{OpenApiUtilClient.get_encode_param(training_job_id)}/labels',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_studio_20220112_models.UpdateTrainingJobLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_training_job_labels(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.UpdateTrainingJobLabelsRequest,
    ) -> pai_studio_20220112_models.UpdateTrainingJobLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_training_job_labels_with_options(training_job_id, request, headers, runtime)

    async def update_training_job_labels_async(
        self,
        training_job_id: str,
        request: pai_studio_20220112_models.UpdateTrainingJobLabelsRequest,
    ) -> pai_studio_20220112_models.UpdateTrainingJobLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_training_job_labels_with_options_async(training_job_id, request, headers, runtime)

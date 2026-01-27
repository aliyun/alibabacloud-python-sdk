# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paistudio20220112 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'pai.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'pai.cn-hangzhou.data.aliyun.com',
            'cn-shanghai': 'pai.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'pai.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'pai.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'pai.ap-southeast-5.aliyuncs.com',
            'us-east-1': 'pai.us-east-1.aliyuncs.com',
            'us-west-1': 'pai.us-west-1.aliyuncs.com',
            'eu-central-1': 'pai.eu-central-1.aliyuncs.com',
            'ap-south-1': 'pai.ap-south-1.aliyuncs.com',
            'me-east-1': 'pai.me-east-1.aliyuncs.com',
            'ap-northeast-1': 'pai.ap-northeast-1.aliyuncs.com',
            'cn-qingdao': 'pai.cn-qingdao.aliyuncs.com',
            'cn-shanghai-finance-1': 'pai.cn-shanghai-finance-1.aliyuncs.com',
            'cn-wulanchabu': 'pai.cn-wulanchabu.aliyuncs.com',
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_instance_web_terminal_with_options(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.CheckInstanceWebTerminalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceWebTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_info):
            body['CheckInfo'] = request.check_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceWebTerminal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/webterminals/action/check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceWebTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_web_terminal_with_options_async(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.CheckInstanceWebTerminalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInstanceWebTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_info):
            body['CheckInfo'] = request.check_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckInstanceWebTerminal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/webterminals/action/check',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInstanceWebTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_web_terminal(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.CheckInstanceWebTerminalRequest,
    ) -> main_models.CheckInstanceWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_instance_web_terminal_with_options(training_job_id, instance_id, request, headers, runtime)

    async def check_instance_web_terminal_async(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.CheckInstanceWebTerminalRequest,
    ) -> main_models.CheckInstanceWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_instance_web_terminal_with_options_async(training_job_id, instance_id, request, headers, runtime)

    def create_algorithm_with_options(
        self,
        request: main_models.CreateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlgorithmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not DaraCore.is_null(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_algorithm_with_options_async(
        self,
        request: main_models.CreateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlgorithmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not DaraCore.is_null(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_algorithm(
        self,
        request: main_models.CreateAlgorithmRequest,
    ) -> main_models.CreateAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_algorithm_with_options(request, headers, runtime)

    async def create_algorithm_async(
        self,
        request: main_models.CreateAlgorithmRequest,
    ) -> main_models.CreateAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_algorithm_with_options_async(request, headers, runtime)

    def create_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: main_models.CreateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlgorithmVersionResponse:
        tmp_req.validate()
        request = main_models.CreateAlgorithmVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not DaraCore.is_null(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: main_models.CreateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlgorithmVersionResponse:
        tmp_req.validate()
        request = main_models.CreateAlgorithmVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not DaraCore.is_null(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: main_models.CreateAlgorithmVersionRequest,
    ) -> main_models.CreateAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_algorithm_version_with_options(algorithm_id, algorithm_version, request, headers, runtime)

    async def create_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: main_models.CreateAlgorithmVersionRequest,
    ) -> main_models.CreateAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_algorithm_version_with_options_async(algorithm_id, algorithm_version, request, headers, runtime)

    def create_instance_web_terminal_with_options(
        self,
        training_job_id: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceWebTerminalResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceWebTerminal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/webterminals',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceWebTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_web_terminal_with_options_async(
        self,
        training_job_id: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceWebTerminalResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceWebTerminal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/webterminals',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceWebTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_web_terminal(
        self,
        training_job_id: str,
        instance_id: str,
    ) -> main_models.CreateInstanceWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_web_terminal_with_options(training_job_id, instance_id, headers, runtime)

    async def create_instance_web_terminal_async(
        self,
        training_job_id: str,
        instance_id: str,
    ) -> main_models.CreateInstanceWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_web_terminal_with_options_async(training_job_id, instance_id, headers, runtime)

    def create_quota_with_options(
        self,
        request: main_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allocate_strategy):
            body['AllocateStrategy'] = request.allocate_strategy
        if not DaraCore.is_null(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.min):
            body['Min'] = request.min
        if not DaraCore.is_null(request.parent_quota_id):
            body['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not DaraCore.is_null(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not DaraCore.is_null(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_with_options_async(
        self,
        request: main_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allocate_strategy):
            body['AllocateStrategy'] = request.allocate_strategy
        if not DaraCore.is_null(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.min):
            body['Min'] = request.min
        if not DaraCore.is_null(request.parent_quota_id):
            body['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not DaraCore.is_null(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not DaraCore.is_null(request.quota_name):
            body['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota(
        self,
        request: main_models.CreateQuotaRequest,
    ) -> main_models.CreateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_quota_with_options(request, headers, runtime)

    async def create_quota_async(
        self,
        request: main_models.CreateQuotaRequest,
    ) -> main_models.CreateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_quota_with_options_async(request, headers, runtime)

    def create_resource_group_with_options(
        self,
        request: main_models.CreateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            body['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: main_models.CreateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            body['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_group_with_options(request, headers, runtime)

    async def create_resource_group_async(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_group_with_options_async(request, headers, runtime)

    def create_training_job_with_options(
        self,
        request: main_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainingJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            body['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.algorithm_spec):
            body['AlgorithmSpec'] = request.algorithm_spec
        if not DaraCore.is_null(request.algorithm_version):
            body['AlgorithmVersion'] = request.algorithm_version
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.code_dir):
            body['CodeDir'] = request.code_dir
        if not DaraCore.is_null(request.compute_resource):
            body['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.environments):
            body['Environments'] = request.environments
        if not DaraCore.is_null(request.experiment_config):
            body['ExperimentConfig'] = request.experiment_config
        if not DaraCore.is_null(request.hyper_parameters):
            body['HyperParameters'] = request.hyper_parameters
        if not DaraCore.is_null(request.input_channels):
            body['InputChannels'] = request.input_channels
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.output_channels):
            body['OutputChannels'] = request.output_channels
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.python_requirements):
            body['PythonRequirements'] = request.python_requirements
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.settings):
            body['Settings'] = request.settings
        if not DaraCore.is_null(request.training_job_description):
            body['TrainingJobDescription'] = request.training_job_description
        if not DaraCore.is_null(request.training_job_name):
            body['TrainingJobName'] = request.training_job_name
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_training_job_with_options_async(
        self,
        request: main_models.CreateTrainingJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainingJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            body['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.algorithm_spec):
            body['AlgorithmSpec'] = request.algorithm_spec
        if not DaraCore.is_null(request.algorithm_version):
            body['AlgorithmVersion'] = request.algorithm_version
        if not DaraCore.is_null(request.assign_node_spec):
            body['AssignNodeSpec'] = request.assign_node_spec
        if not DaraCore.is_null(request.code_dir):
            body['CodeDir'] = request.code_dir
        if not DaraCore.is_null(request.compute_resource):
            body['ComputeResource'] = request.compute_resource
        if not DaraCore.is_null(request.environments):
            body['Environments'] = request.environments
        if not DaraCore.is_null(request.experiment_config):
            body['ExperimentConfig'] = request.experiment_config
        if not DaraCore.is_null(request.hyper_parameters):
            body['HyperParameters'] = request.hyper_parameters
        if not DaraCore.is_null(request.input_channels):
            body['InputChannels'] = request.input_channels
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.output_channels):
            body['OutputChannels'] = request.output_channels
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.python_requirements):
            body['PythonRequirements'] = request.python_requirements
        if not DaraCore.is_null(request.role_arn):
            body['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.settings):
            body['Settings'] = request.settings
        if not DaraCore.is_null(request.training_job_description):
            body['TrainingJobDescription'] = request.training_job_description
        if not DaraCore.is_null(request.training_job_name):
            body['TrainingJobName'] = request.training_job_name
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_training_job(
        self,
        request: main_models.CreateTrainingJobRequest,
    ) -> main_models.CreateTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_training_job_with_options(request, headers, runtime)

    async def create_training_job_async(
        self,
        request: main_models.CreateTrainingJobRequest,
    ) -> main_models.CreateTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_training_job_with_options_async(request, headers, runtime)

    def delete_algorithm_with_options(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlgorithmResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_algorithm_with_options_async(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlgorithmResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_algorithm(
        self,
        algorithm_id: str,
    ) -> main_models.DeleteAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_algorithm_with_options(algorithm_id, headers, runtime)

    async def delete_algorithm_async(
        self,
        algorithm_id: str,
    ) -> main_models.DeleteAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_algorithm_with_options_async(algorithm_id, headers, runtime)

    def delete_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlgorithmVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlgorithmVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> main_models.DeleteAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_algorithm_version_with_options(algorithm_id, algorithm_version, headers, runtime)

    async def delete_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> main_models.DeleteAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_algorithm_version_with_options_async(algorithm_id, algorithm_version, headers, runtime)

    def delete_machine_group_with_options(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_machine_group_with_options_async(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_machine_group(
        self,
        machine_group_id: str,
    ) -> main_models.DeleteMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(machine_group_id, headers, runtime)

    async def delete_machine_group_async(
        self,
        machine_group_id: str,
    ) -> main_models.DeleteMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_machine_group_with_options_async(machine_group_id, headers, runtime)

    def delete_quota_with_options(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_with_options_async(
        self,
        quota_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota(
        self,
        quota_id: str,
    ) -> main_models.DeleteQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_quota_with_options(quota_id, headers, runtime)

    async def delete_quota_async(
        self,
        quota_id: str,
    ) -> main_models.DeleteQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_quota_with_options_async(quota_id, headers, runtime)

    def delete_resource_group_with_options(
        self,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        resource_group_id: str,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_group_with_options(resource_group_id, headers, runtime)

    async def delete_resource_group_async(
        self,
        resource_group_id: str,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_group_with_options_async(resource_group_id, headers, runtime)

    def delete_resource_group_machine_group_with_options(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroupMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_machine_group_with_options_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroupMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group_machine_group(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> main_models.DeleteResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_group_machine_group_with_options(machine_group_id, resource_group_id, headers, runtime)

    async def delete_resource_group_machine_group_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
    ) -> main_models.DeleteResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_group_machine_group_with_options_async(machine_group_id, resource_group_id, headers, runtime)

    def delete_training_job_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_training_job_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_training_job(
        self,
        training_job_id: str,
    ) -> main_models.DeleteTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_training_job_with_options(training_job_id, headers, runtime)

    async def delete_training_job_async(
        self,
        training_job_id: str,
    ) -> main_models.DeleteTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_training_job_with_options_async(training_job_id, headers, runtime)

    def delete_training_job_labels_with_options(
        self,
        training_job_id: str,
        request: main_models.DeleteTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrainingJobLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keys):
            query['Keys'] = request.keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrainingJobLabels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrainingJobLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_training_job_labels_with_options_async(
        self,
        training_job_id: str,
        request: main_models.DeleteTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrainingJobLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keys):
            query['Keys'] = request.keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrainingJobLabels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/labels',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrainingJobLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_training_job_labels(
        self,
        training_job_id: str,
        request: main_models.DeleteTrainingJobLabelsRequest,
    ) -> main_models.DeleteTrainingJobLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_training_job_labels_with_options(training_job_id, request, headers, runtime)

    async def delete_training_job_labels_async(
        self,
        training_job_id: str,
        request: main_models.DeleteTrainingJobLabelsRequest,
    ) -> main_models.DeleteTrainingJobLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_training_job_labels_with_options_async(training_job_id, request, headers, runtime)

    def get_algorithm_with_options(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlgorithmResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_with_options_async(
        self,
        algorithm_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlgorithmResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm(
        self,
        algorithm_id: str,
    ) -> main_models.GetAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_algorithm_with_options(algorithm_id, headers, runtime)

    async def get_algorithm_async(
        self,
        algorithm_id: str,
    ) -> main_models.GetAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_algorithm_with_options_async(algorithm_id, headers, runtime)

    def get_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlgorithmVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlgorithmVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> main_models.GetAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_algorithm_version_with_options(algorithm_id, algorithm_version, headers, runtime)

    async def get_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
    ) -> main_models.GetAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_algorithm_version_with_options_async(algorithm_id, algorithm_version, headers, runtime)

    def get_machine_group_with_options(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_machine_group_with_options_async(
        self,
        machine_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMachineGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_machine_group(
        self,
        machine_group_id: str,
    ) -> main_models.GetMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(machine_group_id, headers, runtime)

    async def get_machine_group_async(
        self,
        machine_group_id: str,
    ) -> main_models.GetMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_machine_group_with_options_async(machine_group_id, headers, runtime)

    def get_node_metrics_with_options(
        self,
        resource_group_id: str,
        metric_type: str,
        request: main_models.GetNodeMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/nodemetrics/{DaraURL.percent_encode(metric_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_metrics_with_options_async(
        self,
        resource_group_id: str,
        metric_type: str,
        request: main_models.GetNodeMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/nodemetrics/{DaraURL.percent_encode(metric_type)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_metrics(
        self,
        resource_group_id: str,
        metric_type: str,
        request: main_models.GetNodeMetricsRequest,
    ) -> main_models.GetNodeMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_node_metrics_with_options(resource_group_id, metric_type, request, headers, runtime)

    async def get_node_metrics_async(
        self,
        resource_group_id: str,
        metric_type: str,
        request: main_models.GetNodeMetricsRequest,
    ) -> main_models.GetNodeMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_node_metrics_with_options_async(resource_group_id, metric_type, request, headers, runtime)

    def get_quota_with_options(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.with_node_meta):
            query['WithNodeMeta'] = request.with_node_meta
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.with_node_meta):
            query['WithNodeMeta'] = request.with_node_meta
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(quota_id, request, headers, runtime)

    async def get_quota_async(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(quota_id, request, headers, runtime)

    def get_resource_group_with_options(
        self,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        resource_group_id: str,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_with_options(resource_group_id, request, headers, runtime)

    async def get_resource_group_async(
        self,
        resource_group_id: str,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_with_options_async(resource_group_id, request, headers, runtime)

    def get_resource_group_machine_group_with_options(
        self,
        machine_group_id: str,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupMachineGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_machine_group_with_options_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupMachineGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupMachineGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_machine_group(
        self,
        machine_group_id: str,
        resource_group_id: str,
        request: main_models.GetResourceGroupMachineGroupRequest,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_machine_group_with_options(machine_group_id, resource_group_id, request, headers, runtime)

    async def get_resource_group_machine_group_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        request: main_models.GetResourceGroupMachineGroupRequest,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_machine_group_with_options_async(machine_group_id, resource_group_id, request, headers, runtime)

    def get_resource_group_request_with_options(
        self,
        request: main_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupRequest',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/request',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_request_with_options_async(
        self,
        request: main_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupRequest',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/request',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_request(
        self,
        request: main_models.GetResourceGroupRequestRequest,
    ) -> main_models.GetResourceGroupRequestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_request_with_options(request, headers, runtime)

    async def get_resource_group_request_async(
        self,
        request: main_models.GetResourceGroupRequestRequest,
    ) -> main_models.GetResourceGroupRequestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_request_with_options_async(request, headers, runtime)

    def get_resource_group_total_with_options(
        self,
        request: main_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupTotal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/total',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_total_with_options_async(
        self,
        request: main_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupTotal',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/total',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_total(
        self,
        request: main_models.GetResourceGroupTotalRequest,
    ) -> main_models.GetResourceGroupTotalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_total_with_options(request, headers, runtime)

    async def get_resource_group_total_async(
        self,
        request: main_models.GetResourceGroupTotalRequest,
    ) -> main_models.GetResourceGroupTotalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_total_with_options_async(request, headers, runtime)

    def get_spot_price_history_with_options(
        self,
        instance_type: str,
        request: main_models.GetSpotPriceHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSpotPriceHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSpotPriceHistory',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/spots/{DaraURL.percent_encode(instance_type)}/pricehistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSpotPriceHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spot_price_history_with_options_async(
        self,
        instance_type: str,
        request: main_models.GetSpotPriceHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSpotPriceHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSpotPriceHistory',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/spots/{DaraURL.percent_encode(instance_type)}/pricehistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSpotPriceHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spot_price_history(
        self,
        instance_type: str,
        request: main_models.GetSpotPriceHistoryRequest,
    ) -> main_models.GetSpotPriceHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_spot_price_history_with_options(instance_type, request, headers, runtime)

    async def get_spot_price_history_async(
        self,
        instance_type: str,
        request: main_models.GetSpotPriceHistoryRequest,
    ) -> main_models.GetSpotPriceHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_spot_price_history_with_options_async(instance_type, request, headers, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_training_job_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_training_job_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_training_job(
        self,
        training_job_id: str,
    ) -> main_models.GetTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_training_job_with_options(training_job_id, headers, runtime)

    async def get_training_job_async(
        self,
        training_job_id: str,
    ) -> main_models.GetTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_training_job_with_options_async(training_job_id, headers, runtime)

    def get_training_job_error_info_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobErrorInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJobErrorInfo',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/errorinfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobErrorInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_training_job_error_info_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobErrorInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJobErrorInfo',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/errorinfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobErrorInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_training_job_error_info(
        self,
        training_job_id: str,
    ) -> main_models.GetTrainingJobErrorInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_training_job_error_info_with_options(training_job_id, headers, runtime)

    async def get_training_job_error_info_async(
        self,
        training_job_id: str,
    ) -> main_models.GetTrainingJobErrorInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_training_job_error_info_with_options_async(training_job_id, headers, runtime)

    def get_training_job_latest_metrics_with_options(
        self,
        training_job_id: str,
        request: main_models.GetTrainingJobLatestMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobLatestMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJobLatestMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/latestmetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobLatestMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_training_job_latest_metrics_with_options_async(
        self,
        training_job_id: str,
        request: main_models.GetTrainingJobLatestMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrainingJobLatestMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrainingJobLatestMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/latestmetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrainingJobLatestMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_training_job_latest_metrics(
        self,
        training_job_id: str,
        request: main_models.GetTrainingJobLatestMetricsRequest,
    ) -> main_models.GetTrainingJobLatestMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_training_job_latest_metrics_with_options(training_job_id, request, headers, runtime)

    async def get_training_job_latest_metrics_async(
        self,
        training_job_id: str,
        request: main_models.GetTrainingJobLatestMetricsRequest,
    ) -> main_models.GetTrainingJobLatestMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_training_job_latest_metrics_with_options_async(training_job_id, request, headers, runtime)

    def get_user_view_metrics_with_options(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserViewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserViewMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/usermetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserViewMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_view_metrics_with_options_async(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserViewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserViewMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/usermetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserViewMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_view_metrics(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
    ) -> main_models.GetUserViewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_view_metrics_with_options(resource_group_id, request, headers, runtime)

    async def get_user_view_metrics_async(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
    ) -> main_models.GetUserViewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_view_metrics_with_options_async(resource_group_id, request, headers, runtime)

    def list_algorithm_versions_with_options(
        self,
        algorithm_id: str,
        request: main_models.ListAlgorithmVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlgorithmVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlgorithmVersions',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlgorithmVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithm_versions_with_options_async(
        self,
        algorithm_id: str,
        request: main_models.ListAlgorithmVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlgorithmVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlgorithmVersions',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlgorithmVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_algorithm_versions(
        self,
        algorithm_id: str,
        request: main_models.ListAlgorithmVersionsRequest,
    ) -> main_models.ListAlgorithmVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_algorithm_versions_with_options(algorithm_id, request, headers, runtime)

    async def list_algorithm_versions_async(
        self,
        algorithm_id: str,
        request: main_models.ListAlgorithmVersionsRequest,
    ) -> main_models.ListAlgorithmVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_algorithm_versions_with_options_async(algorithm_id, request, headers, runtime)

    def list_algorithms_with_options(
        self,
        request: main_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlgorithmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not DaraCore.is_null(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlgorithms',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithms_with_options_async(
        self,
        request: main_models.ListAlgorithmsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlgorithmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not DaraCore.is_null(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlgorithms',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlgorithmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_algorithms(
        self,
        request: main_models.ListAlgorithmsRequest,
    ) -> main_models.ListAlgorithmsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_algorithms_with_options(request, headers, runtime)

    async def list_algorithms_async(
        self,
        request: main_models.ListAlgorithmsRequest,
    ) -> main_models.ListAlgorithmsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_algorithms_with_options_async(request, headers, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_count):
            request.health_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_count, 'HealthCount', 'json')
        if not DaraCore.is_null(tmp_req.health_rate):
            request.health_rate_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_rate, 'HealthRate', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.availability_zone):
            query['AvailabilityZone'] = request.availability_zone
        if not DaraCore.is_null(request.clique_id):
            query['CliqueID'] = request.clique_id
        if not DaraCore.is_null(request.filter_by_quota_id):
            query['FilterByQuotaId'] = request.filter_by_quota_id
        if not DaraCore.is_null(request.filter_by_resource_group_ids):
            query['FilterByResourceGroupIds'] = request.filter_by_resource_group_ids
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.health_count_shrink):
            query['HealthCount'] = request.health_count_shrink
        if not DaraCore.is_null(request.health_rate_shrink):
            query['HealthRate'] = request.health_rate_shrink
        if not DaraCore.is_null(request.hyper_node):
            query['HyperNode'] = request.hyper_node
        if not DaraCore.is_null(request.hyper_zone):
            query['HyperZone'] = request.hyper_zone
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIds'] = request.machine_group_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_statuses):
            query['NodeStatuses'] = request.node_statuses
        if not DaraCore.is_null(request.node_types):
            query['NodeTypes'] = request.node_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_ids):
            query['OrderInstanceIds'] = request.order_instance_ids
        if not DaraCore.is_null(request.order_statuses):
            query['OrderStatuses'] = request.order_statuses
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.reason_codes):
            query['ReasonCodes'] = request.reason_codes
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_count):
            request.health_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_count, 'HealthCount', 'json')
        if not DaraCore.is_null(tmp_req.health_rate):
            request.health_rate_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_rate, 'HealthRate', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.availability_zone):
            query['AvailabilityZone'] = request.availability_zone
        if not DaraCore.is_null(request.clique_id):
            query['CliqueID'] = request.clique_id
        if not DaraCore.is_null(request.filter_by_quota_id):
            query['FilterByQuotaId'] = request.filter_by_quota_id
        if not DaraCore.is_null(request.filter_by_resource_group_ids):
            query['FilterByResourceGroupIds'] = request.filter_by_resource_group_ids
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.health_count_shrink):
            query['HealthCount'] = request.health_count_shrink
        if not DaraCore.is_null(request.health_rate_shrink):
            query['HealthRate'] = request.health_rate_shrink
        if not DaraCore.is_null(request.hyper_node):
            query['HyperNode'] = request.hyper_node
        if not DaraCore.is_null(request.hyper_zone):
            query['HyperZone'] = request.hyper_zone
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIds'] = request.machine_group_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_statuses):
            query['NodeStatuses'] = request.node_statuses
        if not DaraCore.is_null(request.node_types):
            query['NodeTypes'] = request.node_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_ids):
            query['OrderInstanceIds'] = request.order_instance_ids
        if not DaraCore.is_null(request.order_statuses):
            query['OrderStatuses'] = request.order_statuses
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.reason_codes):
            query['ReasonCodes'] = request.reason_codes
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(request, headers, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_nodes_with_options_async(request, headers, runtime)

    def list_quota_workloads_with_options(
        self,
        quota_id: str,
        request: main_models.ListQuotaWorkloadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaWorkloadsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.before_workload_id):
            query['BeforeWorkloadId'] = request.before_workload_id
        if not DaraCore.is_null(request.gmt_dequeued_time_range):
            query['GmtDequeuedTimeRange'] = request.gmt_dequeued_time_range
        if not DaraCore.is_null(request.gmt_enqueued_time_range):
            query['GmtEnqueuedTimeRange'] = request.gmt_enqueued_time_range
        if not DaraCore.is_null(request.gmt_position_modified_time_range):
            query['GmtPositionModifiedTimeRange'] = request.gmt_position_modified_time_range
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_quota_ids):
            query['SubQuotaIds'] = request.sub_quota_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.with_historical_data):
            query['WithHistoricalData'] = request.with_historical_data
        if not DaraCore.is_null(request.workload_created_time_range):
            query['WorkloadCreatedTimeRange'] = request.workload_created_time_range
        if not DaraCore.is_null(request.workload_ids):
            query['WorkloadIds'] = request.workload_ids
        if not DaraCore.is_null(request.workload_statuses):
            query['WorkloadStatuses'] = request.workload_statuses
        if not DaraCore.is_null(request.workload_type):
            query['WorkloadType'] = request.workload_type
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaWorkloads',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}/workloads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaWorkloadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_workloads_with_options_async(
        self,
        quota_id: str,
        request: main_models.ListQuotaWorkloadsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaWorkloadsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.before_workload_id):
            query['BeforeWorkloadId'] = request.before_workload_id
        if not DaraCore.is_null(request.gmt_dequeued_time_range):
            query['GmtDequeuedTimeRange'] = request.gmt_dequeued_time_range
        if not DaraCore.is_null(request.gmt_enqueued_time_range):
            query['GmtEnqueuedTimeRange'] = request.gmt_enqueued_time_range
        if not DaraCore.is_null(request.gmt_position_modified_time_range):
            query['GmtPositionModifiedTimeRange'] = request.gmt_position_modified_time_range
        if not DaraCore.is_null(request.node_name):
            query['NodeName'] = request.node_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_quota_ids):
            query['SubQuotaIds'] = request.sub_quota_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.with_historical_data):
            query['WithHistoricalData'] = request.with_historical_data
        if not DaraCore.is_null(request.workload_created_time_range):
            query['WorkloadCreatedTimeRange'] = request.workload_created_time_range
        if not DaraCore.is_null(request.workload_ids):
            query['WorkloadIds'] = request.workload_ids
        if not DaraCore.is_null(request.workload_statuses):
            query['WorkloadStatuses'] = request.workload_statuses
        if not DaraCore.is_null(request.workload_type):
            query['WorkloadType'] = request.workload_type
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotaWorkloads',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}/workloads',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaWorkloadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota_workloads(
        self,
        quota_id: str,
        request: main_models.ListQuotaWorkloadsRequest,
    ) -> main_models.ListQuotaWorkloadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quota_workloads_with_options(quota_id, request, headers, runtime)

    async def list_quota_workloads_async(
        self,
        quota_id: str,
        request: main_models.ListQuotaWorkloadsRequest,
    ) -> main_models.ListQuotaWorkloadsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quota_workloads_with_options_async(quota_id, request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.has_resource):
            query['HasResource'] = request.has_resource
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.has_resource):
            query['HasResource'] = request.has_resource
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_resource_group_machine_groups_with_options(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not DaraCore.is_null(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIDs'] = request.machine_group_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_id):
            query['OrderInstanceId'] = request.order_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMachineGroups',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMachineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_machine_groups_with_options_async(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not DaraCore.is_null(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIDs'] = request.machine_group_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_id):
            query['OrderInstanceId'] = request.order_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMachineGroups',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMachineGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_machine_groups(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_group_machine_groups_with_options(resource_group_id, request, headers, runtime)

    async def list_resource_group_machine_groups_async(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_group_machine_groups_with_options_async(resource_group_id, request, headers, runtime)

    def list_resource_groups_with_options(
        self,
        request: main_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.has_resource):
            query['HasResource'] = request.has_resource
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIDs'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.show_all):
            query['ShowAll'] = request.show_all
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: main_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.has_resource):
            query['HasResource'] = request.has_resource
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIDs'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.show_all):
            query['ShowAll'] = request.show_all
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_groups_with_options(request, headers, runtime)

    async def list_resource_groups_async(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_groups_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_training_job_events_with_options(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobEvents',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_events_with_options_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobEvents',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_events(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobEventsRequest,
    ) -> main_models.ListTrainingJobEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_events_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_events_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobEventsRequest,
    ) -> main_models.ListTrainingJobEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_events_with_options_async(training_job_id, request, headers, runtime)

    def list_training_job_instance_events_with_options(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.ListTrainingJobInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobInstanceEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobInstanceEvents',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobInstanceEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_instance_events_with_options_async(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.ListTrainingJobInstanceEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobInstanceEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobInstanceEvents',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instances/{DaraURL.percent_encode(instance_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobInstanceEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_instance_events(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.ListTrainingJobInstanceEventsRequest,
    ) -> main_models.ListTrainingJobInstanceEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_instance_events_with_options(training_job_id, instance_id, request, headers, runtime)

    async def list_training_job_instance_events_async(
        self,
        training_job_id: str,
        instance_id: str,
        request: main_models.ListTrainingJobInstanceEventsRequest,
    ) -> main_models.ListTrainingJobInstanceEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_instance_events_with_options_async(training_job_id, instance_id, request, headers, runtime)

    def list_training_job_instance_metrics_with_options(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobInstanceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobInstanceMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instancemetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_instance_metrics_with_options_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobInstanceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobInstanceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobInstanceMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/instancemetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobInstanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_instance_metrics(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobInstanceMetricsRequest,
    ) -> main_models.ListTrainingJobInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_instance_metrics_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_instance_metrics_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobInstanceMetricsRequest,
    ) -> main_models.ListTrainingJobInstanceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_instance_metrics_with_options_async(training_job_id, request, headers, runtime)

    def list_training_job_logs_with_options(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobLogs',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_logs_with_options_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobLogs',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_logs(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobLogsRequest,
    ) -> main_models.ListTrainingJobLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_logs_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_logs_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobLogsRequest,
    ) -> main_models.ListTrainingJobLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_logs_with_options_async(training_job_id, request, headers, runtime)

    def list_training_job_metrics_with_options(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_metrics_with_options_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobMetrics',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_metrics(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobMetricsRequest,
    ) -> main_models.ListTrainingJobMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_metrics_with_options(training_job_id, request, headers, runtime)

    async def list_training_job_metrics_async(
        self,
        training_job_id: str,
        request: main_models.ListTrainingJobMetricsRequest,
    ) -> main_models.ListTrainingJobMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_metrics_with_options_async(training_job_id, request, headers, runtime)

    def list_training_job_output_models_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobOutputModelsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobOutputModels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/outputmodels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobOutputModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_job_output_models_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobOutputModelsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobOutputModels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/outputmodels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobOutputModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_job_output_models(
        self,
        training_job_id: str,
    ) -> main_models.ListTrainingJobOutputModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_job_output_models_with_options(training_job_id, headers, runtime)

    async def list_training_job_output_models_async(
        self,
        training_job_id: str,
    ) -> main_models.ListTrainingJobOutputModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_job_output_models_with_options_async(training_job_id, headers, runtime)

    def list_training_jobs_with_options(
        self,
        tmp_req: main_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobsResponse:
        tmp_req.validate()
        request = main_models.ListTrainingJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_temp_algo):
            query['IsTempAlgo'] = request.is_temp_algo
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        if not DaraCore.is_null(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobs',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_training_jobs_with_options_async(
        self,
        tmp_req: main_models.ListTrainingJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTrainingJobsResponse:
        tmp_req.validate()
        request = main_models.ListTrainingJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.algorithm_name):
            query['AlgorithmName'] = request.algorithm_name
        if not DaraCore.is_null(request.algorithm_provider):
            query['AlgorithmProvider'] = request.algorithm_provider
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_temp_algo):
            query['IsTempAlgo'] = request.is_temp_algo
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.training_job_id):
            query['TrainingJobId'] = request.training_job_id
        if not DaraCore.is_null(request.training_job_name):
            query['TrainingJobName'] = request.training_job_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrainingJobs',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrainingJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_training_jobs(
        self,
        request: main_models.ListTrainingJobsRequest,
    ) -> main_models.ListTrainingJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_training_jobs_with_options(request, headers, runtime)

    async def list_training_jobs_async(
        self,
        request: main_models.ListTrainingJobsRequest,
    ) -> main_models.ListTrainingJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_training_jobs_with_options_async(request, headers, runtime)

    def operate_node_with_options(
        self,
        node_id: str,
        request: main_models.OperateNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['Operation'] = request.operation
        if not DaraCore.is_null(request.operation_parameters):
            body['OperationParameters'] = request.operation_parameters
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateNode',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes/{DaraURL.percent_encode(node_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_node_with_options_async(
        self,
        node_id: str,
        request: main_models.OperateNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['Operation'] = request.operation
        if not DaraCore.is_null(request.operation_parameters):
            body['OperationParameters'] = request.operation_parameters
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateNode',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes/{DaraURL.percent_encode(node_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_node(
        self,
        node_id: str,
        request: main_models.OperateNodeRequest,
    ) -> main_models.OperateNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.operate_node_with_options(node_id, request, headers, runtime)

    async def operate_node_async(
        self,
        node_id: str,
        request: main_models.OperateNodeRequest,
    ) -> main_models.OperateNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.operate_node_with_options_async(node_id, request, headers, runtime)

    def scale_quota_with_options(
        self,
        quota_id: str,
        request: main_models.ScaleQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.min):
            body['Min'] = request.min
        if not DaraCore.is_null(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}/action/scale',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_quota_with_options_async(
        self,
        quota_id: str,
        request: main_models.ScaleQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.min):
            body['Min'] = request.min
        if not DaraCore.is_null(request.resource_group_ids):
            body['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}/action/scale',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_quota(
        self,
        quota_id: str,
        request: main_models.ScaleQuotaRequest,
    ) -> main_models.ScaleQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_quota_with_options(quota_id, request, headers, runtime)

    async def scale_quota_async(
        self,
        quota_id: str,
        request: main_models.ScaleQuotaRequest,
    ) -> main_models.ScaleQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_quota_with_options_async(quota_id, request, headers, runtime)

    def stop_training_job_with_options(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_training_job_with_options_async(
        self,
        training_job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTrainingJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopTrainingJob',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTrainingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_training_job(
        self,
        training_job_id: str,
    ) -> main_models.StopTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_training_job_with_options(training_job_id, headers, runtime)

    async def stop_training_job_async(
        self,
        training_job_id: str,
    ) -> main_models.StopTrainingJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_training_job_with_options_async(training_job_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_algorithm_with_options(
        self,
        algorithm_id: str,
        request: main_models.UpdateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlgorithmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_algorithm_with_options_async(
        self,
        algorithm_id: str,
        request: main_models.UpdateAlgorithmRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlgorithmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.algorithm_description):
            body['AlgorithmDescription'] = request.algorithm_description
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlgorithm',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_algorithm(
        self,
        algorithm_id: str,
        request: main_models.UpdateAlgorithmRequest,
    ) -> main_models.UpdateAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_algorithm_with_options(algorithm_id, request, headers, runtime)

    async def update_algorithm_async(
        self,
        algorithm_id: str,
        request: main_models.UpdateAlgorithmRequest,
    ) -> main_models.UpdateAlgorithmResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_algorithm_with_options_async(algorithm_id, request, headers, runtime)

    def update_algorithm_version_with_options(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: main_models.UpdateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlgorithmVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateAlgorithmVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not DaraCore.is_null(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlgorithmVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_algorithm_version_with_options_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        tmp_req: main_models.UpdateAlgorithmVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlgorithmVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateAlgorithmVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.algorithm_spec):
            request.algorithm_spec_shrink = Utils.array_to_string_with_specified_style(tmp_req.algorithm_spec, 'AlgorithmSpec', 'json')
        body = {}
        if not DaraCore.is_null(request.algorithm_spec_shrink):
            body['AlgorithmSpec'] = request.algorithm_spec_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlgorithmVersion',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/algorithms/{DaraURL.percent_encode(algorithm_id)}/versions/{DaraURL.percent_encode(algorithm_version)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlgorithmVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_algorithm_version(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: main_models.UpdateAlgorithmVersionRequest,
    ) -> main_models.UpdateAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_algorithm_version_with_options(algorithm_id, algorithm_version, request, headers, runtime)

    async def update_algorithm_version_async(
        self,
        algorithm_id: str,
        algorithm_version: str,
        request: main_models.UpdateAlgorithmVersionRequest,
    ) -> main_models.UpdateAlgorithmVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_algorithm_version_with_options_async(algorithm_id, algorithm_version, request, headers, runtime)

    def update_quota_with_options(
        self,
        quota_id: str,
        request: main_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not DaraCore.is_null(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not DaraCore.is_null(request.quota_name):
            body['QuotaName'] = request.quota_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_with_options_async(
        self,
        quota_id: str,
        request: main_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.queue_strategy):
            body['QueueStrategy'] = request.queue_strategy
        if not DaraCore.is_null(request.quota_config):
            body['QuotaConfig'] = request.quota_config
        if not DaraCore.is_null(request.quota_name):
            body['QuotaName'] = request.quota_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuota',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota(
        self,
        quota_id: str,
        request: main_models.UpdateQuotaRequest,
    ) -> main_models.UpdateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(quota_id, request, headers, runtime)

    async def update_quota_async(
        self,
        quota_id: str,
        request: main_models.UpdateQuotaRequest,
    ) -> main_models.UpdateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_quota_with_options_async(quota_id, request, headers, runtime)

    def update_resource_group_with_options(
        self,
        resource_group_id: str,
        request: main_models.UpdateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.unbind):
            body['Unbind'] = request.unbind
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        resource_group_id: str,
        request: main_models.UpdateResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.unbind):
            body['Unbind'] = request.unbind
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceGroup',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        resource_group_id: str,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_group_with_options(resource_group_id, request, headers, runtime)

    async def update_resource_group_async(
        self,
        resource_group_id: str,
        request: main_models.UpdateResourceGroupRequest,
    ) -> main_models.UpdateResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_group_with_options_async(resource_group_id, request, headers, runtime)

    def update_training_job_labels_with_options(
        self,
        training_job_id: str,
        request: main_models.UpdateTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrainingJobLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrainingJobLabels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrainingJobLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_training_job_labels_with_options_async(
        self,
        training_job_id: str,
        request: main_models.UpdateTrainingJobLabelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrainingJobLabelsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrainingJobLabels',
            version = '2022-01-12',
            protocol = 'HTTPS',
            pathname = f'/api/v1/trainingjobs/{DaraURL.percent_encode(training_job_id)}/labels',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrainingJobLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_training_job_labels(
        self,
        training_job_id: str,
        request: main_models.UpdateTrainingJobLabelsRequest,
    ) -> main_models.UpdateTrainingJobLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_training_job_labels_with_options(training_job_id, request, headers, runtime)

    async def update_training_job_labels_async(
        self,
        training_job_id: str,
        request: main_models.UpdateTrainingJobLabelsRequest,
    ) -> main_models.UpdateTrainingJobLabelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_training_job_labels_with_options_async(training_job_id, request, headers, runtime)

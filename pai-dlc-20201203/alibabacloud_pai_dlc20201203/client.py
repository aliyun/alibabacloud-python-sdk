# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pai_dlc20201203 import models as main_models
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
            'ap-northeast-2-pop': 'pai-dlc.aliyuncs.com',
            'ap-south-1': 'pai-dlc.aliyuncs.com',
            'ap-southeast-2': 'pai-dlc.aliyuncs.com',
            'cn-beijing-finance-1': 'pai-dlc.aliyuncs.com',
            'cn-beijing-finance-pop': 'pai-dlc.aliyuncs.com',
            'cn-beijing-gov-1': 'pai-dlc.aliyuncs.com',
            'cn-beijing-nu16-b01': 'pai-dlc.aliyuncs.com',
            'cn-chengdu': 'pai-dlc.aliyuncs.com',
            'cn-edge-1': 'pai-dlc.aliyuncs.com',
            'cn-fujian': 'pai-dlc.aliyuncs.com',
            'cn-haidian-cm12-c01': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-finance': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'pai-dlc.aliyuncs.com',
            'cn-hangzhou-test-306': 'pai-dlc.aliyuncs.com',
            'cn-hongkong-finance-pop': 'pai-dlc.aliyuncs.com',
            'cn-huhehaote': 'pai-dlc.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'pai-dlc.aliyuncs.com',
            'cn-north-2-gov-1': 'pai-dlc.aliyuncs.com',
            'cn-qingdao': 'pai-dlc.aliyuncs.com',
            'cn-qingdao-nebula': 'pai-dlc.aliyuncs.com',
            'cn-shanghai-et15-b01': 'pai-dlc.aliyuncs.com',
            'cn-shanghai-et2-b01': 'pai-dlc.aliyuncs.com',
            'cn-shanghai-inner': 'pai-dlc.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'pai-dlc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'pai-dlc.aliyuncs.com',
            'cn-shenzhen-inner': 'pai-dlc.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'pai-dlc.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'pai-dlc.aliyuncs.com',
            'cn-wuhan': 'pai-dlc.aliyuncs.com',
            'cn-yushanfang': 'pai-dlc.aliyuncs.com',
            'cn-zhangbei': 'pai-dlc.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'pai-dlc.aliyuncs.com',
            'cn-zhangjiakou': 'pai-dlc.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'pai-dlc.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'pai-dlc.aliyuncs.com',
            'eu-west-1': 'pai-dlc.aliyuncs.com',
            'eu-west-1-oxs': 'pai-dlc.aliyuncs.com',
            'me-east-1': 'pai-dlc.aliyuncs.com',
            'rus-west-1-pop': 'pai-dlc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('pai-dlc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_job_with_options(
        self,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.code_source):
            body['CodeSource'] = request.code_source
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.debugger_config_content):
            body['DebuggerConfigContent'] = request.debugger_config_content
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        if not DaraCore.is_null(request.envs):
            body['Envs'] = request.envs
        if not DaraCore.is_null(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not DaraCore.is_null(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.settings):
            body['Settings'] = request.settings
        if not DaraCore.is_null(request.success_policy):
            body['SuccessPolicy'] = request.success_policy
        if not DaraCore.is_null(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not DaraCore.is_null(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.code_source):
            body['CodeSource'] = request.code_source
        if not DaraCore.is_null(request.credential_config):
            body['CredentialConfig'] = request.credential_config
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.debugger_config_content):
            body['DebuggerConfigContent'] = request.debugger_config_content
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        if not DaraCore.is_null(request.envs):
            body['Envs'] = request.envs
        if not DaraCore.is_null(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not DaraCore.is_null(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not DaraCore.is_null(request.job_type):
            body['JobType'] = request.job_type
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.settings):
            body['Settings'] = request.settings
        if not DaraCore.is_null(request.success_policy):
            body['SuccessPolicy'] = request.success_policy
        if not DaraCore.is_null(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not DaraCore.is_null(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not DaraCore.is_null(request.user_command):
            body['UserCommand'] = request.user_command
        if not DaraCore.is_null(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_tensorboard_with_options(
        self,
        request: main_models.CreateTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTensorboardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.cpu):
            body['Cpu'] = request.cpu
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_running_time_minutes):
            body['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.quota_id):
            body['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not DaraCore.is_null(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not DaraCore.is_null(request.tensorboard_data_sources):
            body['TensorboardDataSources'] = request.tensorboard_data_sources
        if not DaraCore.is_null(request.tensorboard_spec):
            body['TensorboardSpec'] = request.tensorboard_spec
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tensorboard_with_options_async(
        self,
        request: main_models.CreateTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTensorboardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.cpu):
            body['Cpu'] = request.cpu
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.data_sources):
            body['DataSources'] = request.data_sources
        if not DaraCore.is_null(request.display_name):
            body['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.job_id):
            body['JobId'] = request.job_id
        if not DaraCore.is_null(request.max_running_time_minutes):
            body['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not DaraCore.is_null(request.memory):
            body['Memory'] = request.memory
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.quota_id):
            body['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.source_id):
            body['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not DaraCore.is_null(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not DaraCore.is_null(request.tensorboard_data_sources):
            body['TensorboardDataSources'] = request.tensorboard_data_sources
        if not DaraCore.is_null(request.tensorboard_spec):
            body['TensorboardSpec'] = request.tensorboard_spec
        if not DaraCore.is_null(request.uri):
            body['Uri'] = request.uri
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tensorboard(
        self,
        request: main_models.CreateTensorboardRequest,
    ) -> main_models.CreateTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_tensorboard_with_options(request, headers, runtime)

    async def create_tensorboard_async(
        self,
        request: main_models.CreateTensorboardRequest,
    ) -> main_models.CreateTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_tensorboard_with_options_async(request, headers, runtime)

    def delete_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        job_id: str,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(job_id, headers, runtime)

    async def delete_job_async(
        self,
        job_id: str,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(job_id, headers, runtime)

    def delete_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: main_models.DeleteTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.DeleteTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tensorboard(
        self,
        tensorboard_id: str,
        request: main_models.DeleteTensorboardRequest,
    ) -> main_models.DeleteTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def delete_tensorboard_async(
        self,
        tensorboard_id: str,
        request: main_models.DeleteTensorboardRequest,
    ) -> main_models.DeleteTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def get_dashboard_with_options(
        self,
        job_id: str,
        request: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['isShared'] = request.is_shared
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/dashboard',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        job_id: str,
        request: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['isShared'] = request.is_shared
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/dashboard',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        job_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(job_id, request, headers, runtime)

    async def get_dashboard_async(
        self,
        job_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(job_id, request, headers, runtime)

    def get_job_with_options(
        self,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.need_detail):
            query['NeedDetail'] = request.need_detail
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.need_detail):
            query['NeedDetail'] = request.need_detail
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, request, headers, runtime)

    async def get_job_async(
        self,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(job_id, request, headers, runtime)

    def get_job_events_with_options(
        self,
        job_id: str,
        request: main_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobEvents',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_events_with_options_async(
        self,
        job_id: str,
        request: main_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobEvents',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_events(
        self,
        job_id: str,
        request: main_models.GetJobEventsRequest,
    ) -> main_models.GetJobEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_events_with_options(job_id, request, headers, runtime)

    async def get_job_events_async(
        self,
        job_id: str,
        request: main_models.GetJobEventsRequest,
    ) -> main_models.GetJobEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_events_with_options_async(job_id, request, headers, runtime)

    def get_job_metrics_with_options(
        self,
        job_id: str,
        request: main_models.GetJobMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobMetrics',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_metrics_with_options_async(
        self,
        job_id: str,
        request: main_models.GetJobMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobMetrics',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_metrics(
        self,
        job_id: str,
        request: main_models.GetJobMetricsRequest,
    ) -> main_models.GetJobMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_metrics_with_options(job_id, request, headers, runtime)

    async def get_job_metrics_async(
        self,
        job_id: str,
        request: main_models.GetJobMetricsRequest,
    ) -> main_models.GetJobMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_metrics_with_options_async(job_id, request, headers, runtime)

    def get_job_sanity_check_result_with_options(
        self,
        job_id: str,
        request: main_models.GetJobSanityCheckResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobSanityCheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sanity_check_number):
            query['SanityCheckNumber'] = request.sanity_check_number
        if not DaraCore.is_null(request.sanity_check_phase):
            query['SanityCheckPhase'] = request.sanity_check_phase
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobSanityCheckResult',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/sanitycheckresult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobSanityCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_sanity_check_result_with_options_async(
        self,
        job_id: str,
        request: main_models.GetJobSanityCheckResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobSanityCheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sanity_check_number):
            query['SanityCheckNumber'] = request.sanity_check_number
        if not DaraCore.is_null(request.sanity_check_phase):
            query['SanityCheckPhase'] = request.sanity_check_phase
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobSanityCheckResult',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/sanitycheckresult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobSanityCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_sanity_check_result(
        self,
        job_id: str,
        request: main_models.GetJobSanityCheckResultRequest,
    ) -> main_models.GetJobSanityCheckResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_sanity_check_result_with_options(job_id, request, headers, runtime)

    async def get_job_sanity_check_result_async(
        self,
        job_id: str,
        request: main_models.GetJobSanityCheckResultRequest,
    ) -> main_models.GetJobSanityCheckResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_sanity_check_result_with_options_async(job_id, request, headers, runtime)

    def get_pod_events_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPodEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPodEvents',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPodEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pod_events_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPodEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPodEvents',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPodEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pod_events(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodEventsRequest,
    ) -> main_models.GetPodEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pod_events_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_events_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodEventsRequest,
    ) -> main_models.GetPodEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pod_events_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_pod_logs_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPodLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPodLogs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPodLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pod_logs_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPodLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPodLogs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPodLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pod_logs(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodLogsRequest,
    ) -> main_models.GetPodLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pod_logs_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_logs_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetPodLogsRequest,
    ) -> main_models.GetPodLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pod_logs_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_ray_dashboard_with_options(
        self,
        job_id: str,
        request: main_models.GetRayDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRayDashboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['isShared'] = request.is_shared
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRayDashboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/rayDashboard',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRayDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ray_dashboard_with_options_async(
        self,
        job_id: str,
        request: main_models.GetRayDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRayDashboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['isShared'] = request.is_shared
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRayDashboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/rayDashboard',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRayDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ray_dashboard(
        self,
        job_id: str,
        request: main_models.GetRayDashboardRequest,
    ) -> main_models.GetRayDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ray_dashboard_with_options(job_id, request, headers, runtime)

    async def get_ray_dashboard_async(
        self,
        job_id: str,
        request: main_models.GetRayDashboardRequest,
    ) -> main_models.GetRayDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ray_dashboard_with_options_async(job_id, request, headers, runtime)

    def get_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jod_id):
            query['JodId'] = request.jod_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.jod_id):
            query['JodId'] = request.jod_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tensorboard(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardRequest,
    ) -> main_models.GetTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def get_tensorboard_async(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardRequest,
    ) -> main_models.GetTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def get_tensorboard_shared_url_with_options(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardSharedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTensorboardSharedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time_seconds):
            query['ExpireTimeSeconds'] = request.expire_time_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTensorboardSharedUrl',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/sharedurl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTensorboardSharedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tensorboard_shared_url_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardSharedUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTensorboardSharedUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time_seconds):
            query['ExpireTimeSeconds'] = request.expire_time_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTensorboardSharedUrl',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/sharedurl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTensorboardSharedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tensorboard_shared_url(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardSharedUrlRequest,
    ) -> main_models.GetTensorboardSharedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tensorboard_shared_url_with_options(tensorboard_id, request, headers, runtime)

    async def get_tensorboard_shared_url_async(
        self,
        tensorboard_id: str,
        request: main_models.GetTensorboardSharedUrlRequest,
    ) -> main_models.GetTensorboardSharedUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tensorboard_shared_url_with_options_async(tensorboard_id, request, headers, runtime)

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
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2020-12-03',
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
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2020-12-03',
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

    def get_web_terminal_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetWebTerminalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebTerminalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebTerminal',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/webterminal',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_web_terminal_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetWebTerminalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebTerminalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.pod_uid):
            query['PodUid'] = request.pod_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebTerminal',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/pods/{DaraURL.percent_encode(pod_id)}/webterminal',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_web_terminal(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetWebTerminalRequest,
    ) -> main_models.GetWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_web_terminal_with_options(job_id, pod_id, request, headers, runtime)

    async def get_web_terminal_async(
        self,
        job_id: str,
        pod_id: str,
        request: main_models.GetWebTerminalRequest,
    ) -> main_models.GetWebTerminalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_web_terminal_with_options_async(job_id, pod_id, request, headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: main_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsSpecs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/ecsspecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: main_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsSpecsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsSpecs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/ecsspecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_specs(
        self,
        request: main_models.ListEcsSpecsRequest,
    ) -> main_models.ListEcsSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: main_models.ListEcsSpecsRequest,
    ) -> main_models.ListEcsSpecsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_job_sanity_check_results_with_options(
        self,
        job_id: str,
        request: main_models.ListJobSanityCheckResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobSanityCheckResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobSanityCheckResults',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/sanitycheckresults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobSanityCheckResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_sanity_check_results_with_options_async(
        self,
        job_id: str,
        request: main_models.ListJobSanityCheckResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobSanityCheckResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobSanityCheckResults',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/sanitycheckresults',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobSanityCheckResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_sanity_check_results(
        self,
        job_id: str,
        request: main_models.ListJobSanityCheckResultsRequest,
    ) -> main_models.ListJobSanityCheckResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_sanity_check_results_with_options(job_id, request, headers, runtime)

    async def list_job_sanity_check_results_async(
        self,
        job_id: str,
        request: main_models.ListJobSanityCheckResultsRequest,
    ) -> main_models.ListJobSanityCheckResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_sanity_check_results_with_options_async(job_id, request, headers, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.display_name_search_mode):
            query['DisplayNameSearchMode'] = request.display_name_search_mode
        if not DaraCore.is_null(request.enable_assign_node):
            query['EnableAssignNode'] = request.enable_assign_node
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.from_all_workspaces):
            query['FromAllWorkspaces'] = request.from_all_workspaces
        if not DaraCore.is_null(request.image_search):
            query['ImageSearch'] = request.image_search
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.numeric_range_field):
            query['NumericRangeField'] = request.numeric_range_field
        if not DaraCore.is_null(request.numeric_range_max):
            query['NumericRangeMax'] = request.numeric_range_max
        if not DaraCore.is_null(request.numeric_range_min):
            query['NumericRangeMin'] = request.numeric_range_min
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.reason_search):
            query['ReasonSearch'] = request.reason_search
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_quota_name):
            query['ResourceQuotaName'] = request.resource_quota_name
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.time_range_field):
            query['TimeRangeField'] = request.time_range_field
        if not DaraCore.is_null(request.user_command_search):
            query['UserCommandSearch'] = request.user_command_search
        if not DaraCore.is_null(request.user_id_for_filter):
            query['UserIdForFilter'] = request.user_id_for_filter
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tmp_req: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        tmp_req.validate()
        request = main_models.ListJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.display_name_search_mode):
            query['DisplayNameSearchMode'] = request.display_name_search_mode
        if not DaraCore.is_null(request.enable_assign_node):
            query['EnableAssignNode'] = request.enable_assign_node
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.from_all_workspaces):
            query['FromAllWorkspaces'] = request.from_all_workspaces
        if not DaraCore.is_null(request.image_search):
            query['ImageSearch'] = request.image_search
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.numeric_range_field):
            query['NumericRangeField'] = request.numeric_range_field
        if not DaraCore.is_null(request.numeric_range_max):
            query['NumericRangeMax'] = request.numeric_range_max
        if not DaraCore.is_null(request.numeric_range_min):
            query['NumericRangeMin'] = request.numeric_range_min
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.reason_search):
            query['ReasonSearch'] = request.reason_search
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_quota_name):
            query['ResourceQuotaName'] = request.resource_quota_name
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.time_range_field):
            query['TimeRangeField'] = request.time_range_field
        if not DaraCore.is_null(request.user_command_search):
            query['UserCommandSearch'] = request.user_command_search
        if not DaraCore.is_null(request.user_id_for_filter):
            query['UserIdForFilter'] = request.user_id_for_filter
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_tensorboards_with_options(
        self,
        request: main_models.ListTensorboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTensorboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTensorboards',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTensorboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tensorboards_with_options_async(
        self,
        request: main_models.ListTensorboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTensorboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.show_own):
            query['ShowOwn'] = request.show_own
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTensorboards',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTensorboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tensorboards(
        self,
        request: main_models.ListTensorboardsRequest,
    ) -> main_models.ListTensorboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tensorboards_with_options(request, headers, runtime)

    async def list_tensorboards_async(
        self,
        request: main_models.ListTensorboardsRequest,
    ) -> main_models.ListTensorboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tensorboards_with_options_async(request, headers, runtime)

    def start_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: main_models.StartTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.StartTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/start',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_tensorboard(
        self,
        tensorboard_id: str,
        request: main_models.StartTensorboardRequest,
    ) -> main_models.StartTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def start_tensorboard_async(
        self,
        tensorboard_id: str,
        request: main_models.StartTensorboardRequest,
    ) -> main_models.StartTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def stop_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        job_id: str,
    ) -> main_models.StopJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    async def stop_job_async(
        self,
        job_id: str,
    ) -> main_models.StopJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_job_with_options_async(job_id, headers, runtime)

    def stop_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: main_models.StopTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.StopTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}/stop',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_tensorboard(
        self,
        tensorboard_id: str,
        request: main_models.StopTensorboardRequest,
    ) -> main_models.StopTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def stop_tensorboard_async(
        self,
        tensorboard_id: str,
        request: main_models.StopTensorboardRequest,
    ) -> main_models.StopTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def update_job_with_options(
        self,
        job_id: str,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        job_id: str,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        job_id: str,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_job_with_options(job_id, request, headers, runtime)

    async def update_job_async(
        self,
        job_id: str,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(job_id, request, headers, runtime)

    def update_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: main_models.UpdateTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: main_models.UpdateTensorboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTensorboardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not DaraCore.is_null(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTensorboard',
            version = '2020-12-03',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tensorboards/{DaraURL.percent_encode(tensorboard_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tensorboard(
        self,
        tensorboard_id: str,
        request: main_models.UpdateTensorboardRequest,
    ) -> main_models.UpdateTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def update_tensorboard_async(
        self,
        tensorboard_id: str,
        request: main_models.UpdateTensorboardRequest,
    ) -> main_models.UpdateTensorboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

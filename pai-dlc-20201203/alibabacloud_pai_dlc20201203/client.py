# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pai_dlc20201203 import models as pai_dlc_20201203_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_code_source(
        self,
        request: pai_dlc_20201203_models.CreateCodeSourceRequest,
    ) -> pai_dlc_20201203_models.CreateCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_code_source_with_options(request, headers, runtime)

    async def create_code_source_async(
        self,
        request: pai_dlc_20201203_models.CreateCodeSourceRequest,
    ) -> pai_dlc_20201203_models.CreateCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_code_source_with_options_async(request, headers, runtime)

    def create_code_source_with_options(
        self,
        request: pai_dlc_20201203_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateCodeSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_code_source_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateCodeSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_repo_access_token):
            body['CodeRepoAccessToken'] = request.code_repo_access_token
        if not UtilClient.is_unset(request.code_repo_user_name):
            body['CodeRepoUserName'] = request.code_repo_user_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: pai_dlc_20201203_models.CreateDataSourceRequest,
    ) -> pai_dlc_20201203_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_source_with_options(request, headers, runtime)

    async def create_data_source_async(
        self,
        request: pai_dlc_20201203_models.CreateDataSourceRequest,
    ) -> pai_dlc_20201203_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_source_with_options_async(request, headers, runtime)

    def create_data_source_with_options(
        self,
        request: pai_dlc_20201203_models.CreateDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.debugger_config_content):
            body['DebuggerConfigContent'] = request.debugger_config_content
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        if not UtilClient.is_unset(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.settings):
            body['Settings'] = request.settings
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.debugger_config_content):
            body['DebuggerConfigContent'] = request.debugger_config_content
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.elastic_spec):
            body['ElasticSpec'] = request.elastic_spec
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        if not UtilClient.is_unset(request.job_max_running_time_minutes):
            body['JobMaxRunningTimeMinutes'] = request.job_max_running_time_minutes
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.settings):
            body['Settings'] = request.settings
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tensorboard(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tensorboard_with_options(request, headers, runtime)

    async def create_tensorboard_async(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tensorboard_with_options_async(request, headers, runtime)

    def create_tensorboard_with_options(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_running_time_minutes):
            body['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tensorboard_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_running_time_minutes):
            body['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_code_source(
        self,
        code_source_id: str,
    ) -> pai_dlc_20201203_models.DeleteCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_code_source_with_options(code_source_id, headers, runtime)

    async def delete_code_source_async(
        self,
        code_source_id: str,
    ) -> pai_dlc_20201203_models.DeleteCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_code_source_with_options_async(code_source_id, headers, runtime)

    def delete_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteCodeSourceResponse:
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{code_source_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteCodeSourceResponse:
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{code_source_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        data_source_id: str,
    ) -> pai_dlc_20201203_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_source_with_options(data_source_id, headers, runtime)

    async def delete_data_source_async(
        self,
        data_source_id: str,
    ) -> pai_dlc_20201203_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_source_with_options_async(data_source_id, headers, runtime)

    def delete_data_source_with_options(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteDataSourceResponse:
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources/{data_source_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteDataSourceResponse:
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources/{data_source_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(job_id, headers, runtime)

    async def delete_job_async(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(job_id, headers, runtime)

    def delete_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: pai_dlc_20201203_models.DeleteJobsRequest,
    ) -> pai_dlc_20201203_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_jobs_with_options(request, headers, runtime)

    async def delete_jobs_async(
        self,
        request: pai_dlc_20201203_models.DeleteJobsRequest,
    ) -> pai_dlc_20201203_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_jobs_with_options_async(request, headers, runtime)

    def delete_jobs_with_options(
        self,
        request: pai_dlc_20201203_models.DeleteJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/jobs/delete',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        request: pai_dlc_20201203_models.DeleteJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/jobs/delete',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def delete_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def delete_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_code_source(
        self,
        code_source_id: str,
    ) -> pai_dlc_20201203_models.GetCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_code_source_with_options(code_source_id, headers, runtime)

    async def get_code_source_async(
        self,
        code_source_id: str,
    ) -> pai_dlc_20201203_models.GetCodeSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_code_source_with_options_async(code_source_id, headers, runtime)

    def get_code_source_with_options(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetCodeSourceResponse:
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{code_source_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetCodeSourceResponse:
        code_source_id = OpenApiUtilClient.get_encode_param(code_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCodeSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources/{code_source_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source(
        self,
        data_source_id: str,
    ) -> pai_dlc_20201203_models.GetDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_with_options(data_source_id, headers, runtime)

    async def get_data_source_async(
        self,
        data_source_id: str,
    ) -> pai_dlc_20201203_models.GetDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_source_with_options_async(data_source_id, headers, runtime)

    def get_data_source_with_options(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetDataSourceResponse:
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources/{data_source_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_with_options_async(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetDataSourceResponse:
        data_source_id = OpenApiUtilClient.get_encode_param(data_source_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources/{data_source_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, headers, runtime)

    async def get_job_async(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(job_id, headers, runtime)

    def get_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_events(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_events_with_options(job_id, request, headers, runtime)

    async def get_job_events_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_events_with_options_async(job_id, request, headers, runtime)

    def get_job_events_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_events_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_metrics(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_metrics_with_options(job_id, request, headers, runtime)

    async def get_job_metrics_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_metrics_with_options_async(job_id, request, headers, runtime)

    def get_job_metrics_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobMetrics',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_metrics_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobMetrics',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pod_events(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_events_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_events_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pod_events_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_pod_events_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/pods/{pod_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pod_events_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodEvents',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/pods/{pod_id}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pod_logs(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_logs_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_logs_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pod_logs_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_pod_logs_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodLogs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/pods/{pod_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pod_logs_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pod_id = OpenApiUtilClient.get_encode_param(pod_id)
        query = {}
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPodLogs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/pods/{pod_id}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def get_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def get_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_code_sources(
        self,
        request: pai_dlc_20201203_models.ListCodeSourcesRequest,
    ) -> pai_dlc_20201203_models.ListCodeSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_code_sources_with_options(request, headers, runtime)

    async def list_code_sources_async(
        self,
        request: pai_dlc_20201203_models.ListCodeSourcesRequest,
    ) -> pai_dlc_20201203_models.ListCodeSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_code_sources_with_options_async(request, headers, runtime)

    def list_code_sources_with_options(
        self,
        request: pai_dlc_20201203_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListCodeSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_code_sources_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListCodeSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListCodeSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCodeSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/codesources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: pai_dlc_20201203_models.ListDataSourcesRequest,
    ) -> pai_dlc_20201203_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(request, headers, runtime)

    async def list_data_sources_async(
        self,
        request: pai_dlc_20201203_models.ListDataSourcesRequest,
    ) -> pai_dlc_20201203_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(request, headers, runtime)

    def list_data_sources_with_options(
        self,
        request: pai_dlc_20201203_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_specs(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsSpecs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/ecsspecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: pai_dlc_20201203_models.ListImagesRequest,
    ) -> pai_dlc_20201203_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: pai_dlc_20201203_models.ListImagesRequest,
    ) -> pai_dlc_20201203_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: pai_dlc_20201203_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/images',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: pai_dlc_20201203_models.ListJobsRequest,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: pai_dlc_20201203_models.ListJobsRequest,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: pai_dlc_20201203_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_all_workspaces):
            query['FromAllWorkspaces'] = request.from_all_workspaces
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tmp_req: pai_dlc_20201203_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_user_id):
            query['BusinessUserId'] = request.business_user_id
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.from_all_workspaces):
            query['FromAllWorkspaces'] = request.from_all_workspaces
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tensorboards(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tensorboards_with_options(request, headers, runtime)

    async def list_tensorboards_async(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tensorboards_with_options_async(request, headers, runtime)

    def list_tensorboards_with_options(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTensorboards',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListTensorboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tensorboards_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tensorboard_id):
            query['TensorboardId'] = request.tensorboard_id
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTensorboards',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListTensorboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def start_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def start_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StartTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}/start',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StartTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_job(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    async def stop_job_async(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_job_with_options_async(job_id, headers, runtime)

    def stop_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_jobs(
        self,
        request: pai_dlc_20201203_models.StopJobsRequest,
    ) -> pai_dlc_20201203_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_jobs_with_options(request, headers, runtime)

    async def stop_jobs_async(
        self,
        request: pai_dlc_20201203_models.StopJobsRequest,
    ) -> pai_dlc_20201203_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_jobs_with_options_async(request, headers, runtime)

    def stop_jobs_with_options(
        self,
        request: pai_dlc_20201203_models.StopJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/jobs/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        request: pai_dlc_20201203_models.StopJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_ids):
            body['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/batch/jobs/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def stop_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def stop_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}/stop',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(job_id, request, headers, runtime)

    async def update_job_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(job_id, request, headers, runtime)

    def update_job_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        body = {}
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        body = {}
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{job_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def update_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def update_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateTensorboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tensorboard_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        UtilClient.validate_model(request)
        tensorboard_id = OpenApiUtilClient.get_encode_param(tensorboard_id)
        query = {}
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTensorboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{tensorboard_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.UpdateTensorboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

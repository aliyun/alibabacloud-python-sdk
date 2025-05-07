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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_job_with_options(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        """
        @summary Creates a job that runs in a cluster. You can configure the data source, code source, startup command, and computing resources of each node on which a job runs.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
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
        if not UtilClient.is_unset(request.success_policy):
            body['SuccessPolicy'] = request.success_policy
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
        """
        @summary Creates a job that runs in a cluster. You can configure the data source, code source, startup command, and computing resources of each node on which a job runs.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.credential_config):
            body['CredentialConfig'] = request.credential_config
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
        if not UtilClient.is_unset(request.success_policy):
            body['SuccessPolicy'] = request.success_policy
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

    def create_job(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        """
        @summary Creates a job that runs in a cluster. You can configure the data source, code source, startup command, and computing resources of each node on which a job runs.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        """
        @summary Creates a job that runs in a cluster. You can configure the data source, code source, startup command, and computing resources of each node on which a job runs.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_tensorboard_with_options(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        """
        @summary Creates a TensorBoard by using a job or specifying a data source configuration.
        
        @param request: CreateTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTensorboardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
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
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.quota_id):
            body['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not UtilClient.is_unset(request.tensorboard_data_sources):
            body['TensorboardDataSources'] = request.tensorboard_data_sources
        if not UtilClient.is_unset(request.tensorboard_spec):
            body['TensorboardSpec'] = request.tensorboard_spec
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
        """
        @summary Creates a TensorBoard by using a job or specifying a data source configuration.
        
        @param request: CreateTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTensorboardResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
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
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.quota_id):
            body['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.summary_path):
            body['SummaryPath'] = request.summary_path
        if not UtilClient.is_unset(request.summary_relative_path):
            body['SummaryRelativePath'] = request.summary_relative_path
        if not UtilClient.is_unset(request.tensorboard_data_sources):
            body['TensorboardDataSources'] = request.tensorboard_data_sources
        if not UtilClient.is_unset(request.tensorboard_spec):
            body['TensorboardSpec'] = request.tensorboard_spec
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

    def create_tensorboard(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        """
        @summary Creates a TensorBoard by using a job or specifying a data source configuration.
        
        @param request: CreateTensorboardRequest
        @return: CreateTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tensorboard_with_options(request, headers, runtime)

    async def create_tensorboard_async(
        self,
        request: pai_dlc_20201203_models.CreateTensorboardRequest,
    ) -> pai_dlc_20201203_models.CreateTensorboardResponse:
        """
        @summary Creates a TensorBoard by using a job or specifying a data source configuration.
        
        @param request: CreateTensorboardRequest
        @return: CreateTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tensorboard_with_options_async(request, headers, runtime)

    def delete_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        """
        @summary Deletes a completed or stopped job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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
        """
        @summary Deletes a completed or stopped job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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

    def delete_job(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        """
        @summary Deletes a completed or stopped job.
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(job_id, headers, runtime)

    async def delete_job_async(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.DeleteJobResponse:
        """
        @summary Deletes a completed or stopped job.
        
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(job_id, headers, runtime)

    def delete_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        """
        @summary Deletes a stopped TensorBoard.
        
        @param request: DeleteTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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
        """
        @summary Deletes a stopped TensorBoard.
        
        @param request: DeleteTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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

    def delete_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        """
        @summary Deletes a stopped TensorBoard.
        
        @param request: DeleteTensorboardRequest
        @return: DeleteTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def delete_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.DeleteTensorboardRequest,
    ) -> pai_dlc_20201203_models.DeleteTensorboardResponse:
        """
        @summary Deletes a stopped TensorBoard.
        
        @param request: DeleteTensorboardRequest
        @return: DeleteTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def get_job_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        """
        @summary Obtains the configuration and runtime information of a job.
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_detail):
            query['NeedDetail'] = request.need_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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
        request: pai_dlc_20201203_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        """
        @summary Obtains the configuration and runtime information of a job.
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_detail):
            query['NeedDetail'] = request.need_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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

    def get_job(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobRequest,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        """
        @summary Obtains the configuration and runtime information of a job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, request, headers, runtime)

    async def get_job_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobRequest,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        """
        @summary Obtains the configuration and runtime information of a job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(job_id, request, headers, runtime)

    def get_job_events_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        """
        @summary Obtains the system events of a job.
        
        @param request: GetJobEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobEventsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/events',
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
        """
        @summary Obtains the system events of a job.
        
        @param request: GetJobEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobEventsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/events',
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

    def get_job_events(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        """
        @summary Obtains the system events of a job.
        
        @param request: GetJobEventsRequest
        @return: GetJobEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_events_with_options(job_id, request, headers, runtime)

    async def get_job_events_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        """
        @summary Obtains the system events of a job.
        
        @param request: GetJobEventsRequest
        @return: GetJobEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_events_with_options_async(job_id, request, headers, runtime)

    def get_job_metrics_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        """
        @summary Obtains the monitoring data of a job, including the CPU, GPU, and memory utilization, network, and disk read/write rate.
        
        @param request: GetJobMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobMetricsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/metrics',
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
        """
        @summary Obtains the monitoring data of a job, including the CPU, GPU, and memory utilization, network, and disk read/write rate.
        
        @param request: GetJobMetricsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobMetricsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/metrics',
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

    def get_job_metrics(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        """
        @summary Obtains the monitoring data of a job, including the CPU, GPU, and memory utilization, network, and disk read/write rate.
        
        @param request: GetJobMetricsRequest
        @return: GetJobMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_metrics_with_options(job_id, request, headers, runtime)

    async def get_job_metrics_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobMetricsRequest,
    ) -> pai_dlc_20201203_models.GetJobMetricsResponse:
        """
        @summary Obtains the monitoring data of a job, including the CPU, GPU, and memory utilization, network, and disk read/write rate.
        
        @param request: GetJobMetricsRequest
        @return: GetJobMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_metrics_with_options_async(job_id, request, headers, runtime)

    def get_job_sanity_check_result_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobSanityCheckResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobSanityCheckResultResponse:
        """
        @summary Obtains specified job sanity check result in a Deep Learning Containers (DLC) job.
        
        @param request: GetJobSanityCheckResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobSanityCheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sanity_check_number):
            query['SanityCheckNumber'] = request.sanity_check_number
        if not UtilClient.is_unset(request.sanity_check_phase):
            query['SanityCheckPhase'] = request.sanity_check_phase
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobSanityCheckResult',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/sanitycheckresult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobSanityCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_sanity_check_result_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobSanityCheckResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobSanityCheckResultResponse:
        """
        @summary Obtains specified job sanity check result in a Deep Learning Containers (DLC) job.
        
        @param request: GetJobSanityCheckResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobSanityCheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sanity_check_number):
            query['SanityCheckNumber'] = request.sanity_check_number
        if not UtilClient.is_unset(request.sanity_check_phase):
            query['SanityCheckPhase'] = request.sanity_check_phase
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobSanityCheckResult',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/sanitycheckresult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobSanityCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_sanity_check_result(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobSanityCheckResultRequest,
    ) -> pai_dlc_20201203_models.GetJobSanityCheckResultResponse:
        """
        @summary Obtains specified job sanity check result in a Deep Learning Containers (DLC) job.
        
        @param request: GetJobSanityCheckResultRequest
        @return: GetJobSanityCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_sanity_check_result_with_options(job_id, request, headers, runtime)

    async def get_job_sanity_check_result_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobSanityCheckResultRequest,
    ) -> pai_dlc_20201203_models.GetJobSanityCheckResultResponse:
        """
        @summary Obtains specified job sanity check result in a Deep Learning Containers (DLC) job.
        
        @param request: GetJobSanityCheckResultRequest
        @return: GetJobSanityCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_sanity_check_result_with_options_async(job_id, request, headers, runtime)

    def get_pod_events_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        """
        @summary Obtains the system events of a specific node in a job to locate and troubleshoot issues.
        
        @param request: GetPodEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPodEventsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/events',
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
        """
        @summary Obtains the system events of a specific node in a job to locate and troubleshoot issues.
        
        @param request: GetPodEventsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPodEventsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/events',
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

    def get_pod_events(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        """
        @summary Obtains the system events of a specific node in a job to locate and troubleshoot issues.
        
        @param request: GetPodEventsRequest
        @return: GetPodEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_events_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_events_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodEventsRequest,
    ) -> pai_dlc_20201203_models.GetPodEventsResponse:
        """
        @summary Obtains the system events of a specific node in a job to locate and troubleshoot issues.
        
        @param request: GetPodEventsRequest
        @return: GetPodEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pod_events_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_pod_logs_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        """
        @summary Obtains or downloads the logs of a node for a task. The logs are from the stdout and stderr of the system and user scripts.
        
        @param request: GetPodLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPodLogsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/logs',
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
        """
        @summary Obtains or downloads the logs of a node for a task. The logs are from the stdout and stderr of the system and user scripts.
        
        @param request: GetPodLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPodLogsResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/logs',
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

    def get_pod_logs(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        """
        @summary Obtains or downloads the logs of a node for a task. The logs are from the stdout and stderr of the system and user scripts.
        
        @param request: GetPodLogsRequest
        @return: GetPodLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pod_logs_with_options(job_id, pod_id, request, headers, runtime)

    async def get_pod_logs_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetPodLogsRequest,
    ) -> pai_dlc_20201203_models.GetPodLogsResponse:
        """
        @summary Obtains or downloads the logs of a node for a task. The logs are from the stdout and stderr of the system and user scripts.
        
        @param request: GetPodLogsRequest
        @return: GetPodLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pod_logs_with_options_async(job_id, pod_id, request, headers, runtime)

    def get_ray_dashboard_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetRayDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetRayDashboardResponse:
        """
        @summary Obtains a Ray Dashboard URL.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: GetRayDashboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRayDashboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_shared):
            query['isShared'] = request.is_shared
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRayDashboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/rayDashboard',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetRayDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ray_dashboard_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetRayDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetRayDashboardResponse:
        """
        @summary Obtains a Ray Dashboard URL.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: GetRayDashboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRayDashboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_shared):
            query['isShared'] = request.is_shared
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRayDashboard',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/rayDashboard',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetRayDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ray_dashboard(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetRayDashboardRequest,
    ) -> pai_dlc_20201203_models.GetRayDashboardResponse:
        """
        @summary Obtains a Ray Dashboard URL.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: GetRayDashboardRequest
        @return: GetRayDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ray_dashboard_with_options(job_id, request, headers, runtime)

    async def get_ray_dashboard_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetRayDashboardRequest,
    ) -> pai_dlc_20201203_models.GetRayDashboardResponse:
        """
        @summary Obtains a Ray Dashboard URL.
        
        @description Before you call this operation, make sure that you understand the billing methods and [pricing](https://help.aliyun.com/document_detail/171758.html) of Deep Learning Containers (DLC) of Platform for AI (PAI).
        
        @param request: GetRayDashboardRequest
        @return: GetRayDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_ray_dashboard_with_options_async(job_id, request, headers, runtime)

    def get_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        """
        @summary Queries the information of a TensorBoard instance.
        
        @param request: GetTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTensorboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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
        """
        @summary Queries the information of a TensorBoard instance.
        
        @param request: GetTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTensorboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jod_id):
            query['JodId'] = request.jod_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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

    def get_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        """
        @summary Queries the information of a TensorBoard instance.
        
        @param request: GetTensorboardRequest
        @return: GetTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def get_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardResponse:
        """
        @summary Queries the information of a TensorBoard instance.
        
        @param request: GetTensorboardRequest
        @return: GetTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def get_tensorboard_shared_url_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardSharedUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTensorboardSharedUrlResponse:
        """
        @summary Obtains the shareable link of a TensorBoard task. The link contains digital tokens. You can use a shareable link to access a TensorBoard task.
        
        @param request: GetTensorboardSharedUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTensorboardSharedUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time_seconds):
            query['ExpireTimeSeconds'] = request.expire_time_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTensorboardSharedUrl',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/sharedurl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardSharedUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tensorboard_shared_url_with_options_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardSharedUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTensorboardSharedUrlResponse:
        """
        @summary Obtains the shareable link of a TensorBoard task. The link contains digital tokens. You can use a shareable link to access a TensorBoard task.
        
        @param request: GetTensorboardSharedUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTensorboardSharedUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time_seconds):
            query['ExpireTimeSeconds'] = request.expire_time_seconds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTensorboardSharedUrl',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/sharedurl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTensorboardSharedUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tensorboard_shared_url(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardSharedUrlRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardSharedUrlResponse:
        """
        @summary Obtains the shareable link of a TensorBoard task. The link contains digital tokens. You can use a shareable link to access a TensorBoard task.
        
        @param request: GetTensorboardSharedUrlRequest
        @return: GetTensorboardSharedUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tensorboard_shared_url_with_options(tensorboard_id, request, headers, runtime)

    async def get_tensorboard_shared_url_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.GetTensorboardSharedUrlRequest,
    ) -> pai_dlc_20201203_models.GetTensorboardSharedUrlResponse:
        """
        @summary Obtains the shareable link of a TensorBoard task. The link contains digital tokens. You can use a shareable link to access a TensorBoard task.
        
        @param request: GetTensorboardSharedUrlRequest
        @return: GetTensorboardSharedUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tensorboard_shared_url_with_options_async(tensorboard_id, request, headers, runtime)

    def get_token_with_options(
        self,
        request: pai_dlc_20201203_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTokenResponse:
        """
        @summary Obtains the sharing token of a DLC job. This token is used to view the information about the shared job.
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: pai_dlc_20201203_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetTokenResponse:
        """
        @summary Obtains the sharing token of a DLC job. This token is used to view the information about the shared job.
        
        @param request: GetTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: pai_dlc_20201203_models.GetTokenRequest,
    ) -> pai_dlc_20201203_models.GetTokenResponse:
        """
        @summary Obtains the sharing token of a DLC job. This token is used to view the information about the shared job.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: pai_dlc_20201203_models.GetTokenRequest,
    ) -> pai_dlc_20201203_models.GetTokenResponse:
        """
        @summary Obtains the sharing token of a DLC job. This token is used to view the information about the shared job.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_web_terminal_with_options(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetWebTerminalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetWebTerminalResponse:
        """
        @summary Provides methods and steps to obtain a HTTP link for accessing a container.
        
        @param request: GetWebTerminalRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebTerminal',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/webterminal',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetWebTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_web_terminal_with_options_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetWebTerminalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetWebTerminalResponse:
        """
        @summary Provides methods and steps to obtain a HTTP link for accessing a container.
        
        @param request: GetWebTerminalRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.pod_uid):
            query['PodUid'] = request.pod_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebTerminal',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/pods/{OpenApiUtilClient.get_encode_param(pod_id)}/webterminal',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetWebTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_web_terminal(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetWebTerminalRequest,
    ) -> pai_dlc_20201203_models.GetWebTerminalResponse:
        """
        @summary Provides methods and steps to obtain a HTTP link for accessing a container.
        
        @param request: GetWebTerminalRequest
        @return: GetWebTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_web_terminal_with_options(job_id, pod_id, request, headers, runtime)

    async def get_web_terminal_async(
        self,
        job_id: str,
        pod_id: str,
        request: pai_dlc_20201203_models.GetWebTerminalRequest,
    ) -> pai_dlc_20201203_models.GetWebTerminalResponse:
        """
        @summary Provides methods and steps to obtain a HTTP link for accessing a container.
        
        @param request: GetWebTerminalRequest
        @return: GetWebTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_web_terminal_with_options_async(job_id, pod_id, request, headers, runtime)

    def list_ecs_specs_with_options(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        """
        @summary Queries the list of supported instance types.
        
        @param request: ListEcsSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
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
        """
        @summary Queries the list of supported instance types.
        
        @param request: ListEcsSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
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

    def list_ecs_specs(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        """
        @summary Queries the list of supported instance types.
        
        @param request: ListEcsSpecsRequest
        @return: ListEcsSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_specs_with_options(request, headers, runtime)

    async def list_ecs_specs_async(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        """
        @summary Queries the list of supported instance types.
        
        @param request: ListEcsSpecsRequest
        @return: ListEcsSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_specs_with_options_async(request, headers, runtime)

    def list_job_sanity_check_results_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.ListJobSanityCheckResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobSanityCheckResultsResponse:
        """
        @summary Obtains the results of all sanity checks for a DLC job.
        
        @param request: ListJobSanityCheckResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobSanityCheckResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobSanityCheckResults',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/sanitycheckresults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobSanityCheckResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_sanity_check_results_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.ListJobSanityCheckResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobSanityCheckResultsResponse:
        """
        @summary Obtains the results of all sanity checks for a DLC job.
        
        @param request: ListJobSanityCheckResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobSanityCheckResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobSanityCheckResults',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/sanitycheckresults',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobSanityCheckResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_sanity_check_results(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.ListJobSanityCheckResultsRequest,
    ) -> pai_dlc_20201203_models.ListJobSanityCheckResultsResponse:
        """
        @summary Obtains the results of all sanity checks for a DLC job.
        
        @param request: ListJobSanityCheckResultsRequest
        @return: ListJobSanityCheckResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_sanity_check_results_with_options(job_id, request, headers, runtime)

    async def list_job_sanity_check_results_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.ListJobSanityCheckResultsRequest,
    ) -> pai_dlc_20201203_models.ListJobSanityCheckResultsResponse:
        """
        @summary Obtains the results of all sanity checks for a DLC job.
        
        @param request: ListJobSanityCheckResultsRequest
        @return: ListJobSanityCheckResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_sanity_check_results_with_options_async(job_id, request, headers, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: pai_dlc_20201203_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        """
        @summary Queries a list of jobs and supports pagination, sorting, and filtering by conditions.
        
        @param tmp_req: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_quota_name):
            query['ResourceQuotaName'] = request.resource_quota_name
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
        if not UtilClient.is_unset(request.user_id_for_filter):
            query['UserIdForFilter'] = request.user_id_for_filter
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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
        """
        @summary Queries a list of jobs and supports pagination, sorting, and filtering by conditions.
        
        @param tmp_req: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_dlc_20201203_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.oversold_info):
            query['OversoldInfo'] = request.oversold_info
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_quota_name):
            query['ResourceQuotaName'] = request.resource_quota_name
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
        if not UtilClient.is_unset(request.user_id_for_filter):
            query['UserIdForFilter'] = request.user_id_for_filter
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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

    def list_jobs(
        self,
        request: pai_dlc_20201203_models.ListJobsRequest,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        """
        @summary Queries a list of jobs and supports pagination, sorting, and filtering by conditions.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: pai_dlc_20201203_models.ListJobsRequest,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        """
        @summary Queries a list of jobs and supports pagination, sorting, and filtering by conditions.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_tensorboards_with_options(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        """
        @summary Queries a list of TensorBoard instances.
        
        @param request: ListTensorboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTensorboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
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
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
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
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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
        """
        @summary Queries a list of TensorBoard instances.
        
        @param request: ListTensorboardsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTensorboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
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
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not UtilClient.is_unset(request.show_own):
            query['ShowOwn'] = request.show_own
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
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
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

    def list_tensorboards(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        """
        @summary Queries a list of TensorBoard instances.
        
        @param request: ListTensorboardsRequest
        @return: ListTensorboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tensorboards_with_options(request, headers, runtime)

    async def list_tensorboards_async(
        self,
        request: pai_dlc_20201203_models.ListTensorboardsRequest,
    ) -> pai_dlc_20201203_models.ListTensorboardsResponse:
        """
        @summary Queries a list of TensorBoard instances.
        
        @param request: ListTensorboardsRequest
        @return: ListTensorboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tensorboards_with_options_async(request, headers, runtime)

    def start_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        """
        @summary Starts a TensorBoard instance.
        
        @param request: StartTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/start',
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
        """
        @summary Starts a TensorBoard instance.
        
        @param request: StartTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/start',
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

    def start_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        """
        @summary Starts a TensorBoard instance.
        
        @param request: StartTensorboardRequest
        @return: StartTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def start_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StartTensorboardRequest,
    ) -> pai_dlc_20201203_models.StartTensorboardResponse:
        """
        @summary Starts a TensorBoard instance.
        
        @param request: StartTensorboardRequest
        @return: StartTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def stop_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        """
        @summary Stops a running job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
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
        """
        @summary Stops a running job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2020-12-03',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
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

    def stop_job(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        """
        @summary Stops a running job.
        
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    async def stop_job_async(
        self,
        job_id: str,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        """
        @summary Stops a running job.
        
        @return: StopJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_job_with_options_async(job_id, headers, runtime)

    def stop_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        """
        @summary Stops a TensorBoard instance.
        
        @param request: StopTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/stop',
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
        """
        @summary Stops a TensorBoard instance.
        
        @param request: StopTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTensorboardResponse
        """
        UtilClient.validate_model(request)
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}/stop',
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

    def stop_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        """
        @summary Stops a TensorBoard instance.
        
        @param request: StopTensorboardRequest
        @return: StopTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def stop_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.StopTensorboardRequest,
    ) -> pai_dlc_20201203_models.StopTensorboardResponse:
        """
        @summary Stops a TensorBoard instance.
        
        @param request: StopTensorboardRequest
        @return: StopTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

    def update_job_with_options(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        """
        @summary Updates the configuration information of a job. For example, you can modify the priority of a job in a queue.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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
        """
        @summary Updates the configuration information of a job. For example, you can modify the priority of a job in a queue.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
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
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
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

    def update_job(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        """
        @summary Updates the configuration information of a job. For example, you can modify the priority of a job in a queue.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(job_id, request, headers, runtime)

    async def update_job_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.UpdateJobRequest,
    ) -> pai_dlc_20201203_models.UpdateJobResponse:
        """
        @summary Updates the configuration information of a job. For example, you can modify the priority of a job in a queue.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(job_id, request, headers, runtime)

    def update_tensorboard_with_options(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        """
        @summary Updates a TensorBoard instance.
        
        @param request: UpdateTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTensorboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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
        """
        @summary Updates a TensorBoard instance.
        
        @param request: UpdateTensorboardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTensorboardResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.max_running_time_minutes):
            query['MaxRunningTimeMinutes'] = request.max_running_time_minutes
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
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
            pathname=f'/api/v1/tensorboards/{OpenApiUtilClient.get_encode_param(tensorboard_id)}',
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

    def update_tensorboard(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        """
        @summary Updates a TensorBoard instance.
        
        @param request: UpdateTensorboardRequest
        @return: UpdateTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tensorboard_with_options(tensorboard_id, request, headers, runtime)

    async def update_tensorboard_async(
        self,
        tensorboard_id: str,
        request: pai_dlc_20201203_models.UpdateTensorboardRequest,
    ) -> pai_dlc_20201203_models.UpdateTensorboardResponse:
        """
        @summary Updates a TensorBoard instance.
        
        @param request: UpdateTensorboardRequest
        @return: UpdateTensorboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_tensorboard_with_options_async(tensorboard_id, request, headers, runtime)

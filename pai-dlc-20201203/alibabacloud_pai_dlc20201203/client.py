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
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            self.do_roarequest('CreateCodeSource', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/codesources', 'json', req, runtime)
        )

    async def create_code_source_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateCodeSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateCodeSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.code_repo):
            body['CodeRepo'] = request.code_repo
        if not UtilClient.is_unset(request.code_branch):
            body['CodeBranch'] = request.code_branch
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateCodeSourceResponse(),
            await self.do_roarequest_async('CreateCodeSource', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/codesources', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            self.do_roarequest('ListDataSources', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListDataSourcesResponse(),
            await self.do_roarequest_async('ListDataSources', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            self.do_roarequest('GetDataSource', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/{data_source_id}', 'json', req, runtime)
        )

    async def get_data_source_with_options_async(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetDataSourceResponse(),
            await self.do_roarequest_async('GetDataSource', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/{data_source_id}', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            self.do_roarequest('GetJob', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}', 'json', req, runtime)
        )

    async def get_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobResponse(),
            await self.do_roarequest_async('GetJob', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            self.do_roarequest('CreateDataSource', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/datasources', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            body['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        if not UtilClient.is_unset(request.mount_path):
            body['MountPath'] = request.mount_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateDataSourceResponse(),
            await self.do_roarequest_async('CreateDataSource', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/datasources', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            self.do_roarequest('GetCodeSource', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/codesources/{code_source_id}', 'json', req, runtime)
        )

    async def get_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetCodeSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetCodeSourceResponse(),
            await self.do_roarequest_async('GetCodeSource', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/codesources/{code_source_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            self.do_roarequest('ListImages', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_provider_type):
            query['ImageProviderType'] = request.image_provider_type
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.framework):
            query['Framework'] = request.framework
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListImagesResponse(),
            await self.do_roarequest_async('ListImages', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    def get_switch(
        self,
        switch_id: str,
    ) -> pai_dlc_20201203_models.GetSwitchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_switch_with_options(switch_id, headers, runtime)

    async def get_switch_async(
        self,
        switch_id: str,
    ) -> pai_dlc_20201203_models.GetSwitchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_switch_with_options_async(switch_id, headers, runtime)

    def get_switch_with_options(
        self,
        switch_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetSwitchResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSwitchResponse(),
            self.do_roarequest('GetSwitch', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/switches/{switch_id}', 'json', req, runtime)
        )

    async def get_switch_with_options_async(
        self,
        switch_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetSwitchResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSwitchResponse(),
            await self.do_roarequest_async('GetSwitch', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/switches/{switch_id}', 'json', req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            self.do_roarequest('GetPodEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/pods/{pod_id}/events', 'json', req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodEventsResponse(),
            await self.do_roarequest_async('GetPodEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/pods/{pod_id}/events', 'json', req, runtime)
        )

    def list_switches(
        self,
        request: pai_dlc_20201203_models.ListSwitchesRequest,
    ) -> pai_dlc_20201203_models.ListSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_switches_with_options(request, headers, runtime)

    async def list_switches_async(
        self,
        request: pai_dlc_20201203_models.ListSwitchesRequest,
    ) -> pai_dlc_20201203_models.ListSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_switches_with_options_async(request, headers, runtime)

    def list_switches_with_options(
        self,
        request: pai_dlc_20201203_models.ListSwitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSwitchesResponse(),
            self.do_roarequest('ListSwitches', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/switches', 'json', req, runtime)
        )

    async def list_switches_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListSwitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSwitchesResponse(),
            await self.do_roarequest_async('ListSwitches', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/switches', 'json', req, runtime)
        )

    def list_security_groups(
        self,
        request: pai_dlc_20201203_models.ListSecurityGroupsRequest,
    ) -> pai_dlc_20201203_models.ListSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_security_groups_with_options(request, headers, runtime)

    async def list_security_groups_async(
        self,
        request: pai_dlc_20201203_models.ListSecurityGroupsRequest,
    ) -> pai_dlc_20201203_models.ListSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_security_groups_with_options_async(request, headers, runtime)

    def list_security_groups_with_options(
        self,
        request: pai_dlc_20201203_models.ListSecurityGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSecurityGroupsResponse(),
            self.do_roarequest('ListSecurityGroups', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/securitygroups', 'json', req, runtime)
        )

    async def list_security_groups_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListSecurityGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListSecurityGroupsResponse(),
            await self.do_roarequest_async('ListSecurityGroups', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/securitygroups', 'json', req, runtime)
        )

    def get_security_group(
        self,
        security_group_id: str,
    ) -> pai_dlc_20201203_models.GetSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_security_group_with_options(security_group_id, headers, runtime)

    async def get_security_group_async(
        self,
        security_group_id: str,
    ) -> pai_dlc_20201203_models.GetSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_security_group_with_options_async(security_group_id, headers, runtime)

    def get_security_group_with_options(
        self,
        security_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetSecurityGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSecurityGroupResponse(),
            self.do_roarequest('GetSecurityGroup', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/securitygroups/{security_group_id}', 'json', req, runtime)
        )

    async def get_security_group_with_options_async(
        self,
        security_group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetSecurityGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetSecurityGroupResponse(),
            await self.do_roarequest_async('GetSecurityGroup', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/securitygroups/{security_group_id}', 'json', req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            self.do_roarequest('GetPodLogs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/pods/{pod_id}/logs', 'json', req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_lines):
            query['MaxLines'] = request.max_lines
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.download_to_file):
            query['DownloadToFile'] = request.download_to_file
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetPodLogsResponse(),
            await self.do_roarequest_async('GetPodLogs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/pods/{pod_id}/logs', 'json', req, runtime)
        )

    def get_user_authorization(
        self,
        user_id: str,
    ) -> pai_dlc_20201203_models.GetUserAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_authorization_with_options(user_id, headers, runtime)

    async def get_user_authorization_async(
        self,
        user_id: str,
    ) -> pai_dlc_20201203_models.GetUserAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_authorization_with_options_async(user_id, headers, runtime)

    def get_user_authorization_with_options(
        self,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetUserAuthorizationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetUserAuthorizationResponse(),
            self.do_roarequest('GetUserAuthorization', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/users/{user_id}/authorization', 'json', req, runtime)
        )

    async def get_user_authorization_with_options_async(
        self,
        user_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetUserAuthorizationResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetUserAuthorizationResponse(),
            await self.do_roarequest_async('GetUserAuthorization', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/users/{user_id}/authorization', 'json', req, runtime)
        )

    def list_vpcs(
        self,
        request: pai_dlc_20201203_models.ListVpcsRequest,
    ) -> pai_dlc_20201203_models.ListVpcsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpcs_with_options(request, headers, runtime)

    async def list_vpcs_async(
        self,
        request: pai_dlc_20201203_models.ListVpcsRequest,
    ) -> pai_dlc_20201203_models.ListVpcsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_vpcs_with_options_async(request, headers, runtime)

    def list_vpcs_with_options(
        self,
        request: pai_dlc_20201203_models.ListVpcsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListVpcsResponse:
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListVpcsResponse(),
            self.do_roarequest('ListVpcs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/vpcs', 'json', req, runtime)
        )

    async def list_vpcs_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListVpcsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListVpcsResponse:
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
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListVpcsResponse(),
            await self.do_roarequest_async('ListVpcs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/vpcs', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            self.do_roarequest('StopJob', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs/{job_id}/stop', 'json', req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.StopJobResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.StopJobResponse(),
            await self.do_roarequest_async('StopJob', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs/{job_id}/stop', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            self.do_roarequest('CreateJob', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: pai_dlc_20201203_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.CreateJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.job_specs):
            body['JobSpecs'] = request.job_specs
        if not UtilClient.is_unset(request.user_command):
            body['UserCommand'] = request.user_command
        if not UtilClient.is_unset(request.data_sources):
            body['DataSources'] = request.data_sources
        if not UtilClient.is_unset(request.code_source):
            body['CodeSource'] = request.code_source
        if not UtilClient.is_unset(request.user_vpc):
            body['UserVpc'] = request.user_vpc
        if not UtilClient.is_unset(request.thirdparty_libs):
            body['ThirdpartyLibs'] = request.thirdparty_libs
        if not UtilClient.is_unset(request.thirdparty_lib_dir):
            body['ThirdpartyLibDir'] = request.thirdparty_lib_dir
        if not UtilClient.is_unset(request.envs):
            body['Envs'] = request.envs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.CreateJobResponse(),
            await self.do_roarequest_async('CreateJob', '2020-12-03', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            self.do_roarequest('ListCodeSources', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/codesources', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListCodeSourcesResponse(),
            await self.do_roarequest_async('ListCodeSources', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/codesources', 'json', req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            self.do_roarequest('GetJobEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/events', 'json', req, runtime)
        )

    async def get_job_events_with_options_async(
        self,
        job_id: str,
        request: pai_dlc_20201203_models.GetJobEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetJobEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_events_num):
            query['MaxEventsNum'] = request.max_events_num
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetJobEventsResponse(),
            await self.do_roarequest_async('GetJobEvents', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}/events', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            self.do_roarequest('DeleteCodeSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', f'/api/v1/codesources/{code_source_id}', 'json', req, runtime)
        )

    async def delete_code_source_with_options_async(
        self,
        code_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteCodeSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteCodeSourceResponse(),
            await self.do_roarequest_async('DeleteCodeSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', f'/api/v1/codesources/{code_source_id}', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            self.do_roarequest('DeleteDataSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', f'/api/v1/datasources/{data_source_id}', 'json', req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        data_source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.DeleteDataSourceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.DeleteDataSourceResponse(),
            await self.do_roarequest_async('DeleteDataSource', '2020-12-03', 'HTTPS', 'DELETE', 'AK', f'/api/v1/datasources/{data_source_id}', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            self.do_roarequest('ListEcsSpecs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/ecsspecs', 'json', req, runtime)
        )

    async def list_ecs_specs_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListEcsSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListEcsSpecsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListEcsSpecsResponse(),
            await self.do_roarequest_async('ListEcsSpecs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/ecsspecs', 'json', req, runtime)
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
        request: pai_dlc_20201203_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            self.do_roarequest('ListJobs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: pai_dlc_20201203_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.ListJobsResponse(),
            await self.do_roarequest_async('ListJobs', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    def get_vpc(
        self,
        vpc_id: str,
    ) -> pai_dlc_20201203_models.GetVpcResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vpc_with_options(vpc_id, headers, runtime)

    async def get_vpc_async(
        self,
        vpc_id: str,
    ) -> pai_dlc_20201203_models.GetVpcResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vpc_with_options_async(vpc_id, headers, runtime)

    def get_vpc_with_options(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetVpcResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetVpcResponse(),
            self.do_roarequest('GetVpc', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/vpcs/{vpc_id}', 'json', req, runtime)
        )

    async def get_vpc_with_options_async(
        self,
        vpc_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_dlc_20201203_models.GetVpcResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_dlc_20201203_models.GetVpcResponse(),
            await self.do_roarequest_async('GetVpc', '2020-12-03', 'HTTPS', 'GET', 'AK', f'/api/v1/vpcs/{vpc_id}', 'json', req, runtime)
        )

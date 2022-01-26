# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vcs20190430 import models as vcs_20190430_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('vcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_compute_task_with_options(
        self,
        request: vcs_20190430_models.CreateComputeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.CreateComputeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_code_list):
            query['AlgorithmCodeList'] = request.algorithm_code_list
        if not UtilClient.is_unset(request.device_code_list):
            query['DeviceCodeList'] = request.device_code_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateComputeTask',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.CreateComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_task_with_options_async(
        self,
        request: vcs_20190430_models.CreateComputeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.CreateComputeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_code_list):
            query['AlgorithmCodeList'] = request.algorithm_code_list
        if not UtilClient.is_unset(request.device_code_list):
            query['DeviceCodeList'] = request.device_code_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateComputeTask',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.CreateComputeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_task(
        self,
        request: vcs_20190430_models.CreateComputeTaskRequest,
    ) -> vcs_20190430_models.CreateComputeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_compute_task_with_options(request, runtime)

    async def create_compute_task_async(
        self,
        request: vcs_20190430_models.CreateComputeTaskRequest,
    ) -> vcs_20190430_models.CreateComputeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_compute_task_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: vcs_20190430_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area_code):
            query['AreaCode'] = request.area_code
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.time_zone_code):
            query['TimeZoneCode'] = request.time_zone_code
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: vcs_20190430_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area_code):
            query['AreaCode'] = request.area_code
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.time_zone_code):
            query['TimeZoneCode'] = request.time_zone_code
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: vcs_20190430_models.CreateProjectRequest,
    ) -> vcs_20190430_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: vcs_20190430_models.CreateProjectRequest,
    ) -> vcs_20190430_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def describe_compute_tasks_with_options(
        self,
        request: vcs_20190430_models.DescribeComputeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeComputeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeTasks',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeComputeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compute_tasks_with_options_async(
        self,
        request: vcs_20190430_models.DescribeComputeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeComputeTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComputeTasks',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeComputeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compute_tasks(
        self,
        request: vcs_20190430_models.DescribeComputeTasksRequest,
    ) -> vcs_20190430_models.DescribeComputeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_compute_tasks_with_options(request, runtime)

    async def describe_compute_tasks_async(
        self,
        request: vcs_20190430_models.DescribeComputeTasksRequest,
    ) -> vcs_20190430_models.DescribeComputeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_compute_tasks_with_options_async(request, runtime)

    def describe_devices_with_options(
        self,
        request: vcs_20190430_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_devices_with_options_async(
        self,
        request: vcs_20190430_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_devices(
        self,
        request: vcs_20190430_models.DescribeDevicesRequest,
    ) -> vcs_20190430_models.DescribeDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    async def describe_devices_async(
        self,
        request: vcs_20190430_models.DescribeDevicesRequest,
    ) -> vcs_20190430_models.DescribeDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_devices_with_options_async(request, runtime)

    def describe_projects_with_options(
        self,
        request: vcs_20190430_models.DescribeProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjects',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_projects_with_options_async(
        self,
        request: vcs_20190430_models.DescribeProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.DescribeProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjects',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.DescribeProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_projects(
        self,
        request: vcs_20190430_models.DescribeProjectsRequest,
    ) -> vcs_20190430_models.DescribeProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_projects_with_options(request, runtime)

    async def describe_projects_async(
        self,
        request: vcs_20190430_models.DescribeProjectsRequest,
    ) -> vcs_20190430_models.DescribeProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_projects_with_options_async(request, runtime)

    def get_picture_search_results_with_options(
        self,
        request: vcs_20190430_models.GetPictureSearchResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.GetPictureSearchResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.picture_contents):
            query['PictureContents'] = request.picture_contents
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPictureSearchResults',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.GetPictureSearchResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_picture_search_results_with_options_async(
        self,
        request: vcs_20190430_models.GetPictureSearchResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.GetPictureSearchResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.picture_contents):
            query['PictureContents'] = request.picture_contents
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPictureSearchResults',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.GetPictureSearchResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_picture_search_results(
        self,
        request: vcs_20190430_models.GetPictureSearchResultsRequest,
    ) -> vcs_20190430_models.GetPictureSearchResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_picture_search_results_with_options(request, runtime)

    async def get_picture_search_results_async(
        self,
        request: vcs_20190430_models.GetPictureSearchResultsRequest,
    ) -> vcs_20190430_models.GetPictureSearchResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_picture_search_results_with_options_async(request, runtime)

    def import_devices_with_options(
        self,
        request: vcs_20190430_models.ImportDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.ImportDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDevices',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.ImportDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_devices_with_options_async(
        self,
        request: vcs_20190430_models.ImportDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20190430_models.ImportDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcs_id):
            query['VcsId'] = request.vcs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDevices',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20190430_models.ImportDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_devices(
        self,
        request: vcs_20190430_models.ImportDevicesRequest,
    ) -> vcs_20190430_models.ImportDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_devices_with_options(request, runtime)

    async def import_devices_async(
        self,
        request: vcs_20190430_models.ImportDevicesRequest,
    ) -> vcs_20190430_models.ImportDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_devices_with_options_async(request, runtime)

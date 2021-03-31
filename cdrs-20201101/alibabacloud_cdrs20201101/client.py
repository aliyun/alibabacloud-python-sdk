# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdrs20201101 import models as cdrs20201101_models
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
        self._endpoint = self.get_endpoint('cdrs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cdrs_monitor_with_options(
        self,
        request: cdrs20201101_models.AddCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.AddCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddCdrsMonitorResponse(),
            self.do_rpcrequest('AddCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cdrs_monitor_with_options_async(
        self,
        request: cdrs20201101_models.AddCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.AddCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddCdrsMonitorResponse(),
            await self.do_rpcrequest_async('AddCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cdrs_monitor(
        self,
        request: cdrs20201101_models.AddCdrsMonitorRequest,
    ) -> cdrs20201101_models.AddCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cdrs_monitor_with_options(request, runtime)

    async def add_cdrs_monitor_async(
        self,
        request: cdrs20201101_models.AddCdrsMonitorRequest,
    ) -> cdrs20201101_models.AddCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cdrs_monitor_with_options_async(request, runtime)

    def add_monitor_with_options(
        self,
        request: cdrs20201101_models.AddMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.AddMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddMonitorResponse(),
            self.do_rpcrequest('AddMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_monitor_with_options_async(
        self,
        request: cdrs20201101_models.AddMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.AddMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddMonitorResponse(),
            await self.do_rpcrequest_async('AddMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_monitor(
        self,
        request: cdrs20201101_models.AddMonitorRequest,
    ) -> cdrs20201101_models.AddMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_monitor_with_options(request, runtime)

    async def add_monitor_async(
        self,
        request: cdrs20201101_models.AddMonitorRequest,
    ) -> cdrs20201101_models.AddMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_monitor_with_options_async(request, runtime)

    def bind_device_with_options(
        self,
        request: cdrs20201101_models.BindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.BindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.BindDeviceResponse(),
            self.do_rpcrequest('BindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_device_with_options_async(
        self,
        request: cdrs20201101_models.BindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.BindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.BindDeviceResponse(),
            await self.do_rpcrequest_async('BindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_device(
        self,
        request: cdrs20201101_models.BindDeviceRequest,
    ) -> cdrs20201101_models.BindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_device_with_options(request, runtime)

    async def bind_device_async(
        self,
        request: cdrs20201101_models.BindDeviceRequest,
    ) -> cdrs20201101_models.BindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_device_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: cdrs20201101_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: cdrs20201101_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.CreateProjectResponse(),
            await self.do_rpcrequest_async('CreateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: cdrs20201101_models.CreateProjectRequest,
    ) -> cdrs20201101_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: cdrs20201101_models.CreateProjectRequest,
    ) -> cdrs20201101_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def detect_trajectory_regular_pattern_with_options(
        self,
        request: cdrs20201101_models.DetectTrajectoryRegularPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.DetectTrajectoryRegularPatternResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.DetectTrajectoryRegularPatternResponse(),
            self.do_rpcrequest('DetectTrajectoryRegularPattern', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_trajectory_regular_pattern_with_options_async(
        self,
        request: cdrs20201101_models.DetectTrajectoryRegularPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.DetectTrajectoryRegularPatternResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.DetectTrajectoryRegularPatternResponse(),
            await self.do_rpcrequest_async('DetectTrajectoryRegularPattern', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_trajectory_regular_pattern(
        self,
        request: cdrs20201101_models.DetectTrajectoryRegularPatternRequest,
    ) -> cdrs20201101_models.DetectTrajectoryRegularPatternResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_trajectory_regular_pattern_with_options(request, runtime)

    async def detect_trajectory_regular_pattern_async(
        self,
        request: cdrs20201101_models.DetectTrajectoryRegularPatternRequest,
    ) -> cdrs20201101_models.DetectTrajectoryRegularPatternResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_trajectory_regular_pattern_with_options_async(request, runtime)

    def get_cdrs_monitor_list_with_options(
        self,
        request: cdrs20201101_models.GetCdrsMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetCdrsMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorListResponse(),
            self.do_rpcrequest('GetCdrsMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cdrs_monitor_list_with_options_async(
        self,
        request: cdrs20201101_models.GetCdrsMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetCdrsMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorListResponse(),
            await self.do_rpcrequest_async('GetCdrsMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdrs_monitor_list(
        self,
        request: cdrs20201101_models.GetCdrsMonitorListRequest,
    ) -> cdrs20201101_models.GetCdrsMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cdrs_monitor_list_with_options(request, runtime)

    async def get_cdrs_monitor_list_async(
        self,
        request: cdrs20201101_models.GetCdrsMonitorListRequest,
    ) -> cdrs20201101_models.GetCdrsMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cdrs_monitor_list_with_options_async(request, runtime)

    def get_cdrs_monitor_result_with_options(
        self,
        request: cdrs20201101_models.GetCdrsMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetCdrsMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorResultResponse(),
            self.do_rpcrequest('GetCdrsMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cdrs_monitor_result_with_options_async(
        self,
        request: cdrs20201101_models.GetCdrsMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetCdrsMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorResultResponse(),
            await self.do_rpcrequest_async('GetCdrsMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdrs_monitor_result(
        self,
        request: cdrs20201101_models.GetCdrsMonitorResultRequest,
    ) -> cdrs20201101_models.GetCdrsMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cdrs_monitor_result_with_options(request, runtime)

    async def get_cdrs_monitor_result_async(
        self,
        request: cdrs20201101_models.GetCdrsMonitorResultRequest,
    ) -> cdrs20201101_models.GetCdrsMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cdrs_monitor_result_with_options_async(request, runtime)

    def get_monitor_list_with_options(
        self,
        request: cdrs20201101_models.GetMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorListResponse(),
            self.do_rpcrequest('GetMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_monitor_list_with_options_async(
        self,
        request: cdrs20201101_models.GetMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorListResponse(),
            await self.do_rpcrequest_async('GetMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_list(
        self,
        request: cdrs20201101_models.GetMonitorListRequest,
    ) -> cdrs20201101_models.GetMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_list_with_options(request, runtime)

    async def get_monitor_list_async(
        self,
        request: cdrs20201101_models.GetMonitorListRequest,
    ) -> cdrs20201101_models.GetMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monitor_list_with_options_async(request, runtime)

    def get_monitor_result_with_options(
        self,
        request: cdrs20201101_models.GetMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorResultResponse(),
            self.do_rpcrequest('GetMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_monitor_result_with_options_async(
        self,
        request: cdrs20201101_models.GetMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.GetMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorResultResponse(),
            await self.do_rpcrequest_async('GetMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_result(
        self,
        request: cdrs20201101_models.GetMonitorResultRequest,
    ) -> cdrs20201101_models.GetMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_result_with_options(request, runtime)

    async def get_monitor_result_async(
        self,
        request: cdrs20201101_models.GetMonitorResultRequest,
    ) -> cdrs20201101_models.GetMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monitor_result_with_options_async(request, runtime)

    def intersect_trajectory_with_options(
        self,
        request: cdrs20201101_models.IntersectTrajectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.IntersectTrajectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.IntersectTrajectoryResponse(),
            self.do_rpcrequest('IntersectTrajectory', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def intersect_trajectory_with_options_async(
        self,
        request: cdrs20201101_models.IntersectTrajectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.IntersectTrajectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.IntersectTrajectoryResponse(),
            await self.do_rpcrequest_async('IntersectTrajectory', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def intersect_trajectory(
        self,
        request: cdrs20201101_models.IntersectTrajectoryRequest,
    ) -> cdrs20201101_models.IntersectTrajectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.intersect_trajectory_with_options(request, runtime)

    async def intersect_trajectory_async(
        self,
        request: cdrs20201101_models.IntersectTrajectoryRequest,
    ) -> cdrs20201101_models.IntersectTrajectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.intersect_trajectory_with_options_async(request, runtime)

    def list_area_hot_spot_metrics_with_options(
        self,
        request: cdrs20201101_models.ListAreaHotSpotMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListAreaHotSpotMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListAreaHotSpotMetricsResponse(),
            self.do_rpcrequest('ListAreaHotSpotMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_area_hot_spot_metrics_with_options_async(
        self,
        request: cdrs20201101_models.ListAreaHotSpotMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListAreaHotSpotMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListAreaHotSpotMetricsResponse(),
            await self.do_rpcrequest_async('ListAreaHotSpotMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_area_hot_spot_metrics(
        self,
        request: cdrs20201101_models.ListAreaHotSpotMetricsRequest,
    ) -> cdrs20201101_models.ListAreaHotSpotMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_area_hot_spot_metrics_with_options(request, runtime)

    async def list_area_hot_spot_metrics_async(
        self,
        request: cdrs20201101_models.ListAreaHotSpotMetricsRequest,
    ) -> cdrs20201101_models.ListAreaHotSpotMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_area_hot_spot_metrics_with_options_async(request, runtime)

    def list_city_map_aois_with_options(
        self,
        request: cdrs20201101_models.ListCityMapAoisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapAoisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapAoisResponse(),
            self.do_rpcrequest('ListCityMapAois', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_aois_with_options_async(
        self,
        request: cdrs20201101_models.ListCityMapAoisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapAoisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapAoisResponse(),
            await self.do_rpcrequest_async('ListCityMapAois', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_aois(
        self,
        request: cdrs20201101_models.ListCityMapAoisRequest,
    ) -> cdrs20201101_models.ListCityMapAoisResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_aois_with_options(request, runtime)

    async def list_city_map_aois_async(
        self,
        request: cdrs20201101_models.ListCityMapAoisRequest,
    ) -> cdrs20201101_models.ListCityMapAoisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_aois_with_options_async(request, runtime)

    def list_city_map_camera_results_with_options(
        self,
        tmp_req: cdrs20201101_models.ListCityMapCameraResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapCameraResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapCameraResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_id_list):
            request.data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id_list, 'DataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraResultsResponse(),
            self.do_rpcrequest('ListCityMapCameraResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_camera_results_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListCityMapCameraResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapCameraResultsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapCameraResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_id_list):
            request.data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id_list, 'DataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraResultsResponse(),
            await self.do_rpcrequest_async('ListCityMapCameraResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_camera_results(
        self,
        request: cdrs20201101_models.ListCityMapCameraResultsRequest,
    ) -> cdrs20201101_models.ListCityMapCameraResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_camera_results_with_options(request, runtime)

    async def list_city_map_camera_results_async(
        self,
        request: cdrs20201101_models.ListCityMapCameraResultsRequest,
    ) -> cdrs20201101_models.ListCityMapCameraResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_camera_results_with_options_async(request, runtime)

    def list_city_map_camera_statistics_with_options(
        self,
        request: cdrs20201101_models.ListCityMapCameraStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapCameraStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraStatisticsResponse(),
            self.do_rpcrequest('ListCityMapCameraStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_camera_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListCityMapCameraStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapCameraStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraStatisticsResponse(),
            await self.do_rpcrequest_async('ListCityMapCameraStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_camera_statistics(
        self,
        request: cdrs20201101_models.ListCityMapCameraStatisticsRequest,
    ) -> cdrs20201101_models.ListCityMapCameraStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_camera_statistics_with_options(request, runtime)

    async def list_city_map_camera_statistics_async(
        self,
        request: cdrs20201101_models.ListCityMapCameraStatisticsRequest,
    ) -> cdrs20201101_models.ListCityMapCameraStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_camera_statistics_with_options_async(request, runtime)

    def list_city_map_image_details_with_options(
        self,
        request: cdrs20201101_models.ListCityMapImageDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapImageDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapImageDetailsResponse(),
            self.do_rpcrequest('ListCityMapImageDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_image_details_with_options_async(
        self,
        request: cdrs20201101_models.ListCityMapImageDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapImageDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapImageDetailsResponse(),
            await self.do_rpcrequest_async('ListCityMapImageDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_image_details(
        self,
        request: cdrs20201101_models.ListCityMapImageDetailsRequest,
    ) -> cdrs20201101_models.ListCityMapImageDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_image_details_with_options(request, runtime)

    async def list_city_map_image_details_async(
        self,
        request: cdrs20201101_models.ListCityMapImageDetailsRequest,
    ) -> cdrs20201101_models.ListCityMapImageDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_image_details_with_options_async(request, runtime)

    def list_city_map_person_flow_with_options(
        self,
        tmp_req: cdrs20201101_models.ListCityMapPersonFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapPersonFlowResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapPersonFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.origin_data_source_id_list):
            request.origin_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.origin_data_source_id_list, 'OriginDataSourceIdList', 'json')
        if not UtilClient.is_unset(tmp_req.target_data_source_id_list):
            request.target_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_data_source_id_list, 'TargetDataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapPersonFlowResponse(),
            self.do_rpcrequest('ListCityMapPersonFlow', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_person_flow_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListCityMapPersonFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapPersonFlowResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapPersonFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.origin_data_source_id_list):
            request.origin_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.origin_data_source_id_list, 'OriginDataSourceIdList', 'json')
        if not UtilClient.is_unset(tmp_req.target_data_source_id_list):
            request.target_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_data_source_id_list, 'TargetDataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapPersonFlowResponse(),
            await self.do_rpcrequest_async('ListCityMapPersonFlow', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_person_flow(
        self,
        request: cdrs20201101_models.ListCityMapPersonFlowRequest,
    ) -> cdrs20201101_models.ListCityMapPersonFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_person_flow_with_options(request, runtime)

    async def list_city_map_person_flow_async(
        self,
        request: cdrs20201101_models.ListCityMapPersonFlowRequest,
    ) -> cdrs20201101_models.ListCityMapPersonFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_person_flow_with_options_async(request, runtime)

    def list_city_map_range_statistic_with_options(
        self,
        request: cdrs20201101_models.ListCityMapRangeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapRangeStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapRangeStatisticResponse(),
            self.do_rpcrequest('ListCityMapRangeStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_city_map_range_statistic_with_options_async(
        self,
        request: cdrs20201101_models.ListCityMapRangeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCityMapRangeStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapRangeStatisticResponse(),
            await self.do_rpcrequest_async('ListCityMapRangeStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_range_statistic(
        self,
        request: cdrs20201101_models.ListCityMapRangeStatisticRequest,
    ) -> cdrs20201101_models.ListCityMapRangeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_range_statistic_with_options(request, runtime)

    async def list_city_map_range_statistic_async(
        self,
        request: cdrs20201101_models.ListCityMapRangeStatisticRequest,
    ) -> cdrs20201101_models.ListCityMapRangeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_city_map_range_statistic_with_options_async(request, runtime)

    def list_corp_metrics_with_options(
        self,
        tmp_req: cdrs20201101_models.ListCorpMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_list):
            request.user_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_list, 'UserGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_group_list):
            request.device_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_group_list, 'DeviceGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_id_list):
            request.device_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_id_list, 'DeviceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpMetricsResponse(),
            self.do_rpcrequest('ListCorpMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_metrics_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListCorpMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_list):
            request.user_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_list, 'UserGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_group_list):
            request.device_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_group_list, 'DeviceGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_id_list):
            request.device_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_id_list, 'DeviceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpMetricsResponse(),
            await self.do_rpcrequest_async('ListCorpMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_metrics(
        self,
        request: cdrs20201101_models.ListCorpMetricsRequest,
    ) -> cdrs20201101_models.ListCorpMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_with_options(request, runtime)

    async def list_corp_metrics_async(
        self,
        request: cdrs20201101_models.ListCorpMetricsRequest,
    ) -> cdrs20201101_models.ListCorpMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_metrics_with_options_async(request, runtime)

    def list_corp_metrics_statistic_with_options(
        self,
        tmp_req: cdrs20201101_models.ListCorpMetricsStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpMetricsStatisticResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpMetricsStatisticShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_group_list):
            request.user_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_list, 'UserGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_group_list):
            request.device_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_group_list, 'DeviceGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_id_list):
            request.device_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_id_list, 'DeviceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpMetricsStatisticResponse(),
            self.do_rpcrequest('ListCorpMetricsStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_metrics_statistic_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListCorpMetricsStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpMetricsStatisticResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpMetricsStatisticShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_group_list):
            request.user_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_list, 'UserGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_group_list):
            request.device_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_group_list, 'DeviceGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_id_list):
            request.device_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_id_list, 'DeviceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpMetricsStatisticResponse(),
            await self.do_rpcrequest_async('ListCorpMetricsStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_metrics_statistic(
        self,
        request: cdrs20201101_models.ListCorpMetricsStatisticRequest,
    ) -> cdrs20201101_models.ListCorpMetricsStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_statistic_with_options(request, runtime)

    async def list_corp_metrics_statistic_async(
        self,
        request: cdrs20201101_models.ListCorpMetricsStatisticRequest,
    ) -> cdrs20201101_models.ListCorpMetricsStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_metrics_statistic_with_options_async(request, runtime)

    def list_corp_track_detail_with_options(
        self,
        tmp_req: cdrs20201101_models.ListCorpTrackDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpTrackDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpTrackDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_id):
            request.data_source_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id, 'DataSourceId', 'json')
        if not UtilClient.is_unset(tmp_req.person_id):
            request.person_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id, 'PersonId', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpTrackDetailResponse(),
            self.do_rpcrequest('ListCorpTrackDetail', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_track_detail_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListCorpTrackDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListCorpTrackDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpTrackDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_id):
            request.data_source_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id, 'DataSourceId', 'json')
        if not UtilClient.is_unset(tmp_req.person_id):
            request.person_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id, 'PersonId', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpTrackDetailResponse(),
            await self.do_rpcrequest_async('ListCorpTrackDetail', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_track_detail(
        self,
        request: cdrs20201101_models.ListCorpTrackDetailRequest,
    ) -> cdrs20201101_models.ListCorpTrackDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_track_detail_with_options(request, runtime)

    async def list_corp_track_detail_async(
        self,
        request: cdrs20201101_models.ListCorpTrackDetailRequest,
    ) -> cdrs20201101_models.ListCorpTrackDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_track_detail_with_options_async(request, runtime)

    def list_data_statistics_with_options(
        self,
        request: cdrs20201101_models.ListDataStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDataStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsResponse(),
            self.do_rpcrequest('ListDataStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListDataStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDataStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsResponse(),
            await self.do_rpcrequest_async('ListDataStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_statistics(
        self,
        request: cdrs20201101_models.ListDataStatisticsRequest,
    ) -> cdrs20201101_models.ListDataStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_statistics_with_options(request, runtime)

    async def list_data_statistics_async(
        self,
        request: cdrs20201101_models.ListDataStatisticsRequest,
    ) -> cdrs20201101_models.ListDataStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_statistics_with_options_async(request, runtime)

    def list_data_statistics_by_day_with_options(
        self,
        request: cdrs20201101_models.ListDataStatisticsByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDataStatisticsByDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsByDayResponse(),
            self.do_rpcrequest('ListDataStatisticsByDay', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_statistics_by_day_with_options_async(
        self,
        request: cdrs20201101_models.ListDataStatisticsByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDataStatisticsByDayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsByDayResponse(),
            await self.do_rpcrequest_async('ListDataStatisticsByDay', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_statistics_by_day(
        self,
        request: cdrs20201101_models.ListDataStatisticsByDayRequest,
    ) -> cdrs20201101_models.ListDataStatisticsByDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_statistics_by_day_with_options(request, runtime)

    async def list_data_statistics_by_day_async(
        self,
        request: cdrs20201101_models.ListDataStatisticsByDayRequest,
    ) -> cdrs20201101_models.ListDataStatisticsByDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_statistics_by_day_with_options_async(request, runtime)

    def list_device_detail_with_options(
        self,
        request: cdrs20201101_models.ListDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceDetailResponse(),
            self.do_rpcrequest('ListDeviceDetail', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_detail_with_options_async(
        self,
        request: cdrs20201101_models.ListDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceDetailResponse(),
            await self.do_rpcrequest_async('ListDeviceDetail', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_detail(
        self,
        request: cdrs20201101_models.ListDeviceDetailRequest,
    ) -> cdrs20201101_models.ListDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_detail_with_options(request, runtime)

    async def list_device_detail_async(
        self,
        request: cdrs20201101_models.ListDeviceDetailRequest,
    ) -> cdrs20201101_models.ListDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_detail_with_options_async(request, runtime)

    def list_device_gender_statistics_with_options(
        self,
        request: cdrs20201101_models.ListDeviceGenderStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceGenderStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceGenderStatisticsResponse(),
            self.do_rpcrequest('ListDeviceGenderStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_gender_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListDeviceGenderStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceGenderStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceGenderStatisticsResponse(),
            await self.do_rpcrequest_async('ListDeviceGenderStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_gender_statistics(
        self,
        request: cdrs20201101_models.ListDeviceGenderStatisticsRequest,
    ) -> cdrs20201101_models.ListDeviceGenderStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_gender_statistics_with_options(request, runtime)

    async def list_device_gender_statistics_async(
        self,
        request: cdrs20201101_models.ListDeviceGenderStatisticsRequest,
    ) -> cdrs20201101_models.ListDeviceGenderStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_gender_statistics_with_options_async(request, runtime)

    def list_device_person_with_options(
        self,
        request: cdrs20201101_models.ListDevicePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDevicePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonResponse(),
            self.do_rpcrequest('ListDevicePerson', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_person_with_options_async(
        self,
        request: cdrs20201101_models.ListDevicePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDevicePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonResponse(),
            await self.do_rpcrequest_async('ListDevicePerson', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_person(
        self,
        request: cdrs20201101_models.ListDevicePersonRequest,
    ) -> cdrs20201101_models.ListDevicePersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_person_with_options(request, runtime)

    async def list_device_person_async(
        self,
        request: cdrs20201101_models.ListDevicePersonRequest,
    ) -> cdrs20201101_models.ListDevicePersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_person_with_options_async(request, runtime)

    def list_device_person_statistics_with_options(
        self,
        request: cdrs20201101_models.ListDevicePersonStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDevicePersonStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonStatisticsResponse(),
            self.do_rpcrequest('ListDevicePersonStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_person_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListDevicePersonStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDevicePersonStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonStatisticsResponse(),
            await self.do_rpcrequest_async('ListDevicePersonStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_person_statistics(
        self,
        request: cdrs20201101_models.ListDevicePersonStatisticsRequest,
    ) -> cdrs20201101_models.ListDevicePersonStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_person_statistics_with_options(request, runtime)

    async def list_device_person_statistics_async(
        self,
        request: cdrs20201101_models.ListDevicePersonStatisticsRequest,
    ) -> cdrs20201101_models.ListDevicePersonStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_person_statistics_with_options_async(request, runtime)

    def list_device_relation_with_options(
        self,
        request: cdrs20201101_models.ListDeviceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceRelationResponse(),
            self.do_rpcrequest('ListDeviceRelation', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_relation_with_options_async(
        self,
        request: cdrs20201101_models.ListDeviceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListDeviceRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceRelationResponse(),
            await self.do_rpcrequest_async('ListDeviceRelation', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_relation(
        self,
        request: cdrs20201101_models.ListDeviceRelationRequest,
    ) -> cdrs20201101_models.ListDeviceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_relation_with_options(request, runtime)

    async def list_device_relation_async(
        self,
        request: cdrs20201101_models.ListDeviceRelationRequest,
    ) -> cdrs20201101_models.ListDeviceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_relation_with_options_async(request, runtime)

    def list_map_route_details_with_options(
        self,
        tmp_req: cdrs20201101_models.ListMapRouteDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListMapRouteDetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListMapRouteDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.route_list):
            request.route_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.route_list, 'RouteList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListMapRouteDetailsResponse(),
            self.do_rpcrequest('ListMapRouteDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_map_route_details_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListMapRouteDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListMapRouteDetailsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListMapRouteDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.route_list):
            request.route_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.route_list, 'RouteList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListMapRouteDetailsResponse(),
            await self.do_rpcrequest_async('ListMapRouteDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_map_route_details(
        self,
        request: cdrs20201101_models.ListMapRouteDetailsRequest,
    ) -> cdrs20201101_models.ListMapRouteDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_map_route_details_with_options(request, runtime)

    async def list_map_route_details_async(
        self,
        request: cdrs20201101_models.ListMapRouteDetailsRequest,
    ) -> cdrs20201101_models.ListMapRouteDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_map_route_details_with_options_async(request, runtime)

    def list_metrics_with_options(
        self,
        tmp_req: cdrs20201101_models.ListMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_code):
            request.tag_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_code, 'TagCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListMetricsResponse(),
            self.do_rpcrequest('ListMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_metrics_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_code):
            request.tag_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_code, 'TagCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListMetricsResponse(),
            await self.do_rpcrequest_async('ListMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_metrics(
        self,
        request: cdrs20201101_models.ListMetricsRequest,
    ) -> cdrs20201101_models.ListMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_metrics_with_options(request, runtime)

    async def list_metrics_async(
        self,
        request: cdrs20201101_models.ListMetricsRequest,
    ) -> cdrs20201101_models.ListMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_metrics_with_options_async(request, runtime)

    def list_person_details_with_options(
        self,
        request: cdrs20201101_models.ListPersonDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonDetailsResponse(),
            self.do_rpcrequest('ListPersonDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_details_with_options_async(
        self,
        request: cdrs20201101_models.ListPersonDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonDetailsResponse(),
            await self.do_rpcrequest_async('ListPersonDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_details(
        self,
        request: cdrs20201101_models.ListPersonDetailsRequest,
    ) -> cdrs20201101_models.ListPersonDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_details_with_options(request, runtime)

    async def list_person_details_async(
        self,
        request: cdrs20201101_models.ListPersonDetailsRequest,
    ) -> cdrs20201101_models.ListPersonDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_details_with_options_async(request, runtime)

    def list_person_result_with_options(
        self,
        request: cdrs20201101_models.ListPersonResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonResultResponse(),
            self.do_rpcrequest('ListPersonResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_result_with_options_async(
        self,
        request: cdrs20201101_models.ListPersonResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonResultResponse(),
            await self.do_rpcrequest_async('ListPersonResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_result(
        self,
        request: cdrs20201101_models.ListPersonResultRequest,
    ) -> cdrs20201101_models.ListPersonResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_result_with_options(request, runtime)

    async def list_person_result_async(
        self,
        request: cdrs20201101_models.ListPersonResultRequest,
    ) -> cdrs20201101_models.ListPersonResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_result_with_options_async(request, runtime)

    def list_person_tag_with_options(
        self,
        request: cdrs20201101_models.ListPersonTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTagResponse(),
            self.do_rpcrequest('ListPersonTag', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_tag_with_options_async(
        self,
        request: cdrs20201101_models.ListPersonTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTagResponse(),
            await self.do_rpcrequest_async('ListPersonTag', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_tag(
        self,
        request: cdrs20201101_models.ListPersonTagRequest,
    ) -> cdrs20201101_models.ListPersonTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_tag_with_options(request, runtime)

    async def list_person_tag_async(
        self,
        request: cdrs20201101_models.ListPersonTagRequest,
    ) -> cdrs20201101_models.ListPersonTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_tag_with_options_async(request, runtime)

    def list_person_top_with_options(
        self,
        request: cdrs20201101_models.ListPersonTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTopResponse(),
            self.do_rpcrequest('ListPersonTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_top_with_options_async(
        self,
        request: cdrs20201101_models.ListPersonTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTopResponse(),
            await self.do_rpcrequest_async('ListPersonTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_top(
        self,
        request: cdrs20201101_models.ListPersonTopRequest,
    ) -> cdrs20201101_models.ListPersonTopResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_top_with_options(request, runtime)

    async def list_person_top_async(
        self,
        request: cdrs20201101_models.ListPersonTopRequest,
    ) -> cdrs20201101_models.ListPersonTopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_top_with_options_async(request, runtime)

    def list_person_trace_with_options(
        self,
        tmp_req: cdrs20201101_models.ListPersonTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListPersonTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.data_source_id):
            request.data_source_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id, 'DataSourceId', 'json')
        if not UtilClient.is_unset(tmp_req.person_id):
            request.person_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id, 'PersonId', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTraceResponse(),
            self.do_rpcrequest('ListPersonTrace', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_trace_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListPersonTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTraceResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListPersonTraceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id):
            request.corp_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id, 'CorpId', 'json')
        if not UtilClient.is_unset(tmp_req.data_source_id):
            request.data_source_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id, 'DataSourceId', 'json')
        if not UtilClient.is_unset(tmp_req.person_id):
            request.person_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id, 'PersonId', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTraceResponse(),
            await self.do_rpcrequest_async('ListPersonTrace', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_trace(
        self,
        request: cdrs20201101_models.ListPersonTraceRequest,
    ) -> cdrs20201101_models.ListPersonTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_with_options(request, runtime)

    async def list_person_trace_async(
        self,
        request: cdrs20201101_models.ListPersonTraceRequest,
    ) -> cdrs20201101_models.ListPersonTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_trace_with_options_async(request, runtime)

    def list_person_track_with_options(
        self,
        request: cdrs20201101_models.ListPersonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTrackResponse(),
            self.do_rpcrequest('ListPersonTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_track_with_options_async(
        self,
        request: cdrs20201101_models.ListPersonTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListPersonTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTrackResponse(),
            await self.do_rpcrequest_async('ListPersonTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_track(
        self,
        request: cdrs20201101_models.ListPersonTrackRequest,
    ) -> cdrs20201101_models.ListPersonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_track_with_options(request, runtime)

    async def list_person_track_async(
        self,
        request: cdrs20201101_models.ListPersonTrackRequest,
    ) -> cdrs20201101_models.ListPersonTrackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_track_with_options_async(request, runtime)

    def list_range_device_with_options(
        self,
        request: cdrs20201101_models.ListRangeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListRangeDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListRangeDeviceResponse(),
            self.do_rpcrequest('ListRangeDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_range_device_with_options_async(
        self,
        request: cdrs20201101_models.ListRangeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListRangeDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListRangeDeviceResponse(),
            await self.do_rpcrequest_async('ListRangeDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_range_device(
        self,
        request: cdrs20201101_models.ListRangeDeviceRequest,
    ) -> cdrs20201101_models.ListRangeDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_range_device_with_options(request, runtime)

    async def list_range_device_async(
        self,
        request: cdrs20201101_models.ListRangeDeviceRequest,
    ) -> cdrs20201101_models.ListRangeDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_range_device_with_options_async(request, runtime)

    def list_storage_statistics_with_options(
        self,
        request: cdrs20201101_models.ListStorageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListStorageStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStorageStatisticsResponse(),
            self.do_rpcrequest('ListStorageStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_storage_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListStorageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListStorageStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStorageStatisticsResponse(),
            await self.do_rpcrequest_async('ListStorageStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_storage_statistics(
        self,
        request: cdrs20201101_models.ListStorageStatisticsRequest,
    ) -> cdrs20201101_models.ListStorageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_storage_statistics_with_options(request, runtime)

    async def list_storage_statistics_async(
        self,
        request: cdrs20201101_models.ListStorageStatisticsRequest,
    ) -> cdrs20201101_models.ListStorageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_storage_statistics_with_options_async(request, runtime)

    def list_structure_statistics_with_options(
        self,
        request: cdrs20201101_models.ListStructureStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListStructureStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStructureStatisticsResponse(),
            self.do_rpcrequest('ListStructureStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_structure_statistics_with_options_async(
        self,
        request: cdrs20201101_models.ListStructureStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListStructureStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStructureStatisticsResponse(),
            await self.do_rpcrequest_async('ListStructureStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_structure_statistics(
        self,
        request: cdrs20201101_models.ListStructureStatisticsRequest,
    ) -> cdrs20201101_models.ListStructureStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_structure_statistics_with_options(request, runtime)

    async def list_structure_statistics_async(
        self,
        request: cdrs20201101_models.ListStructureStatisticsRequest,
    ) -> cdrs20201101_models.ListStructureStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_structure_statistics_with_options_async(request, runtime)

    def list_tag_metrics_with_options(
        self,
        tmp_req: cdrs20201101_models.ListTagMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListTagMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListTagMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_code):
            request.tag_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_code, 'TagCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListTagMetricsResponse(),
            self.do_rpcrequest('ListTagMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_metrics_with_options_async(
        self,
        tmp_req: cdrs20201101_models.ListTagMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListTagMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListTagMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_code):
            request.tag_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_code, 'TagCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListTagMetricsResponse(),
            await self.do_rpcrequest_async('ListTagMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_metrics(
        self,
        request: cdrs20201101_models.ListTagMetricsRequest,
    ) -> cdrs20201101_models.ListTagMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_metrics_with_options(request, runtime)

    async def list_tag_metrics_async(
        self,
        request: cdrs20201101_models.ListTagMetricsRequest,
    ) -> cdrs20201101_models.ListTagMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_metrics_with_options_async(request, runtime)

    def list_vehicle_details_with_options(
        self,
        request: cdrs20201101_models.ListVehicleDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleDetailsResponse(),
            self.do_rpcrequest('ListVehicleDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_details_with_options_async(
        self,
        request: cdrs20201101_models.ListVehicleDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleDetailsResponse(),
            await self.do_rpcrequest_async('ListVehicleDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_details(
        self,
        request: cdrs20201101_models.ListVehicleDetailsRequest,
    ) -> cdrs20201101_models.ListVehicleDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_details_with_options(request, runtime)

    async def list_vehicle_details_async(
        self,
        request: cdrs20201101_models.ListVehicleDetailsRequest,
    ) -> cdrs20201101_models.ListVehicleDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_details_with_options_async(request, runtime)

    def list_vehicle_results_with_options(
        self,
        request: cdrs20201101_models.ListVehicleResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleResultsResponse(),
            self.do_rpcrequest('ListVehicleResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_results_with_options_async(
        self,
        request: cdrs20201101_models.ListVehicleResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleResultsResponse(),
            await self.do_rpcrequest_async('ListVehicleResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_results(
        self,
        request: cdrs20201101_models.ListVehicleResultsRequest,
    ) -> cdrs20201101_models.ListVehicleResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_results_with_options(request, runtime)

    async def list_vehicle_results_async(
        self,
        request: cdrs20201101_models.ListVehicleResultsRequest,
    ) -> cdrs20201101_models.ListVehicleResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_results_with_options_async(request, runtime)

    def list_vehicle_tag_distribute_with_options(
        self,
        request: cdrs20201101_models.ListVehicleTagDistributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTagDistributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTagDistributeResponse(),
            self.do_rpcrequest('ListVehicleTagDistribute', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_tag_distribute_with_options_async(
        self,
        request: cdrs20201101_models.ListVehicleTagDistributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTagDistributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTagDistributeResponse(),
            await self.do_rpcrequest_async('ListVehicleTagDistribute', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_tag_distribute(
        self,
        request: cdrs20201101_models.ListVehicleTagDistributeRequest,
    ) -> cdrs20201101_models.ListVehicleTagDistributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_tag_distribute_with_options(request, runtime)

    async def list_vehicle_tag_distribute_async(
        self,
        request: cdrs20201101_models.ListVehicleTagDistributeRequest,
    ) -> cdrs20201101_models.ListVehicleTagDistributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_tag_distribute_with_options_async(request, runtime)

    def list_vehicle_top_with_options(
        self,
        request: cdrs20201101_models.ListVehicleTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTopResponse(),
            self.do_rpcrequest('ListVehicleTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_top_with_options_async(
        self,
        request: cdrs20201101_models.ListVehicleTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTopResponse(),
            await self.do_rpcrequest_async('ListVehicleTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_top(
        self,
        request: cdrs20201101_models.ListVehicleTopRequest,
    ) -> cdrs20201101_models.ListVehicleTopResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_top_with_options(request, runtime)

    async def list_vehicle_top_async(
        self,
        request: cdrs20201101_models.ListVehicleTopRequest,
    ) -> cdrs20201101_models.ListVehicleTopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_top_with_options_async(request, runtime)

    def list_vehicle_track_with_options(
        self,
        request: cdrs20201101_models.ListVehicleTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTrackResponse(),
            self.do_rpcrequest('ListVehicleTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vehicle_track_with_options_async(
        self,
        request: cdrs20201101_models.ListVehicleTrackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ListVehicleTrackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTrackResponse(),
            await self.do_rpcrequest_async('ListVehicleTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_track(
        self,
        request: cdrs20201101_models.ListVehicleTrackRequest,
    ) -> cdrs20201101_models.ListVehicleTrackResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_track_with_options(request, runtime)

    async def list_vehicle_track_async(
        self,
        request: cdrs20201101_models.ListVehicleTrackRequest,
    ) -> cdrs20201101_models.ListVehicleTrackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vehicle_track_with_options_async(request, runtime)

    def paginate_device_with_options(
        self,
        request: cdrs20201101_models.PaginateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PaginateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateDeviceResponse(),
            self.do_rpcrequest('PaginateDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def paginate_device_with_options_async(
        self,
        request: cdrs20201101_models.PaginateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PaginateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateDeviceResponse(),
            await self.do_rpcrequest_async('PaginateDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def paginate_device(
        self,
        request: cdrs20201101_models.PaginateDeviceRequest,
    ) -> cdrs20201101_models.PaginateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.paginate_device_with_options(request, runtime)

    async def paginate_device_async(
        self,
        request: cdrs20201101_models.PaginateDeviceRequest,
    ) -> cdrs20201101_models.PaginateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.paginate_device_with_options_async(request, runtime)

    def paginate_project_with_options(
        self,
        request: cdrs20201101_models.PaginateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PaginateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateProjectResponse(),
            self.do_rpcrequest('PaginateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def paginate_project_with_options_async(
        self,
        request: cdrs20201101_models.PaginateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PaginateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateProjectResponse(),
            await self.do_rpcrequest_async('PaginateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def paginate_project(
        self,
        request: cdrs20201101_models.PaginateProjectRequest,
    ) -> cdrs20201101_models.PaginateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.paginate_project_with_options(request, runtime)

    async def paginate_project_async(
        self,
        request: cdrs20201101_models.PaginateProjectRequest,
    ) -> cdrs20201101_models.PaginateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.paginate_project_with_options_async(request, runtime)

    def predict_trajectory_destination_with_options(
        self,
        request: cdrs20201101_models.PredictTrajectoryDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PredictTrajectoryDestinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PredictTrajectoryDestinationResponse(),
            self.do_rpcrequest('PredictTrajectoryDestination', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def predict_trajectory_destination_with_options_async(
        self,
        request: cdrs20201101_models.PredictTrajectoryDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.PredictTrajectoryDestinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PredictTrajectoryDestinationResponse(),
            await self.do_rpcrequest_async('PredictTrajectoryDestination', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def predict_trajectory_destination(
        self,
        request: cdrs20201101_models.PredictTrajectoryDestinationRequest,
    ) -> cdrs20201101_models.PredictTrajectoryDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_trajectory_destination_with_options(request, runtime)

    async def predict_trajectory_destination_async(
        self,
        request: cdrs20201101_models.PredictTrajectoryDestinationRequest,
    ) -> cdrs20201101_models.PredictTrajectoryDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_trajectory_destination_with_options_async(request, runtime)

    def query_trajectory_by_id_with_options(
        self,
        request: cdrs20201101_models.QueryTrajectoryByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.QueryTrajectoryByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.QueryTrajectoryByIdResponse(),
            self.do_rpcrequest('QueryTrajectoryById', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trajectory_by_id_with_options_async(
        self,
        request: cdrs20201101_models.QueryTrajectoryByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.QueryTrajectoryByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.QueryTrajectoryByIdResponse(),
            await self.do_rpcrequest_async('QueryTrajectoryById', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trajectory_by_id(
        self,
        request: cdrs20201101_models.QueryTrajectoryByIdRequest,
    ) -> cdrs20201101_models.QueryTrajectoryByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trajectory_by_id_with_options(request, runtime)

    async def query_trajectory_by_id_async(
        self,
        request: cdrs20201101_models.QueryTrajectoryByIdRequest,
    ) -> cdrs20201101_models.QueryTrajectoryByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trajectory_by_id_with_options_async(request, runtime)

    def recall_trajectory_by_coordinate_with_options(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByCoordinateResponse(),
            self.do_rpcrequest('RecallTrajectoryByCoordinate', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recall_trajectory_by_coordinate_with_options_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByCoordinateResponse(),
            await self.do_rpcrequest_async('RecallTrajectoryByCoordinate', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_trajectory_by_coordinate(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateResponse:
        runtime = util_models.RuntimeOptions()
        return self.recall_trajectory_by_coordinate_with_options(request, runtime)

    async def recall_trajectory_by_coordinate_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recall_trajectory_by_coordinate_with_options_async(request, runtime)

    def recall_trajectory_by_coordinate_time_with_options(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse(),
            self.do_rpcrequest('RecallTrajectoryByCoordinateTime', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recall_trajectory_by_coordinate_time_with_options_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse(),
            await self.do_rpcrequest_async('RecallTrajectoryByCoordinateTime', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_trajectory_by_coordinate_time(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateTimeRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.recall_trajectory_by_coordinate_time_with_options(request, runtime)

    async def recall_trajectory_by_coordinate_time_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByCoordinateTimeRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recall_trajectory_by_coordinate_time_with_options_async(request, runtime)

    def recall_trajectory_by_id_with_options(
        self,
        request: cdrs20201101_models.RecallTrajectoryByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByIdResponse(),
            self.do_rpcrequest('RecallTrajectoryById', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recall_trajectory_by_id_with_options_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecallTrajectoryByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByIdResponse(),
            await self.do_rpcrequest_async('RecallTrajectoryById', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_trajectory_by_id(
        self,
        request: cdrs20201101_models.RecallTrajectoryByIdRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.recall_trajectory_by_id_with_options(request, runtime)

    async def recall_trajectory_by_id_async(
        self,
        request: cdrs20201101_models.RecallTrajectoryByIdRequest,
    ) -> cdrs20201101_models.RecallTrajectoryByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recall_trajectory_by_id_with_options_async(request, runtime)

    def recognize_image_with_options(
        self,
        request: cdrs20201101_models.RecognizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecognizeImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecognizeImageResponse(),
            self.do_rpcrequest('RecognizeImage', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_with_options_async(
        self,
        request: cdrs20201101_models.RecognizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.RecognizeImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecognizeImageResponse(),
            await self.do_rpcrequest_async('RecognizeImage', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image(
        self,
        request: cdrs20201101_models.RecognizeImageRequest,
    ) -> cdrs20201101_models.RecognizeImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_with_options(request, runtime)

    async def recognize_image_async(
        self,
        request: cdrs20201101_models.RecognizeImageRequest,
    ) -> cdrs20201101_models.RecognizeImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_with_options_async(request, runtime)

    def search_aggregate_object_with_options(
        self,
        request: cdrs20201101_models.SearchAggregateObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.SearchAggregateObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchAggregateObjectResponse(),
            self.do_rpcrequest('SearchAggregateObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_aggregate_object_with_options_async(
        self,
        request: cdrs20201101_models.SearchAggregateObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.SearchAggregateObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchAggregateObjectResponse(),
            await self.do_rpcrequest_async('SearchAggregateObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_aggregate_object(
        self,
        request: cdrs20201101_models.SearchAggregateObjectRequest,
    ) -> cdrs20201101_models.SearchAggregateObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_aggregate_object_with_options(request, runtime)

    async def search_aggregate_object_async(
        self,
        request: cdrs20201101_models.SearchAggregateObjectRequest,
    ) -> cdrs20201101_models.SearchAggregateObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_aggregate_object_with_options_async(request, runtime)

    def search_object_with_options(
        self,
        request: cdrs20201101_models.SearchObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.SearchObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchObjectResponse(),
            self.do_rpcrequest('SearchObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_object_with_options_async(
        self,
        request: cdrs20201101_models.SearchObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.SearchObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchObjectResponse(),
            await self.do_rpcrequest_async('SearchObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_object(
        self,
        request: cdrs20201101_models.SearchObjectRequest,
    ) -> cdrs20201101_models.SearchObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_object_with_options(request, runtime)

    async def search_object_async(
        self,
        request: cdrs20201101_models.SearchObjectRequest,
    ) -> cdrs20201101_models.SearchObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_object_with_options_async(request, runtime)

    def stop_cdrs_monitor_with_options(
        self,
        request: cdrs20201101_models.StopCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.StopCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopCdrsMonitorResponse(),
            self.do_rpcrequest('StopCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_cdrs_monitor_with_options_async(
        self,
        request: cdrs20201101_models.StopCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.StopCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopCdrsMonitorResponse(),
            await self.do_rpcrequest_async('StopCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_cdrs_monitor(
        self,
        request: cdrs20201101_models.StopCdrsMonitorRequest,
    ) -> cdrs20201101_models.StopCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_cdrs_monitor_with_options(request, runtime)

    async def stop_cdrs_monitor_async(
        self,
        request: cdrs20201101_models.StopCdrsMonitorRequest,
    ) -> cdrs20201101_models.StopCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_cdrs_monitor_with_options_async(request, runtime)

    def stop_monitor_with_options(
        self,
        request: cdrs20201101_models.StopMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.StopMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopMonitorResponse(),
            self.do_rpcrequest('StopMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_monitor_with_options_async(
        self,
        request: cdrs20201101_models.StopMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.StopMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopMonitorResponse(),
            await self.do_rpcrequest_async('StopMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_monitor(
        self,
        request: cdrs20201101_models.StopMonitorRequest,
    ) -> cdrs20201101_models.StopMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_monitor_with_options(request, runtime)

    async def stop_monitor_async(
        self,
        request: cdrs20201101_models.StopMonitorRequest,
    ) -> cdrs20201101_models.StopMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_monitor_with_options_async(request, runtime)

    def unbind_device_with_options(
        self,
        request: cdrs20201101_models.UnbindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UnbindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UnbindDeviceResponse(),
            self.do_rpcrequest('UnbindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_device_with_options_async(
        self,
        request: cdrs20201101_models.UnbindDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UnbindDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UnbindDeviceResponse(),
            await self.do_rpcrequest_async('UnbindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_device(
        self,
        request: cdrs20201101_models.UnbindDeviceRequest,
    ) -> cdrs20201101_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_device_with_options(request, runtime)

    async def unbind_device_async(
        self,
        request: cdrs20201101_models.UnbindDeviceRequest,
    ) -> cdrs20201101_models.UnbindDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_device_with_options_async(request, runtime)

    def update_cdrs_monitor_with_options(
        self,
        request: cdrs20201101_models.UpdateCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateCdrsMonitorResponse(),
            self.do_rpcrequest('UpdateCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cdrs_monitor_with_options_async(
        self,
        request: cdrs20201101_models.UpdateCdrsMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateCdrsMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateCdrsMonitorResponse(),
            await self.do_rpcrequest_async('UpdateCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cdrs_monitor(
        self,
        request: cdrs20201101_models.UpdateCdrsMonitorRequest,
    ) -> cdrs20201101_models.UpdateCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cdrs_monitor_with_options(request, runtime)

    async def update_cdrs_monitor_async(
        self,
        request: cdrs20201101_models.UpdateCdrsMonitorRequest,
    ) -> cdrs20201101_models.UpdateCdrsMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cdrs_monitor_with_options_async(request, runtime)

    def update_monitor_with_options(
        self,
        request: cdrs20201101_models.UpdateMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateMonitorResponse(),
            self.do_rpcrequest('UpdateMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_monitor_with_options_async(
        self,
        request: cdrs20201101_models.UpdateMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateMonitorResponse(),
            await self.do_rpcrequest_async('UpdateMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_monitor(
        self,
        request: cdrs20201101_models.UpdateMonitorRequest,
    ) -> cdrs20201101_models.UpdateMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_monitor_with_options(request, runtime)

    async def update_monitor_async(
        self,
        request: cdrs20201101_models.UpdateMonitorRequest,
    ) -> cdrs20201101_models.UpdateMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_monitor_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: cdrs20201101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: cdrs20201101_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateProjectResponse(),
            await self.do_rpcrequest_async('UpdateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: cdrs20201101_models.UpdateProjectRequest,
    ) -> cdrs20201101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: cdrs20201101_models.UpdateProjectRequest,
    ) -> cdrs20201101_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def validate_trajectory_with_options(
        self,
        request: cdrs20201101_models.ValidateTrajectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ValidateTrajectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ValidateTrajectoryResponse(),
            self.do_rpcrequest('ValidateTrajectory', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_trajectory_with_options_async(
        self,
        request: cdrs20201101_models.ValidateTrajectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdrs20201101_models.ValidateTrajectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ValidateTrajectoryResponse(),
            await self.do_rpcrequest_async('ValidateTrajectory', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_trajectory(
        self,
        request: cdrs20201101_models.ValidateTrajectoryRequest,
    ) -> cdrs20201101_models.ValidateTrajectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_trajectory_with_options(request, runtime)

    async def validate_trajectory_async(
        self,
        request: cdrs20201101_models.ValidateTrajectoryRequest,
    ) -> cdrs20201101_models.ValidateTrajectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_trajectory_with_options_async(request, runtime)

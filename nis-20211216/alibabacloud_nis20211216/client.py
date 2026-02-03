# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_nis20211216 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('nis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_and_analyze_network_path_with_options(
        self,
        request: main_models.CreateAndAnalyzeNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAnalyzeNetworkPathResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAnalyzeNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAnalyzeNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_analyze_network_path_with_options_async(
        self,
        request: main_models.CreateAndAnalyzeNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAnalyzeNetworkPathResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAnalyzeNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAnalyzeNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_analyze_network_path(
        self,
        request: main_models.CreateAndAnalyzeNetworkPathRequest,
    ) -> main_models.CreateAndAnalyzeNetworkPathResponse:
        runtime = RuntimeOptions()
        return self.create_and_analyze_network_path_with_options(request, runtime)

    async def create_and_analyze_network_path_async(
        self,
        request: main_models.CreateAndAnalyzeNetworkPathRequest,
    ) -> main_models.CreateAndAnalyzeNetworkPathResponse:
        runtime = RuntimeOptions()
        return await self.create_and_analyze_network_path_with_options_async(request, runtime)

    def create_network_path_with_options(
        self,
        request: main_models.CreateNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_path_description):
            query['NetworkPathDescription'] = request.network_path_description
        if not DaraCore.is_null(request.network_path_name):
            query['NetworkPathName'] = request.network_path_name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not DaraCore.is_null(request.source_port):
            query['SourcePort'] = request.source_port
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_ip_address):
            query['TargetIpAddress'] = request.target_ip_address
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_path_with_options_async(
        self,
        request: main_models.CreateNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_path_description):
            query['NetworkPathDescription'] = request.network_path_description
        if not DaraCore.is_null(request.network_path_name):
            query['NetworkPathName'] = request.network_path_name
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        if not DaraCore.is_null(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not DaraCore.is_null(request.source_port):
            query['SourcePort'] = request.source_port
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_ip_address):
            query['TargetIpAddress'] = request.target_ip_address
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_path(
        self,
        request: main_models.CreateNetworkPathRequest,
    ) -> main_models.CreateNetworkPathResponse:
        runtime = RuntimeOptions()
        return self.create_network_path_with_options(request, runtime)

    async def create_network_path_async(
        self,
        request: main_models.CreateNetworkPathRequest,
    ) -> main_models.CreateNetworkPathResponse:
        runtime = RuntimeOptions()
        return await self.create_network_path_with_options_async(request, runtime)

    def create_network_reachable_analysis_with_options(
        self,
        request: main_models.CreateNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkReachableAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_path_id):
            query['NetworkPathId'] = request.network_path_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_reachable_analysis_with_options_async(
        self,
        request: main_models.CreateNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkReachableAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_path_id):
            query['NetworkPathId'] = request.network_path_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_reachable_analysis(
        self,
        request: main_models.CreateNetworkReachableAnalysisRequest,
    ) -> main_models.CreateNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return self.create_network_reachable_analysis_with_options(request, runtime)

    async def create_network_reachable_analysis_async(
        self,
        request: main_models.CreateNetworkReachableAnalysisRequest,
    ) -> main_models.CreateNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.create_network_reachable_analysis_with_options_async(request, runtime)

    def delete_network_path_with_options(
        self,
        tmp_req: main_models.DeleteNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkPathResponse:
        tmp_req.validate()
        request = main_models.DeleteNetworkPathShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_path_ids):
            request.network_path_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_path_ids, 'NetworkPathIds', 'json')
        query = {}
        if not DaraCore.is_null(request.network_path_ids_shrink):
            query['NetworkPathIds'] = request.network_path_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_path_with_options_async(
        self,
        tmp_req: main_models.DeleteNetworkPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkPathResponse:
        tmp_req.validate()
        request = main_models.DeleteNetworkPathShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_path_ids):
            request.network_path_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_path_ids, 'NetworkPathIds', 'json')
        query = {}
        if not DaraCore.is_null(request.network_path_ids_shrink):
            query['NetworkPathIds'] = request.network_path_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkPath',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_path(
        self,
        request: main_models.DeleteNetworkPathRequest,
    ) -> main_models.DeleteNetworkPathResponse:
        runtime = RuntimeOptions()
        return self.delete_network_path_with_options(request, runtime)

    async def delete_network_path_async(
        self,
        request: main_models.DeleteNetworkPathRequest,
    ) -> main_models.DeleteNetworkPathResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_path_with_options_async(request, runtime)

    def delete_network_reachable_analysis_with_options(
        self,
        tmp_req: main_models.DeleteNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkReachableAnalysisResponse:
        tmp_req.validate()
        request = main_models.DeleteNetworkReachableAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_reachable_analysis_ids):
            request.network_reachable_analysis_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_reachable_analysis_ids, 'NetworkReachableAnalysisIds', 'json')
        query = {}
        if not DaraCore.is_null(request.network_reachable_analysis_ids_shrink):
            query['NetworkReachableAnalysisIds'] = request.network_reachable_analysis_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_reachable_analysis_with_options_async(
        self,
        tmp_req: main_models.DeleteNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkReachableAnalysisResponse:
        tmp_req.validate()
        request = main_models.DeleteNetworkReachableAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.network_reachable_analysis_ids):
            request.network_reachable_analysis_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.network_reachable_analysis_ids, 'NetworkReachableAnalysisIds', 'json')
        query = {}
        if not DaraCore.is_null(request.network_reachable_analysis_ids_shrink):
            query['NetworkReachableAnalysisIds'] = request.network_reachable_analysis_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_reachable_analysis(
        self,
        request: main_models.DeleteNetworkReachableAnalysisRequest,
    ) -> main_models.DeleteNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return self.delete_network_reachable_analysis_with_options(request, runtime)

    async def delete_network_reachable_analysis_async(
        self,
        request: main_models.DeleteNetworkReachableAnalysisRequest,
    ) -> main_models.DeleteNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_reachable_analysis_with_options_async(request, runtime)

    def delete_nis_inspection_report_with_options(
        self,
        request: main_models.DeleteNisInspectionReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNisInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNisInspectionReport',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNisInspectionReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nis_inspection_report_with_options_async(
        self,
        request: main_models.DeleteNisInspectionReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNisInspectionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNisInspectionReport',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNisInspectionReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nis_inspection_report(
        self,
        request: main_models.DeleteNisInspectionReportRequest,
    ) -> main_models.DeleteNisInspectionReportResponse:
        runtime = RuntimeOptions()
        return self.delete_nis_inspection_report_with_options(request, runtime)

    async def delete_nis_inspection_report_async(
        self,
        request: main_models.DeleteNisInspectionReportRequest,
    ) -> main_models.DeleteNisInspectionReportResponse:
        runtime = RuntimeOptions()
        return await self.delete_nis_inspection_report_with_options_async(request, runtime)

    def delete_nis_inspection_task_with_options(
        self,
        request: main_models.DeleteNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNisInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nis_inspection_task_with_options_async(
        self,
        request: main_models.DeleteNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNisInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nis_inspection_task(
        self,
        request: main_models.DeleteNisInspectionTaskRequest,
    ) -> main_models.DeleteNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_nis_inspection_task_with_options(request, runtime)

    async def delete_nis_inspection_task_async(
        self,
        request: main_models.DeleteNisInspectionTaskRequest,
    ) -> main_models.DeleteNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_nis_inspection_task_with_options_async(request, runtime)

    def describe_nis_inspection_recommendation_resources_with_options(
        self,
        request: main_models.DescribeNisInspectionRecommendationResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionRecommendationResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.recommendation_code):
            query['RecommendationCode'] = request.recommendation_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionRecommendationResources',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionRecommendationResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_inspection_recommendation_resources_with_options_async(
        self,
        request: main_models.DescribeNisInspectionRecommendationResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionRecommendationResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.recommendation_code):
            query['RecommendationCode'] = request.recommendation_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionRecommendationResources',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionRecommendationResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_inspection_recommendation_resources(
        self,
        request: main_models.DescribeNisInspectionRecommendationResourcesRequest,
    ) -> main_models.DescribeNisInspectionRecommendationResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_inspection_recommendation_resources_with_options(request, runtime)

    async def describe_nis_inspection_recommendation_resources_async(
        self,
        request: main_models.DescribeNisInspectionRecommendationResourcesRequest,
    ) -> main_models.DescribeNisInspectionRecommendationResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_inspection_recommendation_resources_with_options_async(request, runtime)

    def describe_nis_inspection_report_check_items_with_options(
        self,
        tmp_req: main_models.DescribeNisInspectionReportCheckItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportCheckItemsResponse:
        tmp_req.validate()
        request = main_models.DescribeNisInspectionReportCheckItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_type):
            request.resource_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_type, 'ResourceType', 'json')
        if not DaraCore.is_null(tmp_req.risk_level):
            request.risk_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.risk_level, 'RiskLevel', 'json')
        query = {}
        if not DaraCore.is_null(request.category_code):
            query['CategoryCode'] = request.category_code
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type_shrink):
            query['ResourceType'] = request.resource_type_shrink
        if not DaraCore.is_null(request.risk_level_shrink):
            query['RiskLevel'] = request.risk_level_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportCheckItems',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportCheckItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_inspection_report_check_items_with_options_async(
        self,
        tmp_req: main_models.DescribeNisInspectionReportCheckItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportCheckItemsResponse:
        tmp_req.validate()
        request = main_models.DescribeNisInspectionReportCheckItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_type):
            request.resource_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_type, 'ResourceType', 'json')
        if not DaraCore.is_null(tmp_req.risk_level):
            request.risk_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.risk_level, 'RiskLevel', 'json')
        query = {}
        if not DaraCore.is_null(request.category_code):
            query['CategoryCode'] = request.category_code
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type_shrink):
            query['ResourceType'] = request.resource_type_shrink
        if not DaraCore.is_null(request.risk_level_shrink):
            query['RiskLevel'] = request.risk_level_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportCheckItems',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportCheckItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_inspection_report_check_items(
        self,
        request: main_models.DescribeNisInspectionReportCheckItemsRequest,
    ) -> main_models.DescribeNisInspectionReportCheckItemsResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_inspection_report_check_items_with_options(request, runtime)

    async def describe_nis_inspection_report_check_items_async(
        self,
        request: main_models.DescribeNisInspectionReportCheckItemsRequest,
    ) -> main_models.DescribeNisInspectionReportCheckItemsResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_inspection_report_check_items_with_options_async(request, runtime)

    def describe_nis_inspection_report_status_with_options(
        self,
        request: main_models.DescribeNisInspectionReportStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportStatus',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_inspection_report_status_with_options_async(
        self,
        request: main_models.DescribeNisInspectionReportStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportStatus',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_inspection_report_status(
        self,
        request: main_models.DescribeNisInspectionReportStatusRequest,
    ) -> main_models.DescribeNisInspectionReportStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_inspection_report_status_with_options(request, runtime)

    async def describe_nis_inspection_report_status_async(
        self,
        request: main_models.DescribeNisInspectionReportStatusRequest,
    ) -> main_models.DescribeNisInspectionReportStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_inspection_report_status_with_options_async(request, runtime)

    def describe_nis_inspection_report_summary_with_options(
        self,
        request: main_models.DescribeNisInspectionReportSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportSummary',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_inspection_report_summary_with_options_async(
        self,
        request: main_models.DescribeNisInspectionReportSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionReportSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_report_id):
            query['InspectionReportId'] = request.inspection_report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionReportSummary',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionReportSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_inspection_report_summary(
        self,
        request: main_models.DescribeNisInspectionReportSummaryRequest,
    ) -> main_models.DescribeNisInspectionReportSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_inspection_report_summary_with_options(request, runtime)

    async def describe_nis_inspection_report_summary_async(
        self,
        request: main_models.DescribeNisInspectionReportSummaryRequest,
    ) -> main_models.DescribeNisInspectionReportSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_inspection_report_summary_with_options_async(request, runtime)

    def describe_nis_inspection_task_with_options(
        self,
        request: main_models.DescribeNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_inspection_task_with_options_async(
        self,
        request: main_models.DescribeNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_inspection_task(
        self,
        request: main_models.DescribeNisInspectionTaskRequest,
    ) -> main_models.DescribeNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_inspection_task_with_options(request, runtime)

    async def describe_nis_inspection_task_async(
        self,
        request: main_models.DescribeNisInspectionTaskRequest,
    ) -> main_models.DescribeNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_inspection_task_with_options_async(request, runtime)

    def describe_nis_traffic_ranking_with_options(
        self,
        request: main_models.DescribeNisTrafficRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisTrafficRankingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.nis_traffic_ranking_id):
            query['NisTrafficRankingId'] = request.nis_traffic_ranking_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisTrafficRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisTrafficRankingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nis_traffic_ranking_with_options_async(
        self,
        request: main_models.DescribeNisTrafficRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNisTrafficRankingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.nis_traffic_ranking_id):
            query['NisTrafficRankingId'] = request.nis_traffic_ranking_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNisTrafficRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNisTrafficRankingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nis_traffic_ranking(
        self,
        request: main_models.DescribeNisTrafficRankingRequest,
    ) -> main_models.DescribeNisTrafficRankingResponse:
        runtime = RuntimeOptions()
        return self.describe_nis_traffic_ranking_with_options(request, runtime)

    async def describe_nis_traffic_ranking_async(
        self,
        request: main_models.DescribeNisTrafficRankingRequest,
    ) -> main_models.DescribeNisTrafficRankingResponse:
        runtime = RuntimeOptions()
        return await self.describe_nis_traffic_ranking_with_options_async(request, runtime)

    def get_internet_tuple_with_options(
        self,
        tmp_req: main_models.GetInternetTupleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInternetTupleResponse:
        tmp_req.validate()
        request = main_models.GetInternetTupleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cloud_ip_list):
            request.cloud_ip_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cloud_ip_list, 'CloudIpList', 'json')
        if not DaraCore.is_null(tmp_req.instance_list):
            request.instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not DaraCore.is_null(request.cloud_ip_list_shrink):
            query['CloudIpList'] = request.cloud_ip_list_shrink
        if not DaraCore.is_null(request.cloud_isp):
            query['CloudIsp'] = request.cloud_isp
        if not DaraCore.is_null(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_city):
            query['OtherCity'] = request.other_city
        if not DaraCore.is_null(request.other_country):
            query['OtherCountry'] = request.other_country
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_isp):
            query['OtherIsp'] = request.other_isp
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.tuple_type):
            query['TupleType'] = request.tuple_type
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInternetTuple',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInternetTupleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_internet_tuple_with_options_async(
        self,
        tmp_req: main_models.GetInternetTupleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInternetTupleResponse:
        tmp_req.validate()
        request = main_models.GetInternetTupleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cloud_ip_list):
            request.cloud_ip_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cloud_ip_list, 'CloudIpList', 'json')
        if not DaraCore.is_null(tmp_req.instance_list):
            request.instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not DaraCore.is_null(request.cloud_ip_list_shrink):
            query['CloudIpList'] = request.cloud_ip_list_shrink
        if not DaraCore.is_null(request.cloud_isp):
            query['CloudIsp'] = request.cloud_isp
        if not DaraCore.is_null(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_city):
            query['OtherCity'] = request.other_city
        if not DaraCore.is_null(request.other_country):
            query['OtherCountry'] = request.other_country
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_isp):
            query['OtherIsp'] = request.other_isp
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.tuple_type):
            query['TupleType'] = request.tuple_type
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInternetTuple',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInternetTupleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_internet_tuple(
        self,
        request: main_models.GetInternetTupleRequest,
    ) -> main_models.GetInternetTupleResponse:
        runtime = RuntimeOptions()
        return self.get_internet_tuple_with_options(request, runtime)

    async def get_internet_tuple_async(
        self,
        request: main_models.GetInternetTupleRequest,
    ) -> main_models.GetInternetTupleResponse:
        runtime = RuntimeOptions()
        return await self.get_internet_tuple_with_options_async(request, runtime)

    def get_nat_top_nwith_options(
        self,
        request: main_models.GetNatTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNatTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNatTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNatTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nat_top_nwith_options_async(
        self,
        request: main_models.GetNatTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNatTopNResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNatTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNatTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nat_top_n(
        self,
        request: main_models.GetNatTopNRequest,
    ) -> main_models.GetNatTopNResponse:
        runtime = RuntimeOptions()
        return self.get_nat_top_nwith_options(request, runtime)

    async def get_nat_top_n_async(
        self,
        request: main_models.GetNatTopNRequest,
    ) -> main_models.GetNatTopNResponse:
        runtime = RuntimeOptions()
        return await self.get_nat_top_nwith_options_async(request, runtime)

    def get_network_reachable_analysis_with_options(
        self,
        request: main_models.GetNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkReachableAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_reachable_analysis_id):
            query['NetworkReachableAnalysisId'] = request.network_reachable_analysis_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_reachable_analysis_with_options_async(
        self,
        request: main_models.GetNetworkReachableAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkReachableAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_reachable_analysis_id):
            query['NetworkReachableAnalysisId'] = request.network_reachable_analysis_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkReachableAnalysis',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_reachable_analysis(
        self,
        request: main_models.GetNetworkReachableAnalysisRequest,
    ) -> main_models.GetNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return self.get_network_reachable_analysis_with_options(request, runtime)

    async def get_network_reachable_analysis_async(
        self,
        request: main_models.GetNetworkReachableAnalysisRequest,
    ) -> main_models.GetNetworkReachableAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.get_network_reachable_analysis_with_options_async(request, runtime)

    def get_nis_network_metrics_with_options(
        self,
        tmp_req: main_models.GetNisNetworkMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNisNetworkMetricsResponse:
        tmp_req.validate()
        request = main_models.GetNisNetworkMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scan_by):
            query['ScanBy'] = request.scan_by
        if not DaraCore.is_null(request.step_minutes):
            query['StepMinutes'] = request.step_minutes
        if not DaraCore.is_null(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNisNetworkMetrics',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNisNetworkMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nis_network_metrics_with_options_async(
        self,
        tmp_req: main_models.GetNisNetworkMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNisNetworkMetricsResponse:
        tmp_req.validate()
        request = main_models.GetNisNetworkMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dimensions):
            request.dimensions_shrink = Utils.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scan_by):
            query['ScanBy'] = request.scan_by
        if not DaraCore.is_null(request.step_minutes):
            query['StepMinutes'] = request.step_minutes
        if not DaraCore.is_null(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNisNetworkMetrics',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNisNetworkMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nis_network_metrics(
        self,
        request: main_models.GetNisNetworkMetricsRequest,
    ) -> main_models.GetNisNetworkMetricsResponse:
        runtime = RuntimeOptions()
        return self.get_nis_network_metrics_with_options(request, runtime)

    async def get_nis_network_metrics_async(
        self,
        request: main_models.GetNisNetworkMetricsRequest,
    ) -> main_models.GetNisNetworkMetricsResponse:
        runtime = RuntimeOptions()
        return await self.get_nis_network_metrics_with_options_async(request, runtime)

    def get_nis_network_ranking_with_options(
        self,
        tmp_req: main_models.GetNisNetworkRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNisNetworkRankingResponse:
        tmp_req.validate()
        request = main_models.GetNisNetworkRankingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNisNetworkRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNisNetworkRankingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nis_network_ranking_with_options_async(
        self,
        tmp_req: main_models.GetNisNetworkRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNisNetworkRankingResponse:
        tmp_req.validate()
        request = main_models.GetNisNetworkRankingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNisNetworkRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNisNetworkRankingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nis_network_ranking(
        self,
        request: main_models.GetNisNetworkRankingRequest,
    ) -> main_models.GetNisNetworkRankingResponse:
        runtime = RuntimeOptions()
        return self.get_nis_network_ranking_with_options(request, runtime)

    async def get_nis_network_ranking_async(
        self,
        request: main_models.GetNisNetworkRankingRequest,
    ) -> main_models.GetNisNetworkRankingResponse:
        runtime = RuntimeOptions()
        return await self.get_nis_network_ranking_with_options_async(request, runtime)

    def get_transit_router_flow_top_nwith_options(
        self,
        tmp_req: main_models.GetTransitRouterFlowTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransitRouterFlowTopNResponse:
        tmp_req.validate()
        request = main_models.GetTransitRouterFlowTopNShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.bandwith_package_id):
            query['BandwithPackageId'] = request.bandwith_package_id
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.other_region):
            query['OtherRegion'] = request.other_region
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.this_ip):
            query['ThisIp'] = request.this_ip
        if not DaraCore.is_null(request.this_port):
            query['ThisPort'] = request.this_port
        if not DaraCore.is_null(request.this_region):
            query['ThisRegion'] = request.this_region
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransitRouterFlowTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransitRouterFlowTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transit_router_flow_top_nwith_options_async(
        self,
        tmp_req: main_models.GetTransitRouterFlowTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransitRouterFlowTopNResponse:
        tmp_req.validate()
        request = main_models.GetTransitRouterFlowTopNShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.bandwith_package_id):
            query['BandwithPackageId'] = request.bandwith_package_id
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.other_region):
            query['OtherRegion'] = request.other_region
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.this_ip):
            query['ThisIp'] = request.this_ip
        if not DaraCore.is_null(request.this_port):
            query['ThisPort'] = request.this_port
        if not DaraCore.is_null(request.this_region):
            query['ThisRegion'] = request.this_region
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransitRouterFlowTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransitRouterFlowTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transit_router_flow_top_n(
        self,
        request: main_models.GetTransitRouterFlowTopNRequest,
    ) -> main_models.GetTransitRouterFlowTopNResponse:
        runtime = RuntimeOptions()
        return self.get_transit_router_flow_top_nwith_options(request, runtime)

    async def get_transit_router_flow_top_n_async(
        self,
        request: main_models.GetTransitRouterFlowTopNRequest,
    ) -> main_models.GetTransitRouterFlowTopNResponse:
        runtime = RuntimeOptions()
        return await self.get_transit_router_flow_top_nwith_options_async(request, runtime)

    def get_vbr_flow_top_nwith_options(
        self,
        tmp_req: main_models.GetVbrFlowTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVbrFlowTopNResponse:
        tmp_req.validate()
        request = main_models.GetVbrFlowTopNShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not DaraCore.is_null(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        if not DaraCore.is_null(request.virtual_border_router_id):
            query['VirtualBorderRouterId'] = request.virtual_border_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVbrFlowTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVbrFlowTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vbr_flow_top_nwith_options_async(
        self,
        tmp_req: main_models.GetVbrFlowTopNRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVbrFlowTopNResponse:
        tmp_req.validate()
        request = main_models.GetVbrFlowTopNShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not DaraCore.is_null(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not DaraCore.is_null(request.other_port):
            query['OtherPort'] = request.other_port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        if not DaraCore.is_null(request.virtual_border_router_id):
            query['VirtualBorderRouterId'] = request.virtual_border_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVbrFlowTopN',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVbrFlowTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vbr_flow_top_n(
        self,
        request: main_models.GetVbrFlowTopNRequest,
    ) -> main_models.GetVbrFlowTopNResponse:
        runtime = RuntimeOptions()
        return self.get_vbr_flow_top_nwith_options(request, runtime)

    async def get_vbr_flow_top_n_async(
        self,
        request: main_models.GetVbrFlowTopNRequest,
    ) -> main_models.GetVbrFlowTopNResponse:
        runtime = RuntimeOptions()
        return await self.get_vbr_flow_top_nwith_options_async(request, runtime)

    def list_nis_inspection_resource_type_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionResourceTypeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListNisInspectionResourceType',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nis_inspection_resource_type_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionResourceTypeResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListNisInspectionResourceType',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nis_inspection_resource_type(self) -> main_models.ListNisInspectionResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.list_nis_inspection_resource_type_with_options(runtime)

    async def list_nis_inspection_resource_type_async(self) -> main_models.ListNisInspectionResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.list_nis_inspection_resource_type_with_options_async(runtime)

    def list_nis_inspection_task_reports_with_options(
        self,
        request: main_models.ListNisInspectionTaskReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionTaskReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNisInspectionTaskReports',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionTaskReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nis_inspection_task_reports_with_options_async(
        self,
        request: main_models.ListNisInspectionTaskReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionTaskReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNisInspectionTaskReports',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionTaskReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nis_inspection_task_reports(
        self,
        request: main_models.ListNisInspectionTaskReportsRequest,
    ) -> main_models.ListNisInspectionTaskReportsResponse:
        runtime = RuntimeOptions()
        return self.list_nis_inspection_task_reports_with_options(request, runtime)

    async def list_nis_inspection_task_reports_async(
        self,
        request: main_models.ListNisInspectionTaskReportsRequest,
    ) -> main_models.ListNisInspectionTaskReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_nis_inspection_task_reports_with_options_async(request, runtime)

    def list_nis_inspection_tasks_with_options(
        self,
        request: main_models.ListNisInspectionTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_name):
            query['InspectionName'] = request.inspection_name
        if not DaraCore.is_null(request.inspection_project):
            query['InspectionProject'] = request.inspection_project
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNisInspectionTasks',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nis_inspection_tasks_with_options_async(
        self,
        request: main_models.ListNisInspectionTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNisInspectionTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_name):
            query['InspectionName'] = request.inspection_name
        if not DaraCore.is_null(request.inspection_project):
            query['InspectionProject'] = request.inspection_project
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNisInspectionTasks',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNisInspectionTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nis_inspection_tasks(
        self,
        request: main_models.ListNisInspectionTasksRequest,
    ) -> main_models.ListNisInspectionTasksResponse:
        runtime = RuntimeOptions()
        return self.list_nis_inspection_tasks_with_options(request, runtime)

    async def list_nis_inspection_tasks_async(
        self,
        request: main_models.ListNisInspectionTasksRequest,
    ) -> main_models.ListNisInspectionTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_nis_inspection_tasks_with_options_async(request, runtime)

    def start_nis_inspection_task_with_options(
        self,
        request: main_models.StartNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartNisInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_nis_inspection_task_with_options_async(
        self,
        request: main_models.StartNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartNisInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_nis_inspection_task(
        self,
        request: main_models.StartNisInspectionTaskRequest,
    ) -> main_models.StartNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.start_nis_inspection_task_with_options(request, runtime)

    async def start_nis_inspection_task_async(
        self,
        request: main_models.StartNisInspectionTaskRequest,
    ) -> main_models.StartNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_nis_inspection_task_with_options_async(request, runtime)

    def start_nis_traffic_ranking_with_options(
        self,
        tmp_req: main_models.StartNisTrafficRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartNisTrafficRankingResponse:
        tmp_req.validate()
        request = main_models.StartNisTrafficRankingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.group_by):
            request.group_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_by, 'GroupBy', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.group_by_shrink):
            query['GroupBy'] = request.group_by_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.storage_interval):
            query['StorageInterval'] = request.storage_interval
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.traffic_analyzer_id):
            query['TrafficAnalyzerId'] = request.traffic_analyzer_id
        if not DaraCore.is_null(request.traffic_scenario):
            query['TrafficScenario'] = request.traffic_scenario
        if not DaraCore.is_null(request.tuple_dimension):
            query['TupleDimension'] = request.tuple_dimension
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartNisTrafficRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartNisTrafficRankingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_nis_traffic_ranking_with_options_async(
        self,
        tmp_req: main_models.StartNisTrafficRankingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartNisTrafficRankingResponse:
        tmp_req.validate()
        request = main_models.StartNisTrafficRankingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.group_by):
            request.group_by_shrink = Utils.array_to_string_with_specified_style(tmp_req.group_by, 'GroupBy', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.group_by_shrink):
            query['GroupBy'] = request.group_by_shrink
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.storage_interval):
            query['StorageInterval'] = request.storage_interval
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.traffic_analyzer_id):
            query['TrafficAnalyzerId'] = request.traffic_analyzer_id
        if not DaraCore.is_null(request.traffic_scenario):
            query['TrafficScenario'] = request.traffic_scenario
        if not DaraCore.is_null(request.tuple_dimension):
            query['TupleDimension'] = request.tuple_dimension
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartNisTrafficRanking',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartNisTrafficRankingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_nis_traffic_ranking(
        self,
        request: main_models.StartNisTrafficRankingRequest,
    ) -> main_models.StartNisTrafficRankingResponse:
        runtime = RuntimeOptions()
        return self.start_nis_traffic_ranking_with_options(request, runtime)

    async def start_nis_traffic_ranking_async(
        self,
        request: main_models.StartNisTrafficRankingRequest,
    ) -> main_models.StartNisTrafficRankingResponse:
        runtime = RuntimeOptions()
        return await self.start_nis_traffic_ranking_with_options_async(request, runtime)

    def update_nis_inspection_task_with_options(
        self,
        request: main_models.UpdateNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNisInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nis_inspection_task_with_options_async(
        self,
        request: main_models.UpdateNisInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNisInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inspection_task_id):
            query['InspectionTaskId'] = request.inspection_task_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNisInspectionTask',
            version = '2021-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNisInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nis_inspection_task(
        self,
        request: main_models.UpdateNisInspectionTaskRequest,
    ) -> main_models.UpdateNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.update_nis_inspection_task_with_options(request, runtime)

    async def update_nis_inspection_task_async(
        self,
        request: main_models.UpdateNisInspectionTaskRequest,
    ) -> main_models.UpdateNisInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_nis_inspection_task_with_options_async(request, runtime)

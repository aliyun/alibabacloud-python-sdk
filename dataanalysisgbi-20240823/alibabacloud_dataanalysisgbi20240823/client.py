# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataanalysisgbi20240823 import models as data_analysis_gbi20240823_models
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
        self._endpoint = self.get_endpoint('dataanalysisgbi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def run_data_analysis_with_options(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_data_analysis_with_options_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_data_analysis(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_data_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_data_analysis_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_data_analysis_with_options_async(workspace_id, request, headers, runtime)

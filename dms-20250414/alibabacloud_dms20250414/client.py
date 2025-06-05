# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dms20250414 import models as dms_20250414_models
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
        self._endpoint = self.get_endpoint('dms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_airflow_login_token_with_options(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary 获取airflow登录凭证
        
        @param request: CreateAirflowLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflowLoginToken',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_airflow_login_token_with_options_async(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary 获取airflow登录凭证
        
        @param request: CreateAirflowLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflowLoginToken',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_airflow_login_token(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary 获取airflow登录凭证
        
        @param request: CreateAirflowLoginTokenRequest
        @return: CreateAirflowLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_airflow_login_token_with_options(request, runtime)

    async def create_airflow_login_token_async(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary 获取airflow登录凭证
        
        @param request: CreateAirflowLoginTokenRequest
        @return: CreateAirflowLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_airflow_login_token_with_options_async(request, runtime)

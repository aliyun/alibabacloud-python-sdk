# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiearth_meteorology20210928 import models as aiearth__meteorology_20210928_models
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
        self._endpoint = self.get_endpoint('aiearth-meteorology', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def grid_query(
        self,
        data_type: str,
        request: aiearth__meteorology_20210928_models.GridQueryRequest,
    ) -> aiearth__meteorology_20210928_models.GridQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grid_query_with_options(data_type, request, headers, runtime)

    async def grid_query_async(
        self,
        data_type: str,
        request: aiearth__meteorology_20210928_models.GridQueryRequest,
    ) -> aiearth__meteorology_20210928_models.GridQueryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grid_query_with_options_async(data_type, request, headers, runtime)

    def grid_query_with_options(
        self,
        data_type: str,
        request: aiearth__meteorology_20210928_models.GridQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20210928_models.GridQueryResponse:
        UtilClient.validate_model(request)
        data_type = OpenApiUtilClient.get_encode_param(data_type)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.report_timestamp):
            query['reportTimestamp'] = request.report_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            aiearth__meteorology_20210928_models.GridQueryResponse(),
            self.do_roarequest('GridQuery', '2021-09-28', 'HTTPS', 'GET', 'AK', f'/grid/{data_type}/v1', 'json', req, runtime)
        )

    async def grid_query_with_options_async(
        self,
        data_type: str,
        request: aiearth__meteorology_20210928_models.GridQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__meteorology_20210928_models.GridQueryResponse:
        UtilClient.validate_model(request)
        data_type = OpenApiUtilClient.get_encode_param(data_type)
        query = {}
        if not UtilClient.is_unset(request.element):
            query['element'] = request.element
        if not UtilClient.is_unset(request.forecast_timestamp):
            query['forecastTimestamp'] = request.forecast_timestamp
        if not UtilClient.is_unset(request.latitude):
            query['latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['longitude'] = request.longitude
        if not UtilClient.is_unset(request.page_no):
            query['pageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.report_timestamp):
            query['reportTimestamp'] = request.report_timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            aiearth__meteorology_20210928_models.GridQueryResponse(),
            await self.do_roarequest_async('GridQuery', '2021-09-28', 'HTTPS', 'GET', 'AK', f'/grid/{data_type}/v1', 'json', req, runtime)
        )

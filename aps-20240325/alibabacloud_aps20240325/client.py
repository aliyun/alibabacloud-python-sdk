# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aps20240325 import models as aps_20240325_models
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
        self._endpoint = self.get_endpoint('aps', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_fx_customer_type_with_options(
        self,
        request: aps_20240325_models.GetFxCustomerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aps_20240325_models.GetFxCustomerTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFxCustomerType',
            version='2024-03-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aps_20240325_models.GetFxCustomerTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fx_customer_type_with_options_async(
        self,
        request: aps_20240325_models.GetFxCustomerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aps_20240325_models.GetFxCustomerTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFxCustomerType',
            version='2024-03-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aps_20240325_models.GetFxCustomerTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fx_customer_type(
        self,
        request: aps_20240325_models.GetFxCustomerTypeRequest,
    ) -> aps_20240325_models.GetFxCustomerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_fx_customer_type_with_options(request, runtime)

    async def get_fx_customer_type_async(
        self,
        request: aps_20240325_models.GetFxCustomerTypeRequest,
    ) -> aps_20240325_models.GetFxCustomerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_fx_customer_type_with_options_async(request, runtime)

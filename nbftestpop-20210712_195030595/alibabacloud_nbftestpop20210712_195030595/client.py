# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nbftestpop20210712_195030595 import models as nbf_test_pop_20210712__195030595_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('nbftestpop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def new_auth_test_with_options(
        self,
        request: nbf_test_pop_20210712__195030595_models.NewAuthTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nbf_test_pop_20210712__195030595_models.NewAuthTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nbf_test_pop_20210712__195030595_models.NewAuthTestResponse(),
            self.do_rpcrequest('NewAuthTest', '2021-07-12_19-50-30-595', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def new_auth_test_with_options_async(
        self,
        request: nbf_test_pop_20210712__195030595_models.NewAuthTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nbf_test_pop_20210712__195030595_models.NewAuthTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            nbf_test_pop_20210712__195030595_models.NewAuthTestResponse(),
            await self.do_rpcrequest_async('NewAuthTest', '2021-07-12_19-50-30-595', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def new_auth_test(
        self,
        request: nbf_test_pop_20210712__195030595_models.NewAuthTestRequest,
    ) -> nbf_test_pop_20210712__195030595_models.NewAuthTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.new_auth_test_with_options(request, runtime)

    async def new_auth_test_async(
        self,
        request: nbf_test_pop_20210712__195030595_models.NewAuthTestRequest,
    ) -> nbf_test_pop_20210712__195030595_models.NewAuthTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.new_auth_test_with_options_async(request, runtime)

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lmztest20210531_172452318 import models as lmz_test_20210531__172452318_models
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
        self._endpoint = self.get_endpoint('lmztest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def yx_test_api_with_options(
        self,
        request: lmz_test_20210531__172452318_models.YxTestApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lmz_test_20210531__172452318_models.YxTestApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lmz_test_20210531__172452318_models.YxTestApiResponse(),
            self.do_rpcrequest('YxTestApi', '2021-05-31_17-24-52-318', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def yx_test_api_with_options_async(
        self,
        request: lmz_test_20210531__172452318_models.YxTestApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lmz_test_20210531__172452318_models.YxTestApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lmz_test_20210531__172452318_models.YxTestApiResponse(),
            await self.do_rpcrequest_async('YxTestApi', '2021-05-31_17-24-52-318', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def yx_test_api(
        self,
        request: lmz_test_20210531__172452318_models.YxTestApiRequest,
    ) -> lmz_test_20210531__172452318_models.YxTestApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.yx_test_api_with_options(request, runtime)

    async def yx_test_api_async(
        self,
        request: lmz_test_20210531__172452318_models.YxTestApiRequest,
    ) -> lmz_test_20210531__172452318_models.YxTestApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.yx_test_api_with_options_async(request, runtime)

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_um_test20211027 import models as um_test_20211027_models
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
        self._endpoint = self.get_endpoint('um-test', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_oss_upload_param_with_options(
        self,
        request: um_test_20211027_models.GetOssUploadParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> um_test_20211027_models.GetOssUploadParamResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUploadParam',
            version='2021-10-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            um_test_20211027_models.GetOssUploadParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_upload_param_with_options_async(
        self,
        request: um_test_20211027_models.GetOssUploadParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> um_test_20211027_models.GetOssUploadParamResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUploadParam',
            version='2021-10-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            um_test_20211027_models.GetOssUploadParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_upload_param(
        self,
        request: um_test_20211027_models.GetOssUploadParamRequest,
    ) -> um_test_20211027_models.GetOssUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_upload_param_with_options(request, runtime)

    async def get_oss_upload_param_async(
        self,
        request: um_test_20211027_models.GetOssUploadParamRequest,
    ) -> um_test_20211027_models.GetOssUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_upload_param_with_options_async(request, runtime)

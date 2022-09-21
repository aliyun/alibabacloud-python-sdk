# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openplatform20191219 import models as open_platform_20191219_models
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
        self._endpoint = self.get_endpoint('openplatform', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def authorize_file_upload_with_options(
        self,
        request: open_platform_20191219_models.AuthorizeFileUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> open_platform_20191219_models.AuthorizeFileUploadResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            open_platform_20191219_models.AuthorizeFileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_file_upload_with_options_async(
        self,
        request: open_platform_20191219_models.AuthorizeFileUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> open_platform_20191219_models.AuthorizeFileUploadResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            open_platform_20191219_models.AuthorizeFileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_file_upload(
        self,
        request: open_platform_20191219_models.AuthorizeFileUploadRequest,
    ) -> open_platform_20191219_models.AuthorizeFileUploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_file_upload_with_options(request, runtime)

    async def authorize_file_upload_async(
        self,
        request: open_platform_20191219_models.AuthorizeFileUploadRequest,
    ) -> open_platform_20191219_models.AuthorizeFileUploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_file_upload_with_options_async(request, runtime)

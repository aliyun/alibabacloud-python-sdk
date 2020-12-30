# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageaudit20191230 import models as imageaudit_20191230_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imageaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def scan_image_with_options(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageaudit_20191230_models.ScanImageResponse().from_map(
            self.do_rpcrequest('ScanImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def scan_image_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageaudit_20191230_models.ScanImageResponse().from_map(
            await self.do_rpcrequest_async('ScanImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scan_image(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_image_with_options(request, runtime)

    async def scan_image_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_image_with_options_async(request, runtime)

    def scan_text_with_options(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageaudit_20191230_models.ScanTextResponse().from_map(
            self.do_rpcrequest('ScanText', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def scan_text_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imageaudit_20191230_models.ScanTextResponse().from_map(
            await self.do_rpcrequest_async('ScanText', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scan_text(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_text_with_options(request, runtime)

    async def scan_text_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_text_with_options_async(request, runtime)

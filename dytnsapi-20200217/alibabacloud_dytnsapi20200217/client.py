# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dytnsapi20200217 import models as dytnsapi_20200217_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dytnsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_phone_number_status_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberStatusResponse(),
            self.do_rpcrequest('DescribePhoneNumberStatus', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_phone_number_status_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberStatusResponse(),
            await self.do_rpcrequest_async('DescribePhoneNumberStatus', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_phone_number_status(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_status_with_options(request, runtime)

    async def describe_phone_number_status_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberStatusRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_status_with_options_async(request, runtime)

    def describe_phone_number_attribute_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse(),
            self.do_rpcrequest('DescribePhoneNumberAttribute', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_phone_number_attribute_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse(),
            await self.do_rpcrequest_async('DescribePhoneNumberAttribute', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_phone_number_attribute(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_attribute_with_options(request, runtime)

    async def describe_phone_number_attribute_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberAttributeRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_attribute_with_options_async(request, runtime)

    def describe_phone_number_resale_with_options(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberResaleResponse(),
            self.do_rpcrequest('DescribePhoneNumberResale', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_phone_number_resale_with_options_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dytnsapi_20200217_models.DescribePhoneNumberResaleResponse(),
            await self.do_rpcrequest_async('DescribePhoneNumberResale', '2020-02-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_phone_number_resale(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_number_resale_with_options(request, runtime)

    async def describe_phone_number_resale_async(
        self,
        request: dytnsapi_20200217_models.DescribePhoneNumberResaleRequest,
    ) -> dytnsapi_20200217_models.DescribePhoneNumberResaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_number_resale_with_options_async(request, runtime)

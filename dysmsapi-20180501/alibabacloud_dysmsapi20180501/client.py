# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysmsapi20180501 import models as dysmsapi_20180501_models
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
        self._endpoint_map = {
            'ap-southeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'dysmsapi-xman.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dysmsapi-proxy.cn-beijing.aliyuncs.com',
            'cn-hongkong': 'dysmsapi-xman.cn-hongkong.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dysmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_message_with_options(
        self,
        request: dysmsapi_20180501_models.QueryMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.QueryMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.QueryMessageResponse(),
            self.do_rpcrequest('QueryMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_message_with_options_async(
        self,
        request: dysmsapi_20180501_models.QueryMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.QueryMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.QueryMessageResponse(),
            await self.do_rpcrequest_async('QueryMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_message(
        self,
        request: dysmsapi_20180501_models.QueryMessageRequest,
    ) -> dysmsapi_20180501_models.QueryMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_message_with_options(request, runtime)

    async def query_message_async(
        self,
        request: dysmsapi_20180501_models.QueryMessageRequest,
    ) -> dysmsapi_20180501_models.QueryMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_message_with_options_async(request, runtime)

    def batch_send_message_to_globe_with_options(
        self,
        request: dysmsapi_20180501_models.BatchSendMessageToGlobeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.BatchSendMessageToGlobeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.BatchSendMessageToGlobeResponse(),
            self.do_rpcrequest('BatchSendMessageToGlobe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_send_message_to_globe_with_options_async(
        self,
        request: dysmsapi_20180501_models.BatchSendMessageToGlobeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.BatchSendMessageToGlobeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.BatchSendMessageToGlobeResponse(),
            await self.do_rpcrequest_async('BatchSendMessageToGlobe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_send_message_to_globe(
        self,
        request: dysmsapi_20180501_models.BatchSendMessageToGlobeRequest,
    ) -> dysmsapi_20180501_models.BatchSendMessageToGlobeResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_send_message_to_globe_with_options(request, runtime)

    async def batch_send_message_to_globe_async(
        self,
        request: dysmsapi_20180501_models.BatchSendMessageToGlobeRequest,
    ) -> dysmsapi_20180501_models.BatchSendMessageToGlobeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_send_message_to_globe_with_options_async(request, runtime)

    def sms_conversion_with_options(
        self,
        request: dysmsapi_20180501_models.SmsConversionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SmsConversionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SmsConversionResponse(),
            self.do_rpcrequest('SmsConversion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sms_conversion_with_options_async(
        self,
        request: dysmsapi_20180501_models.SmsConversionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SmsConversionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SmsConversionResponse(),
            await self.do_rpcrequest_async('SmsConversion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sms_conversion(
        self,
        request: dysmsapi_20180501_models.SmsConversionRequest,
    ) -> dysmsapi_20180501_models.SmsConversionResponse:
        runtime = util_models.RuntimeOptions()
        return self.sms_conversion_with_options(request, runtime)

    async def sms_conversion_async(
        self,
        request: dysmsapi_20180501_models.SmsConversionRequest,
    ) -> dysmsapi_20180501_models.SmsConversionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sms_conversion_with_options_async(request, runtime)

    def send_message_to_globe_with_options(
        self,
        request: dysmsapi_20180501_models.SendMessageToGlobeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SendMessageToGlobeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SendMessageToGlobeResponse(),
            self.do_rpcrequest('SendMessageToGlobe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_message_to_globe_with_options_async(
        self,
        request: dysmsapi_20180501_models.SendMessageToGlobeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SendMessageToGlobeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SendMessageToGlobeResponse(),
            await self.do_rpcrequest_async('SendMessageToGlobe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message_to_globe(
        self,
        request: dysmsapi_20180501_models.SendMessageToGlobeRequest,
    ) -> dysmsapi_20180501_models.SendMessageToGlobeResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_to_globe_with_options(request, runtime)

    async def send_message_to_globe_async(
        self,
        request: dysmsapi_20180501_models.SendMessageToGlobeRequest,
    ) -> dysmsapi_20180501_models.SendMessageToGlobeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_to_globe_with_options_async(request, runtime)

    def conversion_data_with_options(
        self,
        request: dysmsapi_20180501_models.ConversionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.ConversionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.ConversionDataResponse(),
            self.do_rpcrequest('ConversionData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def conversion_data_with_options_async(
        self,
        request: dysmsapi_20180501_models.ConversionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.ConversionDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.ConversionDataResponse(),
            await self.do_rpcrequest_async('ConversionData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def conversion_data(
        self,
        request: dysmsapi_20180501_models.ConversionDataRequest,
    ) -> dysmsapi_20180501_models.ConversionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.conversion_data_with_options(request, runtime)

    async def conversion_data_async(
        self,
        request: dysmsapi_20180501_models.ConversionDataRequest,
    ) -> dysmsapi_20180501_models.ConversionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.conversion_data_with_options_async(request, runtime)

    def send_message_with_template_with_options(
        self,
        request: dysmsapi_20180501_models.SendMessageWithTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SendMessageWithTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SendMessageWithTemplateResponse(),
            self.do_rpcrequest('SendMessageWithTemplate', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_message_with_template_with_options_async(
        self,
        request: dysmsapi_20180501_models.SendMessageWithTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20180501_models.SendMessageWithTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20180501_models.SendMessageWithTemplateResponse(),
            await self.do_rpcrequest_async('SendMessageWithTemplate', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message_with_template(
        self,
        request: dysmsapi_20180501_models.SendMessageWithTemplateRequest,
    ) -> dysmsapi_20180501_models.SendMessageWithTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_template_with_options(request, runtime)

    async def send_message_with_template_async(
        self,
        request: dysmsapi_20180501_models.SendMessageWithTemplateRequest,
    ) -> dysmsapi_20180501_models.SendMessageWithTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_template_with_options_async(request, runtime)

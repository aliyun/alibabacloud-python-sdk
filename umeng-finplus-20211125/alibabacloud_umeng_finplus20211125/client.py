# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_finplus20211125 import models as umeng_finplus_20211125_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('umeng-finplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_message_status_with_options(
        self,
        request: umeng_finplus_20211125_models.GetMessageStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20211125_models.GetMessageStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageStatus',
            version='2021-11-25',
            protocol='HTTPS',
            pathname=f'/sms/message/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211125_models.GetMessageStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_status_with_options_async(
        self,
        request: umeng_finplus_20211125_models.GetMessageStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20211125_models.GetMessageStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageStatus',
            version='2021-11-25',
            protocol='HTTPS',
            pathname=f'/sms/message/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211125_models.GetMessageStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_status(
        self,
        request: umeng_finplus_20211125_models.GetMessageStatusRequest,
    ) -> umeng_finplus_20211125_models.GetMessageStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_status_with_options(request, headers, runtime)

    async def get_message_status_async(
        self,
        request: umeng_finplus_20211125_models.GetMessageStatusRequest,
    ) -> umeng_finplus_20211125_models.GetMessageStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_message_status_with_options_async(request, headers, runtime)

    def send_batch_message_with_options(
        self,
        request: umeng_finplus_20211125_models.SendBatchMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20211125_models.SendBatchMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_flag):
            body['BatchFlag'] = request.batch_flag
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.id_type):
            body['IdType'] = request.id_type
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.specific_channel):
            body['SpecificChannel'] = request.specific_channel
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchMessage',
            version='2021-11-25',
            protocol='HTTPS',
            pathname=f'/sms/message/send',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211125_models.SendBatchMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_message_with_options_async(
        self,
        request: umeng_finplus_20211125_models.SendBatchMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_finplus_20211125_models.SendBatchMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_flag):
            body['BatchFlag'] = request.batch_flag
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.id_type):
            body['IdType'] = request.id_type
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.specific_channel):
            body['SpecificChannel'] = request.specific_channel
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchMessage',
            version='2021-11-25',
            protocol='HTTPS',
            pathname=f'/sms/message/send',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211125_models.SendBatchMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_message(
        self,
        request: umeng_finplus_20211125_models.SendBatchMessageRequest,
    ) -> umeng_finplus_20211125_models.SendBatchMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_batch_message_with_options(request, headers, runtime)

    async def send_batch_message_async(
        self,
        request: umeng_finplus_20211125_models.SendBatchMessageRequest,
    ) -> umeng_finplus_20211125_models.SendBatchMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_batch_message_with_options_async(request, headers, runtime)

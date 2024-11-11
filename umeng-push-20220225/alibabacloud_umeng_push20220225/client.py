# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_push20220225 import models as umeng_push_20220225_models
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
        self._endpoint = self.get_endpoint('umeng-push', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_by_msg_id_with_options(
        self,
        request: umeng_push_20220225_models.CancelByMsgIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.CancelByMsgIdResponse:
        """
        @summary 根据消息ID取消发送
        
        @param request: CancelByMsgIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelByMsgIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelByMsgId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/CancelByMsgId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.CancelByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_by_msg_id_with_options_async(
        self,
        request: umeng_push_20220225_models.CancelByMsgIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.CancelByMsgIdResponse:
        """
        @summary 根据消息ID取消发送
        
        @param request: CancelByMsgIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelByMsgIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelByMsgId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/CancelByMsgId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.CancelByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_by_msg_id(
        self,
        request: umeng_push_20220225_models.CancelByMsgIdRequest,
    ) -> umeng_push_20220225_models.CancelByMsgIdResponse:
        """
        @summary 根据消息ID取消发送
        
        @param request: CancelByMsgIdRequest
        @return: CancelByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_by_msg_id_with_options(request, headers, runtime)

    async def cancel_by_msg_id_async(
        self,
        request: umeng_push_20220225_models.CancelByMsgIdRequest,
    ) -> umeng_push_20220225_models.CancelByMsgIdResponse:
        """
        @summary 根据消息ID取消发送
        
        @param request: CancelByMsgIdRequest
        @return: CancelByMsgIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_by_msg_id_with_options_async(request, headers, runtime)

    def query_msg_stat_with_options(
        self,
        request: umeng_push_20220225_models.QueryMsgStatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.QueryMsgStatResponse:
        """
        @summary 消息状态查询
        
        @param request: QueryMsgStatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMsgStatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMsgStat',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/QueryMsgStat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.QueryMsgStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_msg_stat_with_options_async(
        self,
        request: umeng_push_20220225_models.QueryMsgStatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.QueryMsgStatResponse:
        """
        @summary 消息状态查询
        
        @param request: QueryMsgStatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMsgStatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMsgStat',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/QueryMsgStat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.QueryMsgStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_msg_stat(
        self,
        request: umeng_push_20220225_models.QueryMsgStatRequest,
    ) -> umeng_push_20220225_models.QueryMsgStatResponse:
        """
        @summary 消息状态查询
        
        @param request: QueryMsgStatRequest
        @return: QueryMsgStatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_msg_stat_with_options(request, headers, runtime)

    async def query_msg_stat_async(
        self,
        request: umeng_push_20220225_models.QueryMsgStatRequest,
    ) -> umeng_push_20220225_models.QueryMsgStatResponse:
        """
        @summary 消息状态查询
        
        @param request: QueryMsgStatRequest
        @return: QueryMsgStatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_msg_stat_with_options_async(request, headers, runtime)

    def send_by_alias_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAliasResponse:
        """
        @summary 指定别名发送
        
        @param tmp_req: SendByAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.alias_type):
            body['AliasType'] = request.alias_type
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByAlias',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByAlias',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_alias_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAliasResponse:
        """
        @summary 指定别名发送
        
        @param tmp_req: SendByAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAliasResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAliasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.alias_type):
            body['AliasType'] = request.alias_type
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByAlias',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByAlias',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_alias(
        self,
        request: umeng_push_20220225_models.SendByAliasRequest,
    ) -> umeng_push_20220225_models.SendByAliasResponse:
        """
        @summary 指定别名发送
        
        @param request: SendByAliasRequest
        @return: SendByAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_alias_with_options(request, headers, runtime)

    async def send_by_alias_async(
        self,
        request: umeng_push_20220225_models.SendByAliasRequest,
    ) -> umeng_push_20220225_models.SendByAliasResponse:
        """
        @summary 指定别名发送
        
        @param request: SendByAliasRequest
        @return: SendByAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_alias_with_options_async(request, headers, runtime)

    def send_by_alias_file_id_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByAliasFileIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAliasFileIdResponse:
        """
        @summary 指定别名文件发送
        
        @param tmp_req: SendByAliasFileIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAliasFileIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAliasFileIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.alias_type):
            body['AliasType'] = request.alias_type
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByAliasFileId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByAliasFileId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAliasFileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_alias_file_id_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByAliasFileIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAliasFileIdResponse:
        """
        @summary 指定别名文件发送
        
        @param tmp_req: SendByAliasFileIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAliasFileIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAliasFileIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.alias_type):
            body['AliasType'] = request.alias_type
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByAliasFileId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByAliasFileId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAliasFileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_alias_file_id(
        self,
        request: umeng_push_20220225_models.SendByAliasFileIdRequest,
    ) -> umeng_push_20220225_models.SendByAliasFileIdResponse:
        """
        @summary 指定别名文件发送
        
        @param request: SendByAliasFileIdRequest
        @return: SendByAliasFileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_alias_file_id_with_options(request, headers, runtime)

    async def send_by_alias_file_id_async(
        self,
        request: umeng_push_20220225_models.SendByAliasFileIdRequest,
    ) -> umeng_push_20220225_models.SendByAliasFileIdResponse:
        """
        @summary 指定别名文件发送
        
        @param request: SendByAliasFileIdRequest
        @return: SendByAliasFileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_alias_file_id_with_options_async(request, headers, runtime)

    def send_by_app_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAppResponse:
        """
        @summary 广播
        
        @param tmp_req: SendByAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByApp',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_app_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByAppResponse:
        """
        @summary 广播
        
        @param tmp_req: SendByAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByApp',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_app(
        self,
        request: umeng_push_20220225_models.SendByAppRequest,
    ) -> umeng_push_20220225_models.SendByAppResponse:
        """
        @summary 广播
        
        @param request: SendByAppRequest
        @return: SendByAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_app_with_options(request, headers, runtime)

    async def send_by_app_async(
        self,
        request: umeng_push_20220225_models.SendByAppRequest,
    ) -> umeng_push_20220225_models.SendByAppResponse:
        """
        @summary 广播
        
        @param request: SendByAppRequest
        @return: SendByAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_app_with_options_async(request, headers, runtime)

    def send_by_device_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByDeviceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByDeviceResponse:
        """
        @summary 指定设备发送
        
        @param tmp_req: SendByDeviceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByDevice',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_device_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByDeviceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByDeviceResponse:
        """
        @summary 指定设备发送
        
        @param tmp_req: SendByDeviceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByDeviceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByDevice',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_device(
        self,
        request: umeng_push_20220225_models.SendByDeviceRequest,
    ) -> umeng_push_20220225_models.SendByDeviceResponse:
        """
        @summary 指定设备发送
        
        @param request: SendByDeviceRequest
        @return: SendByDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_device_with_options(request, headers, runtime)

    async def send_by_device_async(
        self,
        request: umeng_push_20220225_models.SendByDeviceRequest,
    ) -> umeng_push_20220225_models.SendByDeviceResponse:
        """
        @summary 指定设备发送
        
        @param request: SendByDeviceRequest
        @return: SendByDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_device_with_options_async(request, headers, runtime)

    def send_by_device_file_id_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByDeviceFileIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByDeviceFileIdResponse:
        """
        @summary 指定设备文件发送
        
        @param tmp_req: SendByDeviceFileIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByDeviceFileIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByDeviceFileIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByDeviceFileId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByDeviceFileId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByDeviceFileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_device_file_id_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByDeviceFileIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByDeviceFileIdResponse:
        """
        @summary 指定设备文件发送
        
        @param tmp_req: SendByDeviceFileIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByDeviceFileIdResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByDeviceFileIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.android_short_payload):
            request.android_short_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            body['FileId'] = request.file_id
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByDeviceFileId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByDeviceFileId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByDeviceFileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_device_file_id(
        self,
        request: umeng_push_20220225_models.SendByDeviceFileIdRequest,
    ) -> umeng_push_20220225_models.SendByDeviceFileIdResponse:
        """
        @summary 指定设备文件发送
        
        @param request: SendByDeviceFileIdRequest
        @return: SendByDeviceFileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_device_file_id_with_options(request, headers, runtime)

    async def send_by_device_file_id_async(
        self,
        request: umeng_push_20220225_models.SendByDeviceFileIdRequest,
    ) -> umeng_push_20220225_models.SendByDeviceFileIdResponse:
        """
        @summary 指定设备文件发送
        
        @param request: SendByDeviceFileIdRequest
        @return: SendByDeviceFileIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_device_file_id_with_options_async(request, headers, runtime)

    def send_by_filter_with_options(
        self,
        tmp_req: umeng_push_20220225_models.SendByFilterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByFilterResponse:
        """
        @summary 根据筛选条件发送
        
        @param tmp_req: SendByFilterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByFilterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByFilterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload):
            body['AndroidShortPayload'] = request.android_short_payload
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByFilter',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByFilter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_filter_with_options_async(
        self,
        tmp_req: umeng_push_20220225_models.SendByFilterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.SendByFilterResponse:
        """
        @summary 根据筛选条件发送
        
        @param tmp_req: SendByFilterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendByFilterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = umeng_push_20220225_models.SendByFilterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.android_payload):
            request.android_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not UtilClient.is_unset(tmp_req.channel_properties):
            request.channel_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not UtilClient.is_unset(tmp_req.ios_payload):
            request.ios_payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not UtilClient.is_unset(request.android_short_payload):
            body['AndroidShortPayload'] = request.android_short_payload
        if not UtilClient.is_unset(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not UtilClient.is_unset(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not UtilClient.is_unset(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not UtilClient.is_unset(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not UtilClient.is_unset(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not UtilClient.is_unset(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendByFilter',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/SendByFilter',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.SendByFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_filter(
        self,
        request: umeng_push_20220225_models.SendByFilterRequest,
    ) -> umeng_push_20220225_models.SendByFilterResponse:
        """
        @summary 根据筛选条件发送
        
        @param request: SendByFilterRequest
        @return: SendByFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_by_filter_with_options(request, headers, runtime)

    async def send_by_filter_async(
        self,
        request: umeng_push_20220225_models.SendByFilterRequest,
    ) -> umeng_push_20220225_models.SendByFilterResponse:
        """
        @summary 根据筛选条件发送
        
        @param request: SendByFilterRequest
        @return: SendByFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_by_filter_with_options_async(request, headers, runtime)

    def upload_device_with_options(
        self,
        request: umeng_push_20220225_models.UploadDeviceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.UploadDeviceResponse:
        """
        @summary 上传设备列表创建设备文件
        
        @param request: UploadDeviceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDevice',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/UploadDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.UploadDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_device_with_options_async(
        self,
        request: umeng_push_20220225_models.UploadDeviceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_push_20220225_models.UploadDeviceResponse:
        """
        @summary 上传设备列表创建设备文件
        
        @param request: UploadDeviceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDevice',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/UploadDevice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_push_20220225_models.UploadDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_device(
        self,
        request: umeng_push_20220225_models.UploadDeviceRequest,
    ) -> umeng_push_20220225_models.UploadDeviceResponse:
        """
        @summary 上传设备列表创建设备文件
        
        @param request: UploadDeviceRequest
        @return: UploadDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_device_with_options(request, headers, runtime)

    async def upload_device_async(
        self,
        request: umeng_push_20220225_models.UploadDeviceRequest,
    ) -> umeng_push_20220225_models.UploadDeviceResponse:
        """
        @summary 上传设备列表创建设备文件
        
        @param request: UploadDeviceRequest
        @return: UploadDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_device_with_options_async(request, headers, runtime)

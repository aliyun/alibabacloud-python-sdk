# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_by_msg_id_with_options(
        self,
        request: main_models.CancelByMsgIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelByMsgIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelByMsgId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/CancelByMsgId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_by_msg_id_with_options_async(
        self,
        request: main_models.CancelByMsgIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelByMsgIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelByMsgId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/CancelByMsgId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_by_msg_id(
        self,
        request: main_models.CancelByMsgIdRequest,
    ) -> main_models.CancelByMsgIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_by_msg_id_with_options(request, headers, runtime)

    async def cancel_by_msg_id_async(
        self,
        request: main_models.CancelByMsgIdRequest,
    ) -> main_models.CancelByMsgIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_by_msg_id_with_options_async(request, headers, runtime)

    def query_msg_stat_with_options(
        self,
        request: main_models.QueryMsgStatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMsgStatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMsgStat',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/QueryMsgStat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMsgStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_msg_stat_with_options_async(
        self,
        request: main_models.QueryMsgStatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMsgStatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.msg_id):
            body['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryMsgStat',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/QueryMsgStat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMsgStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_msg_stat(
        self,
        request: main_models.QueryMsgStatRequest,
    ) -> main_models.QueryMsgStatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_msg_stat_with_options(request, headers, runtime)

    async def query_msg_stat_async(
        self,
        request: main_models.QueryMsgStatRequest,
    ) -> main_models.QueryMsgStatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_msg_stat_with_options_async(request, headers, runtime)

    def send_by_alias_with_options(
        self,
        tmp_req: main_models.SendByAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAliasResponse:
        tmp_req.validate()
        request = main_models.SendByAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.alias_type):
            body['AliasType'] = request.alias_type
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByAlias',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByAlias',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_alias_with_options_async(
        self,
        tmp_req: main_models.SendByAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAliasResponse:
        tmp_req.validate()
        request = main_models.SendByAliasShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.alias_type):
            body['AliasType'] = request.alias_type
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByAlias',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByAlias',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_alias(
        self,
        request: main_models.SendByAliasRequest,
    ) -> main_models.SendByAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_alias_with_options(request, headers, runtime)

    async def send_by_alias_async(
        self,
        request: main_models.SendByAliasRequest,
    ) -> main_models.SendByAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_alias_with_options_async(request, headers, runtime)

    def send_by_alias_file_id_with_options(
        self,
        tmp_req: main_models.SendByAliasFileIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAliasFileIdResponse:
        tmp_req.validate()
        request = main_models.SendByAliasFileIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.alias_type):
            body['AliasType'] = request.alias_type
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByAliasFileId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByAliasFileId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAliasFileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_alias_file_id_with_options_async(
        self,
        tmp_req: main_models.SendByAliasFileIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAliasFileIdResponse:
        tmp_req.validate()
        request = main_models.SendByAliasFileIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.alias_type):
            body['AliasType'] = request.alias_type
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByAliasFileId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByAliasFileId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAliasFileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_alias_file_id(
        self,
        request: main_models.SendByAliasFileIdRequest,
    ) -> main_models.SendByAliasFileIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_alias_file_id_with_options(request, headers, runtime)

    async def send_by_alias_file_id_async(
        self,
        request: main_models.SendByAliasFileIdRequest,
    ) -> main_models.SendByAliasFileIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_alias_file_id_with_options_async(request, headers, runtime)

    def send_by_app_with_options(
        self,
        tmp_req: main_models.SendByAppRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAppResponse:
        tmp_req.validate()
        request = main_models.SendByAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByApp',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByApp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_app_with_options_async(
        self,
        tmp_req: main_models.SendByAppRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByAppResponse:
        tmp_req.validate()
        request = main_models.SendByAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByApp',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByApp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_app(
        self,
        request: main_models.SendByAppRequest,
    ) -> main_models.SendByAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_app_with_options(request, headers, runtime)

    async def send_by_app_async(
        self,
        request: main_models.SendByAppRequest,
    ) -> main_models.SendByAppResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_app_with_options_async(request, headers, runtime)

    def send_by_device_with_options(
        self,
        tmp_req: main_models.SendByDeviceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByDeviceResponse:
        tmp_req.validate()
        request = main_models.SendByDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByDevice',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_device_with_options_async(
        self,
        tmp_req: main_models.SendByDeviceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByDeviceResponse:
        tmp_req.validate()
        request = main_models.SendByDeviceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByDevice',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_device(
        self,
        request: main_models.SendByDeviceRequest,
    ) -> main_models.SendByDeviceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_device_with_options(request, headers, runtime)

    async def send_by_device_async(
        self,
        request: main_models.SendByDeviceRequest,
    ) -> main_models.SendByDeviceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_device_with_options_async(request, headers, runtime)

    def send_by_device_file_id_with_options(
        self,
        tmp_req: main_models.SendByDeviceFileIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByDeviceFileIdResponse:
        tmp_req.validate()
        request = main_models.SendByDeviceFileIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByDeviceFileId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByDeviceFileId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByDeviceFileIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_device_file_id_with_options_async(
        self,
        tmp_req: main_models.SendByDeviceFileIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByDeviceFileIdResponse:
        tmp_req.validate()
        request = main_models.SendByDeviceFileIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.android_short_payload):
            request.android_short_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_short_payload, 'AndroidShortPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload_shrink):
            body['AndroidShortPayload'] = request.android_short_payload_shrink
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByDeviceFileId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByDeviceFileId',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByDeviceFileIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_device_file_id(
        self,
        request: main_models.SendByDeviceFileIdRequest,
    ) -> main_models.SendByDeviceFileIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_device_file_id_with_options(request, headers, runtime)

    async def send_by_device_file_id_async(
        self,
        request: main_models.SendByDeviceFileIdRequest,
    ) -> main_models.SendByDeviceFileIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_device_file_id_with_options_async(request, headers, runtime)

    def send_by_filter_with_options(
        self,
        tmp_req: main_models.SendByFilterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByFilterResponse:
        tmp_req.validate()
        request = main_models.SendByFilterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload):
            body['AndroidShortPayload'] = request.android_short_payload
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByFilter',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByFilter',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_filter_with_options_async(
        self,
        tmp_req: main_models.SendByFilterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendByFilterResponse:
        tmp_req.validate()
        request = main_models.SendByFilterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.android_payload):
            request.android_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.android_payload, 'AndroidPayload', 'json')
        if not DaraCore.is_null(tmp_req.channel_properties):
            request.channel_properties_shrink = Utils.array_to_string_with_specified_style(tmp_req.channel_properties, 'ChannelProperties', 'json')
        if not DaraCore.is_null(tmp_req.harmony_payload):
            request.harmony_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.harmony_payload, 'HarmonyPayload', 'json')
        if not DaraCore.is_null(tmp_req.ios_payload):
            request.ios_payload_shrink = Utils.array_to_string_with_specified_style(tmp_req.ios_payload, 'IosPayload', 'json')
        if not DaraCore.is_null(tmp_req.policy):
            request.policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        body = {}
        if not DaraCore.is_null(request.android_payload_shrink):
            body['AndroidPayload'] = request.android_payload_shrink
        if not DaraCore.is_null(request.android_short_payload):
            body['AndroidShortPayload'] = request.android_short_payload
        if not DaraCore.is_null(request.channel_properties_shrink):
            body['ChannelProperties'] = request.channel_properties_shrink
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.harmony_payload_shrink):
            body['HarmonyPayload'] = request.harmony_payload_shrink
        if not DaraCore.is_null(request.ios_payload_shrink):
            body['IosPayload'] = request.ios_payload_shrink
        if not DaraCore.is_null(request.policy_shrink):
            body['Policy'] = request.policy_shrink
        if not DaraCore.is_null(request.production_mode):
            body['ProductionMode'] = request.production_mode
        if not DaraCore.is_null(request.receipt_type):
            body['ReceiptType'] = request.receipt_type
        if not DaraCore.is_null(request.receipt_url):
            body['ReceiptUrl'] = request.receipt_url
        if not DaraCore.is_null(request.third_party_id):
            body['ThirdPartyId'] = request.third_party_id
        if not DaraCore.is_null(request.callback_params):
            body['callbackParams'] = request.callback_params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendByFilter',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/SendByFilter',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendByFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_filter(
        self,
        request: main_models.SendByFilterRequest,
    ) -> main_models.SendByFilterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_by_filter_with_options(request, headers, runtime)

    async def send_by_filter_async(
        self,
        request: main_models.SendByFilterRequest,
    ) -> main_models.SendByFilterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_by_filter_with_options_async(request, headers, runtime)

    def upload_device_with_options(
        self,
        request: main_models.UploadDeviceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDeviceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDevice',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/UploadDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_device_with_options_async(
        self,
        request: main_models.UploadDeviceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UploadDeviceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_tokens):
            body['DeviceTokens'] = request.device_tokens
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDevice',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/UploadDevice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_device(
        self,
        request: main_models.UploadDeviceRequest,
    ) -> main_models.UploadDeviceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upload_device_with_options(request, headers, runtime)

    async def upload_device_async(
        self,
        request: main_models.UploadDeviceRequest,
    ) -> main_models.UploadDeviceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upload_device_with_options_async(request, headers, runtime)

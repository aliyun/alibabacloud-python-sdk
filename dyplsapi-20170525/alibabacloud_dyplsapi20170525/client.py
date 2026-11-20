# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dyplsapi20170525 import models as main_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        self._product_id = 'Dyplsapi'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dyplsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_axn_track_no_with_options(
        self,
        request: main_models.AddAxnTrackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAxnTrackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAxnTrackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAxnTrackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_axn_track_no_with_options_async(
        self,
        request: main_models.AddAxnTrackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAxnTrackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAxnTrackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAxnTrackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_axn_track_no(
        self,
        request: main_models.AddAxnTrackNoRequest,
    ) -> main_models.AddAxnTrackNoResponse:
        runtime = RuntimeOptions()
        return self.add_axn_track_no_with_options(request, runtime)

    async def add_axn_track_no_async(
        self,
        request: main_models.AddAxnTrackNoRequest,
    ) -> main_models.AddAxnTrackNoResponse:
        runtime = RuntimeOptions()
        return await self.add_axn_track_no_with_options_async(request, runtime)

    def add_secret_blacklist_with_options(
        self,
        request: main_models.AddSecretBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSecretBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.black_type):
            query['BlackType'] = request.black_type
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSecretBlacklist',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSecretBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_secret_blacklist_with_options_async(
        self,
        request: main_models.AddSecretBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSecretBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.black_type):
            query['BlackType'] = request.black_type
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSecretBlacklist',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSecretBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_secret_blacklist(
        self,
        request: main_models.AddSecretBlacklistRequest,
    ) -> main_models.AddSecretBlacklistResponse:
        runtime = RuntimeOptions()
        return self.add_secret_blacklist_with_options(request, runtime)

    async def add_secret_blacklist_async(
        self,
        request: main_models.AddSecretBlacklistRequest,
    ) -> main_models.AddSecretBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.add_secret_blacklist_with_options_async(request, runtime)

    def bind_axbcall_with_options(
        self,
        request: main_models.BindAXBCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAXBCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAXBCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAXBCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axbcall_with_options_async(
        self,
        request: main_models.BindAXBCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAXBCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAXBCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAXBCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axbcall(
        self,
        request: main_models.BindAXBCallRequest,
    ) -> main_models.BindAXBCallResponse:
        runtime = RuntimeOptions()
        return self.bind_axbcall_with_options(request, runtime)

    async def bind_axbcall_async(
        self,
        request: main_models.BindAXBCallRequest,
    ) -> main_models.BindAXBCallResponse:
        runtime = RuntimeOptions()
        return await self.bind_axbcall_with_options_async(request, runtime)

    def bind_axb_with_options(
        self,
        request: main_models.BindAxbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxb',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axb_with_options_async(
        self,
        request: main_models.BindAxbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxb',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axb(
        self,
        request: main_models.BindAxbRequest,
    ) -> main_models.BindAxbResponse:
        runtime = RuntimeOptions()
        return self.bind_axb_with_options(request, runtime)

    async def bind_axb_async(
        self,
        request: main_models.BindAxbRequest,
    ) -> main_models.BindAxbResponse:
        runtime = RuntimeOptions()
        return await self.bind_axb_with_options_async(request, runtime)

    def bind_axb_700with_options(
        self,
        request: main_models.BindAxb700Request,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxb700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.rec_type):
            query['RecType'] = request.rec_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxb700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxb700Response(),
            self.call_api(params, req, runtime)
        )

    async def bind_axb_700with_options_async(
        self,
        request: main_models.BindAxb700Request,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxb700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.rec_type):
            query['RecType'] = request.rec_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxb700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxb700Response(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axb_700(
        self,
        request: main_models.BindAxb700Request,
    ) -> main_models.BindAxb700Response:
        runtime = RuntimeOptions()
        return self.bind_axb_700with_options(request, runtime)

    async def bind_axb_700_async(
        self,
        request: main_models.BindAxb700Request,
    ) -> main_models.BindAxb700Response:
        runtime = RuntimeOptions()
        return await self.bind_axb_700with_options_async(request, runtime)

    def bind_axb_fixed_line_with_options(
        self,
        tmp_req: main_models.BindAxbFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxbFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxbFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxbFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxbFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axb_fixed_line_with_options_async(
        self,
        tmp_req: main_models.BindAxbFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxbFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxbFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxbFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxbFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axb_fixed_line(
        self,
        request: main_models.BindAxbFixedLineRequest,
    ) -> main_models.BindAxbFixedLineResponse:
        runtime = RuntimeOptions()
        return self.bind_axb_fixed_line_with_options(request, runtime)

    async def bind_axb_fixed_line_async(
        self,
        request: main_models.BindAxbFixedLineRequest,
    ) -> main_models.BindAxbFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.bind_axb_fixed_line_with_options_async(request, runtime)

    def bind_axg_with_options(
        self,
        request: main_models.BindAxgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxg',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxgResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axg_with_options_async(
        self,
        request: main_models.BindAxgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxg',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axg(
        self,
        request: main_models.BindAxgRequest,
    ) -> main_models.BindAxgResponse:
        runtime = RuntimeOptions()
        return self.bind_axg_with_options(request, runtime)

    async def bind_axg_async(
        self,
        request: main_models.BindAxgRequest,
    ) -> main_models.BindAxgResponse:
        runtime = RuntimeOptions()
        return await self.bind_axg_with_options_async(request, runtime)

    def bind_axn_with_options(
        self,
        request: main_models.BindAxnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.no_type):
            query['NoType'] = request.no_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxn',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_with_options_async(
        self,
        request: main_models.BindAxnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.no_type):
            query['NoType'] = request.no_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxn',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn(
        self,
        request: main_models.BindAxnRequest,
    ) -> main_models.BindAxnResponse:
        runtime = RuntimeOptions()
        return self.bind_axn_with_options(request, runtime)

    async def bind_axn_async(
        self,
        request: main_models.BindAxnRequest,
    ) -> main_models.BindAxnResponse:
        runtime = RuntimeOptions()
        return await self.bind_axn_with_options_async(request, runtime)

    def bind_axn_extension_with_options(
        self,
        request: main_models.BindAxnExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnExtension',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_extension_with_options_async(
        self,
        request: main_models.BindAxnExtensionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnExtensionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.extension):
            query['Extension'] = request.extension
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnExtension',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn_extension(
        self,
        request: main_models.BindAxnExtensionRequest,
    ) -> main_models.BindAxnExtensionResponse:
        runtime = RuntimeOptions()
        return self.bind_axn_extension_with_options(request, runtime)

    async def bind_axn_extension_async(
        self,
        request: main_models.BindAxnExtensionRequest,
    ) -> main_models.BindAxnExtensionResponse:
        runtime = RuntimeOptions()
        return await self.bind_axn_extension_with_options_async(request, runtime)

    def bind_axn_extension_fixed_line_with_options(
        self,
        tmp_req: main_models.BindAxnExtensionFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnExtensionFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxnExtensionFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extraaxx):
            request.extraaxx_shrink = Utils.array_to_string_with_specified_style(tmp_req.extraaxx, 'Extraaxx', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extraaxx_shrink):
            query['Extraaxx'] = request.extraaxx_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.tel_xext):
            query['TelXext'] = request.tel_xext
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnExtensionFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnExtensionFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_extension_fixed_line_with_options_async(
        self,
        tmp_req: main_models.BindAxnExtensionFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnExtensionFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxnExtensionFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extraaxx):
            request.extraaxx_shrink = Utils.array_to_string_with_specified_style(tmp_req.extraaxx, 'Extraaxx', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extraaxx_shrink):
            query['Extraaxx'] = request.extraaxx_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.tel_xext):
            query['TelXext'] = request.tel_xext
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnExtensionFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnExtensionFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn_extension_fixed_line(
        self,
        request: main_models.BindAxnExtensionFixedLineRequest,
    ) -> main_models.BindAxnExtensionFixedLineResponse:
        runtime = RuntimeOptions()
        return self.bind_axn_extension_fixed_line_with_options(request, runtime)

    async def bind_axn_extension_fixed_line_async(
        self,
        request: main_models.BindAxnExtensionFixedLineRequest,
    ) -> main_models.BindAxnExtensionFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.bind_axn_extension_fixed_line_with_options_async(request, runtime)

    def bind_axn_fixed_line_with_options(
        self,
        tmp_req: main_models.BindAxnFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxnFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_fixed_line_with_options_async(
        self,
        tmp_req: main_models.BindAxnFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAxnFixedLineResponse:
        tmp_req.validate()
        request = main_models.BindAxnFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.areacode):
            query['Areacode'] = request.areacode
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAxnFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAxnFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn_fixed_line(
        self,
        request: main_models.BindAxnFixedLineRequest,
    ) -> main_models.BindAxnFixedLineResponse:
        runtime = RuntimeOptions()
        return self.bind_axn_fixed_line_with_options(request, runtime)

    async def bind_axn_fixed_line_async(
        self,
        request: main_models.BindAxnFixedLineRequest,
    ) -> main_models.BindAxnFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.bind_axn_fixed_line_with_options_async(request, runtime)

    def bind_batch_axg_with_options(
        self,
        tmp_req: main_models.BindBatchAxgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindBatchAxgResponse:
        tmp_req.validate()
        request = main_models.BindBatchAxgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.axg_bind_list):
            request.axg_bind_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.axg_bind_list, 'AxgBindList', 'json')
        query = {}
        if not DaraCore.is_null(request.axg_bind_list_shrink):
            query['AxgBindList'] = request.axg_bind_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindBatchAxg',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindBatchAxgResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_batch_axg_with_options_async(
        self,
        tmp_req: main_models.BindBatchAxgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindBatchAxgResponse:
        tmp_req.validate()
        request = main_models.BindBatchAxgShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.axg_bind_list):
            request.axg_bind_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.axg_bind_list, 'AxgBindList', 'json')
        query = {}
        if not DaraCore.is_null(request.axg_bind_list_shrink):
            query['AxgBindList'] = request.axg_bind_list_shrink
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindBatchAxg',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindBatchAxgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_batch_axg(
        self,
        request: main_models.BindBatchAxgRequest,
    ) -> main_models.BindBatchAxgResponse:
        runtime = RuntimeOptions()
        return self.bind_batch_axg_with_options(request, runtime)

    async def bind_batch_axg_async(
        self,
        request: main_models.BindBatchAxgRequest,
    ) -> main_models.BindBatchAxgResponse:
        runtime = RuntimeOptions()
        return await self.bind_batch_axg_with_options_async(request, runtime)

    def bind_gxb_700with_options(
        self,
        request: main_models.BindGxb700Request,
        runtime: RuntimeOptions,
    ) -> main_models.BindGxb700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.default_a):
            query['DefaultA'] = request.default_a
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.rec_type):
            query['RecType'] = request.rec_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindGxb700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindGxb700Response(),
            self.call_api(params, req, runtime)
        )

    async def bind_gxb_700with_options_async(
        self,
        request: main_models.BindGxb700Request,
        runtime: RuntimeOptions,
    ) -> main_models.BindGxb700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not DaraCore.is_null(request.default_a):
            query['DefaultA'] = request.default_a
        if not DaraCore.is_null(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.rec_type):
            query['RecType'] = request.rec_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindGxb700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindGxb700Response(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_gxb_700(
        self,
        request: main_models.BindGxb700Request,
    ) -> main_models.BindGxb700Response:
        runtime = RuntimeOptions()
        return self.bind_gxb_700with_options(request, runtime)

    async def bind_gxb_700_async(
        self,
        request: main_models.BindGxb700Request,
    ) -> main_models.BindGxb700Response:
        runtime = RuntimeOptions()
        return await self.bind_gxb_700with_options_async(request, runtime)

    def bind_xbwith_options(
        self,
        request: main_models.BindXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_xbwith_options_async(
        self,
        request: main_models.BindXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_xb(
        self,
        request: main_models.BindXBRequest,
    ) -> main_models.BindXBResponse:
        runtime = RuntimeOptions()
        return self.bind_xbwith_options(request, runtime)

    async def bind_xb_async(
        self,
        request: main_models.BindXBRequest,
    ) -> main_models.BindXBResponse:
        runtime = RuntimeOptions()
        return await self.bind_xbwith_options_async(request, runtime)

    def buy_secret_no_with_options(
        self,
        request: main_models.BuySecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BuySecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.display_pool):
            query['DisplayPool'] = request.display_pool
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BuySecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuySecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def buy_secret_no_with_options_async(
        self,
        request: main_models.BuySecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BuySecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.display_pool):
            query['DisplayPool'] = request.display_pool
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BuySecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuySecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def buy_secret_no(
        self,
        request: main_models.BuySecretNoRequest,
    ) -> main_models.BuySecretNoResponse:
        runtime = RuntimeOptions()
        return self.buy_secret_no_with_options(request, runtime)

    async def buy_secret_no_async(
        self,
        request: main_models.BuySecretNoRequest,
    ) -> main_models.BuySecretNoResponse:
        runtime = RuntimeOptions()
        return await self.buy_secret_no_with_options_async(request, runtime)

    def cancel_pick_up_waybill_with_options(
        self,
        request: main_models.CancelPickUpWaybillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPickUpWaybillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cancel_desc):
            query['CancelDesc'] = request.cancel_desc
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPickUpWaybill',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPickUpWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_pick_up_waybill_with_options_async(
        self,
        request: main_models.CancelPickUpWaybillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelPickUpWaybillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cancel_desc):
            query['CancelDesc'] = request.cancel_desc
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelPickUpWaybill',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelPickUpWaybillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_pick_up_waybill(
        self,
        request: main_models.CancelPickUpWaybillRequest,
    ) -> main_models.CancelPickUpWaybillResponse:
        runtime = RuntimeOptions()
        return self.cancel_pick_up_waybill_with_options(request, runtime)

    async def cancel_pick_up_waybill_async(
        self,
        request: main_models.CancelPickUpWaybillRequest,
    ) -> main_models.CancelPickUpWaybillResponse:
        runtime = RuntimeOptions()
        return await self.cancel_pick_up_waybill_with_options_async(request, runtime)

    def config_xwith_options(
        self,
        tmp_req: main_models.ConfigXRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigXResponse:
        tmp_req.validate()
        request = main_models.ConfigXShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sequence_calls):
            request.sequence_calls_shrink = Utils.array_to_string_with_specified_style(tmp_req.sequence_calls, 'SequenceCalls', 'json')
        query = {}
        if not DaraCore.is_null(request.call_ability):
            query['CallAbility'] = request.call_ability
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.gnflag):
            query['GNFlag'] = request.gnflag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sequence_calls_shrink):
            query['SequenceCalls'] = request.sequence_calls_shrink
        if not DaraCore.is_null(request.sequence_mode):
            query['SequenceMode'] = request.sequence_mode
        if not DaraCore.is_null(request.sms_ability):
            query['SmsAbility'] = request.sms_ability
        if not DaraCore.is_null(request.sms_sign_mode):
            query['SmsSignMode'] = request.sms_sign_mode
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigX',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigXResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_xwith_options_async(
        self,
        tmp_req: main_models.ConfigXRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigXResponse:
        tmp_req.validate()
        request = main_models.ConfigXShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sequence_calls):
            request.sequence_calls_shrink = Utils.array_to_string_with_specified_style(tmp_req.sequence_calls, 'SequenceCalls', 'json')
        query = {}
        if not DaraCore.is_null(request.call_ability):
            query['CallAbility'] = request.call_ability
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.gnflag):
            query['GNFlag'] = request.gnflag
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sequence_calls_shrink):
            query['SequenceCalls'] = request.sequence_calls_shrink
        if not DaraCore.is_null(request.sequence_mode):
            query['SequenceMode'] = request.sequence_mode
        if not DaraCore.is_null(request.sms_ability):
            query['SmsAbility'] = request.sms_ability
        if not DaraCore.is_null(request.sms_sign_mode):
            query['SmsSignMode'] = request.sms_sign_mode
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigX',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigXResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_x(
        self,
        request: main_models.ConfigXRequest,
    ) -> main_models.ConfigXResponse:
        runtime = RuntimeOptions()
        return self.config_xwith_options(request, runtime)

    async def config_x_async(
        self,
        request: main_models.ConfigXRequest,
    ) -> main_models.ConfigXResponse:
        runtime = RuntimeOptions()
        return await self.config_xwith_options_async(request, runtime)

    def create_axg_group_with_options(
        self,
        request: main_models.CreateAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.numbers):
            query['Numbers'] = request.numbers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_axg_group_with_options_async(
        self,
        request: main_models.CreateAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.numbers):
            query['Numbers'] = request.numbers
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_axg_group(
        self,
        request: main_models.CreateAxgGroupRequest,
    ) -> main_models.CreateAxgGroupResponse:
        runtime = RuntimeOptions()
        return self.create_axg_group_with_options(request, runtime)

    async def create_axg_group_async(
        self,
        request: main_models.CreateAxgGroupRequest,
    ) -> main_models.CreateAxgGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_axg_group_with_options_async(request, runtime)

    def create_fixed_no_areport_with_options(
        self,
        request: main_models.CreateFixedNoAReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedNoAReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.cust_name):
            query['CustName'] = request.cust_name
        if not DaraCore.is_null(request.cust_phone_no):
            query['CustPhoneNo'] = request.cust_phone_no
        if not DaraCore.is_null(request.cust_type):
            query['CustType'] = request.cust_type
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.document_type):
            query['DocumentType'] = request.document_type
        if not DaraCore.is_null(request.fixed_line_work_id):
            query['FixedLineWorkId'] = request.fixed_line_work_id
        if not DaraCore.is_null(request.fixed_no_a):
            query['FixedNoA'] = request.fixed_no_a
        if not DaraCore.is_null(request.id_card_alive_photo):
            query['IdCardAlivePhoto'] = request.id_card_alive_photo
        if not DaraCore.is_null(request.id_card_back_photo):
            query['IdCardBackPhoto'] = request.id_card_back_photo
        if not DaraCore.is_null(request.id_card_front_photo):
            query['IdCardFrontPhoto'] = request.id_card_front_photo
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedNoAReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedNoAReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fixed_no_areport_with_options_async(
        self,
        request: main_models.CreateFixedNoAReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFixedNoAReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.cust_name):
            query['CustName'] = request.cust_name
        if not DaraCore.is_null(request.cust_phone_no):
            query['CustPhoneNo'] = request.cust_phone_no
        if not DaraCore.is_null(request.cust_type):
            query['CustType'] = request.cust_type
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.document_type):
            query['DocumentType'] = request.document_type
        if not DaraCore.is_null(request.fixed_line_work_id):
            query['FixedLineWorkId'] = request.fixed_line_work_id
        if not DaraCore.is_null(request.fixed_no_a):
            query['FixedNoA'] = request.fixed_no_a
        if not DaraCore.is_null(request.id_card_alive_photo):
            query['IdCardAlivePhoto'] = request.id_card_alive_photo
        if not DaraCore.is_null(request.id_card_back_photo):
            query['IdCardBackPhoto'] = request.id_card_back_photo
        if not DaraCore.is_null(request.id_card_front_photo):
            query['IdCardFrontPhoto'] = request.id_card_front_photo
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFixedNoAReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFixedNoAReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fixed_no_areport(
        self,
        request: main_models.CreateFixedNoAReportRequest,
    ) -> main_models.CreateFixedNoAReportResponse:
        runtime = RuntimeOptions()
        return self.create_fixed_no_areport_with_options(request, runtime)

    async def create_fixed_no_areport_async(
        self,
        request: main_models.CreateFixedNoAReportRequest,
    ) -> main_models.CreateFixedNoAReportResponse:
        runtime = RuntimeOptions()
        return await self.create_fixed_no_areport_with_options_async(request, runtime)

    def create_phone_no_areport_with_options(
        self,
        request: main_models.CreatePhoneNoAReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePhoneNoAReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.cust_name):
            query['CustName'] = request.cust_name
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.document_type):
            query['DocumentType'] = request.document_type
        if not DaraCore.is_null(request.id_card_alive_photo):
            query['IdCardAlivePhoto'] = request.id_card_alive_photo
        if not DaraCore.is_null(request.id_card_back_photo):
            query['IdCardBackPhoto'] = request.id_card_back_photo
        if not DaraCore.is_null(request.id_card_front_photo):
            query['IdCardFrontPhoto'] = request.id_card_front_photo
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePhoneNoAReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePhoneNoAReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_phone_no_areport_with_options_async(
        self,
        request: main_models.CreatePhoneNoAReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePhoneNoAReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.cust_name):
            query['CustName'] = request.cust_name
        if not DaraCore.is_null(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not DaraCore.is_null(request.document_type):
            query['DocumentType'] = request.document_type
        if not DaraCore.is_null(request.id_card_alive_photo):
            query['IdCardAlivePhoto'] = request.id_card_alive_photo
        if not DaraCore.is_null(request.id_card_back_photo):
            query['IdCardBackPhoto'] = request.id_card_back_photo
        if not DaraCore.is_null(request.id_card_front_photo):
            query['IdCardFrontPhoto'] = request.id_card_front_photo
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePhoneNoAReport',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePhoneNoAReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_phone_no_areport(
        self,
        request: main_models.CreatePhoneNoAReportRequest,
    ) -> main_models.CreatePhoneNoAReportResponse:
        runtime = RuntimeOptions()
        return self.create_phone_no_areport_with_options(request, runtime)

    async def create_phone_no_areport_async(
        self,
        request: main_models.CreatePhoneNoAReportRequest,
    ) -> main_models.CreatePhoneNoAReportResponse:
        runtime = RuntimeOptions()
        return await self.create_phone_no_areport_with_options_async(request, runtime)

    def create_pick_up_waybill_with_options(
        self,
        tmp_req: main_models.CreatePickUpWaybillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePickUpWaybillResponse:
        tmp_req.validate()
        request = main_models.CreatePickUpWaybillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.consignee_address):
            request.consignee_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.consignee_address, 'ConsigneeAddress', 'json')
        if not DaraCore.is_null(tmp_req.goods_infos):
            request.goods_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not DaraCore.is_null(tmp_req.send_address):
            request.send_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_address, 'SendAddress', 'json')
        query = {}
        if not DaraCore.is_null(request.appoint_got_end_time):
            query['AppointGotEndTime'] = request.appoint_got_end_time
        if not DaraCore.is_null(request.appoint_got_start_time):
            query['AppointGotStartTime'] = request.appoint_got_start_time
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.consignee_address_shrink):
            query['ConsigneeAddress'] = request.consignee_address_shrink
        if not DaraCore.is_null(request.consignee_mobile):
            query['ConsigneeMobile'] = request.consignee_mobile
        if not DaraCore.is_null(request.consignee_name):
            query['ConsigneeName'] = request.consignee_name
        if not DaraCore.is_null(request.consignee_phone):
            query['ConsigneePhone'] = request.consignee_phone
        if not DaraCore.is_null(request.cp_code):
            query['CpCode'] = request.cp_code
        if not DaraCore.is_null(request.goods_infos_shrink):
            query['GoodsInfos'] = request.goods_infos_shrink
        if not DaraCore.is_null(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.send_address_shrink):
            query['SendAddress'] = request.send_address_shrink
        if not DaraCore.is_null(request.send_mobile):
            query['SendMobile'] = request.send_mobile
        if not DaraCore.is_null(request.send_name):
            query['SendName'] = request.send_name
        if not DaraCore.is_null(request.send_phone):
            query['SendPhone'] = request.send_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePickUpWaybill',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePickUpWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pick_up_waybill_with_options_async(
        self,
        tmp_req: main_models.CreatePickUpWaybillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePickUpWaybillResponse:
        tmp_req.validate()
        request = main_models.CreatePickUpWaybillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.consignee_address):
            request.consignee_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.consignee_address, 'ConsigneeAddress', 'json')
        if not DaraCore.is_null(tmp_req.goods_infos):
            request.goods_infos_shrink = Utils.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not DaraCore.is_null(tmp_req.send_address):
            request.send_address_shrink = Utils.array_to_string_with_specified_style(tmp_req.send_address, 'SendAddress', 'json')
        query = {}
        if not DaraCore.is_null(request.appoint_got_end_time):
            query['AppointGotEndTime'] = request.appoint_got_end_time
        if not DaraCore.is_null(request.appoint_got_start_time):
            query['AppointGotStartTime'] = request.appoint_got_start_time
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.consignee_address_shrink):
            query['ConsigneeAddress'] = request.consignee_address_shrink
        if not DaraCore.is_null(request.consignee_mobile):
            query['ConsigneeMobile'] = request.consignee_mobile
        if not DaraCore.is_null(request.consignee_name):
            query['ConsigneeName'] = request.consignee_name
        if not DaraCore.is_null(request.consignee_phone):
            query['ConsigneePhone'] = request.consignee_phone
        if not DaraCore.is_null(request.cp_code):
            query['CpCode'] = request.cp_code
        if not DaraCore.is_null(request.goods_infos_shrink):
            query['GoodsInfos'] = request.goods_infos_shrink
        if not DaraCore.is_null(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.send_address_shrink):
            query['SendAddress'] = request.send_address_shrink
        if not DaraCore.is_null(request.send_mobile):
            query['SendMobile'] = request.send_mobile
        if not DaraCore.is_null(request.send_name):
            query['SendName'] = request.send_name
        if not DaraCore.is_null(request.send_phone):
            query['SendPhone'] = request.send_phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePickUpWaybill',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePickUpWaybillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pick_up_waybill(
        self,
        request: main_models.CreatePickUpWaybillRequest,
    ) -> main_models.CreatePickUpWaybillResponse:
        runtime = RuntimeOptions()
        return self.create_pick_up_waybill_with_options(request, runtime)

    async def create_pick_up_waybill_async(
        self,
        request: main_models.CreatePickUpWaybillRequest,
    ) -> main_models.CreatePickUpWaybillResponse:
        runtime = RuntimeOptions()
        return await self.create_pick_up_waybill_with_options_async(request, runtime)

    def create_pick_up_waybill_pre_query_with_options(
        self,
        tmp_req: main_models.CreatePickUpWaybillPreQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePickUpWaybillPreQueryResponse:
        tmp_req.validate()
        request = main_models.CreatePickUpWaybillPreQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.consignee_info):
            request.consignee_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.consignee_info, 'ConsigneeInfo', 'json')
        if not DaraCore.is_null(tmp_req.sender_info):
            request.sender_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sender_info, 'SenderInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.consignee_info_shrink):
            query['ConsigneeInfo'] = request.consignee_info_shrink
        if not DaraCore.is_null(request.cp_code):
            query['CpCode'] = request.cp_code
        if not DaraCore.is_null(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.pre_weight):
            query['PreWeight'] = request.pre_weight
        if not DaraCore.is_null(request.sender_info_shrink):
            query['SenderInfo'] = request.sender_info_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePickUpWaybillPreQuery',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePickUpWaybillPreQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pick_up_waybill_pre_query_with_options_async(
        self,
        tmp_req: main_models.CreatePickUpWaybillPreQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePickUpWaybillPreQueryResponse:
        tmp_req.validate()
        request = main_models.CreatePickUpWaybillPreQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.consignee_info):
            request.consignee_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.consignee_info, 'ConsigneeInfo', 'json')
        if not DaraCore.is_null(tmp_req.sender_info):
            request.sender_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.sender_info, 'SenderInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.consignee_info_shrink):
            query['ConsigneeInfo'] = request.consignee_info_shrink
        if not DaraCore.is_null(request.cp_code):
            query['CpCode'] = request.cp_code
        if not DaraCore.is_null(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not DaraCore.is_null(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not DaraCore.is_null(request.pre_weight):
            query['PreWeight'] = request.pre_weight
        if not DaraCore.is_null(request.sender_info_shrink):
            query['SenderInfo'] = request.sender_info_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePickUpWaybillPreQuery',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePickUpWaybillPreQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pick_up_waybill_pre_query(
        self,
        request: main_models.CreatePickUpWaybillPreQueryRequest,
    ) -> main_models.CreatePickUpWaybillPreQueryResponse:
        runtime = RuntimeOptions()
        return self.create_pick_up_waybill_pre_query_with_options(request, runtime)

    async def create_pick_up_waybill_pre_query_async(
        self,
        request: main_models.CreatePickUpWaybillPreQueryRequest,
    ) -> main_models.CreatePickUpWaybillPreQueryResponse:
        runtime = RuntimeOptions()
        return await self.create_pick_up_waybill_pre_query_with_options_async(request, runtime)

    def create_secret_transfer_record_with_options(
        self,
        request: main_models.CreateSecretTransferRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretTransferRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_partner_key):
            query['LastPartnerKey'] = request.last_partner_key
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.origin_partner_key):
            query['OriginPartnerKey'] = request.origin_partner_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecretTransferRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_transfer_record_with_options_async(
        self,
        request: main_models.CreateSecretTransferRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretTransferRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.last_partner_key):
            query['LastPartnerKey'] = request.last_partner_key
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.origin_partner_key):
            query['OriginPartnerKey'] = request.origin_partner_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecretTransferRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretTransferRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret_transfer_record(
        self,
        request: main_models.CreateSecretTransferRecordRequest,
    ) -> main_models.CreateSecretTransferRecordResponse:
        runtime = RuntimeOptions()
        return self.create_secret_transfer_record_with_options(request, runtime)

    async def create_secret_transfer_record_async(
        self,
        request: main_models.CreateSecretTransferRecordRequest,
    ) -> main_models.CreateSecretTransferRecordResponse:
        runtime = RuntimeOptions()
        return await self.create_secret_transfer_record_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        request: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_no):
            query['CalledNo'] = request.called_no
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.calling_no):
            query['CallingNo'] = request.calling_no
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        request: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_no):
            query['CalledNo'] = request.called_no
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.calling_no):
            query['CallingNo'] = request.calling_no
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def delete_axb_bind_fixed_line_with_options(
        self,
        request: main_models.DeleteAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxbBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxbBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_axb_bind_fixed_line_with_options_async(
        self,
        request: main_models.DeleteAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxbBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxbBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_axb_bind_fixed_line(
        self,
        request: main_models.DeleteAxbBindFixedLineRequest,
    ) -> main_models.DeleteAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.delete_axb_bind_fixed_line_with_options(request, runtime)

    async def delete_axb_bind_fixed_line_async(
        self,
        request: main_models.DeleteAxbBindFixedLineRequest,
    ) -> main_models.DeleteAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.delete_axb_bind_fixed_line_with_options_async(request, runtime)

    def delete_axg_group_with_options(
        self,
        request: main_models.DeleteAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_axg_group_with_options_async(
        self,
        request: main_models.DeleteAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_axg_group(
        self,
        request: main_models.DeleteAxgGroupRequest,
    ) -> main_models.DeleteAxgGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_axg_group_with_options(request, runtime)

    async def delete_axg_group_async(
        self,
        request: main_models.DeleteAxgGroupRequest,
    ) -> main_models.DeleteAxgGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_axg_group_with_options_async(request, runtime)

    def delete_axn_bind_fixed_line_with_options(
        self,
        request: main_models.DeleteAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxnBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxnBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_axn_bind_fixed_line_with_options_async(
        self,
        request: main_models.DeleteAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxnBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxnBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_axn_bind_fixed_line(
        self,
        request: main_models.DeleteAxnBindFixedLineRequest,
    ) -> main_models.DeleteAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.delete_axn_bind_fixed_line_with_options(request, runtime)

    async def delete_axn_bind_fixed_line_async(
        self,
        request: main_models.DeleteAxnBindFixedLineRequest,
    ) -> main_models.DeleteAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.delete_axn_bind_fixed_line_with_options_async(request, runtime)

    def delete_axn_extension_bind_fixed_line_with_options(
        self,
        request: main_models.DeleteAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxnExtensionBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxnExtensionBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_axn_extension_bind_fixed_line_with_options_async(
        self,
        request: main_models.DeleteAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAxnExtensionBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAxnExtensionBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_axn_extension_bind_fixed_line(
        self,
        request: main_models.DeleteAxnExtensionBindFixedLineRequest,
    ) -> main_models.DeleteAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.delete_axn_extension_bind_fixed_line_with_options(request, runtime)

    async def delete_axn_extension_bind_fixed_line_async(
        self,
        request: main_models.DeleteAxnExtensionBindFixedLineRequest,
    ) -> main_models.DeleteAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.delete_axn_extension_bind_fixed_line_with_options_async(request, runtime)

    def delete_secret_aphone_no_to_cust_with_options(
        self,
        request: main_models.DeleteSecretAPhoneNoToCustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretAPhoneNoToCustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretAPhoneNoToCust',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretAPhoneNoToCustResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_aphone_no_to_cust_with_options_async(
        self,
        request: main_models.DeleteSecretAPhoneNoToCustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretAPhoneNoToCustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretAPhoneNoToCust',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretAPhoneNoToCustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_aphone_no_to_cust(
        self,
        request: main_models.DeleteSecretAPhoneNoToCustRequest,
    ) -> main_models.DeleteSecretAPhoneNoToCustResponse:
        runtime = RuntimeOptions()
        return self.delete_secret_aphone_no_to_cust_with_options(request, runtime)

    async def delete_secret_aphone_no_to_cust_async(
        self,
        request: main_models.DeleteSecretAPhoneNoToCustRequest,
    ) -> main_models.DeleteSecretAPhoneNoToCustResponse:
        runtime = RuntimeOptions()
        return await self.delete_secret_aphone_no_to_cust_with_options_async(request, runtime)

    def delete_secret_blacklist_with_options(
        self,
        request: main_models.DeleteSecretBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.black_type):
            query['BlackType'] = request.black_type
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretBlacklist',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_blacklist_with_options_async(
        self,
        request: main_models.DeleteSecretBlacklistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretBlacklistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.black_type):
            query['BlackType'] = request.black_type
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretBlacklist',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_blacklist(
        self,
        request: main_models.DeleteSecretBlacklistRequest,
    ) -> main_models.DeleteSecretBlacklistResponse:
        runtime = RuntimeOptions()
        return self.delete_secret_blacklist_with_options(request, runtime)

    async def delete_secret_blacklist_async(
        self,
        request: main_models.DeleteSecretBlacklistRequest,
    ) -> main_models.DeleteSecretBlacklistResponse:
        runtime = RuntimeOptions()
        return await self.delete_secret_blacklist_with_options_async(request, runtime)

    def get_dypls_ossinfo_for_upload_file_with_options(
        self,
        request: main_models.GetDyplsOSSInfoForUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDyplsOSSInfoForUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDyplsOSSInfoForUploadFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDyplsOSSInfoForUploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dypls_ossinfo_for_upload_file_with_options_async(
        self,
        request: main_models.GetDyplsOSSInfoForUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDyplsOSSInfoForUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDyplsOSSInfoForUploadFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDyplsOSSInfoForUploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dypls_ossinfo_for_upload_file(
        self,
        request: main_models.GetDyplsOSSInfoForUploadFileRequest,
    ) -> main_models.GetDyplsOSSInfoForUploadFileResponse:
        runtime = RuntimeOptions()
        return self.get_dypls_ossinfo_for_upload_file_with_options(request, runtime)

    async def get_dypls_ossinfo_for_upload_file_async(
        self,
        request: main_models.GetDyplsOSSInfoForUploadFileRequest,
    ) -> main_models.GetDyplsOSSInfoForUploadFileResponse:
        runtime = RuntimeOptions()
        return await self.get_dypls_ossinfo_for_upload_file_with_options_async(request, runtime)

    def get_secret_asr_detail_with_options(
        self,
        request: main_models.GetSecretAsrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretAsrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretAsrDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretAsrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_asr_detail_with_options_async(
        self,
        request: main_models.GetSecretAsrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretAsrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretAsrDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretAsrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_asr_detail(
        self,
        request: main_models.GetSecretAsrDetailRequest,
    ) -> main_models.GetSecretAsrDetailResponse:
        runtime = RuntimeOptions()
        return self.get_secret_asr_detail_with_options(request, runtime)

    async def get_secret_asr_detail_async(
        self,
        request: main_models.GetSecretAsrDetailRequest,
    ) -> main_models.GetSecretAsrDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_asr_detail_with_options_async(request, runtime)

    def get_total_public_url_with_options(
        self,
        request: main_models.GetTotalPublicUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTotalPublicUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.check_subs):
            query['CheckSubs'] = request.check_subs
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTotalPublicUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTotalPublicUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_total_public_url_with_options_async(
        self,
        request: main_models.GetTotalPublicUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTotalPublicUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.check_subs):
            query['CheckSubs'] = request.check_subs
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTotalPublicUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTotalPublicUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_total_public_url(
        self,
        request: main_models.GetTotalPublicUrlRequest,
    ) -> main_models.GetTotalPublicUrlResponse:
        runtime = RuntimeOptions()
        return self.get_total_public_url_with_options(request, runtime)

    async def get_total_public_url_async(
        self,
        request: main_models.GetTotalPublicUrlRequest,
    ) -> main_models.GetTotalPublicUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_total_public_url_with_options_async(request, runtime)

    def get_xconfig_with_options(
        self,
        request: main_models.GetXConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetXConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetXConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetXConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_xconfig_with_options_async(
        self,
        request: main_models.GetXConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetXConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetXConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetXConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_xconfig(
        self,
        request: main_models.GetXConfigRequest,
    ) -> main_models.GetXConfigResponse:
        runtime = RuntimeOptions()
        return self.get_xconfig_with_options(request, runtime)

    async def get_xconfig_async(
        self,
        request: main_models.GetXConfigRequest,
    ) -> main_models.GetXConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_xconfig_with_options_async(request, runtime)

    def get_xdefault_config_with_options(
        self,
        request: main_models.GetXDefaultConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetXDefaultConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetXDefaultConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetXDefaultConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_xdefault_config_with_options_async(
        self,
        request: main_models.GetXDefaultConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetXDefaultConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetXDefaultConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetXDefaultConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_xdefault_config(
        self,
        request: main_models.GetXDefaultConfigRequest,
    ) -> main_models.GetXDefaultConfigResponse:
        runtime = RuntimeOptions()
        return self.get_xdefault_config_with_options(request, runtime)

    async def get_xdefault_config_async(
        self,
        request: main_models.GetXDefaultConfigRequest,
    ) -> main_models.GetXDefaultConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_xdefault_config_with_options_async(request, runtime)

    def list_xtelephones_with_options(
        self,
        request: main_models.ListXTelephonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListXTelephonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListXTelephones',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListXTelephonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_xtelephones_with_options_async(
        self,
        request: main_models.ListXTelephonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListXTelephonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListXTelephones',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListXTelephonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_xtelephones(
        self,
        request: main_models.ListXTelephonesRequest,
    ) -> main_models.ListXTelephonesResponse:
        runtime = RuntimeOptions()
        return self.list_xtelephones_with_options(request, runtime)

    async def list_xtelephones_async(
        self,
        request: main_models.ListXTelephonesRequest,
    ) -> main_models.ListXTelephonesResponse:
        runtime = RuntimeOptions()
        return await self.list_xtelephones_with_options_async(request, runtime)

    def lock_secret_no_with_options(
        self,
        request: main_models.LockSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_secret_no_with_options_async(
        self,
        request: main_models.LockSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_secret_no(
        self,
        request: main_models.LockSecretNoRequest,
    ) -> main_models.LockSecretNoResponse:
        runtime = RuntimeOptions()
        return self.lock_secret_no_with_options(request, runtime)

    async def lock_secret_no_async(
        self,
        request: main_models.LockSecretNoRequest,
    ) -> main_models.LockSecretNoResponse:
        runtime = RuntimeOptions()
        return await self.lock_secret_no_with_options_async(request, runtime)

    def operate_axg_group_with_options(
        self,
        request: main_models.OperateAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.numbers):
            query['Numbers'] = request.numbers
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_axg_group_with_options_async(
        self,
        request: main_models.OperateAxgGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAxgGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.numbers):
            query['Numbers'] = request.numbers
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAxgGroup',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_axg_group(
        self,
        request: main_models.OperateAxgGroupRequest,
    ) -> main_models.OperateAxgGroupResponse:
        runtime = RuntimeOptions()
        return self.operate_axg_group_with_options(request, runtime)

    async def operate_axg_group_async(
        self,
        request: main_models.OperateAxgGroupRequest,
    ) -> main_models.OperateAxgGroupResponse:
        runtime = RuntimeOptions()
        return await self.operate_axg_group_with_options_async(request, runtime)

    def operate_black_no_with_options(
        self,
        request: main_models.OperateBlackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBlackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tips):
            query['Tips'] = request.tips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBlackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBlackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_black_no_with_options_async(
        self,
        request: main_models.OperateBlackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBlackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.black_no):
            query['BlackNo'] = request.black_no
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tips):
            query['Tips'] = request.tips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBlackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBlackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_black_no(
        self,
        request: main_models.OperateBlackNoRequest,
    ) -> main_models.OperateBlackNoResponse:
        runtime = RuntimeOptions()
        return self.operate_black_no_with_options(request, runtime)

    async def operate_black_no_async(
        self,
        request: main_models.OperateBlackNoRequest,
    ) -> main_models.OperateBlackNoResponse:
        runtime = RuntimeOptions()
        return await self.operate_black_no_with_options_async(request, runtime)

    def query_axb_bind_fixed_line_with_options(
        self,
        request: main_models.QueryAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxbBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxbBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_axb_bind_fixed_line_with_options_async(
        self,
        request: main_models.QueryAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxbBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxbBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_axb_bind_fixed_line(
        self,
        request: main_models.QueryAxbBindFixedLineRequest,
    ) -> main_models.QueryAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.query_axb_bind_fixed_line_with_options(request, runtime)

    async def query_axb_bind_fixed_line_async(
        self,
        request: main_models.QueryAxbBindFixedLineRequest,
    ) -> main_models.QueryAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.query_axb_bind_fixed_line_with_options_async(request, runtime)

    def query_axn_bind_fixed_line_with_options(
        self,
        request: main_models.QueryAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxnBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxnBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_axn_bind_fixed_line_with_options_async(
        self,
        request: main_models.QueryAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxnBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxnBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_axn_bind_fixed_line(
        self,
        request: main_models.QueryAxnBindFixedLineRequest,
    ) -> main_models.QueryAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.query_axn_bind_fixed_line_with_options(request, runtime)

    async def query_axn_bind_fixed_line_async(
        self,
        request: main_models.QueryAxnBindFixedLineRequest,
    ) -> main_models.QueryAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.query_axn_bind_fixed_line_with_options_async(request, runtime)

    def query_axn_extension_bind_fixed_line_with_options(
        self,
        request: main_models.QueryAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxnExtensionBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxnExtensionBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_axn_extension_bind_fixed_line_with_options_async(
        self,
        request: main_models.QueryAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAxnExtensionBindFixedLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAxnExtensionBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_axn_extension_bind_fixed_line(
        self,
        request: main_models.QueryAxnExtensionBindFixedLineRequest,
    ) -> main_models.QueryAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.query_axn_extension_bind_fixed_line_with_options(request, runtime)

    async def query_axn_extension_bind_fixed_line_async(
        self,
        request: main_models.QueryAxnExtensionBindFixedLineRequest,
    ) -> main_models.QueryAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.query_axn_extension_bind_fixed_line_with_options_async(request, runtime)

    def query_phone_no_aby_track_no_with_options(
        self,
        request: main_models.QueryPhoneNoAByTrackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneNoAByTrackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cabinet_no):
            query['CabinetNo'] = request.cabinet_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneNoAByTrackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneNoAByTrackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_no_aby_track_no_with_options_async(
        self,
        request: main_models.QueryPhoneNoAByTrackNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPhoneNoAByTrackNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cabinet_no):
            query['CabinetNo'] = request.cabinet_no
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPhoneNoAByTrackNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPhoneNoAByTrackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_no_aby_track_no(
        self,
        request: main_models.QueryPhoneNoAByTrackNoRequest,
    ) -> main_models.QueryPhoneNoAByTrackNoResponse:
        runtime = RuntimeOptions()
        return self.query_phone_no_aby_track_no_with_options(request, runtime)

    async def query_phone_no_aby_track_no_async(
        self,
        request: main_models.QueryPhoneNoAByTrackNoRequest,
    ) -> main_models.QueryPhoneNoAByTrackNoResponse:
        runtime = RuntimeOptions()
        return await self.query_phone_no_aby_track_no_with_options_async(request, runtime)

    def query_record_file_download_url_with_options(
        self,
        request: main_models.QueryRecordFileDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordFileDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordFileDownloadUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordFileDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_file_download_url_with_options_async(
        self,
        request: main_models.QueryRecordFileDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordFileDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.call_time):
            query['CallTime'] = request.call_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordFileDownloadUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordFileDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_file_download_url(
        self,
        request: main_models.QueryRecordFileDownloadUrlRequest,
    ) -> main_models.QueryRecordFileDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.query_record_file_download_url_with_options(request, runtime)

    async def query_record_file_download_url_async(
        self,
        request: main_models.QueryRecordFileDownloadUrlRequest,
    ) -> main_models.QueryRecordFileDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.query_record_file_download_url_with_options_async(request, runtime)

    def query_secret_aphone_no_to_cust_with_options(
        self,
        request: main_models.QuerySecretAPhoneNoToCustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretAPhoneNoToCustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretAPhoneNoToCust',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretAPhoneNoToCustResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_aphone_no_to_cust_with_options_async(
        self,
        request: main_models.QuerySecretAPhoneNoToCustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretAPhoneNoToCustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ano_white_group_id):
            query['ANoWhiteGroupId'] = request.ano_white_group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretAPhoneNoToCust',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretAPhoneNoToCustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_aphone_no_to_cust(
        self,
        request: main_models.QuerySecretAPhoneNoToCustRequest,
    ) -> main_models.QuerySecretAPhoneNoToCustResponse:
        runtime = RuntimeOptions()
        return self.query_secret_aphone_no_to_cust_with_options(request, runtime)

    async def query_secret_aphone_no_to_cust_async(
        self,
        request: main_models.QuerySecretAPhoneNoToCustRequest,
    ) -> main_models.QuerySecretAPhoneNoToCustResponse:
        runtime = RuntimeOptions()
        return await self.query_secret_aphone_no_to_cust_with_options_async(request, runtime)

    def query_secret_no_detail_with_options(
        self,
        request: main_models.QuerySecretNoDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretNoDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretNoDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretNoDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_no_detail_with_options_async(
        self,
        request: main_models.QuerySecretNoDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretNoDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretNoDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretNoDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_no_detail(
        self,
        request: main_models.QuerySecretNoDetailRequest,
    ) -> main_models.QuerySecretNoDetailResponse:
        runtime = RuntimeOptions()
        return self.query_secret_no_detail_with_options(request, runtime)

    async def query_secret_no_detail_async(
        self,
        request: main_models.QuerySecretNoDetailRequest,
    ) -> main_models.QuerySecretNoDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_secret_no_detail_with_options_async(request, runtime)

    def query_secret_no_remain_with_options(
        self,
        request: main_models.QuerySecretNoRemainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretNoRemainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretNoRemain',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretNoRemainResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_no_remain_with_options_async(
        self,
        request: main_models.QuerySecretNoRemainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretNoRemainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretNoRemain',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretNoRemainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_no_remain(
        self,
        request: main_models.QuerySecretNoRemainRequest,
    ) -> main_models.QuerySecretNoRemainResponse:
        runtime = RuntimeOptions()
        return self.query_secret_no_remain_with_options(request, runtime)

    async def query_secret_no_remain_async(
        self,
        request: main_models.QuerySecretNoRemainRequest,
    ) -> main_models.QuerySecretNoRemainResponse:
        runtime = RuntimeOptions()
        return await self.query_secret_no_remain_with_options_async(request, runtime)

    def query_secret_transfer_details_with_options(
        self,
        request: main_models.QuerySecretTransferDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretTransferDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretTransferDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretTransferDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_transfer_details_with_options_async(
        self,
        request: main_models.QuerySecretTransferDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySecretTransferDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySecretTransferDetails',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySecretTransferDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_transfer_details(
        self,
        request: main_models.QuerySecretTransferDetailsRequest,
    ) -> main_models.QuerySecretTransferDetailsResponse:
        runtime = RuntimeOptions()
        return self.query_secret_transfer_details_with_options(request, runtime)

    async def query_secret_transfer_details_async(
        self,
        request: main_models.QuerySecretTransferDetailsRequest,
    ) -> main_models.QuerySecretTransferDetailsResponse:
        runtime = RuntimeOptions()
        return await self.query_secret_transfer_details_with_options_async(request, runtime)

    def query_sound_record_with_options(
        self,
        request: main_models.QuerySoundRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySoundRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySoundRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySoundRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sound_record_with_options_async(
        self,
        request: main_models.QuerySoundRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySoundRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySoundRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySoundRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sound_record(
        self,
        request: main_models.QuerySoundRecordRequest,
    ) -> main_models.QuerySoundRecordResponse:
        runtime = RuntimeOptions()
        return self.query_sound_record_with_options(request, runtime)

    async def query_sound_record_async(
        self,
        request: main_models.QuerySoundRecordRequest,
    ) -> main_models.QuerySoundRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_sound_record_with_options_async(request, runtime)

    def query_subs_id_with_options(
        self,
        request: main_models.QuerySubsIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySubsIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySubsId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySubsIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subs_id_with_options_async(
        self,
        request: main_models.QuerySubsIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySubsIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySubsId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySubsIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_subs_id(
        self,
        request: main_models.QuerySubsIdRequest,
    ) -> main_models.QuerySubsIdResponse:
        runtime = RuntimeOptions()
        return self.query_subs_id_with_options(request, runtime)

    async def query_subs_id_async(
        self,
        request: main_models.QuerySubsIdRequest,
    ) -> main_models.QuerySubsIdResponse:
        runtime = RuntimeOptions()
        return await self.query_subs_id_with_options_async(request, runtime)

    def query_subscription_detail_with_options(
        self,
        request: main_models.QuerySubscriptionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySubscriptionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySubscriptionDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySubscriptionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subscription_detail_with_options_async(
        self,
        request: main_models.QuerySubscriptionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySubscriptionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySubscriptionDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySubscriptionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_subscription_detail(
        self,
        request: main_models.QuerySubscriptionDetailRequest,
    ) -> main_models.QuerySubscriptionDetailResponse:
        runtime = RuntimeOptions()
        return self.query_subscription_detail_with_options(request, runtime)

    async def query_subscription_detail_async(
        self,
        request: main_models.QuerySubscriptionDetailRequest,
    ) -> main_models.QuerySubscriptionDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_subscription_detail_with_options_async(request, runtime)

    def release_secret_no_with_options(
        self,
        request: main_models.ReleaseSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_secret_no_with_options_async(
        self,
        request: main_models.ReleaseSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_secret_no(
        self,
        request: main_models.ReleaseSecretNoRequest,
    ) -> main_models.ReleaseSecretNoResponse:
        runtime = RuntimeOptions()
        return self.release_secret_no_with_options(request, runtime)

    async def release_secret_no_async(
        self,
        request: main_models.ReleaseSecretNoRequest,
    ) -> main_models.ReleaseSecretNoResponse:
        runtime = RuntimeOptions()
        return await self.release_secret_no_with_options_async(request, runtime)

    def un_bind_axbwith_options(
        self,
        request: main_models.UnBindAXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnBindAXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_id):
            query['BindId'] = request.bind_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnBindAXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnBindAXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_bind_axbwith_options_async(
        self,
        request: main_models.UnBindAXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnBindAXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_id):
            query['BindId'] = request.bind_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnBindAXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnBindAXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_bind_axb(
        self,
        request: main_models.UnBindAXBRequest,
    ) -> main_models.UnBindAXBResponse:
        runtime = RuntimeOptions()
        return self.un_bind_axbwith_options(request, runtime)

    async def un_bind_axb_async(
        self,
        request: main_models.UnBindAXBRequest,
    ) -> main_models.UnBindAXBResponse:
        runtime = RuntimeOptions()
        return await self.un_bind_axbwith_options_async(request, runtime)

    def un_bind_xbwith_options(
        self,
        request: main_models.UnBindXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnBindXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnBindXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnBindXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_bind_xbwith_options_async(
        self,
        request: main_models.UnBindXBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnBindXBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_id):
            query['AuthId'] = request.auth_id
        if not DaraCore.is_null(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not DaraCore.is_null(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.req_id):
            query['ReqId'] = request.req_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnBindXB',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnBindXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_bind_xb(
        self,
        request: main_models.UnBindXBRequest,
    ) -> main_models.UnBindXBResponse:
        runtime = RuntimeOptions()
        return self.un_bind_xbwith_options(request, runtime)

    async def un_bind_xb_async(
        self,
        request: main_models.UnBindXBRequest,
    ) -> main_models.UnBindXBResponse:
        runtime = RuntimeOptions()
        return await self.un_bind_xbwith_options_async(request, runtime)

    def unbind_subs_700with_options(
        self,
        request: main_models.UnbindSubs700Request,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSubs700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSubs700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSubs700Response(),
            self.call_api(params, req, runtime)
        )

    async def unbind_subs_700with_options_async(
        self,
        request: main_models.UnbindSubs700Request,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSubs700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSubs700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSubs700Response(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_subs_700(
        self,
        request: main_models.UnbindSubs700Request,
    ) -> main_models.UnbindSubs700Response:
        runtime = RuntimeOptions()
        return self.unbind_subs_700with_options(request, runtime)

    async def unbind_subs_700_async(
        self,
        request: main_models.UnbindSubs700Request,
    ) -> main_models.UnbindSubs700Response:
        runtime = RuntimeOptions()
        return await self.unbind_subs_700with_options_async(request, runtime)

    def unbind_subscription_with_options(
        self,
        request: main_models.UnbindSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSubscription',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_subscription_with_options_async(
        self,
        request: main_models.UnbindSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSubscription',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_subscription(
        self,
        request: main_models.UnbindSubscriptionRequest,
    ) -> main_models.UnbindSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.unbind_subscription_with_options(request, runtime)

    async def unbind_subscription_async(
        self,
        request: main_models.UnbindSubscriptionRequest,
    ) -> main_models.UnbindSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.unbind_subscription_with_options_async(request, runtime)

    def unlock_secret_no_with_options(
        self,
        request: main_models.UnlockSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_secret_no_with_options_async(
        self,
        request: main_models.UnlockSecretNoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockSecretNoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockSecretNo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_secret_no(
        self,
        request: main_models.UnlockSecretNoRequest,
    ) -> main_models.UnlockSecretNoResponse:
        runtime = RuntimeOptions()
        return self.unlock_secret_no_with_options(request, runtime)

    async def unlock_secret_no_async(
        self,
        request: main_models.UnlockSecretNoRequest,
    ) -> main_models.UnlockSecretNoResponse:
        runtime = RuntimeOptions()
        return await self.unlock_secret_no_with_options_async(request, runtime)

    def update_axb_bind_fixed_line_with_options(
        self,
        tmp_req: main_models.UpdateAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxbBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxbBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxbBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_axb_bind_fixed_line_with_options_async(
        self,
        tmp_req: main_models.UpdateAxbBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxbBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxbBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxbBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxbBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_axb_bind_fixed_line(
        self,
        request: main_models.UpdateAxbBindFixedLineRequest,
    ) -> main_models.UpdateAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.update_axb_bind_fixed_line_with_options(request, runtime)

    async def update_axb_bind_fixed_line_async(
        self,
        request: main_models.UpdateAxbBindFixedLineRequest,
    ) -> main_models.UpdateAxbBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.update_axb_bind_fixed_line_with_options_async(request, runtime)

    def update_axn_bind_fixed_line_with_options(
        self,
        tmp_req: main_models.UpdateAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxnBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxnBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxnBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_axn_bind_fixed_line_with_options_async(
        self,
        tmp_req: main_models.UpdateAxnBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxnBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxnBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra):
            request.extra_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extra_shrink):
            query['Extra'] = request.extra_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxnBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxnBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_axn_bind_fixed_line(
        self,
        request: main_models.UpdateAxnBindFixedLineRequest,
    ) -> main_models.UpdateAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.update_axn_bind_fixed_line_with_options(request, runtime)

    async def update_axn_bind_fixed_line_async(
        self,
        request: main_models.UpdateAxnBindFixedLineRequest,
    ) -> main_models.UpdateAxnBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.update_axn_bind_fixed_line_with_options_async(request, runtime)

    def update_axn_extension_bind_fixed_line_with_options(
        self,
        tmp_req: main_models.UpdateAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxnExtensionBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxnExtensionBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extraaxx):
            request.extraaxx_shrink = Utils.array_to_string_with_specified_style(tmp_req.extraaxx, 'Extraaxx', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extraaxx_shrink):
            query['Extraaxx'] = request.extraaxx_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxnExtensionBindFixedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_axn_extension_bind_fixed_line_with_options_async(
        self,
        tmp_req: main_models.UpdateAxnExtensionBindFixedLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAxnExtensionBindFixedLineResponse:
        tmp_req.validate()
        request = main_models.UpdateAxnExtensionBindFixedLineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extraaxx):
            request.extraaxx_shrink = Utils.array_to_string_with_specified_style(tmp_req.extraaxx, 'Extraaxx', 'json')
        query = {}
        if not DaraCore.is_null(request.anucode):
            query['Anucode'] = request.anucode
        if not DaraCore.is_null(request.anucodecalled):
            query['Anucodecalled'] = request.anucodecalled
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.extraaxx_shrink):
            query['Extraaxx'] = request.extraaxx_shrink
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sub_id):
            query['SubId'] = request.sub_id
        if not DaraCore.is_null(request.subts):
            query['Subts'] = request.subts
        if not DaraCore.is_null(request.tanucode_connect):
            query['TAnucodeConnect'] = request.tanucode_connect
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.ts):
            query['Ts'] = request.ts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAxnExtensionBindFixedLine',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAxnExtensionBindFixedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_axn_extension_bind_fixed_line(
        self,
        request: main_models.UpdateAxnExtensionBindFixedLineRequest,
    ) -> main_models.UpdateAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return self.update_axn_extension_bind_fixed_line_with_options(request, runtime)

    async def update_axn_extension_bind_fixed_line_async(
        self,
        request: main_models.UpdateAxnExtensionBindFixedLineRequest,
    ) -> main_models.UpdateAxnExtensionBindFixedLineResponse:
        runtime = RuntimeOptions()
        return await self.update_axn_extension_bind_fixed_line_with_options_async(request, runtime)

    def update_subs_700with_options(
        self,
        request: main_models.UpdateSubs700Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubs700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.default_a):
            query['DefaultA'] = request.default_a
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubs700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubs700Response(),
            self.call_api(params, req, runtime)
        )

    async def update_subs_700with_options_async(
        self,
        request: main_models.UpdateSubs700Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubs700Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.default_a):
            query['DefaultA'] = request.default_a
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.industrial_id):
            query['IndustrialId'] = request.industrial_id
        if not DaraCore.is_null(request.need_asr):
            query['NeedAsr'] = request.need_asr
        if not DaraCore.is_null(request.need_record):
            query['NeedRecord'] = request.need_record
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        if not DaraCore.is_null(request.tel_a):
            query['TelA'] = request.tel_a
        if not DaraCore.is_null(request.tel_b):
            query['TelB'] = request.tel_b
        if not DaraCore.is_null(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubs700',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubs700Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subs_700(
        self,
        request: main_models.UpdateSubs700Request,
    ) -> main_models.UpdateSubs700Response:
        runtime = RuntimeOptions()
        return self.update_subs_700with_options(request, runtime)

    async def update_subs_700_async(
        self,
        request: main_models.UpdateSubs700Request,
    ) -> main_models.UpdateSubs700Response:
        runtime = RuntimeOptions()
        return await self.update_subs_700with_options_async(request, runtime)

    def update_subscription_with_options(
        self,
        request: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        request: main_models.UpdateSubscriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not DaraCore.is_null(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not DaraCore.is_null(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not DaraCore.is_null(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not DaraCore.is_null(request.expiration):
            query['Expiration'] = request.expiration
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not DaraCore.is_null(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not DaraCore.is_null(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not DaraCore.is_null(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.ring_config):
            query['RingConfig'] = request.ring_config
        if not DaraCore.is_null(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSubscription',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.update_subscription_with_options(request, runtime)

    async def update_subscription_async(
        self,
        request: main_models.UpdateSubscriptionRequest,
    ) -> main_models.UpdateSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_subscription_with_options_async(request, runtime)

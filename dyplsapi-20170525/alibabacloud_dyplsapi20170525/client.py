# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyplsapi20170525 import models as dyplsapi_20170525_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_axn_track_no_with_options(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        if not UtilClient.is_unset(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAxnTrackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddAxnTrackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_axn_track_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        if not UtilClient.is_unset(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAxnTrackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddAxnTrackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_axn_track_no(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_axn_track_no_with_options(request, runtime)

    async def add_axn_track_no_async(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_axn_track_no_with_options_async(request, runtime)

    def add_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecretBlacklist',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddSecretBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_secret_blacklist_with_options_async(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecretBlacklist',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddSecretBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_secret_blacklist(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_secret_blacklist_with_options(request, runtime)

    async def add_secret_blacklist_async(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_secret_blacklist_with_options_async(request, runtime)

    def bind_axb_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxb',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axb_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxb',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axb(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_axb_with_options(request, runtime)

    async def bind_axb_async(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_axb_with_options_async(request, runtime)

    def bind_axg_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxg',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxgResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axg_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxg',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axg(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_axg_with_options(request, runtime)

    async def bind_axg_async(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_axg_with_options_async(request, runtime)

    def bind_axn_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.no_type):
            query['NoType'] = request.no_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxn',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.call_timeout):
            query['CallTimeout'] = request.call_timeout
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.no_type):
            query['NoType'] = request.no_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxn',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_axn_with_options(request, runtime)

    async def bind_axn_async(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_axn_with_options_async(request, runtime)

    def bind_axn_extension_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxnExtension',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axn_extension_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expect_city):
            query['ExpectCity'] = request.expect_city
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.out_order_id):
            query['OutOrderId'] = request.out_order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAxnExtension',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axn_extension(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_axn_extension_with_options(request, runtime)

    async def bind_axn_extension_async(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_axn_extension_with_options_async(request, runtime)

    def buy_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.display_pool):
            query['DisplayPool'] = request.display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BuySecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BuySecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def buy_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.display_pool):
            query['DisplayPool'] = request.display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BuySecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BuySecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def buy_secret_no(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.buy_secret_no_with_options(request, runtime)

    async def buy_secret_no_async(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.buy_secret_no_with_options_async(request, runtime)

    def cancel_pick_up_waybill_with_options(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_desc):
            query['CancelDesc'] = request.cancel_desc
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPickUpWaybill',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CancelPickUpWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_pick_up_waybill_with_options_async(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_desc):
            query['CancelDesc'] = request.cancel_desc
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPickUpWaybill',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CancelPickUpWaybillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_pick_up_waybill(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_pick_up_waybill_with_options(request, runtime)

    async def cancel_pick_up_waybill_async(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_pick_up_waybill_with_options_async(request, runtime)

    def confirm_send_sms_with_options(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmSendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ConfirmSendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_send_sms_with_options_async(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmSendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ConfirmSendSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_send_sms(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_send_sms_with_options(request, runtime)

    async def confirm_send_sms_async(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_send_sms_with_options_async(request, runtime)

    def create_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.numbers):
            query['Numbers'] = request.numbers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAxgGroup',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_axg_group_with_options_async(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.numbers):
            query['Numbers'] = request.numbers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAxgGroup',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_axg_group(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_axg_group_with_options(request, runtime)

    async def create_axg_group_async(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_axg_group_with_options_async(request, runtime)

    def create_pick_up_waybill_with_options(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_address):
            request.consignee_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.consignee_address), 'ConsigneeAddress', 'json')
        if not UtilClient.is_unset(tmp_req.goods_infos):
            request.goods_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not UtilClient.is_unset(tmp_req.send_address):
            request.send_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.send_address), 'SendAddress', 'json')
        query = {}
        if not UtilClient.is_unset(request.appoint_got_end_time):
            query['AppointGotEndTime'] = request.appoint_got_end_time
        if not UtilClient.is_unset(request.appoint_got_start_time):
            query['AppointGotStartTime'] = request.appoint_got_start_time
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.consignee_address_shrink):
            query['ConsigneeAddress'] = request.consignee_address_shrink
        if not UtilClient.is_unset(request.consignee_mobile):
            query['ConsigneeMobile'] = request.consignee_mobile
        if not UtilClient.is_unset(request.consignee_name):
            query['ConsigneeName'] = request.consignee_name
        if not UtilClient.is_unset(request.consignee_phone):
            query['ConsigneePhone'] = request.consignee_phone
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.goods_infos_shrink):
            query['GoodsInfos'] = request.goods_infos_shrink
        if not UtilClient.is_unset(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.send_address_shrink):
            query['SendAddress'] = request.send_address_shrink
        if not UtilClient.is_unset(request.send_mobile):
            query['SendMobile'] = request.send_mobile
        if not UtilClient.is_unset(request.send_name):
            query['SendName'] = request.send_name
        if not UtilClient.is_unset(request.send_phone):
            query['SendPhone'] = request.send_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePickUpWaybill',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreatePickUpWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pick_up_waybill_with_options_async(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_address):
            request.consignee_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.consignee_address), 'ConsigneeAddress', 'json')
        if not UtilClient.is_unset(tmp_req.goods_infos):
            request.goods_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not UtilClient.is_unset(tmp_req.send_address):
            request.send_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.send_address), 'SendAddress', 'json')
        query = {}
        if not UtilClient.is_unset(request.appoint_got_end_time):
            query['AppointGotEndTime'] = request.appoint_got_end_time
        if not UtilClient.is_unset(request.appoint_got_start_time):
            query['AppointGotStartTime'] = request.appoint_got_start_time
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.consignee_address_shrink):
            query['ConsigneeAddress'] = request.consignee_address_shrink
        if not UtilClient.is_unset(request.consignee_mobile):
            query['ConsigneeMobile'] = request.consignee_mobile
        if not UtilClient.is_unset(request.consignee_name):
            query['ConsigneeName'] = request.consignee_name
        if not UtilClient.is_unset(request.consignee_phone):
            query['ConsigneePhone'] = request.consignee_phone
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.goods_infos_shrink):
            query['GoodsInfos'] = request.goods_infos_shrink
        if not UtilClient.is_unset(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.send_address_shrink):
            query['SendAddress'] = request.send_address_shrink
        if not UtilClient.is_unset(request.send_mobile):
            query['SendMobile'] = request.send_mobile
        if not UtilClient.is_unset(request.send_name):
            query['SendName'] = request.send_name
        if not UtilClient.is_unset(request.send_phone):
            query['SendPhone'] = request.send_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePickUpWaybill',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreatePickUpWaybillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pick_up_waybill(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pick_up_waybill_with_options(request, runtime)

    async def create_pick_up_waybill_async(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pick_up_waybill_with_options_async(request, runtime)

    def create_pick_up_waybill_pre_query_with_options(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillPreQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_info):
            request.consignee_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.consignee_info), 'ConsigneeInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sender_info):
            request.sender_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.sender_info), 'SenderInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.consignee_info_shrink):
            query['ConsigneeInfo'] = request.consignee_info_shrink
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.pre_weight):
            query['PreWeight'] = request.pre_weight
        if not UtilClient.is_unset(request.sender_info_shrink):
            query['SenderInfo'] = request.sender_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePickUpWaybillPreQuery',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pick_up_waybill_pre_query_with_options_async(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillPreQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_info):
            request.consignee_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.consignee_info), 'ConsigneeInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sender_info):
            request.sender_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.sender_info), 'SenderInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.consignee_info_shrink):
            query['ConsigneeInfo'] = request.consignee_info_shrink
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.order_channels):
            query['OrderChannels'] = request.order_channels
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
        if not UtilClient.is_unset(request.pre_weight):
            query['PreWeight'] = request.pre_weight
        if not UtilClient.is_unset(request.sender_info_shrink):
            query['SenderInfo'] = request.sender_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePickUpWaybillPreQuery',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pick_up_waybill_pre_query(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pick_up_waybill_pre_query_with_options(request, runtime)

    async def create_pick_up_waybill_pre_query_async(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pick_up_waybill_pre_query_with_options_async(request, runtime)

    def delete_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretBlacklist',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.DeleteSecretBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_blacklist_with_options_async(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.way_control):
            query['WayControl'] = request.way_control
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretBlacklist',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.DeleteSecretBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_blacklist(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_blacklist_with_options(request, runtime)

    async def delete_secret_blacklist_async(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_blacklist_with_options_async(request, runtime)

    def get_secret_asr_detail_with_options(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretAsrDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSecretAsrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_asr_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretAsrDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSecretAsrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_asr_detail(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_asr_detail_with_options(request, runtime)

    async def get_secret_asr_detail_async(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_asr_detail_with_options_async(request, runtime)

    def get_subscription_detail_with_options(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSubscriptionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSubscriptionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_detail(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_detail_with_options(request, runtime)

    async def get_subscription_detail_async(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_detail_with_options_async(request, runtime)

    def get_total_public_url_with_options(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.check_subs):
            query['CheckSubs'] = request.check_subs
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTotalPublicUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetTotalPublicUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_total_public_url_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.check_subs):
            query['CheckSubs'] = request.check_subs
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTotalPublicUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetTotalPublicUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_total_public_url(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_total_public_url_with_options(request, runtime)

    async def get_total_public_url_async(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_total_public_url_with_options_async(request, runtime)

    def lock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.LockSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.LockSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_secret_no(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_secret_no_with_options(request, runtime)

    async def lock_secret_no_async(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_secret_no_with_options_async(request, runtime)

    def operate_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.numbers):
            query['Numbers'] = request.numbers
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAxgGroup',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_axg_group_with_options_async(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.numbers):
            query['Numbers'] = request.numbers
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAxgGroup',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_axg_group(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_axg_group_with_options(request, runtime)

    async def operate_axg_group_async(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_axg_group_with_options_async(request, runtime)

    def operate_black_no_with_options(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tips):
            query['Tips'] = request.tips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBlackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateBlackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_black_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_no):
            query['BlackNo'] = request.black_no
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tips):
            query['Tips'] = request.tips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBlackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateBlackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_black_no(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_black_no_with_options(request, runtime)

    async def operate_black_no_async(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_black_no_with_options_async(request, runtime)

    def query_call_status_with_options(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_no):
            query['CallNo'] = request.call_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallStatus',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryCallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_status_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_no):
            query['CallNo'] = request.call_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallStatus',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryCallStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_status(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_status_with_options(request, runtime)

    async def query_call_status_async(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_status_with_options_async(request, runtime)

    def query_phone_no_aby_track_no_with_options(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cabinet_no):
            query['CabinetNo'] = request.cabinet_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneNoAByTrackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_no_aby_track_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cabinet_no):
            query['CabinetNo'] = request.cabinet_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.track_no):
            query['trackNo'] = request.track_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneNoAByTrackNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_no_aby_track_no(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_phone_no_aby_track_no_with_options(request, runtime)

    async def query_phone_no_aby_track_no_async(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_phone_no_aby_track_no_with_options_async(request, runtime)

    def query_record_file_download_url_with_options(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordFileDownloadUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_file_download_url_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordFileDownloadUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_file_download_url(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_file_download_url_with_options(request, runtime)

    async def query_record_file_download_url_async(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_file_download_url_with_options_async(request, runtime)

    def query_secret_no_detail_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySecretNoDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_no_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySecretNoDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_no_detail(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_secret_no_detail_with_options(request, runtime)

    async def query_secret_no_detail_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_secret_no_detail_with_options_async(request, runtime)

    def query_secret_no_remain_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySecretNoRemain',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoRemainResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_secret_no_remain_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySecretNoRemain',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoRemainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_secret_no_remain(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_secret_no_remain_with_options(request, runtime)

    async def query_secret_no_remain_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_secret_no_remain_with_options_async(request, runtime)

    def query_subs_id_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySubsId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubsIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subs_id_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySubsId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubsIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_subs_id(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_subs_id_with_options(request, runtime)

    async def query_subs_id_async(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_subs_id_with_options_async(request, runtime)

    def query_subscription_detail_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySubscriptionDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubscriptionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subscription_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySubscriptionDetail',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubscriptionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_subscription_detail(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_subscription_detail_with_options(request, runtime)

    async def query_subscription_detail_async(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_subscription_detail_with_options_async(request, runtime)

    def release_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ReleaseSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ReleaseSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_secret_no(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_secret_no_with_options(request, runtime)

    async def release_secret_no_async(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_secret_no_with_options_async(request, runtime)

    def unbind_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSubscription',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnbindSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_subscription_with_options_async(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSubscription',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnbindSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_subscription(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_subscription_with_options(request, runtime)

    async def unbind_subscription_async(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_subscription_with_options_async(request, runtime)

    def unlock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnlockSecretNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockSecretNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnlockSecretNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_secret_no(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_secret_no_with_options(request, runtime)

    async def unlock_secret_no_async(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_secret_no_with_options_async(request, runtime)

    def update_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asrmodel_id):
            query['ASRModelId'] = request.asrmodel_id
        if not UtilClient.is_unset(request.asrstatus):
            query['ASRStatus'] = request.asrstatus
        if not UtilClient.is_unset(request.call_display_type):
            query['CallDisplayType'] = request.call_display_type
        if not UtilClient.is_unset(request.call_restrict):
            query['CallRestrict'] = request.call_restrict
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_recording_enabled):
            query['IsRecordingEnabled'] = request.is_recording_enabled
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.phone_no_x):
            query['PhoneNoX'] = request.phone_no_x
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_config):
            query['RingConfig'] = request.ring_config
        if not UtilClient.is_unset(request.subs_id):
            query['SubsId'] = request.subs_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_subscription_with_options(request, runtime)

    async def update_subscription_async(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_subscription_with_options_async(request, runtime)

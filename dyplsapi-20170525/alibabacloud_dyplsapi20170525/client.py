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
        """
        @summary Adds a tracking number for a private number in the AXN binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAxnTrackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAxnTrackNoResponse
        """
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
        """
        @summary Adds a tracking number for a private number in the AXN binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAxnTrackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAxnTrackNoResponse
        """
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
        """
        @summary Adds a tracking number for a private number in the AXN binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAxnTrackNoRequest
        @return: AddAxnTrackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_axn_track_no_with_options(request, runtime)

    async def add_axn_track_no_async(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        """
        @summary Adds a tracking number for a private number in the AXN binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAxnTrackNoRequest
        @return: AddAxnTrackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_axn_track_no_with_options_async(request, runtime)

    def add_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        """
        @summary Adds a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSecretBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSecretBlacklistResponse
        """
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
        """
        @summary Adds a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSecretBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSecretBlacklistResponse
        """
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
        """
        @summary Adds a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSecretBlacklistRequest
        @return: AddSecretBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_secret_blacklist_with_options(request, runtime)

    async def add_secret_blacklist_async(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        """
        @summary Adds a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSecretBlacklistRequest
        @return: AddSecretBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_secret_blacklist_with_options_async(request, runtime)

    def bind_axbcall_with_options(
        self,
        request: dyplsapi_20170525_models.BindAXBCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAXBCallResponse:
        """
        @summary 调用本接口向工作号平台请求为员工B的工作号X建立呼叫绑定（B，X，A），允许B通过X呼叫客户A
        
        @param request: BindAXBCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAXBCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_id):
            query['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_a):
            query['TelA'] = request.tel_a
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAXBCall',
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
            dyplsapi_20170525_models.BindAXBCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_axbcall_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAXBCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAXBCallResponse:
        """
        @summary 调用本接口向工作号平台请求为员工B的工作号X建立呼叫绑定（B，X，A），允许B通过X呼叫客户A
        
        @param request: BindAXBCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAXBCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_id):
            query['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_a):
            query['TelA'] = request.tel_a
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAXBCall',
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
            dyplsapi_20170525_models.BindAXBCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_axbcall(
        self,
        request: dyplsapi_20170525_models.BindAXBCallRequest,
    ) -> dyplsapi_20170525_models.BindAXBCallResponse:
        """
        @summary 调用本接口向工作号平台请求为员工B的工作号X建立呼叫绑定（B，X，A），允许B通过X呼叫客户A
        
        @param request: BindAXBCallRequest
        @return: BindAXBCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_axbcall_with_options(request, runtime)

    async def bind_axbcall_async(
        self,
        request: dyplsapi_20170525_models.BindAXBCallRequest,
    ) -> dyplsapi_20170525_models.BindAXBCallResponse:
        """
        @summary 调用本接口向工作号平台请求为员工B的工作号X建立呼叫绑定（B，X，A），允许B通过X呼叫客户A
        
        @param request: BindAXBCallRequest
        @return: BindAXBCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_axbcall_with_options_async(request, runtime)

    def bind_axb_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        """
        @summary Adds an AXB binding.
        
        @description Before you add an AXB binding, we recommend that you specify role A and role B in the AXB device certificate (ProductKey, DeviceName, and DeviceSecret) in your business scenario. For example, in a taxi-hailing scenario, role A is the passenger and role B is the driver.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxbResponse
        """
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
        if not UtilClient.is_unset(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
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
        """
        @summary Adds an AXB binding.
        
        @description Before you add an AXB binding, we recommend that you specify role A and role B in the AXB device certificate (ProductKey, DeviceName, and DeviceSecret) in your business scenario. For example, in a taxi-hailing scenario, role A is the passenger and role B is the driver.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxbResponse
        """
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
        if not UtilClient.is_unset(request.dtmf_config):
            query['DtmfConfig'] = request.dtmf_config
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
        """
        @summary Adds an AXB binding.
        
        @description Before you add an AXB binding, we recommend that you specify role A and role B in the AXB device certificate (ProductKey, DeviceName, and DeviceSecret) in your business scenario. For example, in a taxi-hailing scenario, role A is the passenger and role B is the driver.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxbRequest
        @return: BindAxbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_axb_with_options(request, runtime)

    async def bind_axb_async(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        """
        @summary Adds an AXB binding.
        
        @description Before you add an AXB binding, we recommend that you specify role A and role B in the AXB device certificate (ProductKey, DeviceName, and DeviceSecret) in your business scenario. For example, in a taxi-hailing scenario, role A is the passenger and role B is the driver.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxbRequest
        @return: BindAxbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_axb_with_options_async(request, runtime)

    def bind_axg_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        """
        @summary Adds an AXG binding.
        
        @description An AXG protection solution can be configured to meet the requirements for grading users, limiting the scope of calls, and restricting order snatching. The letter G represents a phone number group to which you can add phone numbers as needed.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxgResponse
        """
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
        """
        @summary Adds an AXG binding.
        
        @description An AXG protection solution can be configured to meet the requirements for grading users, limiting the scope of calls, and restricting order snatching. The letter G represents a phone number group to which you can add phone numbers as needed.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxgResponse
        """
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
        """
        @summary Adds an AXG binding.
        
        @description An AXG protection solution can be configured to meet the requirements for grading users, limiting the scope of calls, and restricting order snatching. The letter G represents a phone number group to which you can add phone numbers as needed.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxgRequest
        @return: BindAxgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_axg_with_options(request, runtime)

    async def bind_axg_async(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        """
        @summary Adds an AXG binding.
        
        @description An AXG protection solution can be configured to meet the requirements for grading users, limiting the scope of calls, and restricting order snatching. The letter G represents a phone number group to which you can add phone numbers as needed.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxgRequest
        @return: BindAxgResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_axg_with_options_async(request, runtime)

    def bind_axn_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        """
        @summary Adds an AXN binding.
        
        @description >  An AXN private number is a dedicated private number assigned to phone number A. When an N-side number is used to call phone number X, the call is forwarded to phone number A.
        
        @param request: BindAxnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxnResponse
        """
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
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
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
        """
        @summary Adds an AXN binding.
        
        @description >  An AXN private number is a dedicated private number assigned to phone number A. When an N-side number is used to call phone number X, the call is forwarded to phone number A.
        
        @param request: BindAxnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxnResponse
        """
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
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
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
        """
        @summary Adds an AXN binding.
        
        @description >  An AXN private number is a dedicated private number assigned to phone number A. When an N-side number is used to call phone number X, the call is forwarded to phone number A.
        
        @param request: BindAxnRequest
        @return: BindAxnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_axn_with_options(request, runtime)

    async def bind_axn_async(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        """
        @summary Adds an AXN binding.
        
        @description >  An AXN private number is a dedicated private number assigned to phone number A. When an N-side number is used to call phone number X, the call is forwarded to phone number A.
        
        @param request: BindAxnRequest
        @return: BindAxnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_axn_with_options_async(request, runtime)

    def bind_axn_extension_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        """
        @summary Adds an AXN extension binding.
        
        @description Before you add an AXN extension binding, confirm phone number A and phone number N in the business scenario. Phone number A belongs to a customer, and phone number X is the private number assigned to the customer. When any other phone number is used to call phone number X and the extension, the call is transferred to phone number A. When phone number A is used to call phone number X, the call is transferred to the default phone number B that is specified during the phone number binding.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxnExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxnExtensionResponse
        """
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
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
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
        """
        @summary Adds an AXN extension binding.
        
        @description Before you add an AXN extension binding, confirm phone number A and phone number N in the business scenario. Phone number A belongs to a customer, and phone number X is the private number assigned to the customer. When any other phone number is used to call phone number X and the extension, the call is transferred to phone number A. When phone number A is used to call phone number X, the call is transferred to the default phone number B that is specified during the phone number binding.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxnExtensionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAxnExtensionResponse
        """
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
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
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
        """
        @summary Adds an AXN extension binding.
        
        @description Before you add an AXN extension binding, confirm phone number A and phone number N in the business scenario. Phone number A belongs to a customer, and phone number X is the private number assigned to the customer. When any other phone number is used to call phone number X and the extension, the call is transferred to phone number A. When phone number A is used to call phone number X, the call is transferred to the default phone number B that is specified during the phone number binding.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxnExtensionRequest
        @return: BindAxnExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_axn_extension_with_options(request, runtime)

    async def bind_axn_extension_async(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        """
        @summary Adds an AXN extension binding.
        
        @description Before you add an AXN extension binding, confirm phone number A and phone number N in the business scenario. Phone number A belongs to a customer, and phone number X is the private number assigned to the customer. When any other phone number is used to call phone number X and the extension, the call is transferred to phone number A. When phone number A is used to call phone number X, the call is transferred to the default phone number B that is specified during the phone number binding.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: BindAxnExtensionRequest
        @return: BindAxnExtensionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_axn_extension_with_options_async(request, runtime)

    def bind_batch_axg_with_options(
        self,
        tmp_req: dyplsapi_20170525_models.BindBatchAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindBatchAxgResponse:
        """
        @param tmp_req: BindBatchAxgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindBatchAxgResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.BindBatchAxgShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.axg_bind_list):
            request.axg_bind_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.axg_bind_list, 'AxgBindList', 'json')
        query = {}
        if not UtilClient.is_unset(request.axg_bind_list_shrink):
            query['AxgBindList'] = request.axg_bind_list_shrink
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
            action='BindBatchAxg',
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
            dyplsapi_20170525_models.BindBatchAxgResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_batch_axg_with_options_async(
        self,
        tmp_req: dyplsapi_20170525_models.BindBatchAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindBatchAxgResponse:
        """
        @param tmp_req: BindBatchAxgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindBatchAxgResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.BindBatchAxgShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.axg_bind_list):
            request.axg_bind_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.axg_bind_list, 'AxgBindList', 'json')
        query = {}
        if not UtilClient.is_unset(request.axg_bind_list_shrink):
            query['AxgBindList'] = request.axg_bind_list_shrink
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
            action='BindBatchAxg',
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
            dyplsapi_20170525_models.BindBatchAxgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_batch_axg(
        self,
        request: dyplsapi_20170525_models.BindBatchAxgRequest,
    ) -> dyplsapi_20170525_models.BindBatchAxgResponse:
        """
        @param request: BindBatchAxgRequest
        @return: BindBatchAxgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_batch_axg_with_options(request, runtime)

    async def bind_batch_axg_async(
        self,
        request: dyplsapi_20170525_models.BindBatchAxgRequest,
    ) -> dyplsapi_20170525_models.BindBatchAxgResponse:
        """
        @param request: BindBatchAxgRequest
        @return: BindBatchAxgResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_batch_axg_with_options_async(request, runtime)

    def bind_xbwith_options(
        self,
        request: dyplsapi_20170525_models.BindXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindXBResponse:
        """
        @summary 平台指定工作号X 和员工号B建立关联，完成X 实名认证，绑定生效后，所有X 的呼叫都会转接到B
        
        @param request: BindXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_b):
            query['TelB'] = request.tel_b
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindXB',
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
            dyplsapi_20170525_models.BindXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_xbwith_options_async(
        self,
        request: dyplsapi_20170525_models.BindXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindXBResponse:
        """
        @summary 平台指定工作号X 和员工号B建立关联，完成X 实名认证，绑定生效后，所有X 的呼叫都会转接到B
        
        @param request: BindXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_b):
            query['TelB'] = request.tel_b
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindXB',
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
            dyplsapi_20170525_models.BindXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_xb(
        self,
        request: dyplsapi_20170525_models.BindXBRequest,
    ) -> dyplsapi_20170525_models.BindXBResponse:
        """
        @summary 平台指定工作号X 和员工号B建立关联，完成X 实名认证，绑定生效后，所有X 的呼叫都会转接到B
        
        @param request: BindXBRequest
        @return: BindXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_xbwith_options(request, runtime)

    async def bind_xb_async(
        self,
        request: dyplsapi_20170525_models.BindXBRequest,
    ) -> dyplsapi_20170525_models.BindXBResponse:
        """
        @summary 平台指定工作号X 和员工号B建立关联，完成X 实名认证，绑定生效后，所有X 的呼叫都会转接到B
        
        @param request: BindXBRequest
        @return: BindXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_xbwith_options_async(request, runtime)

    def buy_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        """
        @summary Purchases a phone number.
        
        @description    After you create a phone number pool in the Phone Number Protection console, the phone number pool is empty by default. You must purchase phone numbers and add them to the phone number pool.
        Before you call this operation, make sure that you are familiar with the [pricing](https://help.aliyun.com/document_detail/59825.html) of Phone Number Protection.
        When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before you call this operation to purchase a phone number, check the quantity of phone numbers available for purchase by using the [QuerySecretNoRemain](https://help.aliyun.com/document_detail/111699.html) operation.
        The account used to purchase a phone number must be an enterprise account that has passed real-name verification. For more information about how to perform real-name verification, see [Enterprise verification FAQs](https://help.aliyun.com/document_detail/37172.html).
        
        @param request: BuySecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuySecretNoResponse
        """
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
        """
        @summary Purchases a phone number.
        
        @description    After you create a phone number pool in the Phone Number Protection console, the phone number pool is empty by default. You must purchase phone numbers and add them to the phone number pool.
        Before you call this operation, make sure that you are familiar with the [pricing](https://help.aliyun.com/document_detail/59825.html) of Phone Number Protection.
        When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before you call this operation to purchase a phone number, check the quantity of phone numbers available for purchase by using the [QuerySecretNoRemain](https://help.aliyun.com/document_detail/111699.html) operation.
        The account used to purchase a phone number must be an enterprise account that has passed real-name verification. For more information about how to perform real-name verification, see [Enterprise verification FAQs](https://help.aliyun.com/document_detail/37172.html).
        
        @param request: BuySecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuySecretNoResponse
        """
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
        """
        @summary Purchases a phone number.
        
        @description    After you create a phone number pool in the Phone Number Protection console, the phone number pool is empty by default. You must purchase phone numbers and add them to the phone number pool.
        Before you call this operation, make sure that you are familiar with the [pricing](https://help.aliyun.com/document_detail/59825.html) of Phone Number Protection.
        When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before you call this operation to purchase a phone number, check the quantity of phone numbers available for purchase by using the [QuerySecretNoRemain](https://help.aliyun.com/document_detail/111699.html) operation.
        The account used to purchase a phone number must be an enterprise account that has passed real-name verification. For more information about how to perform real-name verification, see [Enterprise verification FAQs](https://help.aliyun.com/document_detail/37172.html).
        
        @param request: BuySecretNoRequest
        @return: BuySecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.buy_secret_no_with_options(request, runtime)

    async def buy_secret_no_async(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        """
        @summary Purchases a phone number.
        
        @description    After you create a phone number pool in the Phone Number Protection console, the phone number pool is empty by default. You must purchase phone numbers and add them to the phone number pool.
        Before you call this operation, make sure that you are familiar with the [pricing](https://help.aliyun.com/document_detail/59825.html) of Phone Number Protection.
        When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before you call this operation to purchase a phone number, check the quantity of phone numbers available for purchase by using the [QuerySecretNoRemain](https://help.aliyun.com/document_detail/111699.html) operation.
        The account used to purchase a phone number must be an enterprise account that has passed real-name verification. For more information about how to perform real-name verification, see [Enterprise verification FAQs](https://help.aliyun.com/document_detail/37172.html).
        
        @param request: BuySecretNoRequest
        @return: BuySecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.buy_secret_no_with_options_async(request, runtime)

    def cancel_pick_up_waybill_with_options(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        """
        @summary Cancels a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CancelPickUpWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPickUpWaybillResponse
        """
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
        """
        @summary Cancels a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CancelPickUpWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelPickUpWaybillResponse
        """
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
        """
        @summary Cancels a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CancelPickUpWaybillRequest
        @return: CancelPickUpWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_pick_up_waybill_with_options(request, runtime)

    async def cancel_pick_up_waybill_async(
        self,
        request: dyplsapi_20170525_models.CancelPickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CancelPickUpWaybillResponse:
        """
        @summary Cancels a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CancelPickUpWaybillRequest
        @return: CancelPickUpWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_pick_up_waybill_with_options_async(request, runtime)

    def config_xwith_options(
        self,
        tmp_req: dyplsapi_20170525_models.ConfigXRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfigXResponse:
        """
        @summary 配置X号码，单独对工作号的话音呼叫、企业名片等通信功能进行配置操作
        
        @param tmp_req: ConfigXRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigXResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.ConfigXShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sequence_calls):
            request.sequence_calls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sequence_calls, 'SequenceCalls', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_ability):
            query['CallAbility'] = request.call_ability
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.gnflag):
            query['GNFlag'] = request.gnflag
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sequence_calls_shrink):
            query['SequenceCalls'] = request.sequence_calls_shrink
        if not UtilClient.is_unset(request.sequence_mode):
            query['SequenceMode'] = request.sequence_mode
        if not UtilClient.is_unset(request.sms_ability):
            query['SmsAbility'] = request.sms_ability
        if not UtilClient.is_unset(request.sms_sign_mode):
            query['SmsSignMode'] = request.sms_sign_mode
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigX',
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
            dyplsapi_20170525_models.ConfigXResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_xwith_options_async(
        self,
        tmp_req: dyplsapi_20170525_models.ConfigXRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfigXResponse:
        """
        @summary 配置X号码，单独对工作号的话音呼叫、企业名片等通信功能进行配置操作
        
        @param tmp_req: ConfigXRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigXResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.ConfigXShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sequence_calls):
            request.sequence_calls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sequence_calls, 'SequenceCalls', 'json')
        query = {}
        if not UtilClient.is_unset(request.call_ability):
            query['CallAbility'] = request.call_ability
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.gnflag):
            query['GNFlag'] = request.gnflag
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sequence_calls_shrink):
            query['SequenceCalls'] = request.sequence_calls_shrink
        if not UtilClient.is_unset(request.sequence_mode):
            query['SequenceMode'] = request.sequence_mode
        if not UtilClient.is_unset(request.sms_ability):
            query['SmsAbility'] = request.sms_ability
        if not UtilClient.is_unset(request.sms_sign_mode):
            query['SmsSignMode'] = request.sms_sign_mode
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigX',
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
            dyplsapi_20170525_models.ConfigXResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_x(
        self,
        request: dyplsapi_20170525_models.ConfigXRequest,
    ) -> dyplsapi_20170525_models.ConfigXResponse:
        """
        @summary 配置X号码，单独对工作号的话音呼叫、企业名片等通信功能进行配置操作
        
        @param request: ConfigXRequest
        @return: ConfigXResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_xwith_options(request, runtime)

    async def config_x_async(
        self,
        request: dyplsapi_20170525_models.ConfigXRequest,
    ) -> dyplsapi_20170525_models.ConfigXResponse:
        """
        @summary 配置X号码，单独对工作号的话音呼叫、企业名片等通信功能进行配置操作
        
        @param request: ConfigXRequest
        @return: ConfigXResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_xwith_options_async(request, runtime)

    def create_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        """
        @summary Creates number group G.
        
        @description Before you add an AXG binding, you must purchase phone number X, create number group G, and then add phone numbers to number group G. If you do not add phone numbers to number group G after you create number group G, you can call the [OperateAxgGroup](https://help.aliyun.com/document_detail/110252.htm) operation to add phone numbers to number group G.
        >  Up to 2,000 number groups G can be added for a single phone number pool.
        
        @param request: CreateAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAxgGroupResponse
        """
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
        """
        @summary Creates number group G.
        
        @description Before you add an AXG binding, you must purchase phone number X, create number group G, and then add phone numbers to number group G. If you do not add phone numbers to number group G after you create number group G, you can call the [OperateAxgGroup](https://help.aliyun.com/document_detail/110252.htm) operation to add phone numbers to number group G.
        >  Up to 2,000 number groups G can be added for a single phone number pool.
        
        @param request: CreateAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAxgGroupResponse
        """
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
        """
        @summary Creates number group G.
        
        @description Before you add an AXG binding, you must purchase phone number X, create number group G, and then add phone numbers to number group G. If you do not add phone numbers to number group G after you create number group G, you can call the [OperateAxgGroup](https://help.aliyun.com/document_detail/110252.htm) operation to add phone numbers to number group G.
        >  Up to 2,000 number groups G can be added for a single phone number pool.
        
        @param request: CreateAxgGroupRequest
        @return: CreateAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_axg_group_with_options(request, runtime)

    async def create_axg_group_async(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        """
        @summary Creates number group G.
        
        @description Before you add an AXG binding, you must purchase phone number X, create number group G, and then add phone numbers to number group G. If you do not add phone numbers to number group G after you create number group G, you can call the [OperateAxgGroup](https://help.aliyun.com/document_detail/110252.htm) operation to add phone numbers to number group G.
        >  Up to 2,000 number groups G can be added for a single phone number pool.
        
        @param request: CreateAxgGroupRequest
        @return: CreateAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_axg_group_with_options_async(request, runtime)

    def create_pick_up_waybill_with_options(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        """
        @summary Creates a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreatePickUpWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePickUpWaybillResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_address):
            request.consignee_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.consignee_address, 'ConsigneeAddress', 'json')
        if not UtilClient.is_unset(tmp_req.goods_infos):
            request.goods_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not UtilClient.is_unset(tmp_req.send_address):
            request.send_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_address, 'SendAddress', 'json')
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
        """
        @summary Creates a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreatePickUpWaybillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePickUpWaybillResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_address):
            request.consignee_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.consignee_address, 'ConsigneeAddress', 'json')
        if not UtilClient.is_unset(tmp_req.goods_infos):
            request.goods_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.goods_infos, 'GoodsInfos', 'json')
        if not UtilClient.is_unset(tmp_req.send_address):
            request.send_address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.send_address, 'SendAddress', 'json')
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
        """
        @summary Creates a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreatePickUpWaybillRequest
        @return: CreatePickUpWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pick_up_waybill_with_options(request, runtime)

    async def create_pick_up_waybill_async(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillResponse:
        """
        @summary Creates a door-to-door delivery order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreatePickUpWaybillRequest
        @return: CreatePickUpWaybillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pick_up_waybill_with_options_async(request, runtime)

    def create_pick_up_waybill_pre_query_with_options(
        self,
        tmp_req: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        """
        @summary Queries a pickup order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreatePickUpWaybillPreQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePickUpWaybillPreQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillPreQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_info):
            request.consignee_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.consignee_info, 'ConsigneeInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sender_info):
            request.sender_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sender_info, 'SenderInfo', 'json')
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
        """
        @summary Queries a pickup order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreatePickUpWaybillPreQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePickUpWaybillPreQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dyplsapi_20170525_models.CreatePickUpWaybillPreQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.consignee_info):
            request.consignee_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.consignee_info, 'ConsigneeInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sender_info):
            request.sender_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sender_info, 'SenderInfo', 'json')
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
        """
        @summary Queries a pickup order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreatePickUpWaybillPreQueryRequest
        @return: CreatePickUpWaybillPreQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pick_up_waybill_pre_query_with_options(request, runtime)

    async def create_pick_up_waybill_pre_query_async(
        self,
        request: dyplsapi_20170525_models.CreatePickUpWaybillPreQueryRequest,
    ) -> dyplsapi_20170525_models.CreatePickUpWaybillPreQueryResponse:
        """
        @summary Queries a pickup order.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreatePickUpWaybillPreQueryRequest
        @return: CreatePickUpWaybillPreQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pick_up_waybill_pre_query_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        request: dyplsapi_20170525_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary B向A 发短信，客户端获取“短信标签”，尾部添加“标签”。通过“标签”解析被叫A，发短信到A。
        
        @param request: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_no):
            query['CalledNo'] = request.called_no
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.calling_no):
            query['CallingNo'] = request.calling_no
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
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
            dyplsapi_20170525_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        request: dyplsapi_20170525_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary B向A 发短信，客户端获取“短信标签”，尾部添加“标签”。通过“标签”解析被叫A，发短信到A。
        
        @param request: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_no):
            query['CalledNo'] = request.called_no
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.calling_no):
            query['CallingNo'] = request.calling_no
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
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
            dyplsapi_20170525_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: dyplsapi_20170525_models.CreateSmsSignRequest,
    ) -> dyplsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary B向A 发短信，客户端获取“短信标签”，尾部添加“标签”。通过“标签”解析被叫A，发短信到A。
        
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: dyplsapi_20170525_models.CreateSmsSignRequest,
    ) -> dyplsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary B向A 发短信，客户端获取“短信标签”，尾部添加“标签”。通过“标签”解析被叫A，发短信到A。
        
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def delete_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.DeleteAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteAxgGroupResponse:
        """
        @param request: DeleteAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAxgGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteAxgGroup',
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
            dyplsapi_20170525_models.DeleteAxgGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_axg_group_with_options_async(
        self,
        request: dyplsapi_20170525_models.DeleteAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteAxgGroupResponse:
        """
        @param request: DeleteAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAxgGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
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
            action='DeleteAxgGroup',
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
            dyplsapi_20170525_models.DeleteAxgGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_axg_group(
        self,
        request: dyplsapi_20170525_models.DeleteAxgGroupRequest,
    ) -> dyplsapi_20170525_models.DeleteAxgGroupResponse:
        """
        @param request: DeleteAxgGroupRequest
        @return: DeleteAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_axg_group_with_options(request, runtime)

    async def delete_axg_group_async(
        self,
        request: dyplsapi_20170525_models.DeleteAxgGroupRequest,
    ) -> dyplsapi_20170525_models.DeleteAxgGroupResponse:
        """
        @param request: DeleteAxgGroupRequest
        @return: DeleteAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_axg_group_with_options_async(request, runtime)

    def delete_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        """
        @summary Deletes a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSecretBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretBlacklistResponse
        """
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
        """
        @summary Deletes a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSecretBlacklistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecretBlacklistResponse
        """
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
        """
        @summary Deletes a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSecretBlacklistRequest
        @return: DeleteSecretBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_blacklist_with_options(request, runtime)

    async def delete_secret_blacklist_async(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        """
        @summary Deletes a blacklist.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSecretBlacklistRequest
        @return: DeleteSecretBlacklistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_blacklist_with_options_async(request, runtime)

    def get_secret_asr_detail_with_options(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        """
        @summary Obtains the details of the automatic speech recognition (ASR) result.
        
        @description Before you call the GetSecretAsrDetail operation, set the ASRStatus parameter to true in the [BindAxn operation](https://help.aliyun.com/document_detail/400483.html). This ensures that you can obtain the ASR result properly.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetSecretAsrDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretAsrDetailResponse
        """
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
        """
        @summary Obtains the details of the automatic speech recognition (ASR) result.
        
        @description Before you call the GetSecretAsrDetail operation, set the ASRStatus parameter to true in the [BindAxn operation](https://help.aliyun.com/document_detail/400483.html). This ensures that you can obtain the ASR result properly.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetSecretAsrDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecretAsrDetailResponse
        """
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
        """
        @summary Obtains the details of the automatic speech recognition (ASR) result.
        
        @description Before you call the GetSecretAsrDetail operation, set the ASRStatus parameter to true in the [BindAxn operation](https://help.aliyun.com/document_detail/400483.html). This ensures that you can obtain the ASR result properly.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetSecretAsrDetailRequest
        @return: GetSecretAsrDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_asr_detail_with_options(request, runtime)

    async def get_secret_asr_detail_async(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        """
        @summary Obtains the details of the automatic speech recognition (ASR) result.
        
        @description Before you call the GetSecretAsrDetail operation, set the ASRStatus parameter to true in the [BindAxn operation](https://help.aliyun.com/document_detail/400483.html). This ensures that you can obtain the ASR result properly.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetSecretAsrDetailRequest
        @return: GetSecretAsrDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_asr_detail_with_options_async(request, runtime)

    def get_total_public_url_with_options(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        """
        @summary Obtains the download URL of a recorded ringing tone.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetTotalPublicUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTotalPublicUrlResponse
        """
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
        """
        @summary Obtains the download URL of a recorded ringing tone.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetTotalPublicUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTotalPublicUrlResponse
        """
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
        """
        @summary Obtains the download URL of a recorded ringing tone.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetTotalPublicUrlRequest
        @return: GetTotalPublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_total_public_url_with_options(request, runtime)

    async def get_total_public_url_async(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        """
        @summary Obtains the download URL of a recorded ringing tone.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetTotalPublicUrlRequest
        @return: GetTotalPublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_total_public_url_with_options_async(request, runtime)

    def get_xconfig_with_options(
        self,
        request: dyplsapi_20170525_models.GetXConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetXConfigResponse:
        """
        @summary 获取X号码配置信息
        
        @param request: GetXConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetXConfig',
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
            dyplsapi_20170525_models.GetXConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_xconfig_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetXConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetXConfigResponse:
        """
        @summary 获取X号码配置信息
        
        @param request: GetXConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetXConfig',
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
            dyplsapi_20170525_models.GetXConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_xconfig(
        self,
        request: dyplsapi_20170525_models.GetXConfigRequest,
    ) -> dyplsapi_20170525_models.GetXConfigResponse:
        """
        @summary 获取X号码配置信息
        
        @param request: GetXConfigRequest
        @return: GetXConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_xconfig_with_options(request, runtime)

    async def get_xconfig_async(
        self,
        request: dyplsapi_20170525_models.GetXConfigRequest,
    ) -> dyplsapi_20170525_models.GetXConfigResponse:
        """
        @summary 获取X号码配置信息
        
        @param request: GetXConfigRequest
        @return: GetXConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_xconfig_with_options_async(request, runtime)

    def get_xdefault_config_with_options(
        self,
        request: dyplsapi_20170525_models.GetXDefaultConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetXDefaultConfigResponse:
        """
        @summary 获取X号码默认配置信息
        
        @param request: GetXDefaultConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXDefaultConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetXDefaultConfig',
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
            dyplsapi_20170525_models.GetXDefaultConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_xdefault_config_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetXDefaultConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetXDefaultConfigResponse:
        """
        @summary 获取X号码默认配置信息
        
        @param request: GetXDefaultConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetXDefaultConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetXDefaultConfig',
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
            dyplsapi_20170525_models.GetXDefaultConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_xdefault_config(
        self,
        request: dyplsapi_20170525_models.GetXDefaultConfigRequest,
    ) -> dyplsapi_20170525_models.GetXDefaultConfigResponse:
        """
        @summary 获取X号码默认配置信息
        
        @param request: GetXDefaultConfigRequest
        @return: GetXDefaultConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_xdefault_config_with_options(request, runtime)

    async def get_xdefault_config_async(
        self,
        request: dyplsapi_20170525_models.GetXDefaultConfigRequest,
    ) -> dyplsapi_20170525_models.GetXDefaultConfigResponse:
        """
        @summary 获取X号码默认配置信息
        
        @param request: GetXDefaultConfigRequest
        @return: GetXDefaultConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_xdefault_config_with_options_async(request, runtime)

    def list_xtelephones_with_options(
        self,
        request: dyplsapi_20170525_models.ListXTelephonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ListXTelephonesResponse:
        """
        @summary 查询客户名下X号码列表
        
        @param request: ListXTelephonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListXTelephonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListXTelephones',
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
            dyplsapi_20170525_models.ListXTelephonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_xtelephones_with_options_async(
        self,
        request: dyplsapi_20170525_models.ListXTelephonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ListXTelephonesResponse:
        """
        @summary 查询客户名下X号码列表
        
        @param request: ListXTelephonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListXTelephonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListXTelephones',
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
            dyplsapi_20170525_models.ListXTelephonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_xtelephones(
        self,
        request: dyplsapi_20170525_models.ListXTelephonesRequest,
    ) -> dyplsapi_20170525_models.ListXTelephonesResponse:
        """
        @summary 查询客户名下X号码列表
        
        @param request: ListXTelephonesRequest
        @return: ListXTelephonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_xtelephones_with_options(request, runtime)

    async def list_xtelephones_async(
        self,
        request: dyplsapi_20170525_models.ListXTelephonesRequest,
    ) -> dyplsapi_20170525_models.ListXTelephonesResponse:
        """
        @summary 查询客户名下X号码列表
        
        @param request: ListXTelephonesRequest
        @return: ListXTelephonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_xtelephones_with_options_async(request, runtime)

    def lock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        """
        @summary Locks a phone number.
        
        @description After a phone number is locked, the locked phone number cannot be selected when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockSecretNoResponse
        """
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
        """
        @summary Locks a phone number.
        
        @description After a phone number is locked, the locked phone number cannot be selected when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockSecretNoResponse
        """
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
        """
        @summary Locks a phone number.
        
        @description After a phone number is locked, the locked phone number cannot be selected when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockSecretNoRequest
        @return: LockSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_secret_no_with_options(request, runtime)

    async def lock_secret_no_async(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        """
        @summary Locks a phone number.
        
        @description After a phone number is locked, the locked phone number cannot be selected when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockSecretNoRequest
        @return: LockSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_secret_no_with_options_async(request, runtime)

    def operate_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        """
        @summary Modifies number group G.
        
        @description After you create number group G, you can call the OperateAxgGroup operation to modify number group G. For example, you can add phone numbers to number group G, delete phone numbers from number group G, and replace all phone numbers in number group G.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAxgGroupResponse
        """
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
        """
        @summary Modifies number group G.
        
        @description After you create number group G, you can call the OperateAxgGroup operation to modify number group G. For example, you can add phone numbers to number group G, delete phone numbers from number group G, and replace all phone numbers in number group G.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateAxgGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAxgGroupResponse
        """
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
        """
        @summary Modifies number group G.
        
        @description After you create number group G, you can call the OperateAxgGroup operation to modify number group G. For example, you can add phone numbers to number group G, delete phone numbers from number group G, and replace all phone numbers in number group G.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateAxgGroupRequest
        @return: OperateAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_axg_group_with_options(request, runtime)

    async def operate_axg_group_async(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        """
        @summary Modifies number group G.
        
        @description After you create number group G, you can call the OperateAxgGroup operation to modify number group G. For example, you can add phone numbers to number group G, delete phone numbers from number group G, and replace all phone numbers in number group G.
        ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateAxgGroupRequest
        @return: OperateAxgGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_axg_group_with_options_async(request, runtime)

    def operate_black_no_with_options(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        """
        @summary Adds a phone number to a blacklist or deletes a phone number from a blacklist.
        
        @description The OperateBlackNo operation supports the following number pool types: AXN, AXN extension, and 95AXN.
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateBlackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBlackNoResponse
        """
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
        """
        @summary Adds a phone number to a blacklist or deletes a phone number from a blacklist.
        
        @description The OperateBlackNo operation supports the following number pool types: AXN, AXN extension, and 95AXN.
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateBlackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBlackNoResponse
        """
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
        """
        @summary Adds a phone number to a blacklist or deletes a phone number from a blacklist.
        
        @description The OperateBlackNo operation supports the following number pool types: AXN, AXN extension, and 95AXN.
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateBlackNoRequest
        @return: OperateBlackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_black_no_with_options(request, runtime)

    async def operate_black_no_async(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        """
        @summary Adds a phone number to a blacklist or deletes a phone number from a blacklist.
        
        @description The OperateBlackNo operation supports the following number pool types: AXN, AXN extension, and 95AXN.
        ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: OperateBlackNoRequest
        @return: OperateBlackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_black_no_with_options_async(request, runtime)

    def query_phone_no_aby_track_no_with_options(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        """
        @summary Queries the details about a tracking number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneNoAByTrackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneNoAByTrackNoResponse
        """
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
        """
        @summary Queries the details about a tracking number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneNoAByTrackNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneNoAByTrackNoResponse
        """
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
        """
        @summary Queries the details about a tracking number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneNoAByTrackNoRequest
        @return: QueryPhoneNoAByTrackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_phone_no_aby_track_no_with_options(request, runtime)

    async def query_phone_no_aby_track_no_async(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        """
        @summary Queries the details about a tracking number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryPhoneNoAByTrackNoRequest
        @return: QueryPhoneNoAByTrackNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_phone_no_aby_track_no_with_options_async(request, runtime)

    def query_record_file_download_url_with_options(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        """
        @summary Obtains the download URL of a recording file.
        
        @description If the recording feature is enabled for a binding, all calls made by the bound phone numbers are recorded. You can obtain the download URL of a recording file by calling the QueryRecordFileDownloadUrl operation and download the recording file.
        >  We recommend that you subscribe to [the recording status report SecretRecording](https://help.aliyun.com/document_detail/109198.html). The values of the response parameters in SecretRecording can be used as the values of the request parameters for downloading a recording file.
        ### [](#)Procedure for obtaining a recording file
        1.  Specify the request parameter in an update or binding operation to enable the recording feature.
        2.  Subscribe to recording message receipts in the Phone Number Protection console.
        3.  After a recording message receipt is returned, call the QueryRecordFileDownloadUrl operation to obtain the download URL of the recording file, and download the recording file.
        >
        A download URL is valid for 2 hours. Download the recording file as soon as possible after obtaining a download URL.
        The storage period of recording files is 30 days. You can download only the recording files of calls recorded in the last 30 days.
        
        @param request: QueryRecordFileDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRecordFileDownloadUrlResponse
        """
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
        """
        @summary Obtains the download URL of a recording file.
        
        @description If the recording feature is enabled for a binding, all calls made by the bound phone numbers are recorded. You can obtain the download URL of a recording file by calling the QueryRecordFileDownloadUrl operation and download the recording file.
        >  We recommend that you subscribe to [the recording status report SecretRecording](https://help.aliyun.com/document_detail/109198.html). The values of the response parameters in SecretRecording can be used as the values of the request parameters for downloading a recording file.
        ### [](#)Procedure for obtaining a recording file
        1.  Specify the request parameter in an update or binding operation to enable the recording feature.
        2.  Subscribe to recording message receipts in the Phone Number Protection console.
        3.  After a recording message receipt is returned, call the QueryRecordFileDownloadUrl operation to obtain the download URL of the recording file, and download the recording file.
        >
        A download URL is valid for 2 hours. Download the recording file as soon as possible after obtaining a download URL.
        The storage period of recording files is 30 days. You can download only the recording files of calls recorded in the last 30 days.
        
        @param request: QueryRecordFileDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRecordFileDownloadUrlResponse
        """
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
        """
        @summary Obtains the download URL of a recording file.
        
        @description If the recording feature is enabled for a binding, all calls made by the bound phone numbers are recorded. You can obtain the download URL of a recording file by calling the QueryRecordFileDownloadUrl operation and download the recording file.
        >  We recommend that you subscribe to [the recording status report SecretRecording](https://help.aliyun.com/document_detail/109198.html). The values of the response parameters in SecretRecording can be used as the values of the request parameters for downloading a recording file.
        ### [](#)Procedure for obtaining a recording file
        1.  Specify the request parameter in an update or binding operation to enable the recording feature.
        2.  Subscribe to recording message receipts in the Phone Number Protection console.
        3.  After a recording message receipt is returned, call the QueryRecordFileDownloadUrl operation to obtain the download URL of the recording file, and download the recording file.
        >
        A download URL is valid for 2 hours. Download the recording file as soon as possible after obtaining a download URL.
        The storage period of recording files is 30 days. You can download only the recording files of calls recorded in the last 30 days.
        
        @param request: QueryRecordFileDownloadUrlRequest
        @return: QueryRecordFileDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_record_file_download_url_with_options(request, runtime)

    async def query_record_file_download_url_async(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        """
        @summary Obtains the download URL of a recording file.
        
        @description If the recording feature is enabled for a binding, all calls made by the bound phone numbers are recorded. You can obtain the download URL of a recording file by calling the QueryRecordFileDownloadUrl operation and download the recording file.
        >  We recommend that you subscribe to [the recording status report SecretRecording](https://help.aliyun.com/document_detail/109198.html). The values of the response parameters in SecretRecording can be used as the values of the request parameters for downloading a recording file.
        ### [](#)Procedure for obtaining a recording file
        1.  Specify the request parameter in an update or binding operation to enable the recording feature.
        2.  Subscribe to recording message receipts in the Phone Number Protection console.
        3.  After a recording message receipt is returned, call the QueryRecordFileDownloadUrl operation to obtain the download URL of the recording file, and download the recording file.
        >
        A download URL is valid for 2 hours. Download the recording file as soon as possible after obtaining a download URL.
        The storage period of recording files is 30 days. You can download only the recording files of calls recorded in the last 30 days.
        
        @param request: QueryRecordFileDownloadUrlRequest
        @return: QueryRecordFileDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_record_file_download_url_with_options_async(request, runtime)

    def query_secret_no_detail_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        """
        @summary Queries the attributes of a private number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySecretNoDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySecretNoDetailResponse
        """
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
        """
        @summary Queries the attributes of a private number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySecretNoDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySecretNoDetailResponse
        """
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
        """
        @summary Queries the attributes of a private number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySecretNoDetailRequest
        @return: QuerySecretNoDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_secret_no_detail_with_options(request, runtime)

    async def query_secret_no_detail_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoDetailResponse:
        """
        @summary Queries the attributes of a private number.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySecretNoDetailRequest
        @return: QuerySecretNoDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_secret_no_detail_with_options_async(request, runtime)

    def query_secret_no_remain_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        """
        @summary Queries the quantity of remaining phone numbers available for online purchase.
        
        @description When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before calling the [BuySecretNo](~~BuySecretNo~~) operation to purchase a phone number, call the [QuerySecretNoRemain](~~QuerySecretNoRemain~~) operation to query the quantity of remaining phone numbers available for online purchase.
        
        @param request: QuerySecretNoRemainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySecretNoRemainResponse
        """
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
        """
        @summary Queries the quantity of remaining phone numbers available for online purchase.
        
        @description When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before calling the [BuySecretNo](~~BuySecretNo~~) operation to purchase a phone number, call the [QuerySecretNoRemain](~~QuerySecretNoRemain~~) operation to query the quantity of remaining phone numbers available for online purchase.
        
        @param request: QuerySecretNoRemainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySecretNoRemainResponse
        """
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
        """
        @summary Queries the quantity of remaining phone numbers available for online purchase.
        
        @description When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before calling the [BuySecretNo](~~BuySecretNo~~) operation to purchase a phone number, call the [QuerySecretNoRemain](~~QuerySecretNoRemain~~) operation to query the quantity of remaining phone numbers available for online purchase.
        
        @param request: QuerySecretNoRemainRequest
        @return: QuerySecretNoRemainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_secret_no_remain_with_options(request, runtime)

    async def query_secret_no_remain_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        """
        @summary Queries the quantity of remaining phone numbers available for online purchase.
        
        @description When purchasing a phone number, specify the home location. If no sufficient phone numbers are available for purchase in the home location, the purchase of the phone number fails. Before calling the [BuySecretNo](~~BuySecretNo~~) operation to purchase a phone number, call the [QuerySecretNoRemain](~~QuerySecretNoRemain~~) operation to query the quantity of remaining phone numbers available for online purchase.
        
        @param request: QuerySecretNoRemainRequest
        @return: QuerySecretNoRemainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_secret_no_remain_with_options_async(request, runtime)

    def query_sound_record_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySoundRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySoundRecordResponse:
        """
        @summary 查询通话录音链接
        
        @param request: QuerySoundRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySoundRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySoundRecord',
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
            dyplsapi_20170525_models.QuerySoundRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sound_record_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySoundRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySoundRecordResponse:
        """
        @summary 查询通话录音链接
        
        @param request: QuerySoundRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySoundRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySoundRecord',
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
            dyplsapi_20170525_models.QuerySoundRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sound_record(
        self,
        request: dyplsapi_20170525_models.QuerySoundRecordRequest,
    ) -> dyplsapi_20170525_models.QuerySoundRecordResponse:
        """
        @summary 查询通话录音链接
        
        @param request: QuerySoundRecordRequest
        @return: QuerySoundRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sound_record_with_options(request, runtime)

    async def query_sound_record_async(
        self,
        request: dyplsapi_20170525_models.QuerySoundRecordRequest,
    ) -> dyplsapi_20170525_models.QuerySoundRecordResponse:
        """
        @summary 查询通话录音链接
        
        @param request: QuerySoundRecordRequest
        @return: QuerySoundRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_record_with_options_async(request, runtime)

    def query_subs_id_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        """
        @summary Queries binding IDs.
        
        @description You can query binding IDs by phone number X. In the AXB product, multiple bindings may exist for the same phone number X. In this case, multiple binding IDs may be obtained for the same phone number X.
        
        @param request: QuerySubsIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySubsIdResponse
        """
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
        """
        @summary Queries binding IDs.
        
        @description You can query binding IDs by phone number X. In the AXB product, multiple bindings may exist for the same phone number X. In this case, multiple binding IDs may be obtained for the same phone number X.
        
        @param request: QuerySubsIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySubsIdResponse
        """
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
        """
        @summary Queries binding IDs.
        
        @description You can query binding IDs by phone number X. In the AXB product, multiple bindings may exist for the same phone number X. In this case, multiple binding IDs may be obtained for the same phone number X.
        
        @param request: QuerySubsIdRequest
        @return: QuerySubsIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_subs_id_with_options(request, runtime)

    async def query_subs_id_async(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        """
        @summary Queries binding IDs.
        
        @description You can query binding IDs by phone number X. In the AXB product, multiple bindings may exist for the same phone number X. In this case, multiple binding IDs may be obtained for the same phone number X.
        
        @param request: QuerySubsIdRequest
        @return: QuerySubsIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_subs_id_with_options_async(request, runtime)

    def query_subscription_detail_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        """
        @summary Queries the details about a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        ### [](#poolkeyproducttype)Limits on PoolKey and ProductType
        You must specify either PoolKey or ProductType. If both parameters are not specified, an error is reported when you call the QuerySubscriptionDetail operation. We recommend that you specify the ProductType parameter for the original key accounts of Alibaba Cloud and the PoolKey parameter for Alibaba Cloud users.
        
        @param request: QuerySubscriptionDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySubscriptionDetailResponse
        """
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
        """
        @summary Queries the details about a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        ### [](#poolkeyproducttype)Limits on PoolKey and ProductType
        You must specify either PoolKey or ProductType. If both parameters are not specified, an error is reported when you call the QuerySubscriptionDetail operation. We recommend that you specify the ProductType parameter for the original key accounts of Alibaba Cloud and the PoolKey parameter for Alibaba Cloud users.
        
        @param request: QuerySubscriptionDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySubscriptionDetailResponse
        """
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
        """
        @summary Queries the details about a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        ### [](#poolkeyproducttype)Limits on PoolKey and ProductType
        You must specify either PoolKey or ProductType. If both parameters are not specified, an error is reported when you call the QuerySubscriptionDetail operation. We recommend that you specify the ProductType parameter for the original key accounts of Alibaba Cloud and the PoolKey parameter for Alibaba Cloud users.
        
        @param request: QuerySubscriptionDetailRequest
        @return: QuerySubscriptionDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_subscription_detail_with_options(request, runtime)

    async def query_subscription_detail_async(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        """
        @summary Queries the details about a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        ### [](#poolkeyproducttype)Limits on PoolKey and ProductType
        You must specify either PoolKey or ProductType. If both parameters are not specified, an error is reported when you call the QuerySubscriptionDetail operation. We recommend that you specify the ProductType parameter for the original key accounts of Alibaba Cloud and the PoolKey parameter for Alibaba Cloud users.
        
        @param request: QuerySubscriptionDetailRequest
        @return: QuerySubscriptionDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_subscription_detail_with_options_async(request, runtime)

    def release_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        """
        @summary Releases a phone number.
        
        @description    After a phone number is released, it will no longer be charged from the following month.
        Before you release a phone number, log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) to check whether the phone number is bound to other phone numbers. The phone number can be released only if it is not bound to other phone numbers.
        
        @param request: ReleaseSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSecretNoResponse
        """
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
        """
        @summary Releases a phone number.
        
        @description    After a phone number is released, it will no longer be charged from the following month.
        Before you release a phone number, log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) to check whether the phone number is bound to other phone numbers. The phone number can be released only if it is not bound to other phone numbers.
        
        @param request: ReleaseSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseSecretNoResponse
        """
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
        """
        @summary Releases a phone number.
        
        @description    After a phone number is released, it will no longer be charged from the following month.
        Before you release a phone number, log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) to check whether the phone number is bound to other phone numbers. The phone number can be released only if it is not bound to other phone numbers.
        
        @param request: ReleaseSecretNoRequest
        @return: ReleaseSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_secret_no_with_options(request, runtime)

    async def release_secret_no_async(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        """
        @summary Releases a phone number.
        
        @description    After a phone number is released, it will no longer be charged from the following month.
        Before you release a phone number, log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) to check whether the phone number is bound to other phone numbers. The phone number can be released only if it is not bound to other phone numbers.
        
        @param request: ReleaseSecretNoRequest
        @return: ReleaseSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_secret_no_with_options_async(request, runtime)

    def un_bind_axbwith_options(
        self,
        request: dyplsapi_20170525_models.UnBindAXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnBindAXBResponse:
        """
        @summary 解除指定的呼叫绑定关系（A，X，B），解决呼叫绑定关系后，员工B不能通过工作号X呼叫到客户A。
        
        @param request: UnBindAXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnBindAXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_id):
            query['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnBindAXB',
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
            dyplsapi_20170525_models.UnBindAXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_bind_axbwith_options_async(
        self,
        request: dyplsapi_20170525_models.UnBindAXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnBindAXBResponse:
        """
        @summary 解除指定的呼叫绑定关系（A，X，B），解决呼叫绑定关系后，员工B不能通过工作号X呼叫到客户A。
        
        @param request: UnBindAXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnBindAXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_id):
            query['BindId'] = request.bind_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnBindAXB',
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
            dyplsapi_20170525_models.UnBindAXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_bind_axb(
        self,
        request: dyplsapi_20170525_models.UnBindAXBRequest,
    ) -> dyplsapi_20170525_models.UnBindAXBResponse:
        """
        @summary 解除指定的呼叫绑定关系（A，X，B），解决呼叫绑定关系后，员工B不能通过工作号X呼叫到客户A。
        
        @param request: UnBindAXBRequest
        @return: UnBindAXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_bind_axbwith_options(request, runtime)

    async def un_bind_axb_async(
        self,
        request: dyplsapi_20170525_models.UnBindAXBRequest,
    ) -> dyplsapi_20170525_models.UnBindAXBResponse:
        """
        @summary 解除指定的呼叫绑定关系（A，X，B），解决呼叫绑定关系后，员工B不能通过工作号X呼叫到客户A。
        
        @param request: UnBindAXBRequest
        @return: UnBindAXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_bind_axbwith_options_async(request, runtime)

    def un_bind_xbwith_options(
        self,
        request: dyplsapi_20170525_models.UnBindXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnBindXBResponse:
        """
        @summary 调用本接口可取消工作号X与员工号码B的绑定。绑定解除后，对X的呼叫都不会转接给B。
        
        @param request: UnBindXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnBindXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_id):
            query['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnBindXB',
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
            dyplsapi_20170525_models.UnBindXBResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_bind_xbwith_options_async(
        self,
        request: dyplsapi_20170525_models.UnBindXBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnBindXBResponse:
        """
        @summary 调用本接口可取消工作号X与员工号码B的绑定。绑定解除后，对X的呼叫都不会转接给B。
        
        @param request: UnBindXBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnBindXBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_id):
            query['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.customer_pool_key):
            query['CustomerPoolKey'] = request.customer_pool_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.req_id):
            query['ReqId'] = request.req_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tel_x):
            query['TelX'] = request.tel_x
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnBindXB',
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
            dyplsapi_20170525_models.UnBindXBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_bind_xb(
        self,
        request: dyplsapi_20170525_models.UnBindXBRequest,
    ) -> dyplsapi_20170525_models.UnBindXBResponse:
        """
        @summary 调用本接口可取消工作号X与员工号码B的绑定。绑定解除后，对X的呼叫都不会转接给B。
        
        @param request: UnBindXBRequest
        @return: UnBindXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_bind_xbwith_options(request, runtime)

    async def un_bind_xb_async(
        self,
        request: dyplsapi_20170525_models.UnBindXBRequest,
    ) -> dyplsapi_20170525_models.UnBindXBResponse:
        """
        @summary 调用本接口可取消工作号X与员工号码B的绑定。绑定解除后，对X的呼叫都不会转接给B。
        
        @param request: UnBindXBRequest
        @return: UnBindXBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_bind_xbwith_options_async(request, runtime)

    def unbind_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        """
        @summary Unbinds a phone number.
        
        @description Before releasing a phone number, you must call the UnbindSubscription operation to unbind the phone number.
        
        @param request: UnbindSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSubscriptionResponse
        """
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
        """
        @summary Unbinds a phone number.
        
        @description Before releasing a phone number, you must call the UnbindSubscription operation to unbind the phone number.
        
        @param request: UnbindSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSubscriptionResponse
        """
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
        """
        @summary Unbinds a phone number.
        
        @description Before releasing a phone number, you must call the UnbindSubscription operation to unbind the phone number.
        
        @param request: UnbindSubscriptionRequest
        @return: UnbindSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_subscription_with_options(request, runtime)

    async def unbind_subscription_async(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        """
        @summary Unbinds a phone number.
        
        @description Before releasing a phone number, you must call the UnbindSubscription operation to unbind the phone number.
        
        @param request: UnbindSubscriptionRequest
        @return: UnbindSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_subscription_with_options_async(request, runtime)

    def unlock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        """
        @summary Unlocks a phone number.
        
        @description After a phone number is unlocked, you can reselect the unlocked phone number when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockSecretNoResponse
        """
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
        """
        @summary Unlocks a phone number.
        
        @description After a phone number is unlocked, you can reselect the unlocked phone number when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockSecretNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockSecretNoResponse
        """
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
        """
        @summary Unlocks a phone number.
        
        @description After a phone number is unlocked, you can reselect the unlocked phone number when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockSecretNoRequest
        @return: UnlockSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_secret_no_with_options(request, runtime)

    async def unlock_secret_no_async(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        """
        @summary Unlocks a phone number.
        
        @description After a phone number is unlocked, you can reselect the unlocked phone number when you call an operation to create a binding.
        ### [](#qps)QPS limits
        You can call this operation up to 500 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockSecretNoRequest
        @return: UnlockSecretNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_secret_no_with_options_async(request, runtime)

    def update_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        """
        @summary Modifies a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 10,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscriptionResponse
        """
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
        """
        @summary Modifies a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 10,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateSubscriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubscriptionResponse
        """
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
        """
        @summary Modifies a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 10,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateSubscriptionRequest
        @return: UpdateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_subscription_with_options(request, runtime)

    async def update_subscription_async(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        """
        @summary Modifies a phone number binding.
        
        @description ### [](#qps)QPS limits
        You can call this operation up to 10,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateSubscriptionRequest
        @return: UpdateSubscriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_subscription_with_options_async(request, runtime)

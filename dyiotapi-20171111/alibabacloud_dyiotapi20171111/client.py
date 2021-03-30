# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyiotapi20171111 import models as dyiotapi_20171111_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dyiotapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def do_iot_chg_bind_or_un_bind_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotChgBindOrUnBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['Imei'] = request.imei
        query['NewImei'] = request.new_imei
        query['OpionType'] = request.opion_type
        query['MidChannelId'] = request.mid_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotChgBindOrUnBind',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_chg_bind_or_un_bind_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotChgBindOrUnBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['Imei'] = request.imei
        query['NewImei'] = request.new_imei
        query['OpionType'] = request.opion_type
        query['MidChannelId'] = request.mid_channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotChgBindOrUnBind',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_chg_bind_or_un_bind(
        self,
        request: dyiotapi_20171111_models.DoIotChgBindOrUnBindRequest,
    ) -> dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_chg_bind_or_un_bind_with_options(request, runtime)

    async def do_iot_chg_bind_or_un_bind_async(
        self,
        request: dyiotapi_20171111_models.DoIotChgBindOrUnBindRequest,
    ) -> dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_chg_bind_or_un_bind_with_options_async(request, runtime)

    def do_iot_is_imei_exist_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotIsImeiExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotIsImeiExistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Imei'] = request.imei
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotIsImeiExist',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotIsImeiExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_is_imei_exist_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotIsImeiExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotIsImeiExistResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Imei'] = request.imei
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotIsImeiExist',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotIsImeiExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_is_imei_exist(
        self,
        request: dyiotapi_20171111_models.DoIotIsImeiExistRequest,
    ) -> dyiotapi_20171111_models.DoIotIsImeiExistResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_is_imei_exist_with_options(request, runtime)

    async def do_iot_is_imei_exist_async(
        self,
        request: dyiotapi_20171111_models.DoIotIsImeiExistRequest,
    ) -> dyiotapi_20171111_models.DoIotIsImeiExistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_is_imei_exist_with_options_async(request, runtime)

    def do_iot_post_imei_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotPostImeiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotPostImeiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Imei'] = request.imei
        query['Comments'] = request.comments
        query['DeviceType'] = request.device_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotPostImei',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotPostImeiResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_post_imei_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotPostImeiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotPostImeiResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Imei'] = request.imei
        query['Comments'] = request.comments
        query['DeviceType'] = request.device_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotPostImei',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotPostImeiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_post_imei(
        self,
        request: dyiotapi_20171111_models.DoIotPostImeiRequest,
    ) -> dyiotapi_20171111_models.DoIotPostImeiResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_post_imei_with_options(request, runtime)

    async def do_iot_post_imei_async(
        self,
        request: dyiotapi_20171111_models.DoIotPostImeiRequest,
    ) -> dyiotapi_20171111_models.DoIotPostImeiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_post_imei_with_options_async(request, runtime)

    def do_iot_recharge_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotRechargeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotRechargeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['OfferIds'] = request.offer_ids
        query['OutId'] = request.out_id
        query['Amount'] = request.amount
        query['EffCode'] = request.eff_code
        query['OrderNum'] = request.order_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotRecharge',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotRechargeResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_recharge_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotRechargeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotRechargeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['OfferIds'] = request.offer_ids
        query['OutId'] = request.out_id
        query['Amount'] = request.amount
        query['EffCode'] = request.eff_code
        query['OrderNum'] = request.order_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotRecharge',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotRechargeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_recharge(
        self,
        request: dyiotapi_20171111_models.DoIotRechargeRequest,
    ) -> dyiotapi_20171111_models.DoIotRechargeResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_recharge_with_options(request, runtime)

    async def do_iot_recharge_async(
        self,
        request: dyiotapi_20171111_models.DoIotRechargeRequest,
    ) -> dyiotapi_20171111_models.DoIotRechargeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_recharge_with_options_async(request, runtime)

    def do_iot_set_absolute_remind_config_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['ConfigInfo'] = request.config_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotSetAbsoluteRemindConfig',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_set_absolute_remind_config_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['ConfigInfo'] = request.config_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotSetAbsoluteRemindConfig',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_set_absolute_remind_config(
        self,
        request: dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigRequest,
    ) -> dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_set_absolute_remind_config_with_options(request, runtime)

    async def do_iot_set_absolute_remind_config_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigRequest,
    ) -> dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_set_absolute_remind_config_with_options_async(request, runtime)

    def do_iot_set_remind_config_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotSetRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetRemindConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['OperationType'] = request.operation_type
        query['ConfigInfo'] = request.config_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotSetRemindConfig',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotSetRemindConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_set_remind_config_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetRemindConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        query['OperationType'] = request.operation_type
        query['ConfigInfo'] = request.config_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotSetRemindConfig',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotSetRemindConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_set_remind_config(
        self,
        request: dyiotapi_20171111_models.DoIotSetRemindConfigRequest,
    ) -> dyiotapi_20171111_models.DoIotSetRemindConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_set_remind_config_with_options(request, runtime)

    async def do_iot_set_remind_config_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetRemindConfigRequest,
    ) -> dyiotapi_20171111_models.DoIotSetRemindConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_set_remind_config_with_options_async(request, runtime)

    def do_iot_unbind_resume_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotUnbindResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUnbindResumeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotUnbindResume',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotUnbindResumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_unbind_resume_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotUnbindResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUnbindResumeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotUnbindResume',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotUnbindResumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_unbind_resume(
        self,
        request: dyiotapi_20171111_models.DoIotUnbindResumeRequest,
    ) -> dyiotapi_20171111_models.DoIotUnbindResumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_unbind_resume_with_options(request, runtime)

    async def do_iot_unbind_resume_async(
        self,
        request: dyiotapi_20171111_models.DoIotUnbindResumeRequest,
    ) -> dyiotapi_20171111_models.DoIotUnbindResumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_unbind_resume_with_options_async(request, runtime)

    def do_iot_user_stop_resume_with_options(
        self,
        request: dyiotapi_20171111_models.DoIotUserStopResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUserStopResumeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['OptionType'] = request.option_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotUserStopResume',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotUserStopResumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_iot_user_stop_resume_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotUserStopResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUserStopResumeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        query['OptionType'] = request.option_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoIotUserStopResume',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoIotUserStopResumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_iot_user_stop_resume(
        self,
        request: dyiotapi_20171111_models.DoIotUserStopResumeRequest,
    ) -> dyiotapi_20171111_models.DoIotUserStopResumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_iot_user_stop_resume_with_options(request, runtime)

    async def do_iot_user_stop_resume_async(
        self,
        request: dyiotapi_20171111_models.DoIotUserStopResumeRequest,
    ) -> dyiotapi_20171111_models.DoIotUserStopResumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_iot_user_stop_resume_with_options_async(request, runtime)

    def do_send_iot_sms_with_options(
        self,
        request: dyiotapi_20171111_models.DoSendIotSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoSendIotSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SignName'] = request.sign_name
        query['TemplateCode'] = request.template_code
        query['PhoneNumbers'] = request.phone_numbers
        query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoSendIotSms',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoSendIotSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_send_iot_sms_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoSendIotSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoSendIotSmsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SignName'] = request.sign_name
        query['TemplateCode'] = request.template_code
        query['PhoneNumbers'] = request.phone_numbers
        query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DoSendIotSms',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.DoSendIotSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_send_iot_sms(
        self,
        request: dyiotapi_20171111_models.DoSendIotSmsRequest,
    ) -> dyiotapi_20171111_models.DoSendIotSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_send_iot_sms_with_options(request, runtime)

    async def do_send_iot_sms_async(
        self,
        request: dyiotapi_20171111_models.DoSendIotSmsRequest,
    ) -> dyiotapi_20171111_models.DoSendIotSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_send_iot_sms_with_options_async(request, runtime)

    def query_card_flow_info_with_options(
        self,
        request: dyiotapi_20171111_models.QueryCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardFlowInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_flow_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardFlowInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_flow_info(
        self,
        request: dyiotapi_20171111_models.QueryCardFlowInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_flow_info_with_options(request, runtime)

    async def query_card_flow_info_async(
        self,
        request: dyiotapi_20171111_models.QueryCardFlowInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_flow_info_with_options_async(request, runtime)

    def query_card_history_flow_info_with_options(
        self,
        request: dyiotapi_20171111_models.QueryCardHistoryFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Iccid'] = request.iccid
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardHistoryFlowInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_history_flow_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardHistoryFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Iccid'] = request.iccid
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardHistoryFlowInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_history_flow_info(
        self,
        request: dyiotapi_20171111_models.QueryCardHistoryFlowInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_history_flow_info_with_options(request, runtime)

    async def query_card_history_flow_info_async(
        self,
        request: dyiotapi_20171111_models.QueryCardHistoryFlowInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_history_flow_info_with_options_async(request, runtime)

    def query_card_info_with_options(
        self,
        request: dyiotapi_20171111_models.QueryCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_info(
        self,
        request: dyiotapi_20171111_models.QueryCardInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_info_with_options(request, runtime)

    async def query_card_info_async(
        self,
        request: dyiotapi_20171111_models.QueryCardInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_info_with_options_async(request, runtime)

    def query_cards_info_with_options(
        self,
        request: dyiotapi_20171111_models.QueryCardsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardsInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cards_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardsInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cards_info(
        self,
        request: dyiotapi_20171111_models.QueryCardsInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cards_info_with_options(request, runtime)

    async def query_cards_info_async(
        self,
        request: dyiotapi_20171111_models.QueryCardsInfoRequest,
    ) -> dyiotapi_20171111_models.QueryCardsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cards_info_with_options_async(request, runtime)

    def query_card_status_with_options(
        self,
        request: dyiotapi_20171111_models.QueryCardStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardStatus',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_status_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCardStatus',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryCardStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_status(
        self,
        request: dyiotapi_20171111_models.QueryCardStatusRequest,
    ) -> dyiotapi_20171111_models.QueryCardStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_card_status_with_options(request, runtime)

    async def query_card_status_async(
        self,
        request: dyiotapi_20171111_models.QueryCardStatusRequest,
    ) -> dyiotapi_20171111_models.QueryCardStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_card_status_with_options_async(request, runtime)

    def query_iot_card_offer_dtl_with_options(
        self,
        request: dyiotapi_20171111_models.QueryIotCardOfferDtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryIotCardOfferDtlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIotCardOfferDtl',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryIotCardOfferDtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iot_card_offer_dtl_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryIotCardOfferDtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryIotCardOfferDtlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIotCardOfferDtl',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryIotCardOfferDtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_iot_card_offer_dtl(
        self,
        request: dyiotapi_20171111_models.QueryIotCardOfferDtlRequest,
    ) -> dyiotapi_20171111_models.QueryIotCardOfferDtlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_iot_card_offer_dtl_with_options(request, runtime)

    async def query_iot_card_offer_dtl_async(
        self,
        request: dyiotapi_20171111_models.QueryIotCardOfferDtlRequest,
    ) -> dyiotapi_20171111_models.QueryIotCardOfferDtlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_iot_card_offer_dtl_with_options_async(request, runtime)

    def query_personal_info_with_options(
        self,
        request: dyiotapi_20171111_models.QueryPersonalInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryPersonalInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPersonalInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryPersonalInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_personal_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryPersonalInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryPersonalInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPersonalInfo',
            version='2017-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dyiotapi_20171111_models.QueryPersonalInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_personal_info(
        self,
        request: dyiotapi_20171111_models.QueryPersonalInfoRequest,
    ) -> dyiotapi_20171111_models.QueryPersonalInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_personal_info_with_options(request, runtime)

    async def query_personal_info_async(
        self,
        request: dyiotapi_20171111_models.QueryPersonalInfoRequest,
    ) -> dyiotapi_20171111_models.QueryPersonalInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_personal_info_with_options_async(request, runtime)

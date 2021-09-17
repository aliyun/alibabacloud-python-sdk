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

    def delete_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.DeleteSecretBlacklistResponse(),
            self.do_rpcrequest('DeleteSecretBlacklist', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_secret_blacklist_with_options_async(
        self,
        request: dyplsapi_20170525_models.DeleteSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.DeleteSecretBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.DeleteSecretBlacklistResponse(),
            await self.do_rpcrequest_async('DeleteSecretBlacklist', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def bind_axn_extension_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnExtensionResponse(),
            self.do_rpcrequest('BindAxnExtension', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_axn_extension_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxnExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnExtensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnExtensionResponse(),
            await self.do_rpcrequest_async('BindAxnExtension', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_phone_switch_with_options(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdatePhoneSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdatePhoneSwitchResponse(),
            self.do_rpcrequest('UpdatePhoneSwitch', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_phone_switch_with_options_async(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdatePhoneSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdatePhoneSwitchResponse(),
            await self.do_rpcrequest_async('UpdatePhoneSwitch', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_phone_switch(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneSwitchRequest,
    ) -> dyplsapi_20170525_models.UpdatePhoneSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_phone_switch_with_options(request, runtime)

    async def update_phone_switch_async(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneSwitchRequest,
    ) -> dyplsapi_20170525_models.UpdatePhoneSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_switch_with_options_async(request, runtime)

    def get_total_public_url_with_options(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetTotalPublicUrlResponse(),
            self.do_rpcrequest('GetTotalPublicUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_total_public_url_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetTotalPublicUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetTotalPublicUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetTotalPublicUrlResponse(),
            await self.do_rpcrequest_async('GetTotalPublicUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def buy_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BuySecretNoResponse(),
            self.do_rpcrequest('BuySecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def buy_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.BuySecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BuySecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BuySecretNoResponse(),
            await self.do_rpcrequest_async('BuySecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.CreateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateSubscriptionResponse(),
            self.do_rpcrequest('CreateSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_subscription_with_options_async(
        self,
        request: dyplsapi_20170525_models.CreateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateSubscriptionResponse(),
            await self.do_rpcrequest_async('CreateSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_subscription(
        self,
        request: dyplsapi_20170525_models.CreateSubscriptionRequest,
    ) -> dyplsapi_20170525_models.CreateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_with_options(request, runtime)

    async def create_subscription_async(
        self,
        request: dyplsapi_20170525_models.CreateSubscriptionRequest,
    ) -> dyplsapi_20170525_models.CreateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_with_options_async(request, runtime)

    def get_face_verify_with_options(
        self,
        request: dyplsapi_20170525_models.GetFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetFaceVerifyResponse(),
            self.do_rpcrequest('GetFaceVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_face_verify_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetFaceVerifyResponse(),
            await self.do_rpcrequest_async('GetFaceVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_face_verify(
        self,
        request: dyplsapi_20170525_models.GetFaceVerifyRequest,
    ) -> dyplsapi_20170525_models.GetFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_verify_with_options(request, runtime)

    async def get_face_verify_async(
        self,
        request: dyplsapi_20170525_models.GetFaceVerifyRequest,
    ) -> dyplsapi_20170525_models.GetFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_verify_with_options_async(request, runtime)

    def query_subscription_detail_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubscriptionDetailResponse(),
            self.do_rpcrequest('QuerySubscriptionDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_subscription_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubscriptionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubscriptionDetailResponse(),
            await self.do_rpcrequest_async('QuerySubscriptionDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_call_status_with_options(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryCallStatusResponse(),
            self.do_rpcrequest('QueryCallStatus', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_call_status_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryCallStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryCallStatusResponse(),
            await self.do_rpcrequest_async('QueryCallStatus', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_phone_number_with_options(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdatePhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdatePhoneNumberResponse(),
            self.do_rpcrequest('UpdatePhoneNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_phone_number_with_options_async(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdatePhoneNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdatePhoneNumberResponse(),
            await self.do_rpcrequest_async('UpdatePhoneNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_phone_number(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneNumberRequest,
    ) -> dyplsapi_20170525_models.UpdatePhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_phone_number_with_options(request, runtime)

    async def update_phone_number_async(
        self,
        request: dyplsapi_20170525_models.UpdatePhoneNumberRequest,
    ) -> dyplsapi_20170525_models.UpdatePhoneNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_phone_number_with_options_async(request, runtime)

    def operate_black_no_with_options(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateBlackNoResponse(),
            self.do_rpcrequest('OperateBlackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_black_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.OperateBlackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateBlackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateBlackNoResponse(),
            await self.do_rpcrequest_async('OperateBlackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_secret_asr_detail_with_options(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSecretAsrDetailResponse(),
            self.do_rpcrequest('GetSecretAsrDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_secret_asr_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetSecretAsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSecretAsrDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSecretAsrDetailResponse(),
            await self.do_rpcrequest_async('GetSecretAsrDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateSubscriptionResponse(),
            self.do_rpcrequest('UpdateSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        request: dyplsapi_20170525_models.UpdateSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateSubscriptionResponse(),
            await self.do_rpcrequest_async('UpdateSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def lock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.LockSecretNoResponse(),
            self.do_rpcrequest('LockSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lock_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.LockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.LockSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.LockSecretNoResponse(),
            await self.do_rpcrequest_async('LockSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def unlock_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnlockSecretNoResponse(),
            self.do_rpcrequest('UnlockSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unlock_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.UnlockSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnlockSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnlockSecretNoResponse(),
            await self.do_rpcrequest_async('UnlockSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def release_secret_no_with_options(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ReleaseSecretNoResponse(),
            self.do_rpcrequest('ReleaseSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_secret_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.ReleaseSecretNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ReleaseSecretNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ReleaseSecretNoResponse(),
            await self.do_rpcrequest_async('ReleaseSecretNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def operate_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateAxgGroupResponse(),
            self.do_rpcrequest('OperateAxgGroup', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def operate_axg_group_with_options_async(
        self,
        request: dyplsapi_20170525_models.OperateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.OperateAxgGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.OperateAxgGroupResponse(),
            await self.do_rpcrequest_async('OperateAxgGroup', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_default_bwith_options(
        self,
        request: dyplsapi_20170525_models.UpdateDefaultBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateDefaultBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateDefaultBResponse(),
            self.do_rpcrequest('UpdateDefaultB', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_default_bwith_options_async(
        self,
        request: dyplsapi_20170525_models.UpdateDefaultBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UpdateDefaultBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UpdateDefaultBResponse(),
            await self.do_rpcrequest_async('UpdateDefaultB', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_default_b(
        self,
        request: dyplsapi_20170525_models.UpdateDefaultBRequest,
    ) -> dyplsapi_20170525_models.UpdateDefaultBResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_default_bwith_options(request, runtime)

    async def update_default_b_async(
        self,
        request: dyplsapi_20170525_models.UpdateDefaultBRequest,
    ) -> dyplsapi_20170525_models.UpdateDefaultBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_default_bwith_options_async(request, runtime)

    def query_phone_no_aby_track_no_with_options(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse(),
            self.do_rpcrequest('QueryPhoneNoAByTrackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_phone_no_aby_track_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryPhoneNoAByTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryPhoneNoAByTrackNoResponse(),
            await self.do_rpcrequest_async('QueryPhoneNoAByTrackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_axn_track_no_with_options(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddAxnTrackNoResponse(),
            self.do_rpcrequest('AddAxnTrackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_axn_track_no_with_options_async(
        self,
        request: dyplsapi_20170525_models.AddAxnTrackNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddAxnTrackNoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddAxnTrackNoResponse(),
            await self.do_rpcrequest_async('AddAxnTrackNo', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_secret_no_remain_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoRemainResponse(),
            self.do_rpcrequest('QuerySecretNoRemain', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_secret_no_remain_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySecretNoRemainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySecretNoRemainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySecretNoRemainResponse(),
            await self.do_rpcrequest_async('QuerySecretNoRemain', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_axg_group_with_options(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateAxgGroupResponse(),
            self.do_rpcrequest('CreateAxgGroup', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_axg_group_with_options_async(
        self,
        request: dyplsapi_20170525_models.CreateAxgGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.CreateAxgGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.CreateAxgGroupResponse(),
            await self.do_rpcrequest_async('CreateAxgGroup', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def bind_axb_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxbResponse(),
            self.do_rpcrequest('BindAxb', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_axb_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxbResponse(),
            await self.do_rpcrequest_async('BindAxb', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def unbind_subscription_with_options(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnbindSubscriptionResponse(),
            self.do_rpcrequest('UnbindSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_subscription_with_options_async(
        self,
        request: dyplsapi_20170525_models.UnbindSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.UnbindSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.UnbindSubscriptionResponse(),
            await self.do_rpcrequest_async('UnbindSubscription', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_subs_id_with_options(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubsIdResponse(),
            self.do_rpcrequest('QuerySubsId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_subs_id_with_options_async(
        self,
        request: dyplsapi_20170525_models.QuerySubsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QuerySubsIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QuerySubsIdResponse(),
            await self.do_rpcrequest_async('QuerySubsId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def confirm_send_sms_with_options(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ConfirmSendSmsResponse(),
            self.do_rpcrequest('ConfirmSendSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_send_sms_with_options_async(
        self,
        request: dyplsapi_20170525_models.ConfirmSendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.ConfirmSendSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.ConfirmSendSmsResponse(),
            await self.do_rpcrequest_async('ConfirmSendSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_subscription_detail_with_options(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSubscriptionDetailResponse(),
            self.do_rpcrequest('GetSubscriptionDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_subscription_detail_with_options_async(
        self,
        request: dyplsapi_20170525_models.GetSubscriptionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.GetSubscriptionDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.GetSubscriptionDetailResponse(),
            await self.do_rpcrequest_async('GetSubscriptionDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def bind_axg_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxgResponse(),
            self.do_rpcrequest('BindAxg', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_axg_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxgResponse(),
            await self.do_rpcrequest_async('BindAxg', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_record_file_download_url_with_options(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse(),
            self.do_rpcrequest('QueryRecordFileDownloadUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_file_download_url_with_options_async(
        self,
        request: dyplsapi_20170525_models.QueryRecordFileDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.QueryRecordFileDownloadUrlResponse(),
            await self.do_rpcrequest_async('QueryRecordFileDownloadUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def init_face_verify_with_options(
        self,
        request: dyplsapi_20170525_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.InitFaceVerifyResponse(),
            self.do_rpcrequest('InitFaceVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_face_verify_with_options_async(
        self,
        request: dyplsapi_20170525_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.InitFaceVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.InitFaceVerifyResponse(),
            await self.do_rpcrequest_async('InitFaceVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_face_verify(
        self,
        request: dyplsapi_20170525_models.InitFaceVerifyRequest,
    ) -> dyplsapi_20170525_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)

    async def init_face_verify_async(
        self,
        request: dyplsapi_20170525_models.InitFaceVerifyRequest,
    ) -> dyplsapi_20170525_models.InitFaceVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_face_verify_with_options_async(request, runtime)

    def bind_axn_with_options(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnResponse(),
            self.do_rpcrequest('BindAxn', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_axn_with_options_async(
        self,
        request: dyplsapi_20170525_models.BindAxnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.BindAxnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.BindAxnResponse(),
            await self.do_rpcrequest_async('BindAxn', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_secret_blacklist_with_options(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddSecretBlacklistResponse(),
            self.do_rpcrequest('AddSecretBlacklist', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_secret_blacklist_with_options_async(
        self,
        request: dyplsapi_20170525_models.AddSecretBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyplsapi_20170525_models.AddSecretBlacklistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyplsapi_20170525_models.AddSecretBlacklistResponse(),
            await self.do_rpcrequest_async('AddSecretBlacklist', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

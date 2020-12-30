# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyiotapi20171111 import models as dyiotapi_20171111_models
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse().from_map(
            self.do_rpcrequest('DoIotChgBindOrUnBind', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_chg_bind_or_un_bind_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotChgBindOrUnBindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotChgBindOrUnBindResponse().from_map(
            await self.do_rpcrequest_async('DoIotChgBindOrUnBind', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotIsImeiExistResponse().from_map(
            self.do_rpcrequest('DoIotIsImeiExist', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_is_imei_exist_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotIsImeiExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotIsImeiExistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotIsImeiExistResponse().from_map(
            await self.do_rpcrequest_async('DoIotIsImeiExist', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotPostImeiResponse().from_map(
            self.do_rpcrequest('DoIotPostImei', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_post_imei_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotPostImeiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotPostImeiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotPostImeiResponse().from_map(
            await self.do_rpcrequest_async('DoIotPostImei', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotRechargeResponse().from_map(
            self.do_rpcrequest('DoIotRecharge', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_recharge_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotRechargeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotRechargeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotRechargeResponse().from_map(
            await self.do_rpcrequest_async('DoIotRecharge', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse().from_map(
            self.do_rpcrequest('DoIotSetAbsoluteRemindConfig', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_set_absolute_remind_config_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotSetAbsoluteRemindConfigResponse().from_map(
            await self.do_rpcrequest_async('DoIotSetAbsoluteRemindConfig', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotSetRemindConfigResponse().from_map(
            self.do_rpcrequest('DoIotSetRemindConfig', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_set_remind_config_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotSetRemindConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotSetRemindConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotSetRemindConfigResponse().from_map(
            await self.do_rpcrequest_async('DoIotSetRemindConfig', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotUnbindResumeResponse().from_map(
            self.do_rpcrequest('DoIotUnbindResume', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_unbind_resume_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotUnbindResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUnbindResumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotUnbindResumeResponse().from_map(
            await self.do_rpcrequest_async('DoIotUnbindResume', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotUserStopResumeResponse().from_map(
            self.do_rpcrequest('DoIotUserStopResume', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_iot_user_stop_resume_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoIotUserStopResumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoIotUserStopResumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoIotUserStopResumeResponse().from_map(
            await self.do_rpcrequest_async('DoIotUserStopResume', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoSendIotSmsResponse().from_map(
            self.do_rpcrequest('DoSendIotSms', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_send_iot_sms_with_options_async(
        self,
        request: dyiotapi_20171111_models.DoSendIotSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.DoSendIotSmsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.DoSendIotSmsResponse().from_map(
            await self.do_rpcrequest_async('DoSendIotSms', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardFlowInfoResponse().from_map(
            self.do_rpcrequest('QueryCardFlowInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_card_flow_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardFlowInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardFlowInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryCardFlowInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse().from_map(
            self.do_rpcrequest('QueryCardHistoryFlowInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_card_history_flow_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardHistoryFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardHistoryFlowInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryCardHistoryFlowInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardInfoResponse().from_map(
            self.do_rpcrequest('QueryCardInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_card_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryCardInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardsInfoResponse().from_map(
            self.do_rpcrequest('QueryCardsInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cards_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardsInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryCardsInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardStatusResponse().from_map(
            self.do_rpcrequest('QueryCardStatus', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_card_status_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryCardStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryCardStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryCardStatusResponse().from_map(
            await self.do_rpcrequest_async('QueryCardStatus', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryIotCardOfferDtlResponse().from_map(
            self.do_rpcrequest('QueryIotCardOfferDtl', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_iot_card_offer_dtl_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryIotCardOfferDtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryIotCardOfferDtlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryIotCardOfferDtlResponse().from_map(
            await self.do_rpcrequest_async('QueryIotCardOfferDtl', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryPersonalInfoResponse().from_map(
            self.do_rpcrequest('QueryPersonalInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_personal_info_with_options_async(
        self,
        request: dyiotapi_20171111_models.QueryPersonalInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyiotapi_20171111_models.QueryPersonalInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dyiotapi_20171111_models.QueryPersonalInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryPersonalInfo', '2017-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

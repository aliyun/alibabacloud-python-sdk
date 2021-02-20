# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rtc20180111 import models as rtc_20180111_models
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
        self._endpoint = self.get_endpoint('rtc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_record_template_with_options(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.AddRecordTemplateResponse().from_map(
            self.do_rpcrequest('AddRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_record_template_with_options_async(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.AddRecordTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_record_template(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_record_template_with_options(request, runtime)

    async def add_record_template_async(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_record_template_with_options_async(request, runtime)

    def create_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateAutoLiveStreamRuleResponse().from_map(
            self.do_rpcrequest('CreateAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateAutoLiveStreamRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_live_stream_rule_with_options(request, runtime)

    async def create_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_live_stream_rule_with_options_async(request, runtime)

    def create_channel_with_options(
        self,
        request: rtc_20180111_models.CreateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateChannelResponse().from_map(
            self.do_rpcrequest('CreateChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_channel_with_options_async(
        self,
        request: rtc_20180111_models.CreateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateChannelResponse().from_map(
            await self.do_rpcrequest_async('CreateChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_channel(
        self,
        request: rtc_20180111_models.CreateChannelRequest,
    ) -> rtc_20180111_models.CreateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_channel_with_options(request, runtime)

    async def create_channel_async(
        self,
        request: rtc_20180111_models.CreateChannelRequest,
    ) -> rtc_20180111_models.CreateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_channel_with_options_async(request, runtime)

    def create_conference_with_options(
        self,
        request: rtc_20180111_models.CreateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateConferenceResponse().from_map(
            self.do_rpcrequest('CreateConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_conference_with_options_async(
        self,
        request: rtc_20180111_models.CreateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateConferenceResponse().from_map(
            await self.do_rpcrequest_async('CreateConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_conference(
        self,
        request: rtc_20180111_models.CreateConferenceRequest,
    ) -> rtc_20180111_models.CreateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_conference_with_options(request, runtime)

    async def create_conference_async(
        self,
        request: rtc_20180111_models.CreateConferenceRequest,
    ) -> rtc_20180111_models.CreateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_conference_with_options_async(request, runtime)

    def create_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateEventSubscribeResponse().from_map(
            self.do_rpcrequest('CreateEventSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateEventSubscribeResponse().from_map(
            await self.do_rpcrequest_async('CreateEventSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_event_subscribe(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_subscribe_with_options(request, runtime)

    async def create_event_subscribe_async(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_subscribe_with_options_async(request, runtime)

    def create_mpulayout_with_options(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateMPULayoutResponse().from_map(
            self.do_rpcrequest('CreateMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateMPULayoutResponse().from_map(
            await self.do_rpcrequest_async('CreateMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mpulayout(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mpulayout_with_options(request, runtime)

    async def create_mpulayout_async(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mpulayout_with_options_async(request, runtime)

    def create_mpurule_with_options(
        self,
        request: rtc_20180111_models.CreateMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateMPURuleResponse().from_map(
            self.do_rpcrequest('CreateMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mpurule_with_options_async(
        self,
        request: rtc_20180111_models.CreateMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateMPURuleResponse().from_map(
            await self.do_rpcrequest_async('CreateMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mpurule(
        self,
        request: rtc_20180111_models.CreateMPURuleRequest,
    ) -> rtc_20180111_models.CreateMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mpurule_with_options(request, runtime)

    async def create_mpurule_async(
        self,
        request: rtc_20180111_models.CreateMPURuleRequest,
    ) -> rtc_20180111_models.CreateMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mpurule_with_options_async(request, runtime)

    def create_service_linked_role_for_rtc_with_options(
        self,
        request: rtc_20180111_models.CreateServiceLinkedRoleForRtcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse().from_map(
            self.do_rpcrequest('CreateServiceLinkedRoleForRtc', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_for_rtc_with_options_async(
        self,
        request: rtc_20180111_models.CreateServiceLinkedRoleForRtcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse().from_map(
            await self.do_rpcrequest_async('CreateServiceLinkedRoleForRtc', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role_for_rtc(
        self,
        request: rtc_20180111_models.CreateServiceLinkedRoleForRtcRequest,
    ) -> rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_for_rtc_with_options(request, runtime)

    async def create_service_linked_role_for_rtc_async(
        self,
        request: rtc_20180111_models.CreateServiceLinkedRoleForRtcRequest,
    ) -> rtc_20180111_models.CreateServiceLinkedRoleForRtcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_for_rtc_with_options_async(request, runtime)

    def create_subscribe_with_options(
        self,
        request: rtc_20180111_models.CreateSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateSubscribeResponse().from_map(
            self.do_rpcrequest('CreateSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.CreateSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.CreateSubscribeResponse().from_map(
            await self.do_rpcrequest_async('CreateSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_subscribe(
        self,
        request: rtc_20180111_models.CreateSubscribeRequest,
    ) -> rtc_20180111_models.CreateSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_with_options(request, runtime)

    async def create_subscribe_async(
        self,
        request: rtc_20180111_models.CreateSubscribeRequest,
    ) -> rtc_20180111_models.CreateSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscribe_with_options_async(request, runtime)

    def delete_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteAutoLiveStreamRuleResponse().from_map(
            self.do_rpcrequest('DeleteAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteAutoLiveStreamRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_live_stream_rule_with_options(request, runtime)

    async def delete_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_live_stream_rule_with_options_async(request, runtime)

    def delete_channel_with_options(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteChannelResponse().from_map(
            self.do_rpcrequest('DeleteChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_channel_with_options_async(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteChannelResponse().from_map(
            await self.do_rpcrequest_async('DeleteChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_channel(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    async def delete_channel_async(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_channel_with_options_async(request, runtime)

    def delete_conference_with_options(
        self,
        request: rtc_20180111_models.DeleteConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteConferenceResponse().from_map(
            self.do_rpcrequest('DeleteConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_conference_with_options_async(
        self,
        request: rtc_20180111_models.DeleteConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteConferenceResponse().from_map(
            await self.do_rpcrequest_async('DeleteConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_conference(
        self,
        request: rtc_20180111_models.DeleteConferenceRequest,
    ) -> rtc_20180111_models.DeleteConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_conference_with_options(request, runtime)

    async def delete_conference_async(
        self,
        request: rtc_20180111_models.DeleteConferenceRequest,
    ) -> rtc_20180111_models.DeleteConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_conference_with_options_async(request, runtime)

    def delete_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteEventSubscribeResponse().from_map(
            self.do_rpcrequest('DeleteEventSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteEventSubscribeResponse().from_map(
            await self.do_rpcrequest_async('DeleteEventSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_event_subscribe(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_subscribe_with_options(request, runtime)

    async def delete_event_subscribe_async(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_subscribe_with_options_async(request, runtime)

    def delete_mpulayout_with_options(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteMPULayoutResponse().from_map(
            self.do_rpcrequest('DeleteMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteMPULayoutResponse().from_map(
            await self.do_rpcrequest_async('DeleteMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mpulayout(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mpulayout_with_options(request, runtime)

    async def delete_mpulayout_async(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mpulayout_with_options_async(request, runtime)

    def delete_mpurule_with_options(
        self,
        request: rtc_20180111_models.DeleteMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteMPURuleResponse().from_map(
            self.do_rpcrequest('DeleteMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mpurule_with_options_async(
        self,
        request: rtc_20180111_models.DeleteMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteMPURuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mpurule(
        self,
        request: rtc_20180111_models.DeleteMPURuleRequest,
    ) -> rtc_20180111_models.DeleteMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mpurule_with_options(request, runtime)

    async def delete_mpurule_async(
        self,
        request: rtc_20180111_models.DeleteMPURuleRequest,
    ) -> rtc_20180111_models.DeleteMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mpurule_with_options_async(request, runtime)

    def delete_record_template_with_options(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteRecordTemplateResponse().from_map(
            self.do_rpcrequest('DeleteRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_record_template_with_options_async(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteRecordTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_record_template(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_record_template_with_options(request, runtime)

    async def delete_record_template_async(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_template_with_options_async(request, runtime)

    def delete_subscribe_with_options(
        self,
        request: rtc_20180111_models.DeleteSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteSubscribeResponse().from_map(
            self.do_rpcrequest('DeleteSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.DeleteSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DeleteSubscribeResponse().from_map(
            await self.do_rpcrequest_async('DeleteSubscribe', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_subscribe(
        self,
        request: rtc_20180111_models.DeleteSubscribeRequest,
    ) -> rtc_20180111_models.DeleteSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_with_options(request, runtime)

    async def delete_subscribe_async(
        self,
        request: rtc_20180111_models.DeleteSubscribeRequest,
    ) -> rtc_20180111_models.DeleteSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_subscribe_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeAppsResponse().from_map(
            self.do_rpcrequest('DescribeApps', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeAppsResponse().from_map(
            await self.do_rpcrequest_async('DescribeApps', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apps(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeAutoLiveStreamRuleResponse().from_map(
            self.do_rpcrequest('DescribeAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeAutoLiveStreamRuleResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoLiveStreamRule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_live_stream_rule_with_options(request, runtime)

    async def describe_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_live_stream_rule_with_options_async(request, runtime)

    def describe_channel_participants_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeChannelParticipantsResponse().from_map(
            self.do_rpcrequest('DescribeChannelParticipants', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_channel_participants_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeChannelParticipantsResponse().from_map(
            await self.do_rpcrequest_async('DescribeChannelParticipants', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_channel_participants(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_participants_with_options(request, runtime)

    async def describe_channel_participants_async(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_participants_with_options_async(request, runtime)

    def describe_channel_users_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeChannelUsersResponse().from_map(
            self.do_rpcrequest('DescribeChannelUsers', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_channel_users_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeChannelUsersResponse().from_map(
            await self.do_rpcrequest_async('DescribeChannelUsers', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_channel_users(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_users_with_options(request, runtime)

    async def describe_channel_users_async(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_users_with_options_async(request, runtime)

    def describe_conference_auth_info_with_options(
        self,
        request: rtc_20180111_models.DescribeConferenceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeConferenceAuthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeConferenceAuthInfoResponse().from_map(
            self.do_rpcrequest('DescribeConferenceAuthInfo', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_conference_auth_info_with_options_async(
        self,
        request: rtc_20180111_models.DescribeConferenceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeConferenceAuthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeConferenceAuthInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeConferenceAuthInfo', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_conference_auth_info(
        self,
        request: rtc_20180111_models.DescribeConferenceAuthInfoRequest,
    ) -> rtc_20180111_models.DescribeConferenceAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_conference_auth_info_with_options(request, runtime)

    async def describe_conference_auth_info_async(
        self,
        request: rtc_20180111_models.DescribeConferenceAuthInfoRequest,
    ) -> rtc_20180111_models.DescribeConferenceAuthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_conference_auth_info_with_options_async(request, runtime)

    def describe_mpulayout_info_with_options(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutInfoResponse().from_map(
            self.do_rpcrequest('DescribeMPULayoutInfo', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mpulayout_info_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeMPULayoutInfo', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mpulayout_info(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_info_with_options(request, runtime)

    async def describe_mpulayout_info_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mpulayout_info_with_options_async(request, runtime)

    def describe_mpulayout_info_list_with_options(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutInfoListResponse().from_map(
            self.do_rpcrequest('DescribeMPULayoutInfoList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mpulayout_info_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutInfoListResponse().from_map(
            await self.do_rpcrequest_async('DescribeMPULayoutInfoList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mpulayout_info_list(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_info_list_with_options(request, runtime)

    async def describe_mpulayout_info_list_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mpulayout_info_list_with_options_async(request, runtime)

    def describe_mpulayout_list_with_options(
        self,
        request: rtc_20180111_models.DescribeMPULayoutListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutListResponse().from_map(
            self.do_rpcrequest('DescribeMPULayoutList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mpulayout_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPULayoutListResponse().from_map(
            await self.do_rpcrequest_async('DescribeMPULayoutList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mpulayout_list(
        self,
        request: rtc_20180111_models.DescribeMPULayoutListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_list_with_options(request, runtime)

    async def describe_mpulayout_list_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mpulayout_list_with_options_async(request, runtime)

    def describe_mpurule_with_options(
        self,
        request: rtc_20180111_models.DescribeMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPURuleResponse().from_map(
            self.do_rpcrequest('DescribeMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mpurule_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeMPURuleResponse().from_map(
            await self.do_rpcrequest_async('DescribeMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mpurule(
        self,
        request: rtc_20180111_models.DescribeMPURuleRequest,
    ) -> rtc_20180111_models.DescribeMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mpurule_with_options(request, runtime)

    async def describe_mpurule_async(
        self,
        request: rtc_20180111_models.DescribeMPURuleRequest,
    ) -> rtc_20180111_models.DescribeMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mpurule_with_options_async(request, runtime)

    def describe_record_files_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordFilesResponse().from_map(
            self.do_rpcrequest('DescribeRecordFiles', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_files_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordFiles', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_files(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_files_with_options(request, runtime)

    async def describe_record_files_async(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_files_with_options_async(request, runtime)

    def describe_record_tasks_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordTasksResponse().from_map(
            self.do_rpcrequest('DescribeRecordTasks', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_tasks_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordTasks', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_tasks(
        self,
        request: rtc_20180111_models.DescribeRecordTasksRequest,
    ) -> rtc_20180111_models.DescribeRecordTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_tasks_with_options(request, runtime)

    async def describe_record_tasks_async(
        self,
        request: rtc_20180111_models.DescribeRecordTasksRequest,
    ) -> rtc_20180111_models.DescribeRecordTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_tasks_with_options_async(request, runtime)

    def describe_record_templates_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeRecordTemplates', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_templates_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRecordTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecordTemplates', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_templates(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_templates_with_options(request, runtime)

    async def describe_record_templates_async(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_templates_with_options_async(request, runtime)

    def describe_rtcapp_key_with_options(
        self,
        request: rtc_20180111_models.DescribeRTCAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRTCAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRTCAppKeyResponse().from_map(
            self.do_rpcrequest('DescribeRTCAppKey', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtcapp_key_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRTCAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRTCAppKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRTCAppKeyResponse().from_map(
            await self.do_rpcrequest_async('DescribeRTCAppKey', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtcapp_key(
        self,
        request: rtc_20180111_models.DescribeRTCAppKeyRequest,
    ) -> rtc_20180111_models.DescribeRTCAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtcapp_key_with_options(request, runtime)

    async def describe_rtcapp_key_async(
        self,
        request: rtc_20180111_models.DescribeRTCAppKeyRequest,
    ) -> rtc_20180111_models.DescribeRTCAppKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtcapp_key_with_options_async(request, runtime)

    def describe_rtc_channel_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelCntDataResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelCntDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_cnt_data_with_options(request, runtime)

    async def describe_rtc_channel_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_cnt_data_with_options_async(request, runtime)

    def describe_rtc_channel_detail_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelDetailResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelDetail', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_detail_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelDetail', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_detail(
        self,
        request: rtc_20180111_models.DescribeRtcChannelDetailRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_detail_with_options(request, runtime)

    async def describe_rtc_channel_detail_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelDetailRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_detail_with_options_async(request, runtime)

    def describe_rtc_channel_list_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelListResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_list(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_list_with_options(request, runtime)

    async def describe_rtc_channel_list_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_list_with_options_async(request, runtime)

    def describe_rtc_channel_metric_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelMetricResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelMetric', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_metric_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelMetricResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelMetric', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_metric(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_metric_with_options(request, runtime)

    async def describe_rtc_channel_metric_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_metric_with_options_async(request, runtime)

    def describe_rtc_channel_metrics_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelMetricsResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelMetrics', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_metrics_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelMetricsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelMetrics', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_metrics(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricsRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_metrics_with_options(request, runtime)

    async def describe_rtc_channel_metrics_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricsRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_metrics_with_options_async(request, runtime)

    def describe_rtc_channels_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelsResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannels', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channels_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannels', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channels(
        self,
        request: rtc_20180111_models.DescribeRtcChannelsRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channels_with_options(request, runtime)

    async def describe_rtc_channels_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelsRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channels_with_options_async(request, runtime)

    def describe_rtc_channel_user_list_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelUserListResponse().from_map(
            self.do_rpcrequest('DescribeRtcChannelUserList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_channel_user_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcChannelUserListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcChannelUserList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_channel_user_list(
        self,
        request: rtc_20180111_models.DescribeRtcChannelUserListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_user_list_with_options(request, runtime)

    async def describe_rtc_channel_user_list_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelUserListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_user_list_with_options_async(request, runtime)

    def describe_rtc_duration_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcDurationDataResponse().from_map(
            self.do_rpcrequest('DescribeRtcDurationData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_duration_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcDurationDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcDurationData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_duration_data(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_duration_data_with_options(request, runtime)

    async def describe_rtc_duration_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_duration_data_with_options_async(request, runtime)

    def describe_rtc_peak_channel_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse().from_map(
            self.do_rpcrequest('DescribeRtcPeakChannelCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_peak_channel_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcPeakChannelCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_peak_channel_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_peak_channel_cnt_data_with_options(request, runtime)

    async def describe_rtc_peak_channel_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_peak_channel_cnt_data_with_options_async(request, runtime)

    def describe_rtc_peak_user_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcPeakUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcPeakUserCntDataResponse().from_map(
            self.do_rpcrequest('DescribeRtcPeakUserCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_peak_user_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcPeakUserCntDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcPeakUserCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_peak_user_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcPeakUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_peak_user_cnt_data_with_options(request, runtime)

    async def describe_rtc_peak_user_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_peak_user_cnt_data_with_options_async(request, runtime)

    def describe_rtc_scale_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcScaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcScaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcScaleResponse().from_map(
            self.do_rpcrequest('DescribeRtcScale', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_scale_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcScaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcScaleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcScaleResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcScale', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_scale(
        self,
        request: rtc_20180111_models.DescribeRtcScaleRequest,
    ) -> rtc_20180111_models.DescribeRtcScaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_scale_with_options(request, runtime)

    async def describe_rtc_scale_async(
        self,
        request: rtc_20180111_models.DescribeRtcScaleRequest,
    ) -> rtc_20180111_models.DescribeRtcScaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_scale_with_options_async(request, runtime)

    def describe_rtc_scale_detail_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcScaleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcScaleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcScaleDetailResponse().from_map(
            self.do_rpcrequest('DescribeRtcScaleDetail', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_scale_detail_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcScaleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcScaleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcScaleDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcScaleDetail', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_scale_detail(
        self,
        request: rtc_20180111_models.DescribeRtcScaleDetailRequest,
    ) -> rtc_20180111_models.DescribeRtcScaleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_scale_detail_with_options(request, runtime)

    async def describe_rtc_scale_detail_async(
        self,
        request: rtc_20180111_models.DescribeRtcScaleDetailRequest,
    ) -> rtc_20180111_models.DescribeRtcScaleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_scale_detail_with_options_async(request, runtime)

    def describe_rtc_user_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserCntDataResponse().from_map(
            self.do_rpcrequest('DescribeRtcUserCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_user_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserCntDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcUserCntData', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_user_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_user_cnt_data_with_options(request, runtime)

    async def describe_rtc_user_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_user_cnt_data_with_options_async(request, runtime)

    def describe_rtc_user_events_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcUserEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserEventsResponse().from_map(
            self.do_rpcrequest('DescribeRtcUserEvents', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_user_events_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcUserEvents', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_user_events(
        self,
        request: rtc_20180111_models.DescribeRtcUserEventsRequest,
    ) -> rtc_20180111_models.DescribeRtcUserEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_user_events_with_options(request, runtime)

    async def describe_rtc_user_events_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserEventsRequest,
    ) -> rtc_20180111_models.DescribeRtcUserEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_user_events_with_options_async(request, runtime)

    def describe_rtc_user_list_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserListResponse().from_map(
            self.do_rpcrequest('DescribeRtcUserList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rtc_user_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeRtcUserListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRtcUserList', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rtc_user_list(
        self,
        request: rtc_20180111_models.DescribeRtcUserListRequest,
    ) -> rtc_20180111_models.DescribeRtcUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_user_list_with_options(request, runtime)

    async def describe_rtc_user_list_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserListRequest,
    ) -> rtc_20180111_models.DescribeRtcUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_user_list_with_options_async(request, runtime)

    def describe_user_info_in_channel_with_options(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeUserInfoInChannelResponse().from_map(
            self.do_rpcrequest('DescribeUserInfoInChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_info_in_channel_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DescribeUserInfoInChannelResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserInfoInChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_info_in_channel(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_in_channel_with_options(request, runtime)

    async def describe_user_info_in_channel_async(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_info_in_channel_with_options_async(request, runtime)

    def disable_mpurule_with_options(
        self,
        request: rtc_20180111_models.DisableMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DisableMPURuleResponse().from_map(
            self.do_rpcrequest('DisableMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_mpurule_with_options_async(
        self,
        request: rtc_20180111_models.DisableMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.DisableMPURuleResponse().from_map(
            await self.do_rpcrequest_async('DisableMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_mpurule(
        self,
        request: rtc_20180111_models.DisableMPURuleRequest,
    ) -> rtc_20180111_models.DisableMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_mpurule_with_options(request, runtime)

    async def disable_mpurule_async(
        self,
        request: rtc_20180111_models.DisableMPURuleRequest,
    ) -> rtc_20180111_models.DisableMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_mpurule_with_options_async(request, runtime)

    def enable_mpurule_with_options(
        self,
        request: rtc_20180111_models.EnableMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.EnableMPURuleResponse().from_map(
            self.do_rpcrequest('EnableMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_mpurule_with_options_async(
        self,
        request: rtc_20180111_models.EnableMPURuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableMPURuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.EnableMPURuleResponse().from_map(
            await self.do_rpcrequest_async('EnableMPURule', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_mpurule(
        self,
        request: rtc_20180111_models.EnableMPURuleRequest,
    ) -> rtc_20180111_models.EnableMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_mpurule_with_options(request, runtime)

    async def enable_mpurule_async(
        self,
        request: rtc_20180111_models.EnableMPURuleRequest,
    ) -> rtc_20180111_models.EnableMPURuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_mpurule_with_options_async(request, runtime)

    def get_mputask_status_with_options(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.GetMPUTaskStatusResponse().from_map(
            self.do_rpcrequest('GetMPUTaskStatus', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mputask_status_with_options_async(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.GetMPUTaskStatusResponse().from_map(
            await self.do_rpcrequest_async('GetMPUTaskStatus', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mputask_status(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mputask_status_with_options(request, runtime)

    async def get_mputask_status_async(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mputask_status_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyAppResponse().from_map(
            self.do_rpcrequest('ModifyApp', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyAppResponse().from_map(
            await self.do_rpcrequest_async('ModifyApp', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_app(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
    ) -> rtc_20180111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
    ) -> rtc_20180111_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_conference_with_options(
        self,
        request: rtc_20180111_models.ModifyConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyConferenceResponse().from_map(
            self.do_rpcrequest('ModifyConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_conference_with_options_async(
        self,
        request: rtc_20180111_models.ModifyConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyConferenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyConferenceResponse().from_map(
            await self.do_rpcrequest_async('ModifyConference', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_conference(
        self,
        request: rtc_20180111_models.ModifyConferenceRequest,
    ) -> rtc_20180111_models.ModifyConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_conference_with_options(request, runtime)

    async def modify_conference_async(
        self,
        request: rtc_20180111_models.ModifyConferenceRequest,
    ) -> rtc_20180111_models.ModifyConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_conference_with_options_async(request, runtime)

    def modify_mpulayout_with_options(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyMPULayoutResponse().from_map(
            self.do_rpcrequest('ModifyMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ModifyMPULayoutResponse().from_map(
            await self.do_rpcrequest_async('ModifyMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_mpulayout(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_mpulayout_with_options(request, runtime)

    async def modify_mpulayout_async(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_mpulayout_with_options_async(request, runtime)

    def mute_audio_with_options(
        self,
        request: rtc_20180111_models.MuteAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.MuteAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.MuteAudioResponse().from_map(
            self.do_rpcrequest('MuteAudio', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mute_audio_with_options_async(
        self,
        request: rtc_20180111_models.MuteAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.MuteAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.MuteAudioResponse().from_map(
            await self.do_rpcrequest_async('MuteAudio', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_audio(
        self,
        request: rtc_20180111_models.MuteAudioRequest,
    ) -> rtc_20180111_models.MuteAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.mute_audio_with_options(request, runtime)

    async def mute_audio_async(
        self,
        request: rtc_20180111_models.MuteAudioRequest,
    ) -> rtc_20180111_models.MuteAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mute_audio_with_options_async(request, runtime)

    def mute_audio_all_with_options(
        self,
        request: rtc_20180111_models.MuteAudioAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.MuteAudioAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.MuteAudioAllResponse().from_map(
            self.do_rpcrequest('MuteAudioAll', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mute_audio_all_with_options_async(
        self,
        request: rtc_20180111_models.MuteAudioAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.MuteAudioAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.MuteAudioAllResponse().from_map(
            await self.do_rpcrequest_async('MuteAudioAll', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_audio_all(
        self,
        request: rtc_20180111_models.MuteAudioAllRequest,
    ) -> rtc_20180111_models.MuteAudioAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.mute_audio_all_with_options(request, runtime)

    async def mute_audio_all_async(
        self,
        request: rtc_20180111_models.MuteAudioAllRequest,
    ) -> rtc_20180111_models.MuteAudioAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mute_audio_all_with_options_async(request, runtime)

    def receive_notify_with_options(
        self,
        request: rtc_20180111_models.ReceiveNotifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ReceiveNotifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ReceiveNotifyResponse().from_map(
            self.do_rpcrequest('ReceiveNotify', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def receive_notify_with_options_async(
        self,
        request: rtc_20180111_models.ReceiveNotifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ReceiveNotifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.ReceiveNotifyResponse().from_map(
            await self.do_rpcrequest_async('ReceiveNotify', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def receive_notify(
        self,
        request: rtc_20180111_models.ReceiveNotifyRequest,
    ) -> rtc_20180111_models.ReceiveNotifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.receive_notify_with_options(request, runtime)

    async def receive_notify_async(
        self,
        request: rtc_20180111_models.ReceiveNotifyRequest,
    ) -> rtc_20180111_models.ReceiveNotifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.receive_notify_with_options_async(request, runtime)

    def remove_participants_with_options(
        self,
        request: rtc_20180111_models.RemoveParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveParticipantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.RemoveParticipantsResponse().from_map(
            self.do_rpcrequest('RemoveParticipants', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_participants_with_options_async(
        self,
        request: rtc_20180111_models.RemoveParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveParticipantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.RemoveParticipantsResponse().from_map(
            await self.do_rpcrequest_async('RemoveParticipants', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_participants(
        self,
        request: rtc_20180111_models.RemoveParticipantsRequest,
    ) -> rtc_20180111_models.RemoveParticipantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_participants_with_options(request, runtime)

    async def remove_participants_async(
        self,
        request: rtc_20180111_models.RemoveParticipantsRequest,
    ) -> rtc_20180111_models.RemoveParticipantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_participants_with_options_async(request, runtime)

    def remove_terminals_with_options(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.RemoveTerminalsResponse().from_map(
            self.do_rpcrequest('RemoveTerminals', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_terminals_with_options_async(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.RemoveTerminalsResponse().from_map(
            await self.do_rpcrequest_async('RemoveTerminals', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_terminals(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_terminals_with_options(request, runtime)

    async def remove_terminals_async(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_terminals_with_options_async(request, runtime)

    def set_channel_property_with_options(
        self,
        request: rtc_20180111_models.SetChannelPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.SetChannelPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.SetChannelPropertyResponse().from_map(
            self.do_rpcrequest('SetChannelProperty', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_channel_property_with_options_async(
        self,
        request: rtc_20180111_models.SetChannelPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.SetChannelPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.SetChannelPropertyResponse().from_map(
            await self.do_rpcrequest_async('SetChannelProperty', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_channel_property(
        self,
        request: rtc_20180111_models.SetChannelPropertyRequest,
    ) -> rtc_20180111_models.SetChannelPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_channel_property_with_options(request, runtime)

    async def set_channel_property_async(
        self,
        request: rtc_20180111_models.SetChannelPropertyRequest,
    ) -> rtc_20180111_models.SetChannelPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_channel_property_with_options_async(request, runtime)

    def start_mputask_with_options(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StartMPUTaskResponse().from_map(
            self.do_rpcrequest('StartMPUTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_mputask_with_options_async(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StartMPUTaskResponse().from_map(
            await self.do_rpcrequest_async('StartMPUTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_mputask(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_mputask_with_options(request, runtime)

    async def start_mputask_async(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_mputask_with_options_async(request, runtime)

    def start_record_task_with_options(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StartRecordTaskResponse().from_map(
            self.do_rpcrequest('StartRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StartRecordTaskResponse().from_map(
            await self.do_rpcrequest_async('StartRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_record_task(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_record_task_with_options(request, runtime)

    async def start_record_task_async(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_record_task_with_options_async(request, runtime)

    def stop_channel_user_publish_with_options(
        self,
        request: rtc_20180111_models.StopChannelUserPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopChannelUserPublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopChannelUserPublishResponse().from_map(
            self.do_rpcrequest('StopChannelUserPublish', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_channel_user_publish_with_options_async(
        self,
        request: rtc_20180111_models.StopChannelUserPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopChannelUserPublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopChannelUserPublishResponse().from_map(
            await self.do_rpcrequest_async('StopChannelUserPublish', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_channel_user_publish(
        self,
        request: rtc_20180111_models.StopChannelUserPublishRequest,
    ) -> rtc_20180111_models.StopChannelUserPublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_channel_user_publish_with_options(request, runtime)

    async def stop_channel_user_publish_async(
        self,
        request: rtc_20180111_models.StopChannelUserPublishRequest,
    ) -> rtc_20180111_models.StopChannelUserPublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_channel_user_publish_with_options_async(request, runtime)

    def stop_mputask_with_options(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopMPUTaskResponse().from_map(
            self.do_rpcrequest('StopMPUTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_mputask_with_options_async(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopMPUTaskResponse().from_map(
            await self.do_rpcrequest_async('StopMPUTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_mputask(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_mputask_with_options(request, runtime)

    async def stop_mputask_async(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_mputask_with_options_async(request, runtime)

    def stop_record_task_with_options(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopRecordTaskResponse().from_map(
            self.do_rpcrequest('StopRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.StopRecordTaskResponse().from_map(
            await self.do_rpcrequest_async('StopRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_record_task(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_record_task_with_options(request, runtime)

    async def stop_record_task_async(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_record_task_with_options_async(request, runtime)

    def unmute_audio_with_options(
        self,
        request: rtc_20180111_models.UnmuteAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UnmuteAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UnmuteAudioResponse().from_map(
            self.do_rpcrequest('UnmuteAudio', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unmute_audio_with_options_async(
        self,
        request: rtc_20180111_models.UnmuteAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UnmuteAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UnmuteAudioResponse().from_map(
            await self.do_rpcrequest_async('UnmuteAudio', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unmute_audio(
        self,
        request: rtc_20180111_models.UnmuteAudioRequest,
    ) -> rtc_20180111_models.UnmuteAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.unmute_audio_with_options(request, runtime)

    async def unmute_audio_async(
        self,
        request: rtc_20180111_models.UnmuteAudioRequest,
    ) -> rtc_20180111_models.UnmuteAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unmute_audio_with_options_async(request, runtime)

    def unmute_audio_all_with_options(
        self,
        request: rtc_20180111_models.UnmuteAudioAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UnmuteAudioAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UnmuteAudioAllResponse().from_map(
            self.do_rpcrequest('UnmuteAudioAll', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unmute_audio_all_with_options_async(
        self,
        request: rtc_20180111_models.UnmuteAudioAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UnmuteAudioAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UnmuteAudioAllResponse().from_map(
            await self.do_rpcrequest_async('UnmuteAudioAll', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unmute_audio_all(
        self,
        request: rtc_20180111_models.UnmuteAudioAllRequest,
    ) -> rtc_20180111_models.UnmuteAudioAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.unmute_audio_all_with_options(request, runtime)

    async def unmute_audio_all_async(
        self,
        request: rtc_20180111_models.UnmuteAudioAllRequest,
    ) -> rtc_20180111_models.UnmuteAudioAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unmute_audio_all_with_options_async(request, runtime)

    def update_channel_with_options(
        self,
        request: rtc_20180111_models.UpdateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateChannelResponse().from_map(
            self.do_rpcrequest('UpdateChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_channel_with_options_async(
        self,
        request: rtc_20180111_models.UpdateChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateChannelResponse().from_map(
            await self.do_rpcrequest_async('UpdateChannel', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_channel(
        self,
        request: rtc_20180111_models.UpdateChannelRequest,
    ) -> rtc_20180111_models.UpdateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_channel_with_options(request, runtime)

    async def update_channel_async(
        self,
        request: rtc_20180111_models.UpdateChannelRequest,
    ) -> rtc_20180111_models.UpdateChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_channel_with_options_async(request, runtime)

    def update_mpulayout_with_options(
        self,
        request: rtc_20180111_models.UpdateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateMPULayoutResponse().from_map(
            self.do_rpcrequest('UpdateMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.UpdateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPULayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateMPULayoutResponse().from_map(
            await self.do_rpcrequest_async('UpdateMPULayout', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mpulayout(
        self,
        request: rtc_20180111_models.UpdateMPULayoutRequest,
    ) -> rtc_20180111_models.UpdateMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mpulayout_with_options(request, runtime)

    async def update_mpulayout_async(
        self,
        request: rtc_20180111_models.UpdateMPULayoutRequest,
    ) -> rtc_20180111_models.UpdateMPULayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mpulayout_with_options_async(request, runtime)

    def update_record_task_with_options(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateRecordTaskResponse().from_map(
            self.do_rpcrequest('UpdateRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_record_task_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateRecordTaskResponse().from_map(
            await self.do_rpcrequest_async('UpdateRecordTask', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_record_task(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_record_task_with_options(request, runtime)

    async def update_record_task_async(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_record_task_with_options_async(request, runtime)

    def update_record_template_with_options(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateRecordTemplateResponse().from_map(
            self.do_rpcrequest('UpdateRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_record_template_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rtc_20180111_models.UpdateRecordTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateRecordTemplate', '2018-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_record_template(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_record_template_with_options(request, runtime)

    async def update_record_template_async(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_record_template_with_options_async(request, runtime)

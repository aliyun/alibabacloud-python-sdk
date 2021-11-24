# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rtc20180111 import models as rtc_20180111_models
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
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.AddRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_record_template_with_options_async(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.AddRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallbackUrl'] = request.callback_url
        query['ChannelId'] = request.channel_id
        query['ClientToken'] = request.client_token
        query['Events'] = request.events
        query['OwnerId'] = request.owner_id
        query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallbackUrl'] = request.callback_url
        query['ChannelId'] = request.channel_id
        query['ClientToken'] = request.client_token
        query['Events'] = request.events
        query['OwnerId'] = request.owner_id
        query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_record_template_with_options(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_template_with_options_async(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['Order'] = request.order
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_participants_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['Order'] = request.order
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_users_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_mpulayout_info_list_with_options(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mpulayout_info_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_record_files_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['EndTime'] = request.end_time
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_files_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['EndTime'] = request.end_time
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordFilesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_record_templates_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_templates_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_user_info_in_channel_with_options(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_info_in_channel_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            await self.call_api_async(params, req, runtime)
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

    def disable_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_live_stream_rule_with_options(request, runtime)

    async def disable_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_live_stream_rule_with_options_async(request, runtime)

    def enable_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_live_stream_rule_with_options(request, runtime)

    async def enable_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_live_stream_rule_with_options_async(request, runtime)

    def get_mputask_status_with_options(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mputask_status_with_options_async(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_mpulayout_with_options(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.ModifyMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.ModifyMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_terminals_with_options(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.RemoveTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_terminals_with_options_async(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.RemoveTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def start_mputask_with_options(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ChannelId'] = request.channel_id
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['PayloadType'] = request.payload_type
        query['ReportVad'] = request.report_vad
        query['RtpExtInfo'] = request.rtp_ext_info
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['StreamURL'] = request.stream_url
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskType'] = request.task_type
        query['TimeStampRef'] = request.time_stamp_ref
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['VadInterval'] = request.vad_interval
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_mputask_with_options_async(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ChannelId'] = request.channel_id
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['PayloadType'] = request.payload_type
        query['ReportVad'] = request.report_vad
        query['RtpExtInfo'] = request.rtp_ext_info
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['StreamURL'] = request.stream_url
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskType'] = request.task_type
        query['TimeStampRef'] = request.time_stamp_ref
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['VadInterval'] = request.vad_interval
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopChannelUserPublish',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopChannelUserPublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_channel_user_publish_with_options_async(
        self,
        request: rtc_20180111_models.StopChannelUserPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopChannelUserPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopChannelUserPublish',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopChannelUserPublishResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_mputask_with_options_async(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleId'] = request.rule_id
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleId'] = request.rule_id
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_live_stream_rule_with_options(request, runtime)

    async def update_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_live_stream_rule_with_options_async(request, runtime)

    def update_mputask_with_options(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mputask_with_options_async(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mputask(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mputask_with_options(request, runtime)

    async def update_mputask_async(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mputask_with_options_async(request, runtime)

    def update_record_task_with_options(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['LayoutIds'] = request.layout_ids
        query['OwnerId'] = request.owner_id
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_task_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['LayoutIds'] = request.layout_ids
        query['OwnerId'] = request.owner_id
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_template_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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

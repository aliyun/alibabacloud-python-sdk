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
        """
        @param request: AddRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
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
            rtc_20180111_models.AddRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_record_template_with_options_async(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        """
        @param request: AddRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
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
            rtc_20180111_models.AddRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_record_template(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        """
        @param request: AddRecordTemplateRequest
        @return: AddRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_record_template_with_options(request, runtime)

    async def add_record_template_async(
        self,
        request: rtc_20180111_models.AddRecordTemplateRequest,
    ) -> rtc_20180111_models.AddRecordTemplateResponse:
        """
        @param request: AddRecordTemplateRequest
        @return: AddRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_record_template_with_options_async(request, runtime)

    def create_app_layout_with_options(
        self,
        tmp_req: rtc_20180111_models.CreateAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppLayoutResponse:
        """
        @summary 新增app自定义布局
        
        @param tmp_req: CreateAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppLayout',
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
            rtc_20180111_models.CreateAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_layout_with_options_async(
        self,
        tmp_req: rtc_20180111_models.CreateAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppLayoutResponse:
        """
        @summary 新增app自定义布局
        
        @param tmp_req: CreateAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppLayout',
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
            rtc_20180111_models.CreateAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_layout(
        self,
        request: rtc_20180111_models.CreateAppLayoutRequest,
    ) -> rtc_20180111_models.CreateAppLayoutResponse:
        """
        @summary 新增app自定义布局
        
        @param request: CreateAppLayoutRequest
        @return: CreateAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_layout_with_options(request, runtime)

    async def create_app_layout_async(
        self,
        request: rtc_20180111_models.CreateAppLayoutRequest,
    ) -> rtc_20180111_models.CreateAppLayoutResponse:
        """
        @summary 新增app自定义布局
        
        @param request: CreateAppLayoutRequest
        @return: CreateAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_layout_with_options_async(request, runtime)

    def create_app_record_template_with_options(
        self,
        tmp_req: rtc_20180111_models.CreateAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppRecordTemplateResponse:
        """
        @summary 增加应用录制模版
        
        @param tmp_req: CreateAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_template):
            request.record_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppRecordTemplate',
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
            rtc_20180111_models.CreateAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_record_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.CreateAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppRecordTemplateResponse:
        """
        @summary 增加应用录制模版
        
        @param tmp_req: CreateAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_template):
            request.record_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppRecordTemplate',
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
            rtc_20180111_models.CreateAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_record_template(
        self,
        request: rtc_20180111_models.CreateAppRecordTemplateRequest,
    ) -> rtc_20180111_models.CreateAppRecordTemplateResponse:
        """
        @summary 增加应用录制模版
        
        @param request: CreateAppRecordTemplateRequest
        @return: CreateAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_record_template_with_options(request, runtime)

    async def create_app_record_template_async(
        self,
        request: rtc_20180111_models.CreateAppRecordTemplateRequest,
    ) -> rtc_20180111_models.CreateAppRecordTemplateResponse:
        """
        @summary 增加应用录制模版
        
        @param request: CreateAppRecordTemplateRequest
        @return: CreateAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_record_template_with_options_async(request, runtime)

    def create_app_streaming_out_template_with_options(
        self,
        tmp_req: rtc_20180111_models.CreateAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppStreamingOutTemplateResponse:
        """
        @summary 创建应用推流模版
        
        @param tmp_req: CreateAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppStreamingOutTemplate',
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
            rtc_20180111_models.CreateAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_streaming_out_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.CreateAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAppStreamingOutTemplateResponse:
        """
        @summary 创建应用推流模版
        
        @param tmp_req: CreateAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppStreamingOutTemplate',
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
            rtc_20180111_models.CreateAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_streaming_out_template(
        self,
        request: rtc_20180111_models.CreateAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.CreateAppStreamingOutTemplateResponse:
        """
        @summary 创建应用推流模版
        
        @param request: CreateAppStreamingOutTemplateRequest
        @return: CreateAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_streaming_out_template_with_options(request, runtime)

    async def create_app_streaming_out_template_async(
        self,
        request: rtc_20180111_models.CreateAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.CreateAppStreamingOutTemplateResponse:
        """
        @summary 创建应用推流模版
        
        @param request: CreateAppStreamingOutTemplateRequest
        @return: CreateAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_streaming_out_template_with_options_async(request, runtime)

    def create_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        """
        @param request: CreateAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
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
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        """
        @param request: CreateAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
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
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        """
        @param request: CreateAutoLiveStreamRuleRequest
        @return: CreateAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_live_stream_rule_with_options(request, runtime)

    async def create_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.CreateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.CreateAutoLiveStreamRuleResponse:
        """
        @param request: CreateAutoLiveStreamRuleRequest
        @return: CreateAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_live_stream_rule_with_options_async(request, runtime)

    def create_cloud_note_phrases_with_options(
        self,
        tmp_req: rtc_20180111_models.CreateCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateCloudNotePhrasesResponse:
        """
        @summary 增加纪要热词表
        
        @param tmp_req: CreateCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudNotePhrases',
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
            rtc_20180111_models.CreateCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_note_phrases_with_options_async(
        self,
        tmp_req: rtc_20180111_models.CreateCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateCloudNotePhrasesResponse:
        """
        @summary 增加纪要热词表
        
        @param tmp_req: CreateCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudNotePhrases',
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
            rtc_20180111_models.CreateCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_note_phrases(
        self,
        request: rtc_20180111_models.CreateCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.CreateCloudNotePhrasesResponse:
        """
        @summary 增加纪要热词表
        
        @param request: CreateCloudNotePhrasesRequest
        @return: CreateCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_note_phrases_with_options(request, runtime)

    async def create_cloud_note_phrases_async(
        self,
        request: rtc_20180111_models.CreateCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.CreateCloudNotePhrasesResponse:
        """
        @summary 增加纪要热词表
        
        @param request: CreateCloudNotePhrasesRequest
        @return: CreateCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_note_phrases_with_options_async(request, runtime)

    def create_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        """
        @param request: CreateEventSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.events):
            query['Events'] = request.events
        if not UtilClient.is_unset(request.need_callback_auth):
            query['NeedCallbackAuth'] = request.need_callback_auth
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
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
            rtc_20180111_models.CreateEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        """
        @param request: CreateEventSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.events):
            query['Events'] = request.events
        if not UtilClient.is_unset(request.need_callback_auth):
            query['NeedCallbackAuth'] = request.need_callback_auth
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
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
            rtc_20180111_models.CreateEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_subscribe(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        """
        @param request: CreateEventSubscribeRequest
        @return: CreateEventSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_subscribe_with_options(request, runtime)

    async def create_event_subscribe_async(
        self,
        request: rtc_20180111_models.CreateEventSubscribeRequest,
    ) -> rtc_20180111_models.CreateEventSubscribeResponse:
        """
        @param request: CreateEventSubscribeRequest
        @return: CreateEventSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_event_subscribe_with_options_async(request, runtime)

    def create_mpulayout_with_options(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        """
        @param request: CreateMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
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
            rtc_20180111_models.CreateMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        """
        @param request: CreateMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
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
            rtc_20180111_models.CreateMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mpulayout(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        """
        @param request: CreateMPULayoutRequest
        @return: CreateMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mpulayout_with_options(request, runtime)

    async def create_mpulayout_async(
        self,
        request: rtc_20180111_models.CreateMPULayoutRequest,
    ) -> rtc_20180111_models.CreateMPULayoutResponse:
        """
        @param request: CreateMPULayoutRequest
        @return: CreateMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mpulayout_with_options_async(request, runtime)

    def delete_app_layout_with_options(
        self,
        tmp_req: rtc_20180111_models.DeleteAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppLayoutResponse:
        """
        @summary 删除app自定义布局
        
        @param tmp_req: DeleteAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppLayout',
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
            rtc_20180111_models.DeleteAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_layout_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DeleteAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppLayoutResponse:
        """
        @summary 删除app自定义布局
        
        @param tmp_req: DeleteAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppLayout',
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
            rtc_20180111_models.DeleteAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_layout(
        self,
        request: rtc_20180111_models.DeleteAppLayoutRequest,
    ) -> rtc_20180111_models.DeleteAppLayoutResponse:
        """
        @summary 删除app自定义布局
        
        @param request: DeleteAppLayoutRequest
        @return: DeleteAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_layout_with_options(request, runtime)

    async def delete_app_layout_async(
        self,
        request: rtc_20180111_models.DeleteAppLayoutRequest,
    ) -> rtc_20180111_models.DeleteAppLayoutResponse:
        """
        @summary 删除app自定义布局
        
        @param request: DeleteAppLayoutRequest
        @return: DeleteAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_layout_with_options_async(request, runtime)

    def delete_app_record_template_with_options(
        self,
        tmp_req: rtc_20180111_models.DeleteAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppRecordTemplateResponse:
        """
        @summary 删除应用录制模版
        
        @param tmp_req: DeleteAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppRecordTemplate',
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
            rtc_20180111_models.DeleteAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_record_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DeleteAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppRecordTemplateResponse:
        """
        @summary 删除应用录制模版
        
        @param tmp_req: DeleteAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppRecordTemplate',
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
            rtc_20180111_models.DeleteAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_record_template(
        self,
        request: rtc_20180111_models.DeleteAppRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteAppRecordTemplateResponse:
        """
        @summary 删除应用录制模版
        
        @param request: DeleteAppRecordTemplateRequest
        @return: DeleteAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_record_template_with_options(request, runtime)

    async def delete_app_record_template_async(
        self,
        request: rtc_20180111_models.DeleteAppRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteAppRecordTemplateResponse:
        """
        @summary 删除应用录制模版
        
        @param request: DeleteAppRecordTemplateRequest
        @return: DeleteAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_record_template_with_options_async(request, runtime)

    def delete_app_streaming_out_template_with_options(
        self,
        tmp_req: rtc_20180111_models.DeleteAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppStreamingOutTemplateResponse:
        """
        @summary 删除应用推流模版
        
        @param tmp_req: DeleteAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppStreamingOutTemplate',
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
            rtc_20180111_models.DeleteAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_streaming_out_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DeleteAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAppStreamingOutTemplateResponse:
        """
        @summary 删除应用推流模版
        
        @param tmp_req: DeleteAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppStreamingOutTemplate',
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
            rtc_20180111_models.DeleteAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_streaming_out_template(
        self,
        request: rtc_20180111_models.DeleteAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.DeleteAppStreamingOutTemplateResponse:
        """
        @summary 删除应用推流模版
        
        @param request: DeleteAppStreamingOutTemplateRequest
        @return: DeleteAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_streaming_out_template_with_options(request, runtime)

    async def delete_app_streaming_out_template_async(
        self,
        request: rtc_20180111_models.DeleteAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.DeleteAppStreamingOutTemplateResponse:
        """
        @summary 删除应用推流模版
        
        @param request: DeleteAppStreamingOutTemplateRequest
        @return: DeleteAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_streaming_out_template_with_options_async(request, runtime)

    def delete_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        """
        @param request: DeleteAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
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
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        """
        @param request: DeleteAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
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
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        """
        @param request: DeleteAutoLiveStreamRuleRequest
        @return: DeleteAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_live_stream_rule_with_options(request, runtime)

    async def delete_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DeleteAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DeleteAutoLiveStreamRuleResponse:
        """
        @param request: DeleteAutoLiveStreamRuleRequest
        @return: DeleteAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_live_stream_rule_with_options_async(request, runtime)

    def delete_channel_with_options(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        """
        @param request: DeleteChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChannel',
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
            rtc_20180111_models.DeleteChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_channel_with_options_async(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        """
        @param request: DeleteChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChannel',
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
            rtc_20180111_models.DeleteChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_channel(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        """
        @param request: DeleteChannelRequest
        @return: DeleteChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    async def delete_channel_async(
        self,
        request: rtc_20180111_models.DeleteChannelRequest,
    ) -> rtc_20180111_models.DeleteChannelResponse:
        """
        @param request: DeleteChannelRequest
        @return: DeleteChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_channel_with_options_async(request, runtime)

    def delete_cloud_note_phrases_with_options(
        self,
        tmp_req: rtc_20180111_models.DeleteCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteCloudNotePhrasesResponse:
        """
        @summary 删除纪要热词表
        
        @param tmp_req: DeleteCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudNotePhrases',
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
            rtc_20180111_models.DeleteCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_note_phrases_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DeleteCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteCloudNotePhrasesResponse:
        """
        @summary 删除纪要热词表
        
        @param tmp_req: DeleteCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudNotePhrases',
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
            rtc_20180111_models.DeleteCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_note_phrases(
        self,
        request: rtc_20180111_models.DeleteCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.DeleteCloudNotePhrasesResponse:
        """
        @summary 删除纪要热词表
        
        @param request: DeleteCloudNotePhrasesRequest
        @return: DeleteCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_note_phrases_with_options(request, runtime)

    async def delete_cloud_note_phrases_async(
        self,
        request: rtc_20180111_models.DeleteCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.DeleteCloudNotePhrasesResponse:
        """
        @summary 删除纪要热词表
        
        @param request: DeleteCloudNotePhrasesRequest
        @return: DeleteCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_note_phrases_with_options_async(request, runtime)

    def delete_event_subscribe_with_options(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        """
        @param request: DeleteEventSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscribe_id):
            query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
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
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_subscribe_with_options_async(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        """
        @param request: DeleteEventSubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventSubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscribe_id):
            query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
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
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_subscribe(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        """
        @param request: DeleteEventSubscribeRequest
        @return: DeleteEventSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_event_subscribe_with_options(request, runtime)

    async def delete_event_subscribe_async(
        self,
        request: rtc_20180111_models.DeleteEventSubscribeRequest,
    ) -> rtc_20180111_models.DeleteEventSubscribeResponse:
        """
        @param request: DeleteEventSubscribeRequest
        @return: DeleteEventSubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_subscribe_with_options_async(request, runtime)

    def delete_mpulayout_with_options(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        """
        @param request: DeleteMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
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
            rtc_20180111_models.DeleteMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        """
        @param request: DeleteMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
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
            rtc_20180111_models.DeleteMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mpulayout(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        """
        @param request: DeleteMPULayoutRequest
        @return: DeleteMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mpulayout_with_options(request, runtime)

    async def delete_mpulayout_async(
        self,
        request: rtc_20180111_models.DeleteMPULayoutRequest,
    ) -> rtc_20180111_models.DeleteMPULayoutResponse:
        """
        @param request: DeleteMPULayoutRequest
        @return: DeleteMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mpulayout_with_options_async(request, runtime)

    def delete_record_template_with_options(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        """
        @param request: DeleteRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
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
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_template_with_options_async(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        """
        @param request: DeleteRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
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
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record_template(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        """
        @param request: DeleteRecordTemplateRequest
        @return: DeleteRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_record_template_with_options(request, runtime)

    async def delete_record_template_async(
        self,
        request: rtc_20180111_models.DeleteRecordTemplateRequest,
    ) -> rtc_20180111_models.DeleteRecordTemplateResponse:
        """
        @param request: DeleteRecordTemplateRequest
        @return: DeleteRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_template_with_options_async(request, runtime)

    def describe_all_callback_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAllCallbackResponse:
        """
        @summary 列出系统支持的事件回调
        
        @param request: DescribeAllCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllCallbackResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAllCallback',
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
            rtc_20180111_models.DescribeAllCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_callback_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAllCallbackResponse:
        """
        @summary 列出系统支持的事件回调
        
        @param request: DescribeAllCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllCallbackResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAllCallback',
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
            rtc_20180111_models.DescribeAllCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_callback(self) -> rtc_20180111_models.DescribeAllCallbackResponse:
        """
        @summary 列出系统支持的事件回调
        
        @return: DescribeAllCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_callback_with_options(runtime)

    async def describe_all_callback_async(self) -> rtc_20180111_models.DescribeAllCallbackResponse:
        """
        @summary 列出系统支持的事件回调
        
        @return: DescribeAllCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_callback_with_options_async(runtime)

    def describe_app_call_status_with_options(
        self,
        request: rtc_20180111_models.DescribeAppCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppCallStatusResponse:
        """
        @summary 查看app回调开关
        
        @param request: DescribeAppCallStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppCallStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppCallStatus',
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
            rtc_20180111_models.DescribeAppCallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_call_status_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppCallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppCallStatusResponse:
        """
        @summary 查看app回调开关
        
        @param request: DescribeAppCallStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppCallStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppCallStatus',
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
            rtc_20180111_models.DescribeAppCallStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_call_status(
        self,
        request: rtc_20180111_models.DescribeAppCallStatusRequest,
    ) -> rtc_20180111_models.DescribeAppCallStatusResponse:
        """
        @summary 查看app回调开关
        
        @param request: DescribeAppCallStatusRequest
        @return: DescribeAppCallStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_call_status_with_options(request, runtime)

    async def describe_app_call_status_async(
        self,
        request: rtc_20180111_models.DescribeAppCallStatusRequest,
    ) -> rtc_20180111_models.DescribeAppCallStatusResponse:
        """
        @summary 查看app回调开关
        
        @param request: DescribeAppCallStatusRequest
        @return: DescribeAppCallStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_call_status_with_options_async(request, runtime)

    def describe_app_callback_secret_key_with_options(
        self,
        request: rtc_20180111_models.DescribeAppCallbackSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppCallbackSecretKeyResponse:
        """
        @summary 获取app回调密钥
        
        @param request: DescribeAppCallbackSecretKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppCallbackSecretKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppCallbackSecretKey',
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
            rtc_20180111_models.DescribeAppCallbackSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_callback_secret_key_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppCallbackSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppCallbackSecretKeyResponse:
        """
        @summary 获取app回调密钥
        
        @param request: DescribeAppCallbackSecretKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppCallbackSecretKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppCallbackSecretKey',
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
            rtc_20180111_models.DescribeAppCallbackSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_callback_secret_key(
        self,
        request: rtc_20180111_models.DescribeAppCallbackSecretKeyRequest,
    ) -> rtc_20180111_models.DescribeAppCallbackSecretKeyResponse:
        """
        @summary 获取app回调密钥
        
        @param request: DescribeAppCallbackSecretKeyRequest
        @return: DescribeAppCallbackSecretKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_callback_secret_key_with_options(request, runtime)

    async def describe_app_callback_secret_key_async(
        self,
        request: rtc_20180111_models.DescribeAppCallbackSecretKeyRequest,
    ) -> rtc_20180111_models.DescribeAppCallbackSecretKeyResponse:
        """
        @summary 获取app回调密钥
        
        @param request: DescribeAppCallbackSecretKeyRequest
        @return: DescribeAppCallbackSecretKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_callback_secret_key_with_options_async(request, runtime)

    def describe_app_key_with_options(
        self,
        request: rtc_20180111_models.DescribeAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppKeyResponse:
        """
        @summary 查看AppKey
        
        @param request: DescribeAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppKey',
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
            rtc_20180111_models.DescribeAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_key_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppKeyResponse:
        """
        @summary 查看AppKey
        
        @param request: DescribeAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppKey',
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
            rtc_20180111_models.DescribeAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_key(
        self,
        request: rtc_20180111_models.DescribeAppKeyRequest,
    ) -> rtc_20180111_models.DescribeAppKeyResponse:
        """
        @summary 查看AppKey
        
        @param request: DescribeAppKeyRequest
        @return: DescribeAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_key_with_options(request, runtime)

    async def describe_app_key_async(
        self,
        request: rtc_20180111_models.DescribeAppKeyRequest,
    ) -> rtc_20180111_models.DescribeAppKeyResponse:
        """
        @summary 查看AppKey
        
        @param request: DescribeAppKeyRequest
        @return: DescribeAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_key_with_options_async(request, runtime)

    def describe_app_layouts_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeAppLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppLayoutsResponse:
        """
        @summary 查询app自定义布局
        
        @param tmp_req: DescribeAppLayoutsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppLayoutsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppLayoutsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppLayouts',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_layouts_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeAppLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppLayoutsResponse:
        """
        @summary 查询app自定义布局
        
        @param tmp_req: DescribeAppLayoutsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppLayoutsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppLayoutsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppLayouts',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppLayoutsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_layouts(
        self,
        request: rtc_20180111_models.DescribeAppLayoutsRequest,
    ) -> rtc_20180111_models.DescribeAppLayoutsResponse:
        """
        @summary 查询app自定义布局
        
        @param request: DescribeAppLayoutsRequest
        @return: DescribeAppLayoutsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_layouts_with_options(request, runtime)

    async def describe_app_layouts_async(
        self,
        request: rtc_20180111_models.DescribeAppLayoutsRequest,
    ) -> rtc_20180111_models.DescribeAppLayoutsResponse:
        """
        @summary 查询app自定义布局
        
        @param request: DescribeAppLayoutsRequest
        @return: DescribeAppLayoutsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_layouts_with_options_async(request, runtime)

    def describe_app_live_stream_status_with_options(
        self,
        request: rtc_20180111_models.DescribeAppLiveStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppLiveStreamStatusResponse:
        """
        @summary 查看应用旁路开关
        
        @param request: DescribeAppLiveStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppLiveStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppLiveStreamStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppLiveStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_live_stream_status_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppLiveStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppLiveStreamStatusResponse:
        """
        @summary 查看应用旁路开关
        
        @param request: DescribeAppLiveStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppLiveStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppLiveStreamStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppLiveStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_live_stream_status(
        self,
        request: rtc_20180111_models.DescribeAppLiveStreamStatusRequest,
    ) -> rtc_20180111_models.DescribeAppLiveStreamStatusResponse:
        """
        @summary 查看应用旁路开关
        
        @param request: DescribeAppLiveStreamStatusRequest
        @return: DescribeAppLiveStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_live_stream_status_with_options(request, runtime)

    async def describe_app_live_stream_status_async(
        self,
        request: rtc_20180111_models.DescribeAppLiveStreamStatusRequest,
    ) -> rtc_20180111_models.DescribeAppLiveStreamStatusResponse:
        """
        @summary 查看应用旁路开关
        
        @param request: DescribeAppLiveStreamStatusRequest
        @return: DescribeAppLiveStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_live_stream_status_with_options_async(request, runtime)

    def describe_app_record_status_with_options(
        self,
        request: rtc_20180111_models.DescribeAppRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordStatusResponse:
        """
        @summary 查询应用录制开关
        
        @param request: DescribeAppRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_record_status_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordStatusResponse:
        """
        @summary 查询应用录制开关
        
        @param request: DescribeAppRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_record_status(
        self,
        request: rtc_20180111_models.DescribeAppRecordStatusRequest,
    ) -> rtc_20180111_models.DescribeAppRecordStatusResponse:
        """
        @summary 查询应用录制开关
        
        @param request: DescribeAppRecordStatusRequest
        @return: DescribeAppRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_record_status_with_options(request, runtime)

    async def describe_app_record_status_async(
        self,
        request: rtc_20180111_models.DescribeAppRecordStatusRequest,
    ) -> rtc_20180111_models.DescribeAppRecordStatusResponse:
        """
        @summary 查询应用录制开关
        
        @param request: DescribeAppRecordStatusRequest
        @return: DescribeAppRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_record_status_with_options_async(request, runtime)

    def describe_app_record_templates_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeAppRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordTemplatesResponse:
        """
        @summary 应用录制模版列表
        
        @param tmp_req: DescribeAppRecordTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppRecordTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordTemplates',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_record_templates_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeAppRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordTemplatesResponse:
        """
        @summary 应用录制模版列表
        
        @param tmp_req: DescribeAppRecordTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppRecordTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordTemplates',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_record_templates(
        self,
        request: rtc_20180111_models.DescribeAppRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeAppRecordTemplatesResponse:
        """
        @summary 应用录制模版列表
        
        @param request: DescribeAppRecordTemplatesRequest
        @return: DescribeAppRecordTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_record_templates_with_options(request, runtime)

    async def describe_app_record_templates_async(
        self,
        request: rtc_20180111_models.DescribeAppRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeAppRecordTemplatesResponse:
        """
        @summary 应用录制模版列表
        
        @param request: DescribeAppRecordTemplatesRequest
        @return: DescribeAppRecordTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_record_templates_with_options_async(request, runtime)

    def describe_app_recording_files_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeAppRecordingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordingFilesResponse:
        """
        @summary 查询录制列表
        
        @param tmp_req: DescribeAppRecordingFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordingFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppRecordingFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordingFiles',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordingFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_recording_files_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeAppRecordingFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppRecordingFilesResponse:
        """
        @summary 查询录制列表
        
        @param tmp_req: DescribeAppRecordingFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppRecordingFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppRecordingFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppRecordingFiles',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAppRecordingFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_recording_files(
        self,
        request: rtc_20180111_models.DescribeAppRecordingFilesRequest,
    ) -> rtc_20180111_models.DescribeAppRecordingFilesResponse:
        """
        @summary 查询录制列表
        
        @param request: DescribeAppRecordingFilesRequest
        @return: DescribeAppRecordingFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_recording_files_with_options(request, runtime)

    async def describe_app_recording_files_async(
        self,
        request: rtc_20180111_models.DescribeAppRecordingFilesRequest,
    ) -> rtc_20180111_models.DescribeAppRecordingFilesResponse:
        """
        @summary 查询录制列表
        
        @param request: DescribeAppRecordingFilesRequest
        @return: DescribeAppRecordingFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_recording_files_with_options_async(request, runtime)

    def describe_app_streaming_out_templates_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeAppStreamingOutTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse:
        """
        @summary 应用推流模版列表
        
        @param tmp_req: DescribeAppStreamingOutTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppStreamingOutTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppStreamingOutTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppStreamingOutTemplates',
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
            rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_streaming_out_templates_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeAppStreamingOutTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse:
        """
        @summary 应用推流模版列表
        
        @param tmp_req: DescribeAppStreamingOutTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppStreamingOutTemplatesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppStreamingOutTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppStreamingOutTemplates',
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
            rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_streaming_out_templates(
        self,
        request: rtc_20180111_models.DescribeAppStreamingOutTemplatesRequest,
    ) -> rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse:
        """
        @summary 应用推流模版列表
        
        @param request: DescribeAppStreamingOutTemplatesRequest
        @return: DescribeAppStreamingOutTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_streaming_out_templates_with_options(request, runtime)

    async def describe_app_streaming_out_templates_async(
        self,
        request: rtc_20180111_models.DescribeAppStreamingOutTemplatesRequest,
    ) -> rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse:
        """
        @summary 应用推流模版列表
        
        @param request: DescribeAppStreamingOutTemplatesRequest
        @return: DescribeAppStreamingOutTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_streaming_out_templates_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        """
        @summary App列表
        
        @param request: DescribeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
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
            rtc_20180111_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        """
        @summary App列表
        
        @param request: DescribeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
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
            rtc_20180111_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        """
        @summary App列表
        
        @param request: DescribeAppsRequest
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: rtc_20180111_models.DescribeAppsRequest,
    ) -> rtc_20180111_models.DescribeAppsResponse:
        """
        @summary App列表
        
        @param request: DescribeAppsRequest
        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        """
        @param request: DescribeAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
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
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        """
        @param request: DescribeAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
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
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        """
        @param request: DescribeAutoLiveStreamRuleRequest
        @return: DescribeAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_live_stream_rule_with_options(request, runtime)

    async def describe_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DescribeAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DescribeAutoLiveStreamRuleResponse:
        """
        @param request: DescribeAutoLiveStreamRuleRequest
        @return: DescribeAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_live_stream_rule_with_options_async(request, runtime)

    def describe_call_with_options(
        self,
        request: rtc_20180111_models.DescribeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallResponse:
        """
        @summary 调用DescribeCall获取单次通信详情。
        
        @param request: DescribeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCall',
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
            rtc_20180111_models.DescribeCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_call_with_options_async(
        self,
        request: rtc_20180111_models.DescribeCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallResponse:
        """
        @summary 调用DescribeCall获取单次通信详情。
        
        @param request: DescribeCallRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCall',
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
            rtc_20180111_models.DescribeCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_call(
        self,
        request: rtc_20180111_models.DescribeCallRequest,
    ) -> rtc_20180111_models.DescribeCallResponse:
        """
        @summary 调用DescribeCall获取单次通信详情。
        
        @param request: DescribeCallRequest
        @return: DescribeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_call_with_options(request, runtime)

    async def describe_call_async(
        self,
        request: rtc_20180111_models.DescribeCallRequest,
    ) -> rtc_20180111_models.DescribeCallResponse:
        """
        @summary 调用DescribeCall获取单次通信详情。
        
        @param request: DescribeCallRequest
        @return: DescribeCallResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_call_with_options_async(request, runtime)

    def describe_call_list_with_options(
        self,
        request: rtc_20180111_models.DescribeCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallListResponse:
        """
        @summary 调用DescribeCallList分页查询时间范围内创建的通信信息。
        
        @param request: DescribeCallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallList',
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
            rtc_20180111_models.DescribeCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_call_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallListResponse:
        """
        @summary 调用DescribeCallList分页查询时间范围内创建的通信信息。
        
        @param request: DescribeCallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallList',
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
            rtc_20180111_models.DescribeCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_call_list(
        self,
        request: rtc_20180111_models.DescribeCallListRequest,
    ) -> rtc_20180111_models.DescribeCallListResponse:
        """
        @summary 调用DescribeCallList分页查询时间范围内创建的通信信息。
        
        @param request: DescribeCallListRequest
        @return: DescribeCallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_call_list_with_options(request, runtime)

    async def describe_call_list_async(
        self,
        request: rtc_20180111_models.DescribeCallListRequest,
    ) -> rtc_20180111_models.DescribeCallListResponse:
        """
        @summary 调用DescribeCallList分页查询时间范围内创建的通信信息。
        
        @param request: DescribeCallListRequest
        @return: DescribeCallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_call_list_with_options_async(request, runtime)

    def describe_callbacks_with_options(
        self,
        request: rtc_20180111_models.DescribeCallbacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallbacksResponse:
        """
        @summary app事件回调列表
        
        @param request: DescribeCallbacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallbacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallbacks',
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
            rtc_20180111_models.DescribeCallbacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_callbacks_with_options_async(
        self,
        request: rtc_20180111_models.DescribeCallbacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCallbacksResponse:
        """
        @summary app事件回调列表
        
        @param request: DescribeCallbacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCallbacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallbacks',
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
            rtc_20180111_models.DescribeCallbacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_callbacks(
        self,
        request: rtc_20180111_models.DescribeCallbacksRequest,
    ) -> rtc_20180111_models.DescribeCallbacksResponse:
        """
        @summary app事件回调列表
        
        @param request: DescribeCallbacksRequest
        @return: DescribeCallbacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_callbacks_with_options(request, runtime)

    async def describe_callbacks_async(
        self,
        request: rtc_20180111_models.DescribeCallbacksRequest,
    ) -> rtc_20180111_models.DescribeCallbacksResponse:
        """
        @summary app事件回调列表
        
        @param request: DescribeCallbacksRequest
        @return: DescribeCallbacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_callbacks_with_options_async(request, runtime)

    def describe_channel_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelResponse:
        """
        @summary DescribeChannel
        
        @param request: DescribeChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannel',
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
            rtc_20180111_models.DescribeChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelResponse:
        """
        @summary DescribeChannel
        
        @param request: DescribeChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannel',
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
            rtc_20180111_models.DescribeChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel(
        self,
        request: rtc_20180111_models.DescribeChannelRequest,
    ) -> rtc_20180111_models.DescribeChannelResponse:
        """
        @summary DescribeChannel
        
        @param request: DescribeChannelRequest
        @return: DescribeChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_with_options(request, runtime)

    async def describe_channel_async(
        self,
        request: rtc_20180111_models.DescribeChannelRequest,
    ) -> rtc_20180111_models.DescribeChannelResponse:
        """
        @summary DescribeChannel
        
        @param request: DescribeChannelRequest
        @return: DescribeChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_with_options_async(request, runtime)

    def describe_channel_all_users_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelAllUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelAllUsersResponse:
        """
        @summary 查询频道的所有参会者
        
        @param request: DescribeChannelAllUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAllUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAllUsers',
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
            rtc_20180111_models.DescribeChannelAllUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_all_users_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelAllUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelAllUsersResponse:
        """
        @summary 查询频道的所有参会者
        
        @param request: DescribeChannelAllUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAllUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAllUsers',
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
            rtc_20180111_models.DescribeChannelAllUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_all_users(
        self,
        request: rtc_20180111_models.DescribeChannelAllUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelAllUsersResponse:
        """
        @summary 查询频道的所有参会者
        
        @param request: DescribeChannelAllUsersRequest
        @return: DescribeChannelAllUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_all_users_with_options(request, runtime)

    async def describe_channel_all_users_async(
        self,
        request: rtc_20180111_models.DescribeChannelAllUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelAllUsersResponse:
        """
        @summary 查询频道的所有参会者
        
        @param request: DescribeChannelAllUsersRequest
        @return: DescribeChannelAllUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_all_users_with_options_async(request, runtime)

    def describe_channel_area_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelAreaDistributionStatData获取频道地区分布统计数据。
        
        @param request: DescribeChannelAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAreaDistributionStatData',
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
            rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_area_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelAreaDistributionStatData获取频道地区分布统计数据。
        
        @param request: DescribeChannelAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAreaDistributionStatData',
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
            rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_area_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelAreaDistributionStatData获取频道地区分布统计数据。
        
        @param request: DescribeChannelAreaDistributionStatDataRequest
        @return: DescribeChannelAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_area_distribution_stat_data_with_options(request, runtime)

    async def describe_channel_area_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelAreaDistributionStatData获取频道地区分布统计数据。
        
        @param request: DescribeChannelAreaDistributionStatDataRequest
        @return: DescribeChannelAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_channel_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelDistributionStatData获取频道分布统计数据。
        
        @param request: DescribeChannelDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelDistributionStatData',
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
            rtc_20180111_models.DescribeChannelDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelDistributionStatData获取频道分布统计数据。
        
        @param request: DescribeChannelDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelDistributionStatData',
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
            rtc_20180111_models.DescribeChannelDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeChannelDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeChannelDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelDistributionStatData获取频道分布统计数据。
        
        @param request: DescribeChannelDistributionStatDataRequest
        @return: DescribeChannelDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_distribution_stat_data_with_options(request, runtime)

    async def describe_channel_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeChannelDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeChannelDistributionStatDataResponse:
        """
        @summary 调用DescribeChannelDistributionStatData获取频道分布统计数据。
        
        @param request: DescribeChannelDistributionStatDataRequest
        @return: DescribeChannelDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_distribution_stat_data_with_options_async(request, runtime)

    def describe_channel_overall_data_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelOverallDataResponse:
        """
        @summary 调用DescribeChannelOverallData查询频道概览数据。
        
        @param request: DescribeChannelOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelOverallData',
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
            rtc_20180111_models.DescribeChannelOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_overall_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelOverallDataResponse:
        """
        @summary 调用DescribeChannelOverallData查询频道概览数据。
        
        @param request: DescribeChannelOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelOverallData',
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
            rtc_20180111_models.DescribeChannelOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_overall_data(
        self,
        request: rtc_20180111_models.DescribeChannelOverallDataRequest,
    ) -> rtc_20180111_models.DescribeChannelOverallDataResponse:
        """
        @summary 调用DescribeChannelOverallData查询频道概览数据。
        
        @param request: DescribeChannelOverallDataRequest
        @return: DescribeChannelOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_overall_data_with_options(request, runtime)

    async def describe_channel_overall_data_async(
        self,
        request: rtc_20180111_models.DescribeChannelOverallDataRequest,
    ) -> rtc_20180111_models.DescribeChannelOverallDataResponse:
        """
        @summary 调用DescribeChannelOverallData查询频道概览数据。
        
        @param request: DescribeChannelOverallDataRequest
        @return: DescribeChannelOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_overall_data_with_options_async(request, runtime)

    def describe_channel_participants_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        """
        @param request: DescribeChannelParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelParticipantsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
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
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_participants_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        """
        @param request: DescribeChannelParticipantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelParticipantsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
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
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_participants(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        """
        @param request: DescribeChannelParticipantsRequest
        @return: DescribeChannelParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_participants_with_options(request, runtime)

    async def describe_channel_participants_async(
        self,
        request: rtc_20180111_models.DescribeChannelParticipantsRequest,
    ) -> rtc_20180111_models.DescribeChannelParticipantsResponse:
        """
        @param request: DescribeChannelParticipantsRequest
        @return: DescribeChannelParticipantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_participants_with_options_async(request, runtime)

    def describe_channel_top_pub_user_list_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelTopPubUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelTopPubUserListResponse:
        """
        @summary 调用DescribeChannelTopPubUserList获取频道内发布端的用户列表（按用户在线时长降序）。
        
        @param request: DescribeChannelTopPubUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelTopPubUserListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTopPubUserList',
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
            rtc_20180111_models.DescribeChannelTopPubUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_top_pub_user_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelTopPubUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelTopPubUserListResponse:
        """
        @summary 调用DescribeChannelTopPubUserList获取频道内发布端的用户列表（按用户在线时长降序）。
        
        @param request: DescribeChannelTopPubUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelTopPubUserListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTopPubUserList',
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
            rtc_20180111_models.DescribeChannelTopPubUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_top_pub_user_list(
        self,
        request: rtc_20180111_models.DescribeChannelTopPubUserListRequest,
    ) -> rtc_20180111_models.DescribeChannelTopPubUserListResponse:
        """
        @summary 调用DescribeChannelTopPubUserList获取频道内发布端的用户列表（按用户在线时长降序）。
        
        @param request: DescribeChannelTopPubUserListRequest
        @return: DescribeChannelTopPubUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_top_pub_user_list_with_options(request, runtime)

    async def describe_channel_top_pub_user_list_async(
        self,
        request: rtc_20180111_models.DescribeChannelTopPubUserListRequest,
    ) -> rtc_20180111_models.DescribeChannelTopPubUserListResponse:
        """
        @summary 调用DescribeChannelTopPubUserList获取频道内发布端的用户列表（按用户在线时长降序）。
        
        @param request: DescribeChannelTopPubUserListRequest
        @return: DescribeChannelTopPubUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_top_pub_user_list_with_options_async(request, runtime)

    def describe_channel_user_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUserResponse:
        """
        @summary DescribeChannelUser
        
        @param request: DescribeChannelUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUser',
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
            rtc_20180111_models.DescribeChannelUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_user_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUserResponse:
        """
        @summary DescribeChannelUser
        
        @param request: DescribeChannelUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUser',
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
            rtc_20180111_models.DescribeChannelUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_user(
        self,
        request: rtc_20180111_models.DescribeChannelUserRequest,
    ) -> rtc_20180111_models.DescribeChannelUserResponse:
        """
        @summary DescribeChannelUser
        
        @param request: DescribeChannelUserRequest
        @return: DescribeChannelUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_user_with_options(request, runtime)

    async def describe_channel_user_async(
        self,
        request: rtc_20180111_models.DescribeChannelUserRequest,
    ) -> rtc_20180111_models.DescribeChannelUserResponse:
        """
        @summary DescribeChannelUser
        
        @param request: DescribeChannelUserRequest
        @return: DescribeChannelUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_user_with_options_async(request, runtime)

    def describe_channel_user_metrics_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelUserMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUserMetricsResponse:
        """
        @summary 调用DescribeChannelUserMetrics查询频道总览中的用户数据。
        
        @param request: DescribeChannelUserMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUserMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUserMetrics',
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
            rtc_20180111_models.DescribeChannelUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_user_metrics_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelUserMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUserMetricsResponse:
        """
        @summary 调用DescribeChannelUserMetrics查询频道总览中的用户数据。
        
        @param request: DescribeChannelUserMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUserMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUserMetrics',
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
            rtc_20180111_models.DescribeChannelUserMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_user_metrics(
        self,
        request: rtc_20180111_models.DescribeChannelUserMetricsRequest,
    ) -> rtc_20180111_models.DescribeChannelUserMetricsResponse:
        """
        @summary 调用DescribeChannelUserMetrics查询频道总览中的用户数据。
        
        @param request: DescribeChannelUserMetricsRequest
        @return: DescribeChannelUserMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_user_metrics_with_options(request, runtime)

    async def describe_channel_user_metrics_async(
        self,
        request: rtc_20180111_models.DescribeChannelUserMetricsRequest,
    ) -> rtc_20180111_models.DescribeChannelUserMetricsResponse:
        """
        @summary 调用DescribeChannelUserMetrics查询频道总览中的用户数据。
        
        @param request: DescribeChannelUserMetricsRequest
        @return: DescribeChannelUserMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_user_metrics_with_options_async(request, runtime)

    def describe_channel_users_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        """
        @param request: DescribeChannelUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
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
            rtc_20180111_models.DescribeChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channel_users_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        """
        @param request: DescribeChannelUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
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
            rtc_20180111_models.DescribeChannelUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channel_users(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        """
        @param request: DescribeChannelUsersRequest
        @return: DescribeChannelUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_users_with_options(request, runtime)

    async def describe_channel_users_async(
        self,
        request: rtc_20180111_models.DescribeChannelUsersRequest,
    ) -> rtc_20180111_models.DescribeChannelUsersResponse:
        """
        @param request: DescribeChannelUsersRequest
        @return: DescribeChannelUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channel_users_with_options_async(request, runtime)

    def describe_channels_with_options(
        self,
        request: rtc_20180111_models.DescribeChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelsResponse:
        """
        @summary 查询在线频道列表
        
        @param request: DescribeChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannels',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_channels_with_options_async(
        self,
        request: rtc_20180111_models.DescribeChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeChannelsResponse:
        """
        @summary 查询在线频道列表
        
        @param request: DescribeChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeChannelsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannels',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_channels(
        self,
        request: rtc_20180111_models.DescribeChannelsRequest,
    ) -> rtc_20180111_models.DescribeChannelsResponse:
        """
        @summary 查询在线频道列表
        
        @param request: DescribeChannelsRequest
        @return: DescribeChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_channels_with_options(request, runtime)

    async def describe_channels_async(
        self,
        request: rtc_20180111_models.DescribeChannelsRequest,
    ) -> rtc_20180111_models.DescribeChannelsResponse:
        """
        @summary 查询在线频道列表
        
        @param request: DescribeChannelsRequest
        @return: DescribeChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_channels_with_options_async(request, runtime)

    def describe_cloud_note_phrases_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudNotePhrasesResponse:
        """
        @summary 纪要热词列表
        
        @param tmp_req: DescribeCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudNotePhrases',
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
            rtc_20180111_models.DescribeCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_note_phrases_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudNotePhrasesResponse:
        """
        @summary 纪要热词列表
        
        @param tmp_req: DescribeCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudNotePhrases',
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
            rtc_20180111_models.DescribeCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_note_phrases(
        self,
        request: rtc_20180111_models.DescribeCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.DescribeCloudNotePhrasesResponse:
        """
        @summary 纪要热词列表
        
        @param request: DescribeCloudNotePhrasesRequest
        @return: DescribeCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_note_phrases_with_options(request, runtime)

    async def describe_cloud_note_phrases_async(
        self,
        request: rtc_20180111_models.DescribeCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.DescribeCloudNotePhrasesResponse:
        """
        @summary 纪要热词列表
        
        @param request: DescribeCloudNotePhrasesRequest
        @return: DescribeCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_note_phrases_with_options_async(request, runtime)

    def describe_cloud_notes_with_options(
        self,
        tmp_req: rtc_20180111_models.DescribeCloudNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudNotesResponse:
        """
        @summary 纪要列表
        
        @param tmp_req: DescribeCloudNotesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudNotesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeCloudNotesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudNotes',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeCloudNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_notes_with_options_async(
        self,
        tmp_req: rtc_20180111_models.DescribeCloudNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudNotesResponse:
        """
        @summary 纪要列表
        
        @param tmp_req: DescribeCloudNotesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudNotesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeCloudNotesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudNotes',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeCloudNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_notes(
        self,
        request: rtc_20180111_models.DescribeCloudNotesRequest,
    ) -> rtc_20180111_models.DescribeCloudNotesResponse:
        """
        @summary 纪要列表
        
        @param request: DescribeCloudNotesRequest
        @return: DescribeCloudNotesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_notes_with_options(request, runtime)

    async def describe_cloud_notes_async(
        self,
        request: rtc_20180111_models.DescribeCloudNotesRequest,
    ) -> rtc_20180111_models.DescribeCloudNotesResponse:
        """
        @summary 纪要列表
        
        @param request: DescribeCloudNotesRequest
        @return: DescribeCloudNotesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_notes_with_options_async(request, runtime)

    def describe_cloud_record_status_with_options(
        self,
        request: rtc_20180111_models.DescribeCloudRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudRecordStatusResponse:
        """
        @summary 查询录制任务状态
        
        @param request: DescribeCloudRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudRecordStatus',
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
            rtc_20180111_models.DescribeCloudRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_record_status_with_options_async(
        self,
        request: rtc_20180111_models.DescribeCloudRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeCloudRecordStatusResponse:
        """
        @summary 查询录制任务状态
        
        @param request: DescribeCloudRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudRecordStatus',
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
            rtc_20180111_models.DescribeCloudRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_record_status(
        self,
        request: rtc_20180111_models.DescribeCloudRecordStatusRequest,
    ) -> rtc_20180111_models.DescribeCloudRecordStatusResponse:
        """
        @summary 查询录制任务状态
        
        @param request: DescribeCloudRecordStatusRequest
        @return: DescribeCloudRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_record_status_with_options(request, runtime)

    async def describe_cloud_record_status_async(
        self,
        request: rtc_20180111_models.DescribeCloudRecordStatusRequest,
    ) -> rtc_20180111_models.DescribeCloudRecordStatusResponse:
        """
        @summary 查询录制任务状态
        
        @param request: DescribeCloudRecordStatusRequest
        @return: DescribeCloudRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_record_status_with_options_async(request, runtime)

    def describe_end_point_event_list_with_options(
        self,
        request: rtc_20180111_models.DescribeEndPointEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeEndPointEventListResponse:
        """
        @summary 调用DescribeEndPointEventList获取端对端用户事件列表。
        
        @param request: DescribeEndPointEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndPointEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointEventList',
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
            rtc_20180111_models.DescribeEndPointEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_end_point_event_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeEndPointEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeEndPointEventListResponse:
        """
        @summary 调用DescribeEndPointEventList获取端对端用户事件列表。
        
        @param request: DescribeEndPointEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndPointEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointEventList',
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
            rtc_20180111_models.DescribeEndPointEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_end_point_event_list(
        self,
        request: rtc_20180111_models.DescribeEndPointEventListRequest,
    ) -> rtc_20180111_models.DescribeEndPointEventListResponse:
        """
        @summary 调用DescribeEndPointEventList获取端对端用户事件列表。
        
        @param request: DescribeEndPointEventListRequest
        @return: DescribeEndPointEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_end_point_event_list_with_options(request, runtime)

    async def describe_end_point_event_list_async(
        self,
        request: rtc_20180111_models.DescribeEndPointEventListRequest,
    ) -> rtc_20180111_models.DescribeEndPointEventListResponse:
        """
        @summary 调用DescribeEndPointEventList获取端对端用户事件列表。
        
        @param request: DescribeEndPointEventListRequest
        @return: DescribeEndPointEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_end_point_event_list_with_options_async(request, runtime)

    def describe_end_point_metric_data_with_options(
        self,
        request: rtc_20180111_models.DescribeEndPointMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeEndPointMetricDataResponse:
        """
        @summary 调用DescribeEndPointMetricData获取端对端指标数据。
        
        @param request: DescribeEndPointMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndPointMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointMetricData',
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
            rtc_20180111_models.DescribeEndPointMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_end_point_metric_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeEndPointMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeEndPointMetricDataResponse:
        """
        @summary 调用DescribeEndPointMetricData获取端对端指标数据。
        
        @param request: DescribeEndPointMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndPointMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointMetricData',
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
            rtc_20180111_models.DescribeEndPointMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_end_point_metric_data(
        self,
        request: rtc_20180111_models.DescribeEndPointMetricDataRequest,
    ) -> rtc_20180111_models.DescribeEndPointMetricDataResponse:
        """
        @summary 调用DescribeEndPointMetricData获取端对端指标数据。
        
        @param request: DescribeEndPointMetricDataRequest
        @return: DescribeEndPointMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_end_point_metric_data_with_options(request, runtime)

    async def describe_end_point_metric_data_async(
        self,
        request: rtc_20180111_models.DescribeEndPointMetricDataRequest,
    ) -> rtc_20180111_models.DescribeEndPointMetricDataResponse:
        """
        @summary 调用DescribeEndPointMetricData获取端对端指标数据。
        
        @param request: DescribeEndPointMetricDataRequest
        @return: DescribeEndPointMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_end_point_metric_data_with_options_async(request, runtime)

    def describe_fault_diagnosis_factor_distribution_stat_with_options(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        """
        @summary 获取异常诊断影响因素分布
        
        @param request: DescribeFaultDiagnosisFactorDistributionStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisFactorDistributionStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisFactorDistributionStat',
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
            rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_factor_distribution_stat_with_options_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        """
        @summary 获取异常诊断影响因素分布
        
        @param request: DescribeFaultDiagnosisFactorDistributionStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisFactorDistributionStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisFactorDistributionStat',
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
            rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_factor_distribution_stat(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        """
        @summary 获取异常诊断影响因素分布
        
        @param request: DescribeFaultDiagnosisFactorDistributionStatRequest
        @return: DescribeFaultDiagnosisFactorDistributionStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_factor_distribution_stat_with_options(request, runtime)

    async def describe_fault_diagnosis_factor_distribution_stat_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        """
        @summary 获取异常诊断影响因素分布
        
        @param request: DescribeFaultDiagnosisFactorDistributionStatRequest
        @return: DescribeFaultDiagnosisFactorDistributionStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_fault_diagnosis_factor_distribution_stat_with_options_async(request, runtime)

    def describe_fault_diagnosis_overall_data_with_options(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse:
        """
        @summary 获取异常诊断总览数据
        
        @param request: DescribeFaultDiagnosisOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisOverallData',
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
            rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_overall_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse:
        """
        @summary 获取异常诊断总览数据
        
        @param request: DescribeFaultDiagnosisOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisOverallData',
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
            rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_overall_data(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse:
        """
        @summary 获取异常诊断总览数据
        
        @param request: DescribeFaultDiagnosisOverallDataRequest
        @return: DescribeFaultDiagnosisOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_overall_data_with_options(request, runtime)

    async def describe_fault_diagnosis_overall_data_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse:
        """
        @summary 获取异常诊断总览数据
        
        @param request: DescribeFaultDiagnosisOverallDataRequest
        @return: DescribeFaultDiagnosisOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_fault_diagnosis_overall_data_with_options_async(request, runtime)

    def describe_fault_diagnosis_user_detail_with_options(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse:
        """
        @summary 获取异常诊断用户详情
        
        @param request: DescribeFaultDiagnosisUserDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisUserDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserDetail',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_user_detail_with_options_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse:
        """
        @summary 获取异常诊断用户详情
        
        @param request: DescribeFaultDiagnosisUserDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisUserDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserDetail',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_user_detail(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse:
        """
        @summary 获取异常诊断用户详情
        
        @param request: DescribeFaultDiagnosisUserDetailRequest
        @return: DescribeFaultDiagnosisUserDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_user_detail_with_options(request, runtime)

    async def describe_fault_diagnosis_user_detail_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse:
        """
        @summary 获取异常诊断用户详情
        
        @param request: DescribeFaultDiagnosisUserDetailRequest
        @return: DescribeFaultDiagnosisUserDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_fault_diagnosis_user_detail_with_options_async(request, runtime)

    def describe_fault_diagnosis_user_list_with_options(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserListResponse:
        """
        @summary 获取异常诊断用户明细列表
        
        @param request: DescribeFaultDiagnosisUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisUserListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserList',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fault_diagnosis_user_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserListResponse:
        """
        @summary 获取异常诊断用户明细列表
        
        @param request: DescribeFaultDiagnosisUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaultDiagnosisUserListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserList',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fault_diagnosis_user_list(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserListRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserListResponse:
        """
        @summary 获取异常诊断用户明细列表
        
        @param request: DescribeFaultDiagnosisUserListRequest
        @return: DescribeFaultDiagnosisUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_user_list_with_options(request, runtime)

    async def describe_fault_diagnosis_user_list_async(
        self,
        request: rtc_20180111_models.DescribeFaultDiagnosisUserListRequest,
    ) -> rtc_20180111_models.DescribeFaultDiagnosisUserListResponse:
        """
        @summary 获取异常诊断用户明细列表
        
        @param request: DescribeFaultDiagnosisUserListRequest
        @return: DescribeFaultDiagnosisUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_fault_diagnosis_user_list_with_options_async(request, runtime)

    def describe_mpulayout_info_list_with_options(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        """
        @param request: DescribeMPULayoutInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMPULayoutInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
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
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mpulayout_info_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        """
        @param request: DescribeMPULayoutInfoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMPULayoutInfoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
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
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mpulayout_info_list(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        """
        @param request: DescribeMPULayoutInfoListRequest
        @return: DescribeMPULayoutInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_info_list_with_options(request, runtime)

    async def describe_mpulayout_info_list_async(
        self,
        request: rtc_20180111_models.DescribeMPULayoutInfoListRequest,
    ) -> rtc_20180111_models.DescribeMPULayoutInfoListResponse:
        """
        @param request: DescribeMPULayoutInfoListRequest
        @return: DescribeMPULayoutInfoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mpulayout_info_list_with_options_async(request, runtime)

    def describe_pub_user_list_by_sub_user_with_options(
        self,
        request: rtc_20180111_models.DescribePubUserListBySubUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribePubUserListBySubUserResponse:
        """
        @summary 调用DescribePubUserListBySubUser根据订阅端获取通信中发布端用户列表。
        
        @param request: DescribePubUserListBySubUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePubUserListBySubUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePubUserListBySubUser',
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
            rtc_20180111_models.DescribePubUserListBySubUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pub_user_list_by_sub_user_with_options_async(
        self,
        request: rtc_20180111_models.DescribePubUserListBySubUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribePubUserListBySubUserResponse:
        """
        @summary 调用DescribePubUserListBySubUser根据订阅端获取通信中发布端用户列表。
        
        @param request: DescribePubUserListBySubUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePubUserListBySubUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePubUserListBySubUser',
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
            rtc_20180111_models.DescribePubUserListBySubUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pub_user_list_by_sub_user(
        self,
        request: rtc_20180111_models.DescribePubUserListBySubUserRequest,
    ) -> rtc_20180111_models.DescribePubUserListBySubUserResponse:
        """
        @summary 调用DescribePubUserListBySubUser根据订阅端获取通信中发布端用户列表。
        
        @param request: DescribePubUserListBySubUserRequest
        @return: DescribePubUserListBySubUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pub_user_list_by_sub_user_with_options(request, runtime)

    async def describe_pub_user_list_by_sub_user_async(
        self,
        request: rtc_20180111_models.DescribePubUserListBySubUserRequest,
    ) -> rtc_20180111_models.DescribePubUserListBySubUserResponse:
        """
        @summary 调用DescribePubUserListBySubUser根据订阅端获取通信中发布端用户列表。
        
        @param request: DescribePubUserListBySubUserRequest
        @return: DescribePubUserListBySubUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pub_user_list_by_sub_user_with_options_async(request, runtime)

    def describe_qoe_metric_data_with_options(
        self,
        request: rtc_20180111_models.DescribeQoeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQoeMetricDataResponse:
        """
        @summary 调用DescribeQoeMetricData获取单次通信中用户的下行体验质量指标。
        
        @param request: DescribeQoeMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQoeMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoeMetricData',
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
            rtc_20180111_models.DescribeQoeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_qoe_metric_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeQoeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQoeMetricDataResponse:
        """
        @summary 调用DescribeQoeMetricData获取单次通信中用户的下行体验质量指标。
        
        @param request: DescribeQoeMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQoeMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoeMetricData',
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
            rtc_20180111_models.DescribeQoeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_qoe_metric_data(
        self,
        request: rtc_20180111_models.DescribeQoeMetricDataRequest,
    ) -> rtc_20180111_models.DescribeQoeMetricDataResponse:
        """
        @summary 调用DescribeQoeMetricData获取单次通信中用户的下行体验质量指标。
        
        @param request: DescribeQoeMetricDataRequest
        @return: DescribeQoeMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_qoe_metric_data_with_options(request, runtime)

    async def describe_qoe_metric_data_async(
        self,
        request: rtc_20180111_models.DescribeQoeMetricDataRequest,
    ) -> rtc_20180111_models.DescribeQoeMetricDataResponse:
        """
        @summary 调用DescribeQoeMetricData获取单次通信中用户的下行体验质量指标。
        
        @param request: DescribeQoeMetricDataRequest
        @return: DescribeQoeMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_qoe_metric_data_with_options_async(request, runtime)

    def describe_quality_area_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeQualityAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse:
        """
        @summary 获取质量统计区域分布统计数据
        
        @param request: DescribeQualityAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityAreaDistributionStatData',
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
            rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_area_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeQualityAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse:
        """
        @summary 获取质量统计区域分布统计数据
        
        @param request: DescribeQualityAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityAreaDistributionStatData',
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
            rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_area_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse:
        """
        @summary 获取质量统计区域分布统计数据
        
        @param request: DescribeQualityAreaDistributionStatDataRequest
        @return: DescribeQualityAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_area_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_area_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse:
        """
        @summary 获取质量统计区域分布统计数据
        
        @param request: DescribeQualityAreaDistributionStatDataRequest
        @return: DescribeQualityAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_quality_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeQualityDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityDistributionStatDataResponse:
        """
        @summary 获取质量统计分布数据
        
        @param request: DescribeQualityDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityDistributionStatData',
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
            rtc_20180111_models.DescribeQualityDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeQualityDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityDistributionStatDataResponse:
        """
        @summary 获取质量统计分布数据
        
        @param request: DescribeQualityDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityDistributionStatData',
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
            rtc_20180111_models.DescribeQualityDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeQualityDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityDistributionStatDataResponse:
        """
        @summary 获取质量统计分布数据
        
        @param request: DescribeQualityDistributionStatDataRequest
        @return: DescribeQualityDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeQualityDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityDistributionStatDataResponse:
        """
        @summary 获取质量统计分布数据
        
        @param request: DescribeQualityDistributionStatDataRequest
        @return: DescribeQualityDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_quality_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取质量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeQualityOsSdkVersionDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityOsSdkVersionDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取质量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeQualityOsSdkVersionDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityOsSdkVersionDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_os_sdk_version_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取质量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeQualityOsSdkVersionDistributionStatDataRequest
        @return: DescribeQualityOsSdkVersionDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    async def describe_quality_os_sdk_version_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取质量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeQualityOsSdkVersionDistributionStatDataRequest
        @return: DescribeQualityOsSdkVersionDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_quality_os_sdk_version_distribution_stat_data_with_options_async(request, runtime)

    def describe_quality_overall_data_with_options(
        self,
        request: rtc_20180111_models.DescribeQualityOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityOverallDataResponse:
        """
        @summary 获取质量统计概览数据
        
        @param request: DescribeQualityOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOverallData',
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
            rtc_20180111_models.DescribeQualityOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quality_overall_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeQualityOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeQualityOverallDataResponse:
        """
        @summary 获取质量统计概览数据
        
        @param request: DescribeQualityOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeQualityOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOverallData',
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
            rtc_20180111_models.DescribeQualityOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quality_overall_data(
        self,
        request: rtc_20180111_models.DescribeQualityOverallDataRequest,
    ) -> rtc_20180111_models.DescribeQualityOverallDataResponse:
        """
        @summary 获取质量统计概览数据
        
        @param request: DescribeQualityOverallDataRequest
        @return: DescribeQualityOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_overall_data_with_options(request, runtime)

    async def describe_quality_overall_data_async(
        self,
        request: rtc_20180111_models.DescribeQualityOverallDataRequest,
    ) -> rtc_20180111_models.DescribeQualityOverallDataResponse:
        """
        @summary 获取质量统计概览数据
        
        @param request: DescribeQualityOverallDataRequest
        @return: DescribeQualityOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_quality_overall_data_with_options_async(request, runtime)

    def describe_record_files_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        """
        @param request: DescribeRecordFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
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
            rtc_20180111_models.DescribeRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_files_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        """
        @param request: DescribeRecordFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
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
            rtc_20180111_models.DescribeRecordFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_files(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        """
        @param request: DescribeRecordFilesRequest
        @return: DescribeRecordFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_files_with_options(request, runtime)

    async def describe_record_files_async(
        self,
        request: rtc_20180111_models.DescribeRecordFilesRequest,
    ) -> rtc_20180111_models.DescribeRecordFilesResponse:
        """
        @param request: DescribeRecordFilesRequest
        @return: DescribeRecordFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_files_with_options_async(request, runtime)

    def describe_record_templates_with_options(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        """
        @param request: DescribeRecordTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
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
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_record_templates_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        """
        @param request: DescribeRecordTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
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
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_record_templates(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        """
        @param request: DescribeRecordTemplatesRequest
        @return: DescribeRecordTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_templates_with_options(request, runtime)

    async def describe_record_templates_async(
        self,
        request: rtc_20180111_models.DescribeRecordTemplatesRequest,
    ) -> rtc_20180111_models.DescribeRecordTemplatesResponse:
        """
        @param request: DescribeRecordTemplatesRequest
        @return: DescribeRecordTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_templates_with_options_async(request, runtime)

    def describe_rtc_channel_list_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        """
        @param request: DescribeRtcChannelListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcChannelListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelList',
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
            rtc_20180111_models.DescribeRtcChannelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_channel_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        """
        @param request: DescribeRtcChannelListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcChannelListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelList',
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
            rtc_20180111_models.DescribeRtcChannelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_channel_list(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        """
        @param request: DescribeRtcChannelListRequest
        @return: DescribeRtcChannelListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_list_with_options(request, runtime)

    async def describe_rtc_channel_list_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelListRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelListResponse:
        """
        @param request: DescribeRtcChannelListRequest
        @return: DescribeRtcChannelListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_list_with_options_async(request, runtime)

    def describe_rtc_channel_metric_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        """
        @param request: DescribeRtcChannelMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcChannelMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelMetric',
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
            rtc_20180111_models.DescribeRtcChannelMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_channel_metric_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        """
        @param request: DescribeRtcChannelMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcChannelMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelMetric',
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
            rtc_20180111_models.DescribeRtcChannelMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_channel_metric(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        """
        @param request: DescribeRtcChannelMetricRequest
        @return: DescribeRtcChannelMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_metric_with_options(request, runtime)

    async def describe_rtc_channel_metric_async(
        self,
        request: rtc_20180111_models.DescribeRtcChannelMetricRequest,
    ) -> rtc_20180111_models.DescribeRtcChannelMetricResponse:
        """
        @param request: DescribeRtcChannelMetricRequest
        @return: DescribeRtcChannelMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_channel_metric_with_options_async(request, runtime)

    def describe_rtc_duration_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        """
        @param request: DescribeRtcDurationDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcDurationDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcDurationData',
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
            rtc_20180111_models.DescribeRtcDurationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_duration_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        """
        @param request: DescribeRtcDurationDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcDurationDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcDurationData',
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
            rtc_20180111_models.DescribeRtcDurationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_duration_data(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        """
        @param request: DescribeRtcDurationDataRequest
        @return: DescribeRtcDurationDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_duration_data_with_options(request, runtime)

    async def describe_rtc_duration_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcDurationDataRequest,
    ) -> rtc_20180111_models.DescribeRtcDurationDataResponse:
        """
        @param request: DescribeRtcDurationDataRequest
        @return: DescribeRtcDurationDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_duration_data_with_options_async(request, runtime)

    def describe_rtc_peak_channel_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        """
        @param request: DescribeRtcPeakChannelCntDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcPeakChannelCntDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcPeakChannelCntData',
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
            rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_peak_channel_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        """
        @param request: DescribeRtcPeakChannelCntDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcPeakChannelCntDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcPeakChannelCntData',
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
            rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_peak_channel_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        """
        @param request: DescribeRtcPeakChannelCntDataRequest
        @return: DescribeRtcPeakChannelCntDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_peak_channel_cnt_data_with_options(request, runtime)

    async def describe_rtc_peak_channel_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcPeakChannelCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse:
        """
        @param request: DescribeRtcPeakChannelCntDataRequest
        @return: DescribeRtcPeakChannelCntDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_peak_channel_cnt_data_with_options_async(request, runtime)

    def describe_rtc_user_cnt_data_with_options(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        """
        @param request: DescribeRtcUserCntDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcUserCntDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcUserCntData',
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
            rtc_20180111_models.DescribeRtcUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtc_user_cnt_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        """
        @param request: DescribeRtcUserCntDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRtcUserCntDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcUserCntData',
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
            rtc_20180111_models.DescribeRtcUserCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtc_user_cnt_data(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        """
        @param request: DescribeRtcUserCntDataRequest
        @return: DescribeRtcUserCntDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_user_cnt_data_with_options(request, runtime)

    async def describe_rtc_user_cnt_data_async(
        self,
        request: rtc_20180111_models.DescribeRtcUserCntDataRequest,
    ) -> rtc_20180111_models.DescribeRtcUserCntDataResponse:
        """
        @param request: DescribeRtcUserCntDataRequest
        @return: DescribeRtcUserCntDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtc_user_cnt_data_with_options_async(request, runtime)

    def describe_streaming_out_status_with_options(
        self,
        request: rtc_20180111_models.DescribeStreamingOutStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeStreamingOutStatusResponse:
        """
        @summary 查询旁路推流状态
        
        @param request: DescribeStreamingOutStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamingOutStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamingOutStatus',
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
            rtc_20180111_models.DescribeStreamingOutStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streaming_out_status_with_options_async(
        self,
        request: rtc_20180111_models.DescribeStreamingOutStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeStreamingOutStatusResponse:
        """
        @summary 查询旁路推流状态
        
        @param request: DescribeStreamingOutStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamingOutStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamingOutStatus',
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
            rtc_20180111_models.DescribeStreamingOutStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streaming_out_status(
        self,
        request: rtc_20180111_models.DescribeStreamingOutStatusRequest,
    ) -> rtc_20180111_models.DescribeStreamingOutStatusResponse:
        """
        @summary 查询旁路推流状态
        
        @param request: DescribeStreamingOutStatusRequest
        @return: DescribeStreamingOutStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_streaming_out_status_with_options(request, runtime)

    async def describe_streaming_out_status_async(
        self,
        request: rtc_20180111_models.DescribeStreamingOutStatusRequest,
    ) -> rtc_20180111_models.DescribeStreamingOutStatusResponse:
        """
        @summary 查询旁路推流状态
        
        @param request: DescribeStreamingOutStatusRequest
        @return: DescribeStreamingOutStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_streaming_out_status_with_options_async(request, runtime)

    def describe_system_layout_list_with_options(
        self,
        request: rtc_20180111_models.DescribeSystemLayoutListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeSystemLayoutListResponse:
        """
        @summary 系统内置布局
        
        @param request: DescribeSystemLayoutListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemLayoutListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemLayoutList',
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
            rtc_20180111_models.DescribeSystemLayoutListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_layout_list_with_options_async(
        self,
        request: rtc_20180111_models.DescribeSystemLayoutListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeSystemLayoutListResponse:
        """
        @summary 系统内置布局
        
        @param request: DescribeSystemLayoutListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSystemLayoutListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemLayoutList',
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
            rtc_20180111_models.DescribeSystemLayoutListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_layout_list(
        self,
        request: rtc_20180111_models.DescribeSystemLayoutListRequest,
    ) -> rtc_20180111_models.DescribeSystemLayoutListResponse:
        """
        @summary 系统内置布局
        
        @param request: DescribeSystemLayoutListRequest
        @return: DescribeSystemLayoutListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_system_layout_list_with_options(request, runtime)

    async def describe_system_layout_list_async(
        self,
        request: rtc_20180111_models.DescribeSystemLayoutListRequest,
    ) -> rtc_20180111_models.DescribeSystemLayoutListResponse:
        """
        @summary 系统内置布局
        
        @param request: DescribeSystemLayoutListRequest
        @return: DescribeSystemLayoutListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_layout_list_with_options_async(request, runtime)

    def describe_usage_area_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeUsageAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse:
        """
        @summary 获取用量统计地域分布数据
        
        @param request: DescribeUsageAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageAreaDistributionStatData',
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
            rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_area_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUsageAreaDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse:
        """
        @summary 获取用量统计地域分布数据
        
        @param request: DescribeUsageAreaDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageAreaDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageAreaDistributionStatData',
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
            rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_area_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse:
        """
        @summary 获取用量统计地域分布数据
        
        @param request: DescribeUsageAreaDistributionStatDataRequest
        @return: DescribeUsageAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_area_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_area_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse:
        """
        @summary 获取用量统计地域分布数据
        
        @param request: DescribeUsageAreaDistributionStatDataRequest
        @return: DescribeUsageAreaDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_area_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeUsageDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageDistributionStatDataResponse:
        """
        @summary 获取用量统计分布数据
        
        @param request: DescribeUsageDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageDistributionStatData',
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
            rtc_20180111_models.DescribeUsageDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUsageDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageDistributionStatDataResponse:
        """
        @summary 获取用量统计分布数据
        
        @param request: DescribeUsageDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageDistributionStatData',
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
            rtc_20180111_models.DescribeUsageDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeUsageDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageDistributionStatDataResponse:
        """
        @summary 获取用量统计分布数据
        
        @param request: DescribeUsageDistributionStatDataRequest
        @return: DescribeUsageDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeUsageDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageDistributionStatDataResponse:
        """
        @summary 获取用量统计分布数据
        
        @param request: DescribeUsageDistributionStatDataRequest
        @return: DescribeUsageDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取用量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeUsageOsSdkVersionDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageOsSdkVersionDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取用量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeUsageOsSdkVersionDistributionStatDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageOsSdkVersionDistributionStatDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_os_sdk_version_distribution_stat_data(
        self,
        request: rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取用量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeUsageOsSdkVersionDistributionStatDataRequest
        @return: DescribeUsageOsSdkVersionDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    async def describe_usage_os_sdk_version_distribution_stat_data_async(
        self,
        request: rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        """
        @summary 获取用量统计各操作系统下SDK版本分布数据
        
        @param request: DescribeUsageOsSdkVersionDistributionStatDataRequest
        @return: DescribeUsageOsSdkVersionDistributionStatDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_os_sdk_version_distribution_stat_data_with_options_async(request, runtime)

    def describe_usage_overall_data_with_options(
        self,
        request: rtc_20180111_models.DescribeUsageOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageOverallDataResponse:
        """
        @summary 获取用量统计概览数据
        
        @param request: DescribeUsageOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOverallData',
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
            rtc_20180111_models.DescribeUsageOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_usage_overall_data_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUsageOverallDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUsageOverallDataResponse:
        """
        @summary 获取用量统计概览数据
        
        @param request: DescribeUsageOverallDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsageOverallDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOverallData',
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
            rtc_20180111_models.DescribeUsageOverallDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_usage_overall_data(
        self,
        request: rtc_20180111_models.DescribeUsageOverallDataRequest,
    ) -> rtc_20180111_models.DescribeUsageOverallDataResponse:
        """
        @summary 获取用量统计概览数据
        
        @param request: DescribeUsageOverallDataRequest
        @return: DescribeUsageOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_overall_data_with_options(request, runtime)

    async def describe_usage_overall_data_async(
        self,
        request: rtc_20180111_models.DescribeUsageOverallDataRequest,
    ) -> rtc_20180111_models.DescribeUsageOverallDataResponse:
        """
        @summary 获取用量统计概览数据
        
        @param request: DescribeUsageOverallDataRequest
        @return: DescribeUsageOverallDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_overall_data_with_options_async(request, runtime)

    def describe_user_info_in_channel_with_options(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        """
        @param request: DescribeUserInfoInChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserInfoInChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
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
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_info_in_channel_with_options_async(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        """
        @param request: DescribeUserInfoInChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserInfoInChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
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
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_info_in_channel(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        """
        @param request: DescribeUserInfoInChannelRequest
        @return: DescribeUserInfoInChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_in_channel_with_options(request, runtime)

    async def describe_user_info_in_channel_async(
        self,
        request: rtc_20180111_models.DescribeUserInfoInChannelRequest,
    ) -> rtc_20180111_models.DescribeUserInfoInChannelResponse:
        """
        @param request: DescribeUserInfoInChannelRequest
        @return: DescribeUserInfoInChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_info_in_channel_with_options_async(request, runtime)

    def disable_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        """
        @param request: DisableAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
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
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        """
        @param request: DisableAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
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
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        """
        @param request: DisableAutoLiveStreamRuleRequest
        @return: DisableAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_live_stream_rule_with_options(request, runtime)

    async def disable_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.DisableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.DisableAutoLiveStreamRuleResponse:
        """
        @param request: DisableAutoLiveStreamRuleRequest
        @return: DisableAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_live_stream_rule_with_options_async(request, runtime)

    def enable_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        """
        @param request: EnableAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
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
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        """
        @param request: EnableAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
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
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        """
        @param request: EnableAutoLiveStreamRuleRequest
        @return: EnableAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_live_stream_rule_with_options(request, runtime)

    async def enable_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.EnableAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.EnableAutoLiveStreamRuleResponse:
        """
        @param request: EnableAutoLiveStreamRuleRequest
        @return: EnableAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_live_stream_rule_with_options_async(request, runtime)

    def get_mputask_status_with_options(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        """
        @param request: GetMPUTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMPUTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
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
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mputask_status_with_options_async(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        """
        @param request: GetMPUTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMPUTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
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
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mputask_status(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        """
        @param request: GetMPUTaskStatusRequest
        @return: GetMPUTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mputask_status_with_options(request, runtime)

    async def get_mputask_status_async(
        self,
        request: rtc_20180111_models.GetMPUTaskStatusRequest,
    ) -> rtc_20180111_models.GetMPUTaskStatusResponse:
        """
        @param request: GetMPUTaskStatusRequest
        @return: GetMPUTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mputask_status_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppResponse:
        """
        @summary 修改App信息
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
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
            rtc_20180111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppResponse:
        """
        @summary 修改App信息
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
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
            rtc_20180111_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
    ) -> rtc_20180111_models.ModifyAppResponse:
        """
        @summary 修改App信息
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: rtc_20180111_models.ModifyAppRequest,
    ) -> rtc_20180111_models.ModifyAppResponse:
        """
        @summary 修改App信息
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_app_callback_status_with_options(
        self,
        request: rtc_20180111_models.ModifyAppCallbackStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppCallbackStatusResponse:
        """
        @summary 更新app回调事件开关
        
        @param request: ModifyAppCallbackStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppCallbackStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppCallbackStatus',
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
            rtc_20180111_models.ModifyAppCallbackStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_callback_status_with_options_async(
        self,
        request: rtc_20180111_models.ModifyAppCallbackStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppCallbackStatusResponse:
        """
        @summary 更新app回调事件开关
        
        @param request: ModifyAppCallbackStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppCallbackStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppCallbackStatus',
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
            rtc_20180111_models.ModifyAppCallbackStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_callback_status(
        self,
        request: rtc_20180111_models.ModifyAppCallbackStatusRequest,
    ) -> rtc_20180111_models.ModifyAppCallbackStatusResponse:
        """
        @summary 更新app回调事件开关
        
        @param request: ModifyAppCallbackStatusRequest
        @return: ModifyAppCallbackStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_callback_status_with_options(request, runtime)

    async def modify_app_callback_status_async(
        self,
        request: rtc_20180111_models.ModifyAppCallbackStatusRequest,
    ) -> rtc_20180111_models.ModifyAppCallbackStatusResponse:
        """
        @summary 更新app回调事件开关
        
        @param request: ModifyAppCallbackStatusRequest
        @return: ModifyAppCallbackStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_callback_status_with_options_async(request, runtime)

    def modify_app_layout_with_options(
        self,
        tmp_req: rtc_20180111_models.ModifyAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppLayoutResponse:
        """
        @summary 修改app自定义布局
        
        @param tmp_req: ModifyAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppLayout',
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
            rtc_20180111_models.ModifyAppLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_layout_with_options_async(
        self,
        tmp_req: rtc_20180111_models.ModifyAppLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppLayoutResponse:
        """
        @summary 修改app自定义布局
        
        @param tmp_req: ModifyAppLayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppLayoutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppLayoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout):
            request.layout_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout, 'Layout', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.layout_shrink):
            query['Layout'] = request.layout_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppLayout',
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
            rtc_20180111_models.ModifyAppLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_layout(
        self,
        request: rtc_20180111_models.ModifyAppLayoutRequest,
    ) -> rtc_20180111_models.ModifyAppLayoutResponse:
        """
        @summary 修改app自定义布局
        
        @param request: ModifyAppLayoutRequest
        @return: ModifyAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_layout_with_options(request, runtime)

    async def modify_app_layout_async(
        self,
        request: rtc_20180111_models.ModifyAppLayoutRequest,
    ) -> rtc_20180111_models.ModifyAppLayoutResponse:
        """
        @summary 修改app自定义布局
        
        @param request: ModifyAppLayoutRequest
        @return: ModifyAppLayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_layout_with_options_async(request, runtime)

    def modify_app_live_stream_status_with_options(
        self,
        request: rtc_20180111_models.ModifyAppLiveStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppLiveStreamStatusResponse:
        """
        @summary 修改应用旁路开关
        
        @param request: ModifyAppLiveStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppLiveStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppLiveStreamStatus',
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
            rtc_20180111_models.ModifyAppLiveStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_live_stream_status_with_options_async(
        self,
        request: rtc_20180111_models.ModifyAppLiveStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppLiveStreamStatusResponse:
        """
        @summary 修改应用旁路开关
        
        @param request: ModifyAppLiveStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppLiveStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppLiveStreamStatus',
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
            rtc_20180111_models.ModifyAppLiveStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_live_stream_status(
        self,
        request: rtc_20180111_models.ModifyAppLiveStreamStatusRequest,
    ) -> rtc_20180111_models.ModifyAppLiveStreamStatusResponse:
        """
        @summary 修改应用旁路开关
        
        @param request: ModifyAppLiveStreamStatusRequest
        @return: ModifyAppLiveStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_live_stream_status_with_options(request, runtime)

    async def modify_app_live_stream_status_async(
        self,
        request: rtc_20180111_models.ModifyAppLiveStreamStatusRequest,
    ) -> rtc_20180111_models.ModifyAppLiveStreamStatusResponse:
        """
        @summary 修改应用旁路开关
        
        @param request: ModifyAppLiveStreamStatusRequest
        @return: ModifyAppLiveStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_live_stream_status_with_options_async(request, runtime)

    def modify_app_record_status_with_options(
        self,
        request: rtc_20180111_models.ModifyAppRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppRecordStatusResponse:
        """
        @summary 修改应用录制开关
        
        @param request: ModifyAppRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppRecordStatus',
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
            rtc_20180111_models.ModifyAppRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_record_status_with_options_async(
        self,
        request: rtc_20180111_models.ModifyAppRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppRecordStatusResponse:
        """
        @summary 修改应用录制开关
        
        @param request: ModifyAppRecordStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppRecordStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppRecordStatus',
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
            rtc_20180111_models.ModifyAppRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_record_status(
        self,
        request: rtc_20180111_models.ModifyAppRecordStatusRequest,
    ) -> rtc_20180111_models.ModifyAppRecordStatusResponse:
        """
        @summary 修改应用录制开关
        
        @param request: ModifyAppRecordStatusRequest
        @return: ModifyAppRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_record_status_with_options(request, runtime)

    async def modify_app_record_status_async(
        self,
        request: rtc_20180111_models.ModifyAppRecordStatusRequest,
    ) -> rtc_20180111_models.ModifyAppRecordStatusResponse:
        """
        @summary 修改应用录制开关
        
        @param request: ModifyAppRecordStatusRequest
        @return: ModifyAppRecordStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_record_status_with_options_async(request, runtime)

    def modify_app_record_template_with_options(
        self,
        tmp_req: rtc_20180111_models.ModifyAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppRecordTemplateResponse:
        """
        @summary 修改应用录制模版
        
        @param tmp_req: ModifyAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_template):
            request.record_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppRecordTemplate',
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
            rtc_20180111_models.ModifyAppRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_record_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.ModifyAppRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppRecordTemplateResponse:
        """
        @summary 修改应用录制模版
        
        @param tmp_req: ModifyAppRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppRecordTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_template):
            request.record_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_template, 'RecordTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.record_template_shrink):
            query['RecordTemplate'] = request.record_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppRecordTemplate',
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
            rtc_20180111_models.ModifyAppRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_record_template(
        self,
        request: rtc_20180111_models.ModifyAppRecordTemplateRequest,
    ) -> rtc_20180111_models.ModifyAppRecordTemplateResponse:
        """
        @summary 修改应用录制模版
        
        @param request: ModifyAppRecordTemplateRequest
        @return: ModifyAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_record_template_with_options(request, runtime)

    async def modify_app_record_template_async(
        self,
        request: rtc_20180111_models.ModifyAppRecordTemplateRequest,
    ) -> rtc_20180111_models.ModifyAppRecordTemplateResponse:
        """
        @summary 修改应用录制模版
        
        @param request: ModifyAppRecordTemplateRequest
        @return: ModifyAppRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_record_template_with_options_async(request, runtime)

    def modify_app_streaming_out_template_with_options(
        self,
        tmp_req: rtc_20180111_models.ModifyAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppStreamingOutTemplateResponse:
        """
        @summary 更新应用推流模版
        
        @param tmp_req: ModifyAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppStreamingOutTemplate',
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
            rtc_20180111_models.ModifyAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_streaming_out_template_with_options_async(
        self,
        tmp_req: rtc_20180111_models.ModifyAppStreamingOutTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyAppStreamingOutTemplateResponse:
        """
        @summary 更新应用推流模版
        
        @param tmp_req: ModifyAppStreamingOutTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppStreamingOutTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppStreamingOutTemplate',
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
            rtc_20180111_models.ModifyAppStreamingOutTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_streaming_out_template(
        self,
        request: rtc_20180111_models.ModifyAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.ModifyAppStreamingOutTemplateResponse:
        """
        @summary 更新应用推流模版
        
        @param request: ModifyAppStreamingOutTemplateRequest
        @return: ModifyAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_streaming_out_template_with_options(request, runtime)

    async def modify_app_streaming_out_template_async(
        self,
        request: rtc_20180111_models.ModifyAppStreamingOutTemplateRequest,
    ) -> rtc_20180111_models.ModifyAppStreamingOutTemplateResponse:
        """
        @summary 更新应用推流模版
        
        @param request: ModifyAppStreamingOutTemplateRequest
        @return: ModifyAppStreamingOutTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_streaming_out_template_with_options_async(request, runtime)

    def modify_callback_meta_with_options(
        self,
        tmp_req: rtc_20180111_models.ModifyCallbackMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyCallbackMetaResponse:
        """
        @summary 更新app回调
        
        @param tmp_req: ModifyCallbackMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCallbackMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyCallbackMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCallbackMeta',
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
            rtc_20180111_models.ModifyCallbackMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_callback_meta_with_options_async(
        self,
        tmp_req: rtc_20180111_models.ModifyCallbackMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyCallbackMetaResponse:
        """
        @summary 更新app回调
        
        @param tmp_req: ModifyCallbackMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCallbackMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyCallbackMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCallbackMeta',
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
            rtc_20180111_models.ModifyCallbackMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_callback_meta(
        self,
        request: rtc_20180111_models.ModifyCallbackMetaRequest,
    ) -> rtc_20180111_models.ModifyCallbackMetaResponse:
        """
        @summary 更新app回调
        
        @param request: ModifyCallbackMetaRequest
        @return: ModifyCallbackMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_callback_meta_with_options(request, runtime)

    async def modify_callback_meta_async(
        self,
        request: rtc_20180111_models.ModifyCallbackMetaRequest,
    ) -> rtc_20180111_models.ModifyCallbackMetaResponse:
        """
        @summary 更新app回调
        
        @param request: ModifyCallbackMetaRequest
        @return: ModifyCallbackMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_callback_meta_with_options_async(request, runtime)

    def modify_cloud_note_phrases_with_options(
        self,
        tmp_req: rtc_20180111_models.ModifyCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyCloudNotePhrasesResponse:
        """
        @summary 更新纪要热词表
        
        @param tmp_req: ModifyCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudNotePhrases',
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
            rtc_20180111_models.ModifyCloudNotePhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_note_phrases_with_options_async(
        self,
        tmp_req: rtc_20180111_models.ModifyCloudNotePhrasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyCloudNotePhrasesResponse:
        """
        @summary 更新纪要热词表
        
        @param tmp_req: ModifyCloudNotePhrasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCloudNotePhrasesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyCloudNotePhrasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phrase):
            request.phrase_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phrase, 'Phrase', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.phrase_shrink):
            query['Phrase'] = request.phrase_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudNotePhrases',
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
            rtc_20180111_models.ModifyCloudNotePhrasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_note_phrases(
        self,
        request: rtc_20180111_models.ModifyCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.ModifyCloudNotePhrasesResponse:
        """
        @summary 更新纪要热词表
        
        @param request: ModifyCloudNotePhrasesRequest
        @return: ModifyCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_note_phrases_with_options(request, runtime)

    async def modify_cloud_note_phrases_async(
        self,
        request: rtc_20180111_models.ModifyCloudNotePhrasesRequest,
    ) -> rtc_20180111_models.ModifyCloudNotePhrasesResponse:
        """
        @summary 更新纪要热词表
        
        @param request: ModifyCloudNotePhrasesRequest
        @return: ModifyCloudNotePhrasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cloud_note_phrases_with_options_async(request, runtime)

    def modify_mpulayout_with_options(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        """
        @param request: ModifyMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
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
            rtc_20180111_models.ModifyMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mpulayout_with_options_async(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        """
        @param request: ModifyMPULayoutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMPULayoutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
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
            rtc_20180111_models.ModifyMPULayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mpulayout(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        """
        @param request: ModifyMPULayoutRequest
        @return: ModifyMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_mpulayout_with_options(request, runtime)

    async def modify_mpulayout_async(
        self,
        request: rtc_20180111_models.ModifyMPULayoutRequest,
    ) -> rtc_20180111_models.ModifyMPULayoutResponse:
        """
        @param request: ModifyMPULayoutRequest
        @return: ModifyMPULayoutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_mpulayout_with_options_async(request, runtime)

    def remove_terminals_with_options(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        """
        @param request: RemoveTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTerminalsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.terminal_ids):
            query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
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
            rtc_20180111_models.RemoveTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_terminals_with_options_async(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        """
        @param request: RemoveTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTerminalsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.terminal_ids):
            query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
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
            rtc_20180111_models.RemoveTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_terminals(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        """
        @param request: RemoveTerminalsRequest
        @return: RemoveTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_terminals_with_options(request, runtime)

    async def remove_terminals_async(
        self,
        request: rtc_20180111_models.RemoveTerminalsRequest,
    ) -> rtc_20180111_models.RemoveTerminalsResponse:
        """
        @param request: RemoveTerminalsRequest
        @return: RemoveTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_terminals_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: rtc_20180111_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveUsersResponse:
        """
        @summary RemoveUsers
        
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
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
            rtc_20180111_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: rtc_20180111_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.RemoveUsersResponse:
        """
        @summary RemoveUsers
        
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
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
            rtc_20180111_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: rtc_20180111_models.RemoveUsersRequest,
    ) -> rtc_20180111_models.RemoveUsersResponse:
        """
        @summary RemoveUsers
        
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: rtc_20180111_models.RemoveUsersRequest,
    ) -> rtc_20180111_models.RemoveUsersResponse:
        """
        @summary RemoveUsers
        
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def start_category_callback_with_options(
        self,
        tmp_req: rtc_20180111_models.StartCategoryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCategoryCallbackResponse:
        """
        @summary 开启某个事件回调
        
        @param tmp_req: StartCategoryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCategoryCallbackResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCategoryCallbackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCategoryCallback',
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
            rtc_20180111_models.StartCategoryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_category_callback_with_options_async(
        self,
        tmp_req: rtc_20180111_models.StartCategoryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCategoryCallbackResponse:
        """
        @summary 开启某个事件回调
        
        @param tmp_req: StartCategoryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCategoryCallbackResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCategoryCallbackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCategoryCallback',
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
            rtc_20180111_models.StartCategoryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_category_callback(
        self,
        request: rtc_20180111_models.StartCategoryCallbackRequest,
    ) -> rtc_20180111_models.StartCategoryCallbackResponse:
        """
        @summary 开启某个事件回调
        
        @param request: StartCategoryCallbackRequest
        @return: StartCategoryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_category_callback_with_options(request, runtime)

    async def start_category_callback_async(
        self,
        request: rtc_20180111_models.StartCategoryCallbackRequest,
    ) -> rtc_20180111_models.StartCategoryCallbackResponse:
        """
        @summary 开启某个事件回调
        
        @param request: StartCategoryCallbackRequest
        @return: StartCategoryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_category_callback_with_options_async(request, runtime)

    def start_cloud_note_with_options(
        self,
        tmp_req: rtc_20180111_models.StartCloudNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCloudNoteResponse:
        """
        @summary 开启智能纪要
        
        @param tmp_req: StartCloudNoteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCloudNoteResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCloudNoteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_chapters):
            request.auto_chapters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_chapters, 'AutoChapters', 'json')
        if not UtilClient.is_unset(tmp_req.custom_prompt):
            request.custom_prompt_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_prompt, 'CustomPrompt', 'json')
        if not UtilClient.is_unset(tmp_req.meeting_assistance):
            request.meeting_assistance_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.meeting_assistance, 'MeetingAssistance', 'json')
        if not UtilClient.is_unset(tmp_req.realtime_subtitle):
            request.realtime_subtitle_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.realtime_subtitle, 'RealtimeSubtitle', 'json')
        if not UtilClient.is_unset(tmp_req.service_inspection):
            request.service_inspection_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_inspection, 'ServiceInspection', 'json')
        if not UtilClient.is_unset(tmp_req.summarization):
            request.summarization_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not UtilClient.is_unset(tmp_req.text_polish):
            request.text_polish_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_polish, 'TextPolish', 'json')
        if not UtilClient.is_unset(tmp_req.transcription):
            request.transcription_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcription, 'Transcription', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_chapters_shrink):
            query['AutoChapters'] = request.auto_chapters_shrink
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.custom_prompt_shrink):
            query['CustomPrompt'] = request.custom_prompt_shrink
        if not UtilClient.is_unset(request.language_hints):
            query['LanguageHints'] = request.language_hints
        if not UtilClient.is_unset(request.meeting_assistance_shrink):
            query['MeetingAssistance'] = request.meeting_assistance_shrink
        if not UtilClient.is_unset(request.realtime_subtitle_shrink):
            query['RealtimeSubtitle'] = request.realtime_subtitle_shrink
        if not UtilClient.is_unset(request.service_inspection_shrink):
            query['ServiceInspection'] = request.service_inspection_shrink
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not UtilClient.is_unset(request.summarization_shrink):
            query['Summarization'] = request.summarization_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.text_polish_shrink):
            query['TextPolish'] = request.text_polish_shrink
        if not UtilClient.is_unset(request.transcription_shrink):
            query['Transcription'] = request.transcription_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCloudNote',
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
            rtc_20180111_models.StartCloudNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_note_with_options_async(
        self,
        tmp_req: rtc_20180111_models.StartCloudNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCloudNoteResponse:
        """
        @summary 开启智能纪要
        
        @param tmp_req: StartCloudNoteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCloudNoteResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCloudNoteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_chapters):
            request.auto_chapters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_chapters, 'AutoChapters', 'json')
        if not UtilClient.is_unset(tmp_req.custom_prompt):
            request.custom_prompt_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_prompt, 'CustomPrompt', 'json')
        if not UtilClient.is_unset(tmp_req.meeting_assistance):
            request.meeting_assistance_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.meeting_assistance, 'MeetingAssistance', 'json')
        if not UtilClient.is_unset(tmp_req.realtime_subtitle):
            request.realtime_subtitle_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.realtime_subtitle, 'RealtimeSubtitle', 'json')
        if not UtilClient.is_unset(tmp_req.service_inspection):
            request.service_inspection_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_inspection, 'ServiceInspection', 'json')
        if not UtilClient.is_unset(tmp_req.summarization):
            request.summarization_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not UtilClient.is_unset(tmp_req.text_polish):
            request.text_polish_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_polish, 'TextPolish', 'json')
        if not UtilClient.is_unset(tmp_req.transcription):
            request.transcription_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcription, 'Transcription', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_chapters_shrink):
            query['AutoChapters'] = request.auto_chapters_shrink
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.custom_prompt_shrink):
            query['CustomPrompt'] = request.custom_prompt_shrink
        if not UtilClient.is_unset(request.language_hints):
            query['LanguageHints'] = request.language_hints
        if not UtilClient.is_unset(request.meeting_assistance_shrink):
            query['MeetingAssistance'] = request.meeting_assistance_shrink
        if not UtilClient.is_unset(request.realtime_subtitle_shrink):
            query['RealtimeSubtitle'] = request.realtime_subtitle_shrink
        if not UtilClient.is_unset(request.service_inspection_shrink):
            query['ServiceInspection'] = request.service_inspection_shrink
        if not UtilClient.is_unset(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not UtilClient.is_unset(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not UtilClient.is_unset(request.summarization_shrink):
            query['Summarization'] = request.summarization_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.text_polish_shrink):
            query['TextPolish'] = request.text_polish_shrink
        if not UtilClient.is_unset(request.transcription_shrink):
            query['Transcription'] = request.transcription_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCloudNote',
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
            rtc_20180111_models.StartCloudNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_note(
        self,
        request: rtc_20180111_models.StartCloudNoteRequest,
    ) -> rtc_20180111_models.StartCloudNoteResponse:
        """
        @summary 开启智能纪要
        
        @param request: StartCloudNoteRequest
        @return: StartCloudNoteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_cloud_note_with_options(request, runtime)

    async def start_cloud_note_async(
        self,
        request: rtc_20180111_models.StartCloudNoteRequest,
    ) -> rtc_20180111_models.StartCloudNoteResponse:
        """
        @summary 开启智能纪要
        
        @param request: StartCloudNoteRequest
        @return: StartCloudNoteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_cloud_note_with_options_async(request, runtime)

    def start_cloud_record_with_options(
        self,
        tmp_req: rtc_20180111_models.StartCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCloudRecordResponse:
        """
        @summary StartCloudRecord
        
        @param tmp_req: StartCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCloudRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not UtilClient.is_unset(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not UtilClient.is_unset(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not UtilClient.is_unset(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCloudRecord',
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
            rtc_20180111_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_record_with_options_async(
        self,
        tmp_req: rtc_20180111_models.StartCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartCloudRecordResponse:
        """
        @summary StartCloudRecord
        
        @param tmp_req: StartCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartCloudRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not UtilClient.is_unset(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not UtilClient.is_unset(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not UtilClient.is_unset(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCloudRecord',
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
            rtc_20180111_models.StartCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_record(
        self,
        request: rtc_20180111_models.StartCloudRecordRequest,
    ) -> rtc_20180111_models.StartCloudRecordResponse:
        """
        @summary StartCloudRecord
        
        @param request: StartCloudRecordRequest
        @return: StartCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_cloud_record_with_options(request, runtime)

    async def start_cloud_record_async(
        self,
        request: rtc_20180111_models.StartCloudRecordRequest,
    ) -> rtc_20180111_models.StartCloudRecordResponse:
        """
        @summary StartCloudRecord
        
        @param request: StartCloudRecordRequest
        @return: StartCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_cloud_record_with_options_async(request, runtime)

    def start_mputask_with_options(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        """
        @param request: StartMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payload_type):
            query['PayloadType'] = request.payload_type
        if not UtilClient.is_unset(request.report_vad):
            query['ReportVad'] = request.report_vad
        if not UtilClient.is_unset(request.rtp_ext_info):
            query['RtpExtInfo'] = request.rtp_ext_info
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.time_stamp_ref):
            query['TimeStampRef'] = request.time_stamp_ref
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.vad_interval):
            query['VadInterval'] = request.vad_interval
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.enhanced_param):
            body_flat['EnhancedParam'] = request.enhanced_param
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @param request: StartMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payload_type):
            query['PayloadType'] = request.payload_type
        if not UtilClient.is_unset(request.report_vad):
            query['ReportVad'] = request.report_vad
        if not UtilClient.is_unset(request.rtp_ext_info):
            query['RtpExtInfo'] = request.rtp_ext_info
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.time_stamp_ref):
            query['TimeStampRef'] = request.time_stamp_ref
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.vad_interval):
            query['VadInterval'] = request.vad_interval
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.enhanced_param):
            body_flat['EnhancedParam'] = request.enhanced_param
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @param request: StartMPUTaskRequest
        @return: StartMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_mputask_with_options(request, runtime)

    async def start_mputask_async(
        self,
        request: rtc_20180111_models.StartMPUTaskRequest,
    ) -> rtc_20180111_models.StartMPUTaskResponse:
        """
        @param request: StartMPUTaskRequest
        @return: StartMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_mputask_with_options_async(request, runtime)

    def start_record_task_with_options(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        """
        @param request: StartRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
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
            rtc_20180111_models.StartRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        """
        @param request: StartRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
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
            rtc_20180111_models.StartRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_record_task(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        """
        @param request: StartRecordTaskRequest
        @return: StartRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_record_task_with_options(request, runtime)

    async def start_record_task_async(
        self,
        request: rtc_20180111_models.StartRecordTaskRequest,
    ) -> rtc_20180111_models.StartRecordTaskResponse:
        """
        @param request: StartRecordTaskRequest
        @return: StartRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_record_task_with_options_async(request, runtime)

    def start_streaming_out_with_options(
        self,
        tmp_req: rtc_20180111_models.StartStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartStreamingOutResponse:
        """
        @summary StartStreamingOut
        
        @param tmp_req: StartStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartStreamingOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartStreamingOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not UtilClient.is_unset(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not UtilClient.is_unset(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not UtilClient.is_unset(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not UtilClient.is_unset(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStreamingOut',
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
            rtc_20180111_models.StartStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_streaming_out_with_options_async(
        self,
        tmp_req: rtc_20180111_models.StartStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StartStreamingOutResponse:
        """
        @summary StartStreamingOut
        
        @param tmp_req: StartStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartStreamingOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StartStreamingOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.reserve_pane_for_no_camera_user):
            query['ReservePaneForNoCameraUser'] = request.reserve_pane_for_no_camera_user
        if not UtilClient.is_unset(request.show_default_background_on_mute):
            query['ShowDefaultBackgroundOnMute'] = request.show_default_background_on_mute
        if not UtilClient.is_unset(request.start_without_channel):
            query['StartWithoutChannel'] = request.start_without_channel
        if not UtilClient.is_unset(request.start_without_channel_wait_time):
            query['StartWithoutChannelWaitTime'] = request.start_without_channel_wait_time
        if not UtilClient.is_unset(request.sub_high_resolution_stream):
            query['SubHighResolutionStream'] = request.sub_high_resolution_stream
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStreamingOut',
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
            rtc_20180111_models.StartStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_streaming_out(
        self,
        request: rtc_20180111_models.StartStreamingOutRequest,
    ) -> rtc_20180111_models.StartStreamingOutResponse:
        """
        @summary StartStreamingOut
        
        @param request: StartStreamingOutRequest
        @return: StartStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_streaming_out_with_options(request, runtime)

    async def start_streaming_out_async(
        self,
        request: rtc_20180111_models.StartStreamingOutRequest,
    ) -> rtc_20180111_models.StartStreamingOutResponse:
        """
        @summary StartStreamingOut
        
        @param request: StartStreamingOutRequest
        @return: StartStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_streaming_out_with_options_async(request, runtime)

    def stop_category_callback_with_options(
        self,
        tmp_req: rtc_20180111_models.StopCategoryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCategoryCallbackResponse:
        """
        @summary 关闭某个事件回调
        
        @param tmp_req: StopCategoryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCategoryCallbackResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StopCategoryCallbackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCategoryCallback',
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
            rtc_20180111_models.StopCategoryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_category_callback_with_options_async(
        self,
        tmp_req: rtc_20180111_models.StopCategoryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCategoryCallbackResponse:
        """
        @summary 关闭某个事件回调
        
        @param tmp_req: StopCategoryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCategoryCallbackResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.StopCategoryCallbackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.callback):
            request.callback_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.callback, 'Callback', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_shrink):
            query['Callback'] = request.callback_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCategoryCallback',
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
            rtc_20180111_models.StopCategoryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_category_callback(
        self,
        request: rtc_20180111_models.StopCategoryCallbackRequest,
    ) -> rtc_20180111_models.StopCategoryCallbackResponse:
        """
        @summary 关闭某个事件回调
        
        @param request: StopCategoryCallbackRequest
        @return: StopCategoryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_category_callback_with_options(request, runtime)

    async def stop_category_callback_async(
        self,
        request: rtc_20180111_models.StopCategoryCallbackRequest,
    ) -> rtc_20180111_models.StopCategoryCallbackResponse:
        """
        @summary 关闭某个事件回调
        
        @param request: StopCategoryCallbackRequest
        @return: StopCategoryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_category_callback_with_options_async(request, runtime)

    def stop_channel_with_options(
        self,
        request: rtc_20180111_models.StopChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopChannelResponse:
        """
        @summary 删除频道
        
        @param request: StopChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopChannel',
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
            rtc_20180111_models.StopChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_channel_with_options_async(
        self,
        request: rtc_20180111_models.StopChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopChannelResponse:
        """
        @summary 删除频道
        
        @param request: StopChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopChannel',
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
            rtc_20180111_models.StopChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_channel(
        self,
        request: rtc_20180111_models.StopChannelRequest,
    ) -> rtc_20180111_models.StopChannelResponse:
        """
        @summary 删除频道
        
        @param request: StopChannelRequest
        @return: StopChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_channel_with_options(request, runtime)

    async def stop_channel_async(
        self,
        request: rtc_20180111_models.StopChannelRequest,
    ) -> rtc_20180111_models.StopChannelResponse:
        """
        @summary 删除频道
        
        @param request: StopChannelRequest
        @return: StopChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_channel_with_options_async(request, runtime)

    def stop_cloud_note_with_options(
        self,
        request: rtc_20180111_models.StopCloudNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCloudNoteResponse:
        """
        @summary 停止智能纪要
        
        @param request: StopCloudNoteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudNoteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudNote',
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
            rtc_20180111_models.StopCloudNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_note_with_options_async(
        self,
        request: rtc_20180111_models.StopCloudNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCloudNoteResponse:
        """
        @summary 停止智能纪要
        
        @param request: StopCloudNoteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudNoteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudNote',
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
            rtc_20180111_models.StopCloudNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_note(
        self,
        request: rtc_20180111_models.StopCloudNoteRequest,
    ) -> rtc_20180111_models.StopCloudNoteResponse:
        """
        @summary 停止智能纪要
        
        @param request: StopCloudNoteRequest
        @return: StopCloudNoteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_note_with_options(request, runtime)

    async def stop_cloud_note_async(
        self,
        request: rtc_20180111_models.StopCloudNoteRequest,
    ) -> rtc_20180111_models.StopCloudNoteResponse:
        """
        @summary 停止智能纪要
        
        @param request: StopCloudNoteRequest
        @return: StopCloudNoteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_cloud_note_with_options_async(request, runtime)

    def stop_cloud_record_with_options(
        self,
        request: rtc_20180111_models.StopCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCloudRecordResponse:
        """
        @summary StopCloudRecord
        
        @param request: StopCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudRecord',
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
            rtc_20180111_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_record_with_options_async(
        self,
        request: rtc_20180111_models.StopCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopCloudRecordResponse:
        """
        @summary StopCloudRecord
        
        @param request: StopCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopCloudRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudRecord',
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
            rtc_20180111_models.StopCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_record(
        self,
        request: rtc_20180111_models.StopCloudRecordRequest,
    ) -> rtc_20180111_models.StopCloudRecordResponse:
        """
        @summary StopCloudRecord
        
        @param request: StopCloudRecordRequest
        @return: StopCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_record_with_options(request, runtime)

    async def stop_cloud_record_async(
        self,
        request: rtc_20180111_models.StopCloudRecordRequest,
    ) -> rtc_20180111_models.StopCloudRecordResponse:
        """
        @summary StopCloudRecord
        
        @param request: StopCloudRecordRequest
        @return: StopCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_cloud_record_with_options_async(request, runtime)

    def stop_mputask_with_options(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        """
        @param request: StopMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
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
            rtc_20180111_models.StopMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_mputask_with_options_async(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        """
        @param request: StopMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
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
            rtc_20180111_models.StopMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_mputask(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        """
        @param request: StopMPUTaskRequest
        @return: StopMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_mputask_with_options(request, runtime)

    async def stop_mputask_async(
        self,
        request: rtc_20180111_models.StopMPUTaskRequest,
    ) -> rtc_20180111_models.StopMPUTaskResponse:
        """
        @param request: StopMPUTaskRequest
        @return: StopMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_mputask_with_options_async(request, runtime)

    def stop_record_task_with_options(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        """
        @param request: StopRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
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
            rtc_20180111_models.StopRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_task_with_options_async(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        """
        @param request: StopRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
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
            rtc_20180111_models.StopRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_record_task(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        """
        @param request: StopRecordTaskRequest
        @return: StopRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_record_task_with_options(request, runtime)

    async def stop_record_task_async(
        self,
        request: rtc_20180111_models.StopRecordTaskRequest,
    ) -> rtc_20180111_models.StopRecordTaskResponse:
        """
        @param request: StopRecordTaskRequest
        @return: StopRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_record_task_with_options_async(request, runtime)

    def stop_streaming_out_with_options(
        self,
        request: rtc_20180111_models.StopStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopStreamingOutResponse:
        """
        @summary StopStreamingOut
        
        @param request: StopStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStreamingOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStreamingOut',
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
            rtc_20180111_models.StopStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_streaming_out_with_options_async(
        self,
        request: rtc_20180111_models.StopStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.StopStreamingOutResponse:
        """
        @summary StopStreamingOut
        
        @param request: StopStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStreamingOutResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStreamingOut',
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
            rtc_20180111_models.StopStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_streaming_out(
        self,
        request: rtc_20180111_models.StopStreamingOutRequest,
    ) -> rtc_20180111_models.StopStreamingOutResponse:
        """
        @summary StopStreamingOut
        
        @param request: StopStreamingOutRequest
        @return: StopStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_streaming_out_with_options(request, runtime)

    async def stop_streaming_out_async(
        self,
        request: rtc_20180111_models.StopStreamingOutRequest,
    ) -> rtc_20180111_models.StopStreamingOutResponse:
        """
        @summary StopStreamingOut
        
        @param request: StopStreamingOutRequest
        @return: StopStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_streaming_out_with_options_async(request, runtime)

    def update_auto_live_stream_rule_with_options(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        """
        @param request: UpdateAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
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
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_live_stream_rule_with_options_async(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        """
        @param request: UpdateAutoLiveStreamRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAutoLiveStreamRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
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
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_live_stream_rule(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        """
        @param request: UpdateAutoLiveStreamRuleRequest
        @return: UpdateAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auto_live_stream_rule_with_options(request, runtime)

    async def update_auto_live_stream_rule_async(
        self,
        request: rtc_20180111_models.UpdateAutoLiveStreamRuleRequest,
    ) -> rtc_20180111_models.UpdateAutoLiveStreamRuleResponse:
        """
        @param request: UpdateAutoLiveStreamRuleRequest
        @return: UpdateAutoLiveStreamRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_live_stream_rule_with_options_async(request, runtime)

    def update_cloud_record_with_options(
        self,
        tmp_req: rtc_20180111_models.UpdateCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateCloudRecordResponse:
        """
        @summary 更新云端录制任务
        
        @param tmp_req: UpdateCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.UpdateCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudRecord',
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
            rtc_20180111_models.UpdateCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_record_with_options_async(
        self,
        tmp_req: rtc_20180111_models.UpdateCloudRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateCloudRecordResponse:
        """
        @summary 更新云端录制任务
        
        @param tmp_req: UpdateCloudRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.UpdateCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudRecord',
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
            rtc_20180111_models.UpdateCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_record(
        self,
        request: rtc_20180111_models.UpdateCloudRecordRequest,
    ) -> rtc_20180111_models.UpdateCloudRecordResponse:
        """
        @summary 更新云端录制任务
        
        @param request: UpdateCloudRecordRequest
        @return: UpdateCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_record_with_options(request, runtime)

    async def update_cloud_record_async(
        self,
        request: rtc_20180111_models.UpdateCloudRecordRequest,
    ) -> rtc_20180111_models.UpdateCloudRecordResponse:
        """
        @summary 更新云端录制任务
        
        @param request: UpdateCloudRecordRequest
        @return: UpdateCloudRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_record_with_options_async(request, runtime)

    def update_mputask_with_options(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        """
        @param request: UpdateMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
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
            rtc_20180111_models.UpdateMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mputask_with_options_async(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        """
        @param request: UpdateMPUTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMPUTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
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
            rtc_20180111_models.UpdateMPUTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mputask(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        """
        @param request: UpdateMPUTaskRequest
        @return: UpdateMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mputask_with_options(request, runtime)

    async def update_mputask_async(
        self,
        request: rtc_20180111_models.UpdateMPUTaskRequest,
    ) -> rtc_20180111_models.UpdateMPUTaskResponse:
        """
        @param request: UpdateMPUTaskRequest
        @return: UpdateMPUTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mputask_with_options_async(request, runtime)

    def update_record_task_with_options(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        """
        @param request: UpdateRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
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
            rtc_20180111_models.UpdateRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_task_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        """
        @param request: UpdateRecordTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
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
            rtc_20180111_models.UpdateRecordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_task(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        """
        @param request: UpdateRecordTaskRequest
        @return: UpdateRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_record_task_with_options(request, runtime)

    async def update_record_task_async(
        self,
        request: rtc_20180111_models.UpdateRecordTaskRequest,
    ) -> rtc_20180111_models.UpdateRecordTaskResponse:
        """
        @param request: UpdateRecordTaskRequest
        @return: UpdateRecordTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_record_task_with_options_async(request, runtime)

    def update_record_template_with_options(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        """
        @param request: UpdateRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
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
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_template_with_options_async(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        """
        @param request: UpdateRecordTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
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
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_template(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        """
        @param request: UpdateRecordTemplateRequest
        @return: UpdateRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_record_template_with_options(request, runtime)

    async def update_record_template_async(
        self,
        request: rtc_20180111_models.UpdateRecordTemplateRequest,
    ) -> rtc_20180111_models.UpdateRecordTemplateResponse:
        """
        @param request: UpdateRecordTemplateRequest
        @return: UpdateRecordTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_record_template_with_options_async(request, runtime)

    def update_streaming_out_with_options(
        self,
        tmp_req: rtc_20180111_models.UpdateStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateStreamingOutResponse:
        """
        @summary 更新旁路推流任务
        
        @param tmp_req: UpdateStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStreamingOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.UpdateStreamingOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStreamingOut',
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
            rtc_20180111_models.UpdateStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_streaming_out_with_options_async(
        self,
        tmp_req: rtc_20180111_models.UpdateStreamingOutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rtc_20180111_models.UpdateStreamingOutResponse:
        """
        @summary 更新旁路推流任务
        
        @param tmp_req: UpdateStreamingOutRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStreamingOutResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.UpdateStreamingOutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.layout_specified_users):
            request.layout_specified_users_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.layout_specified_users, 'LayoutSpecifiedUsers', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.bg_color):
            query['BgColor'] = request.bg_color
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.layout_specified_users_shrink):
            query['LayoutSpecifiedUsers'] = request.layout_specified_users_shrink
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.region_color):
            query['RegionColor'] = request.region_color
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.texts):
            query['Texts'] = request.texts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStreamingOut',
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
            rtc_20180111_models.UpdateStreamingOutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_streaming_out(
        self,
        request: rtc_20180111_models.UpdateStreamingOutRequest,
    ) -> rtc_20180111_models.UpdateStreamingOutResponse:
        """
        @summary 更新旁路推流任务
        
        @param request: UpdateStreamingOutRequest
        @return: UpdateStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_streaming_out_with_options(request, runtime)

    async def update_streaming_out_async(
        self,
        request: rtc_20180111_models.UpdateStreamingOutRequest,
    ) -> rtc_20180111_models.UpdateStreamingOutResponse:
        """
        @summary 更新旁路推流任务
        
        @param request: UpdateStreamingOutRequest
        @return: UpdateStreamingOutResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_streaming_out_with_options_async(request, runtime)

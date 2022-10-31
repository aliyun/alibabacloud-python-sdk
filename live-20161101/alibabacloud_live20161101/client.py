# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_live20161101 import models as live_20161101_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'live.aliyuncs.com',
            'cn-beijing': 'live.aliyuncs.com',
            'cn-hangzhou': 'live.aliyuncs.com',
            'cn-shanghai': 'live.aliyuncs.com',
            'cn-shenzhen': 'live.aliyuncs.com',
            'ap-southeast-1': 'live.aliyuncs.com',
            'ap-southeast-5': 'live.aliyuncs.com',
            'ap-northeast-1': 'live.aliyuncs.com',
            'eu-central-1': 'live.aliyuncs.com',
            'ap-south-1': 'live.aliyuncs.com',
            'ap-northeast-2-pop': 'live.aliyuncs.com',
            'ap-southeast-2': 'live.aliyuncs.com',
            'ap-southeast-3': 'live.aliyuncs.com',
            'cn-beijing-finance-1': 'live.aliyuncs.com',
            'cn-beijing-finance-pop': 'live.aliyuncs.com',
            'cn-beijing-gov-1': 'live.aliyuncs.com',
            'cn-beijing-nu16-b01': 'live.aliyuncs.com',
            'cn-chengdu': 'live.aliyuncs.com',
            'cn-edge-1': 'live.aliyuncs.com',
            'cn-fujian': 'live.aliyuncs.com',
            'cn-haidian-cm12-c01': 'live.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'live.aliyuncs.com',
            'cn-hangzhou-finance': 'live.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'live.aliyuncs.com',
            'cn-hangzhou-test-306': 'live.aliyuncs.com',
            'cn-hongkong': 'live.aliyuncs.com',
            'cn-hongkong-finance-pop': 'live.aliyuncs.com',
            'cn-huhehaote': 'live.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'live.aliyuncs.com',
            'cn-north-2-gov-1': 'live.aliyuncs.com',
            'cn-qingdao-nebula': 'live.aliyuncs.com',
            'cn-shanghai-et15-b01': 'live.aliyuncs.com',
            'cn-shanghai-et2-b01': 'live.aliyuncs.com',
            'cn-shanghai-finance-1': 'live.aliyuncs.com',
            'cn-shanghai-inner': 'live.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'live.aliyuncs.com',
            'cn-shenzhen-finance-1': 'live.aliyuncs.com',
            'cn-shenzhen-inner': 'live.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'live.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'live.aliyuncs.com',
            'cn-wuhan': 'live.aliyuncs.com',
            'cn-wulanchabu': 'live.aliyuncs.com',
            'cn-yushanfang': 'live.aliyuncs.com',
            'cn-zhangbei': 'live.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'live.aliyuncs.com',
            'cn-zhangjiakou': 'live.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'live.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'live.aliyuncs.com',
            'eu-west-1': 'live.aliyuncs.com',
            'eu-west-1-oxs': 'live.aliyuncs.com',
            'me-east-1': 'live.aliyuncs.com',
            'rus-west-1-pop': 'live.aliyuncs.com',
            'us-east-1': 'live.aliyuncs.com',
            'us-west-1': 'live.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('live', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_caster_component_with_options(
        self,
        request: live_20161101_models.AddCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.html_layer_content):
            query['HtmlLayerContent'] = request.html_layer_content
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.layer_order):
            query['LayerOrder'] = request.layer_order
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_component_with_options_async(
        self,
        request: live_20161101_models.AddCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.html_layer_content):
            query['HtmlLayerContent'] = request.html_layer_content
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.layer_order):
            query['LayerOrder'] = request.layer_order
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_component(
        self,
        request: live_20161101_models.AddCasterComponentRequest,
    ) -> live_20161101_models.AddCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_component_with_options(request, runtime)

    async def add_caster_component_async(
        self,
        request: live_20161101_models.AddCasterComponentRequest,
    ) -> live_20161101_models.AddCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_component_with_options_async(request, runtime)

    def add_caster_episode_with_options(
        self,
        request: live_20161101_models.AddCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_episode_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_episode(
        self,
        request: live_20161101_models.AddCasterEpisodeRequest,
    ) -> live_20161101_models.AddCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_with_options(request, runtime)

    async def add_caster_episode_async(
        self,
        request: live_20161101_models.AddCasterEpisodeRequest,
    ) -> live_20161101_models.AddCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_episode_with_options_async(request, runtime)

    def add_caster_episode_group_with_options(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_episode_group_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_episode_group(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupRequest,
    ) -> live_20161101_models.AddCasterEpisodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_with_options(request, runtime)

    async def add_caster_episode_group_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupRequest,
    ) -> live_20161101_models.AddCasterEpisodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_episode_group_with_options_async(request, runtime)

    def add_caster_episode_group_content_with_options(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroupContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_episode_group_content_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroupContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_episode_group_content(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupContentRequest,
    ) -> live_20161101_models.AddCasterEpisodeGroupContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_content_with_options(request, runtime)

    async def add_caster_episode_group_content_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupContentRequest,
    ) -> live_20161101_models.AddCasterEpisodeGroupContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_episode_group_content_with_options_async(request, runtime)

    def add_caster_layout_with_options(
        self,
        request: live_20161101_models.AddCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_layout_with_options_async(
        self,
        request: live_20161101_models.AddCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_layout(
        self,
        request: live_20161101_models.AddCasterLayoutRequest,
    ) -> live_20161101_models.AddCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_layout_with_options(request, runtime)

    async def add_caster_layout_async(
        self,
        request: live_20161101_models.AddCasterLayoutRequest,
    ) -> live_20161101_models.AddCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_layout_with_options_async(request, runtime)

    def add_caster_program_with_options(
        self,
        request: live_20161101_models.AddCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_program_with_options_async(
        self,
        request: live_20161101_models.AddCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_program(
        self,
        request: live_20161101_models.AddCasterProgramRequest,
    ) -> live_20161101_models.AddCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_program_with_options(request, runtime)

    async def add_caster_program_async(
        self,
        request: live_20161101_models.AddCasterProgramRequest,
    ) -> live_20161101_models.AddCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_program_with_options_async(request, runtime)

    def add_caster_video_resource_with_options(
        self,
        request: live_20161101_models.AddCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.fixed_delay_duration):
            query['FixedDelayDuration'] = request.fixed_delay_duration
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.AddCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.fixed_delay_duration):
            query['FixedDelayDuration'] = request.fixed_delay_duration
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterVideoResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_caster_video_resource(
        self,
        request: live_20161101_models.AddCasterVideoResourceRequest,
    ) -> live_20161101_models.AddCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_caster_video_resource_with_options(request, runtime)

    async def add_caster_video_resource_async(
        self,
        request: live_20161101_models.AddCasterVideoResourceRequest,
    ) -> live_20161101_models.AddCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_caster_video_resource_with_options_async(request, runtime)

    def add_custom_live_stream_transcode_with_options(
        self,
        request: live_20161101_models.AddCustomLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCustomLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.kms_key_expire_interval):
            query['KmsKeyExpireInterval'] = request.kms_key_expire_interval
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyID'] = request.kms_key_id
        if not UtilClient.is_unset(request.kms_uid):
            query['KmsUID'] = request.kms_uid
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCustomLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddCustomLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCustomLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.kms_key_expire_interval):
            query['KmsKeyExpireInterval'] = request.kms_key_expire_interval
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyID'] = request.kms_key_id
        if not UtilClient.is_unset(request.kms_uid):
            query['KmsUID'] = request.kms_uid
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCustomLiveStreamTranscodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_live_stream_transcode(
        self,
        request: live_20161101_models.AddCustomLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddCustomLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_custom_live_stream_transcode_with_options(request, runtime)

    async def add_custom_live_stream_transcode_async(
        self,
        request: live_20161101_models.AddCustomLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddCustomLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_live_stream_transcode_with_options_async(request, runtime)

    def add_live_app_record_config_with_options(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.on_demand):
            query['OnDemand'] = request.on_demand
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_format):
            query['RecordFormat'] = request.record_format
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.transcode_record_format):
            query['TranscodeRecordFormat'] = request.transcode_record_format
        if not UtilClient.is_unset(request.transcode_templates):
            query['TranscodeTemplates'] = request.transcode_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_app_record_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.on_demand):
            query['OnDemand'] = request.on_demand
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_format):
            query['RecordFormat'] = request.record_format
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.transcode_record_format):
            query['TranscodeRecordFormat'] = request.transcode_record_format
        if not UtilClient.is_unset(request.transcode_templates):
            query['TranscodeTemplates'] = request.transcode_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppRecordConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_app_record_config(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_record_config_with_options(request, runtime)

    async def add_live_app_record_config_async(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_app_record_config_with_options_async(request, runtime)

    def add_live_app_snapshot_config_with_options(
        self,
        request: live_20161101_models.AddLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppSnapshotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_app_snapshot_config(
        self,
        request: live_20161101_models.AddLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.AddLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_snapshot_config_with_options(request, runtime)

    async def add_live_app_snapshot_config_async(
        self,
        request: live_20161101_models.AddLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.AddLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_app_snapshot_config_with_options_async(request, runtime)

    def add_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_audio_audit_config(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_config_with_options(request, runtime)

    async def add_live_audio_audit_config_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_audio_audit_config_with_options_async(request, runtime)

    def add_live_audio_audit_notify_config_with_options(
        self,
        request: live_20161101_models.AddLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_audio_audit_notify_config(
        self,
        request: live_20161101_models.AddLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_notify_config_with_options(request, runtime)

    async def add_live_audio_audit_notify_config_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_audio_audit_notify_config_with_options_async(request, runtime)

    def add_live_detect_notify_config_with_options(
        self,
        request: live_20161101_models.AddLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDetectNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_detect_notify_config(
        self,
        request: live_20161101_models.AddLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_detect_notify_config_with_options(request, runtime)

    async def add_live_detect_notify_config_async(
        self,
        request: live_20161101_models.AddLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_detect_notify_config_with_options_async(request, runtime)

    def add_live_domain_with_options(
        self,
        request: live_20161101_models.AddLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_domain_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_domain(
        self,
        request: live_20161101_models.AddLiveDomainRequest,
    ) -> live_20161101_models.AddLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_with_options(request, runtime)

    async def add_live_domain_async(
        self,
        request: live_20161101_models.AddLiveDomainRequest,
    ) -> live_20161101_models.AddLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_domain_with_options_async(request, runtime)

    def add_live_domain_mapping_with_options(
        self,
        request: live_20161101_models.AddLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_domain_mapping(
        self,
        request: live_20161101_models.AddLiveDomainMappingRequest,
    ) -> live_20161101_models.AddLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_mapping_with_options(request, runtime)

    async def add_live_domain_mapping_async(
        self,
        request: live_20161101_models.AddLiveDomainMappingRequest,
    ) -> live_20161101_models.AddLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_domain_mapping_with_options_async(request, runtime)

    def add_live_domain_play_mapping_with_options(
        self,
        request: live_20161101_models.AddLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainPlayMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_domain_play_mapping_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainPlayMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_domain_play_mapping(
        self,
        request: live_20161101_models.AddLiveDomainPlayMappingRequest,
    ) -> live_20161101_models.AddLiveDomainPlayMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_play_mapping_with_options(request, runtime)

    async def add_live_domain_play_mapping_async(
        self,
        request: live_20161101_models.AddLiveDomainPlayMappingRequest,
    ) -> live_20161101_models.AddLiveDomainPlayMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_domain_play_mapping_with_options_async(request, runtime)

    def add_live_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.AddLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.AddLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLivePullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_pull_stream_info_config(
        self,
        request: live_20161101_models.AddLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.AddLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_pull_stream_info_config_with_options(request, runtime)

    async def add_live_pull_stream_info_config_async(
        self,
        request: live_20161101_models.AddLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.AddLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_pull_stream_info_config_with_options_async(request, runtime)

    def add_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.AddLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_record_notify_config(
        self,
        request: live_20161101_models.AddLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_notify_config_with_options(request, runtime)

    async def add_live_record_notify_config_async(
        self,
        request: live_20161101_models.AddLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.AddLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_record_notify_config_with_options_async(request, runtime)

    def add_live_record_vod_config_with_options(
        self,
        request: live_20161101_models.AddLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_compose):
            query['AutoCompose'] = request.auto_compose
        if not UtilClient.is_unset(request.compose_vod_transcode_group_id):
            query['ComposeVodTranscodeGroupId'] = request.compose_vod_transcode_group_id
        if not UtilClient.is_unset(request.cycle_duration):
            query['CycleDuration'] = request.cycle_duration
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vod_transcode_group_id):
            query['VodTranscodeGroupId'] = request.vod_transcode_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordVodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_record_vod_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_compose):
            query['AutoCompose'] = request.auto_compose
        if not UtilClient.is_unset(request.compose_vod_transcode_group_id):
            query['ComposeVodTranscodeGroupId'] = request.compose_vod_transcode_group_id
        if not UtilClient.is_unset(request.cycle_duration):
            query['CycleDuration'] = request.cycle_duration
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vod_transcode_group_id):
            query['VodTranscodeGroupId'] = request.vod_transcode_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordVodConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_record_vod_config(
        self,
        request: live_20161101_models.AddLiveRecordVodConfigRequest,
    ) -> live_20161101_models.AddLiveRecordVodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_vod_config_with_options(request, runtime)

    async def add_live_record_vod_config_async(
        self,
        request: live_20161101_models.AddLiveRecordVodConfigRequest,
    ) -> live_20161101_models.AddLiveRecordVodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_record_vod_config_with_options_async(request, runtime)

    def add_live_snapshot_detect_porn_config_with_options(
        self,
        request: live_20161101_models.AddLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveSnapshotDetectPornConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_snapshot_detect_porn_config(
        self,
        request: live_20161101_models.AddLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.AddLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_snapshot_detect_porn_config_with_options(request, runtime)

    async def add_live_snapshot_detect_porn_config_async(
        self,
        request: live_20161101_models.AddLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.AddLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_snapshot_detect_porn_config_with_options_async(request, runtime)

    def add_live_stream_transcode_with_options(
        self,
        request: live_20161101_models.AddLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamTranscodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_stream_transcode(
        self,
        request: live_20161101_models.AddLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_transcode_with_options(request, runtime)

    async def add_live_stream_transcode_async(
        self,
        request: live_20161101_models.AddLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_stream_transcode_with_options_async(request, runtime)

    def add_live_stream_watermark_with_options(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_stream_watermark_with_options_async(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_stream_watermark(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRequest,
    ) -> live_20161101_models.AddLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_watermark_with_options(request, runtime)

    async def add_live_stream_watermark_async(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRequest,
    ) -> live_20161101_models.AddLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_stream_watermark_with_options_async(request, runtime)

    def add_live_stream_watermark_rule_with_options(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_live_stream_watermark_rule_with_options_async(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_live_stream_watermark_rule(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.AddLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_watermark_rule_with_options(request, runtime)

    async def add_live_stream_watermark_rule_async(
        self,
        request: live_20161101_models.AddLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.AddLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_stream_watermark_rule_with_options_async(request, runtime)

    def add_multi_rate_config_with_options(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.av_format):
            query['AvFormat'] = request.av_format
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_lazy):
            query['IsLazy'] = request.is_lazy
        if not UtilClient.is_unset(request.is_time_align):
            query['IsTimeAlign'] = request.is_time_align
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.av_format):
            query['AvFormat'] = request.av_format
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_lazy):
            query['IsLazy'] = request.is_lazy
        if not UtilClient.is_unset(request.is_time_align):
            query['IsTimeAlign'] = request.is_time_align
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddMultiRateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_multi_rate_config(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_multi_rate_config_with_options(request, runtime)

    async def add_multi_rate_config_async(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_multi_rate_config_with_options_async(request, runtime)

    def add_playlist_items_with_options(
        self,
        request: live_20161101_models.AddPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddPlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddPlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_playlist_items_with_options_async(
        self,
        request: live_20161101_models.AddPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddPlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddPlaylistItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_playlist_items(
        self,
        request: live_20161101_models.AddPlaylistItemsRequest,
    ) -> live_20161101_models.AddPlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_playlist_items_with_options(request, runtime)

    async def add_playlist_items_async(
        self,
        request: live_20161101_models.AddPlaylistItemsRequest,
    ) -> live_20161101_models.AddPlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_playlist_items_with_options_async(request, runtime)

    def add_rts_live_stream_transcode_with_options(
        self,
        request: live_20161101_models.AddRtsLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddRtsLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.delete_bframes):
            query['DeleteBframes'] = request.delete_bframes
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.opus):
            query['Opus'] = request.opus
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRtsLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddRtsLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rts_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddRtsLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddRtsLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.delete_bframes):
            query['DeleteBframes'] = request.delete_bframes
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.opus):
            query['Opus'] = request.opus
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRtsLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddRtsLiveStreamTranscodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rts_live_stream_transcode(
        self,
        request: live_20161101_models.AddRtsLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddRtsLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_rts_live_stream_transcode_with_options(request, runtime)

    async def add_rts_live_stream_transcode_async(
        self,
        request: live_20161101_models.AddRtsLiveStreamTranscodeRequest,
    ) -> live_20161101_models.AddRtsLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_rts_live_stream_transcode_with_options_async(request, runtime)

    def add_show_into_show_list_with_options(
        self,
        request: live_20161101_models.AddShowIntoShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddShowIntoShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.live_input_type):
            query['LiveInputType'] = request.live_input_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_url):
            query['ResourceUrl'] = request.resource_url
        if not UtilClient.is_unset(request.show_name):
            query['ShowName'] = request.show_name
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_list):
            query['showList'] = request.show_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShowIntoShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddShowIntoShowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_show_into_show_list_with_options_async(
        self,
        request: live_20161101_models.AddShowIntoShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddShowIntoShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.live_input_type):
            query['LiveInputType'] = request.live_input_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_url):
            query['ResourceUrl'] = request.resource_url
        if not UtilClient.is_unset(request.show_name):
            query['ShowName'] = request.show_name
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_list):
            query['showList'] = request.show_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShowIntoShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddShowIntoShowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_show_into_show_list(
        self,
        request: live_20161101_models.AddShowIntoShowListRequest,
    ) -> live_20161101_models.AddShowIntoShowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_show_into_show_list_with_options(request, runtime)

    async def add_show_into_show_list_async(
        self,
        request: live_20161101_models.AddShowIntoShowListRequest,
    ) -> live_20161101_models.AddShowIntoShowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_show_into_show_list_with_options_async(request, runtime)

    def add_studio_layout_with_options(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.layout_type):
            query['LayoutType'] = request.layout_type
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_studio_layout_with_options_async(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.layout_type):
            query['LayoutType'] = request.layout_type
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddStudioLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_studio_layout(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_studio_layout_with_options(request, runtime)

    async def add_studio_layout_async(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_studio_layout_with_options_async(request, runtime)

    def add_trancode_seiwith_options(
        self,
        request: live_20161101_models.AddTrancodeSEIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddTrancodeSEIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pattern):
            query['Pattern'] = request.pattern
        if not UtilClient.is_unset(request.repeat):
            query['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrancodeSEI',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddTrancodeSEIResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_trancode_seiwith_options_async(
        self,
        request: live_20161101_models.AddTrancodeSEIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddTrancodeSEIResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pattern):
            query['Pattern'] = request.pattern
        if not UtilClient.is_unset(request.repeat):
            query['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrancodeSEI',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddTrancodeSEIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_trancode_sei(
        self,
        request: live_20161101_models.AddTrancodeSEIRequest,
    ) -> live_20161101_models.AddTrancodeSEIResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_trancode_seiwith_options(request, runtime)

    async def add_trancode_sei_async(
        self,
        request: live_20161101_models.AddTrancodeSEIRequest,
    ) -> live_20161101_models.AddTrancodeSEIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_trancode_seiwith_options_async(request, runtime)

    def allow_push_stream_with_options(
        self,
        request: live_20161101_models.AllowPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AllowPushStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllowPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AllowPushStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def allow_push_stream_with_options_async(
        self,
        request: live_20161101_models.AllowPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AllowPushStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllowPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AllowPushStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allow_push_stream(
        self,
        request: live_20161101_models.AllowPushStreamRequest,
    ) -> live_20161101_models.AllowPushStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.allow_push_stream_with_options(request, runtime)

    async def allow_push_stream_async(
        self,
        request: live_20161101_models.AllowPushStreamRequest,
    ) -> live_20161101_models.AllowPushStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allow_push_stream_with_options_async(request, runtime)

    def batch_delete_live_domain_configs_with_options(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchDeleteLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchDeleteLiveDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_live_domain_configs(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_live_domain_configs_with_options(request, runtime)

    async def batch_delete_live_domain_configs_async(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_live_domain_configs_with_options_async(request, runtime)

    def batch_set_live_domain_configs_with_options(
        self,
        request: live_20161101_models.BatchSetLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchSetLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchSetLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.BatchSetLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchSetLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchSetLiveDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_live_domain_configs(
        self,
        request: live_20161101_models.BatchSetLiveDomainConfigsRequest,
    ) -> live_20161101_models.BatchSetLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_live_domain_configs_with_options(request, runtime)

    async def batch_set_live_domain_configs_async(
        self,
        request: live_20161101_models.BatchSetLiveDomainConfigsRequest,
    ) -> live_20161101_models.BatchSetLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_live_domain_configs_with_options_async(request, runtime)

    def cancel_mute_all_group_user_with_options(
        self,
        request: live_20161101_models.CancelMuteAllGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CancelMuteAllGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.operator_user_id):
            body['OperatorUserId'] = request.operator_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelMuteAllGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CancelMuteAllGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_mute_all_group_user_with_options_async(
        self,
        request: live_20161101_models.CancelMuteAllGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CancelMuteAllGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.operator_user_id):
            body['OperatorUserId'] = request.operator_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelMuteAllGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CancelMuteAllGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_mute_all_group_user(
        self,
        request: live_20161101_models.CancelMuteAllGroupUserRequest,
    ) -> live_20161101_models.CancelMuteAllGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_mute_all_group_user_with_options(request, runtime)

    async def cancel_mute_all_group_user_async(
        self,
        request: live_20161101_models.CancelMuteAllGroupUserRequest,
    ) -> live_20161101_models.CancelMuteAllGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_mute_all_group_user_with_options_async(request, runtime)

    def close_live_shift_with_options(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseLiveShiftResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_live_shift_with_options_async(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseLiveShiftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_live_shift(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_live_shift_with_options(request, runtime)

    async def close_live_shift_async(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_live_shift_with_options_async(request, runtime)

    def close_message_group_with_options(
        self,
        request: live_20161101_models.CloseMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_message_group_with_options_async(
        self,
        request: live_20161101_models.CloseMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_message_group(
        self,
        request: live_20161101_models.CloseMessageGroupRequest,
    ) -> live_20161101_models.CloseMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_message_group_with_options(request, runtime)

    async def close_message_group_async(
        self,
        request: live_20161101_models.CloseMessageGroupRequest,
    ) -> live_20161101_models.CloseMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_message_group_with_options_async(request, runtime)

    def copy_caster_with_options(
        self,
        request: live_20161101_models.CopyCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.src_caster_id):
            query['SrcCasterId'] = request.src_caster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_caster_with_options_async(
        self,
        request: live_20161101_models.CopyCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.src_caster_id):
            query['SrcCasterId'] = request.src_caster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_caster(
        self,
        request: live_20161101_models.CopyCasterRequest,
    ) -> live_20161101_models.CopyCasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_with_options(request, runtime)

    async def copy_caster_async(
        self,
        request: live_20161101_models.CopyCasterRequest,
    ) -> live_20161101_models.CopyCasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_caster_with_options_async(request, runtime)

    def copy_caster_scene_config_with_options(
        self,
        request: live_20161101_models.CopyCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.from_scene_id):
            query['FromSceneId'] = request.from_scene_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.to_scene_id):
            query['ToSceneId'] = request.to_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.CopyCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.from_scene_id):
            query['FromSceneId'] = request.from_scene_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.to_scene_id):
            query['ToSceneId'] = request.to_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_caster_scene_config(
        self,
        request: live_20161101_models.CopyCasterSceneConfigRequest,
    ) -> live_20161101_models.CopyCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_scene_config_with_options(request, runtime)

    async def copy_caster_scene_config_async(
        self,
        request: live_20161101_models.CopyCasterSceneConfigRequest,
    ) -> live_20161101_models.CopyCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_caster_scene_config_with_options_async(request, runtime)

    def create_caster_with_options(
        self,
        request: live_20161101_models.CreateCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.caster_template):
            query['CasterTemplate'] = request.caster_template
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.purchase_time):
            query['PurchaseTime'] = request.purchase_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_caster_with_options_async(
        self,
        request: live_20161101_models.CreateCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.caster_template):
            query['CasterTemplate'] = request.caster_template
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.purchase_time):
            query['PurchaseTime'] = request.purchase_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_caster(
        self,
        request: live_20161101_models.CreateCasterRequest,
    ) -> live_20161101_models.CreateCasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_caster_with_options(request, runtime)

    async def create_caster_async(
        self,
        request: live_20161101_models.CreateCasterRequest,
    ) -> live_20161101_models.CreateCasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_caster_with_options_async(request, runtime)

    def create_custom_template_with_options(
        self,
        request: live_20161101_models.CreateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_template):
            query['CustomTemplate'] = request.custom_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_template_with_options_async(
        self,
        request: live_20161101_models.CreateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_template):
            query['CustomTemplate'] = request.custom_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_template(
        self,
        request: live_20161101_models.CreateCustomTemplateRequest,
    ) -> live_20161101_models.CreateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_template_with_options(request, runtime)

    async def create_custom_template_async(
        self,
        request: live_20161101_models.CreateCustomTemplateRequest,
    ) -> live_20161101_models.CreateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_template_with_options_async(request, runtime)

    def create_live_real_time_log_delivery_with_options(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveRealTimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_real_time_log_delivery_with_options_async(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveRealTimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveRealTimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_real_time_log_delivery(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_real_time_log_delivery_with_options(request, runtime)

    async def create_live_real_time_log_delivery_async(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_real_time_log_delivery_with_options_async(request, runtime)

    def create_live_stream_monitor_with_options(
        self,
        request: live_20161101_models.CreateLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_stream_monitor_with_options_async(
        self,
        request: live_20161101_models.CreateLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_stream_monitor(
        self,
        request: live_20161101_models.CreateLiveStreamMonitorRequest,
    ) -> live_20161101_models.CreateLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_stream_monitor_with_options(request, runtime)

    async def create_live_stream_monitor_async(
        self,
        request: live_20161101_models.CreateLiveStreamMonitorRequest,
    ) -> live_20161101_models.CreateLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_stream_monitor_with_options_async(request, runtime)

    def create_live_stream_record_index_files_with_options(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_stream_record_index_files_with_options_async(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamRecordIndexFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_stream_record_index_files(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_stream_record_index_files_with_options(request, runtime)

    async def create_live_stream_record_index_files_async(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_stream_record_index_files_with_options_async(request, runtime)

    def create_live_transcode_template_with_options(
        self,
        request: live_20161101_models.CreateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_transcode_template_with_options_async(
        self,
        request: live_20161101_models.CreateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveTranscodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_transcode_template(
        self,
        request: live_20161101_models.CreateLiveTranscodeTemplateRequest,
    ) -> live_20161101_models.CreateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_transcode_template_with_options(request, runtime)

    async def create_live_transcode_template_async(
        self,
        request: live_20161101_models.CreateLiveTranscodeTemplateRequest,
    ) -> live_20161101_models.CreateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_transcode_template_with_options_async(request, runtime)

    def create_message_group_with_options(
        self,
        tmp_req: live_20161101_models.CreateMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMessageGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.CreateMessageGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_group_with_options_async(
        self,
        tmp_req: live_20161101_models.CreateMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMessageGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.CreateMessageGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_group(
        self,
        request: live_20161101_models.CreateMessageGroupRequest,
    ) -> live_20161101_models.CreateMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_message_group_with_options(request, runtime)

    async def create_message_group_async(
        self,
        request: live_20161101_models.CreateMessageGroupRequest,
    ) -> live_20161101_models.CreateMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_message_group_with_options_async(request, runtime)

    def create_mix_stream_with_options(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_config):
            query['CallbackConfig'] = request.callback_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mix_stream_with_options_async(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_config):
            query['CallbackConfig'] = request.callback_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMixStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mix_stream(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
    ) -> live_20161101_models.CreateMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mix_stream_with_options(request, runtime)

    async def create_mix_stream_async(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
    ) -> live_20161101_models.CreateMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mix_stream_with_options_async(request, runtime)

    def delete_caster_with_options(
        self,
        request: live_20161101_models.DeleteCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster(
        self,
        request: live_20161101_models.DeleteCasterRequest,
    ) -> live_20161101_models.DeleteCasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_with_options(request, runtime)

    async def delete_caster_async(
        self,
        request: live_20161101_models.DeleteCasterRequest,
    ) -> live_20161101_models.DeleteCasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_with_options_async(request, runtime)

    def delete_caster_component_with_options(
        self,
        request: live_20161101_models.DeleteCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_component_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_component(
        self,
        request: live_20161101_models.DeleteCasterComponentRequest,
    ) -> live_20161101_models.DeleteCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_component_with_options(request, runtime)

    async def delete_caster_component_async(
        self,
        request: live_20161101_models.DeleteCasterComponentRequest,
    ) -> live_20161101_models.DeleteCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_component_with_options_async(request, runtime)

    def delete_caster_episode_with_options(
        self,
        request: live_20161101_models.DeleteCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_episode_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_episode(
        self,
        request: live_20161101_models.DeleteCasterEpisodeRequest,
    ) -> live_20161101_models.DeleteCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_with_options(request, runtime)

    async def delete_caster_episode_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeRequest,
    ) -> live_20161101_models.DeleteCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_episode_with_options_async(request, runtime)

    def delete_caster_episode_group_with_options(
        self,
        request: live_20161101_models.DeleteCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_episode_group_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_episode_group(
        self,
        request: live_20161101_models.DeleteCasterEpisodeGroupRequest,
    ) -> live_20161101_models.DeleteCasterEpisodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_group_with_options(request, runtime)

    async def delete_caster_episode_group_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeGroupRequest,
    ) -> live_20161101_models.DeleteCasterEpisodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_episode_group_with_options_async(request, runtime)

    def delete_caster_layout_with_options(
        self,
        request: live_20161101_models.DeleteCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_layout_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_layout(
        self,
        request: live_20161101_models.DeleteCasterLayoutRequest,
    ) -> live_20161101_models.DeleteCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_layout_with_options(request, runtime)

    async def delete_caster_layout_async(
        self,
        request: live_20161101_models.DeleteCasterLayoutRequest,
    ) -> live_20161101_models.DeleteCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_layout_with_options_async(request, runtime)

    def delete_caster_program_with_options(
        self,
        request: live_20161101_models.DeleteCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_program_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_program(
        self,
        request: live_20161101_models.DeleteCasterProgramRequest,
    ) -> live_20161101_models.DeleteCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_program_with_options(request, runtime)

    async def delete_caster_program_async(
        self,
        request: live_20161101_models.DeleteCasterProgramRequest,
    ) -> live_20161101_models.DeleteCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_program_with_options_async(request, runtime)

    def delete_caster_scene_config_with_options(
        self,
        request: live_20161101_models.DeleteCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_scene_config(
        self,
        request: live_20161101_models.DeleteCasterSceneConfigRequest,
    ) -> live_20161101_models.DeleteCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_scene_config_with_options(request, runtime)

    async def delete_caster_scene_config_async(
        self,
        request: live_20161101_models.DeleteCasterSceneConfigRequest,
    ) -> live_20161101_models.DeleteCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_scene_config_with_options_async(request, runtime)

    def delete_caster_video_resource_with_options(
        self,
        request: live_20161101_models.DeleteCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterVideoResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_caster_video_resource(
        self,
        request: live_20161101_models.DeleteCasterVideoResourceRequest,
    ) -> live_20161101_models.DeleteCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_video_resource_with_options(request, runtime)

    async def delete_caster_video_resource_async(
        self,
        request: live_20161101_models.DeleteCasterVideoResourceRequest,
    ) -> live_20161101_models.DeleteCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_caster_video_resource_with_options_async(request, runtime)

    def delete_custom_template_with_options(
        self,
        request: live_20161101_models.DeleteCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_template_with_options_async(
        self,
        request: live_20161101_models.DeleteCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_template(
        self,
        request: live_20161101_models.DeleteCustomTemplateRequest,
    ) -> live_20161101_models.DeleteCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_template_with_options(request, runtime)

    async def delete_custom_template_async(
        self,
        request: live_20161101_models.DeleteCustomTemplateRequest,
    ) -> live_20161101_models.DeleteCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_template_with_options_async(request, runtime)

    def delete_live_app_record_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_app_record_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppRecordConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_app_record_config(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_record_config_with_options(request, runtime)

    async def delete_live_app_record_config_async(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_app_record_config_with_options_async(request, runtime)

    def delete_live_app_snapshot_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppSnapshotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_app_snapshot_config(
        self,
        request: live_20161101_models.DeleteLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.DeleteLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_snapshot_config_with_options(request, runtime)

    async def delete_live_app_snapshot_config_async(
        self,
        request: live_20161101_models.DeleteLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.DeleteLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_app_snapshot_config_with_options_async(request, runtime)

    def delete_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_audio_audit_config(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_config_with_options(request, runtime)

    async def delete_live_audio_audit_config_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_audio_audit_config_with_options_async(request, runtime)

    def delete_live_audio_audit_notify_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_audio_audit_notify_config(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_notify_config_with_options(request, runtime)

    async def delete_live_audio_audit_notify_config_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_audio_audit_notify_config_with_options_async(request, runtime)

    def delete_live_detect_notify_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDetectNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_detect_notify_config(
        self,
        request: live_20161101_models.DeleteLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_detect_notify_config_with_options(request, runtime)

    async def delete_live_detect_notify_config_async(
        self,
        request: live_20161101_models.DeleteLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_detect_notify_config_with_options_async(request, runtime)

    def delete_live_domain_with_options(
        self,
        request: live_20161101_models.DeleteLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_domain_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_domain(
        self,
        request: live_20161101_models.DeleteLiveDomainRequest,
    ) -> live_20161101_models.DeleteLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_with_options(request, runtime)

    async def delete_live_domain_async(
        self,
        request: live_20161101_models.DeleteLiveDomainRequest,
    ) -> live_20161101_models.DeleteLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_domain_with_options_async(request, runtime)

    def delete_live_domain_mapping_with_options(
        self,
        request: live_20161101_models.DeleteLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_domain_mapping(
        self,
        request: live_20161101_models.DeleteLiveDomainMappingRequest,
    ) -> live_20161101_models.DeleteLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_mapping_with_options(request, runtime)

    async def delete_live_domain_mapping_async(
        self,
        request: live_20161101_models.DeleteLiveDomainMappingRequest,
    ) -> live_20161101_models.DeleteLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_domain_mapping_with_options_async(request, runtime)

    def delete_live_domain_play_mapping_with_options(
        self,
        request: live_20161101_models.DeleteLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainPlayMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_domain_play_mapping_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainPlayMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_domain_play_mapping(
        self,
        request: live_20161101_models.DeleteLiveDomainPlayMappingRequest,
    ) -> live_20161101_models.DeleteLiveDomainPlayMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_play_mapping_with_options(request, runtime)

    async def delete_live_domain_play_mapping_async(
        self,
        request: live_20161101_models.DeleteLiveDomainPlayMappingRequest,
    ) -> live_20161101_models.DeleteLiveDomainPlayMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_domain_play_mapping_with_options_async(request, runtime)

    def delete_live_edge_transfer_with_options(
        self,
        request: live_20161101_models.DeleteLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_edge_transfer_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveEdgeTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_edge_transfer(
        self,
        request: live_20161101_models.DeleteLiveEdgeTransferRequest,
    ) -> live_20161101_models.DeleteLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_edge_transfer_with_options(request, runtime)

    async def delete_live_edge_transfer_async(
        self,
        request: live_20161101_models.DeleteLiveEdgeTransferRequest,
    ) -> live_20161101_models.DeleteLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_edge_transfer_with_options_async(request, runtime)

    def delete_live_lazy_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_lazy_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_lazy_pull_stream_info_config(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_lazy_pull_stream_info_config_with_options(request, runtime)

    async def delete_live_lazy_pull_stream_info_config_async(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_lazy_pull_stream_info_config_with_options_async(request, runtime)

    def delete_live_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.DeleteLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLivePullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_pull_stream_info_config(
        self,
        request: live_20161101_models.DeleteLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.DeleteLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_pull_stream_info_config_with_options(request, runtime)

    async def delete_live_pull_stream_info_config_async(
        self,
        request: live_20161101_models.DeleteLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.DeleteLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_pull_stream_info_config_with_options_async(request, runtime)

    def delete_live_real_time_log_logstore_with_options(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealTimeLogLogstore',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_real_time_log_logstore_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealTimeLogLogstore',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_real_time_log_logstore(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_real_time_log_logstore_with_options(request, runtime)

    async def delete_live_real_time_log_logstore_async(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_real_time_log_logstore_with_options_async(request, runtime)

    def delete_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_realtime_log_delivery(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_realtime_log_delivery_with_options(request, runtime)

    async def delete_live_realtime_log_delivery_async(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_realtime_log_delivery_with_options_async(request, runtime)

    def delete_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_record_notify_config(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_notify_config_with_options(request, runtime)

    async def delete_live_record_notify_config_async(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_record_notify_config_with_options_async(request, runtime)

    def delete_live_record_vod_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordVodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_record_vod_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordVodConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_record_vod_config(
        self,
        request: live_20161101_models.DeleteLiveRecordVodConfigRequest,
    ) -> live_20161101_models.DeleteLiveRecordVodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_vod_config_with_options(request, runtime)

    async def delete_live_record_vod_config_async(
        self,
        request: live_20161101_models.DeleteLiveRecordVodConfigRequest,
    ) -> live_20161101_models.DeleteLiveRecordVodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_record_vod_config_with_options_async(request, runtime)

    def delete_live_snapshot_detect_porn_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_snapshot_detect_porn_config(
        self,
        request: live_20161101_models.DeleteLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_detect_porn_config_with_options(request, runtime)

    async def delete_live_snapshot_detect_porn_config_async(
        self,
        request: live_20161101_models.DeleteLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_snapshot_detect_porn_config_with_options_async(request, runtime)

    def delete_live_specific_staging_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSpecificStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_specific_staging_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveSpecificStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveSpecificStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSpecificStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSpecificStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_specific_staging_config(
        self,
        request: live_20161101_models.DeleteLiveSpecificStagingConfigRequest,
    ) -> live_20161101_models.DeleteLiveSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_specific_staging_config_with_options(request, runtime)

    async def delete_live_specific_staging_config_async(
        self,
        request: live_20161101_models.DeleteLiveSpecificStagingConfigRequest,
    ) -> live_20161101_models.DeleteLiveSpecificStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_specific_staging_config_with_options_async(request, runtime)

    def delete_live_stream_monitor_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_stream_monitor_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_stream_monitor(
        self,
        request: live_20161101_models.DeleteLiveStreamMonitorRequest,
    ) -> live_20161101_models.DeleteLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_monitor_with_options(request, runtime)

    async def delete_live_stream_monitor_async(
        self,
        request: live_20161101_models.DeleteLiveStreamMonitorRequest,
    ) -> live_20161101_models.DeleteLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_stream_monitor_with_options_async(request, runtime)

    def delete_live_stream_record_index_files_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_stream_record_index_files_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_stream_record_index_files(
        self,
        request: live_20161101_models.DeleteLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_record_index_files_with_options(request, runtime)

    async def delete_live_stream_record_index_files_async(
        self,
        request: live_20161101_models.DeleteLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_stream_record_index_files_with_options_async(request, runtime)

    def delete_live_stream_transcode_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamTranscodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_stream_transcode(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_transcode_with_options(request, runtime)

    async def delete_live_stream_transcode_async(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_stream_transcode_with_options_async(request, runtime)

    def delete_live_stream_watermark_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_stream_watermark_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_stream_watermark(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRequest,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_watermark_with_options(request, runtime)

    async def delete_live_stream_watermark_async(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRequest,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_stream_watermark_with_options_async(request, runtime)

    def delete_live_stream_watermark_rule_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_stream_watermark_rule_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_stream_watermark_rule(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_watermark_rule_with_options(request, runtime)

    async def delete_live_stream_watermark_rule_async(
        self,
        request: live_20161101_models.DeleteLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.DeleteLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_stream_watermark_rule_with_options_async(request, runtime)

    def delete_live_streams_notify_url_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_streams_notify_url_config(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_streams_notify_url_config_with_options(request, runtime)

    async def delete_live_streams_notify_url_config_async(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_streams_notify_url_config_with_options_async(request, runtime)

    def delete_message_app_with_options(
        self,
        request: live_20161101_models.DeleteMessageAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMessageAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMessageApp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMessageAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_app_with_options_async(
        self,
        request: live_20161101_models.DeleteMessageAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMessageAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMessageApp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMessageAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_app(
        self,
        request: live_20161101_models.DeleteMessageAppRequest,
    ) -> live_20161101_models.DeleteMessageAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_message_app_with_options(request, runtime)

    async def delete_message_app_async(
        self,
        request: live_20161101_models.DeleteMessageAppRequest,
    ) -> live_20161101_models.DeleteMessageAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_app_with_options_async(request, runtime)

    def delete_mix_stream_with_options(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mix_stream_with_options_async(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMixStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mix_stream(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mix_stream_with_options(request, runtime)

    async def delete_mix_stream_async(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mix_stream_with_options_async(request, runtime)

    def delete_multi_rate_config_with_options(
        self,
        request: live_20161101_models.DeleteMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.DeleteMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMultiRateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multi_rate_config(
        self,
        request: live_20161101_models.DeleteMultiRateConfigRequest,
    ) -> live_20161101_models.DeleteMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_multi_rate_config_with_options(request, runtime)

    async def delete_multi_rate_config_async(
        self,
        request: live_20161101_models.DeleteMultiRateConfigRequest,
    ) -> live_20161101_models.DeleteMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_multi_rate_config_with_options_async(request, runtime)

    def delete_playlist_with_options(
        self,
        request: live_20161101_models.DeletePlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_playlist_with_options_async(
        self,
        request: live_20161101_models.DeletePlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_playlist(
        self,
        request: live_20161101_models.DeletePlaylistRequest,
    ) -> live_20161101_models.DeletePlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_playlist_with_options(request, runtime)

    async def delete_playlist_async(
        self,
        request: live_20161101_models.DeletePlaylistRequest,
    ) -> live_20161101_models.DeletePlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_playlist_with_options_async(request, runtime)

    def delete_playlist_items_with_options(
        self,
        request: live_20161101_models.DeletePlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_playlist_items_with_options_async(
        self,
        request: live_20161101_models.DeletePlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_playlist_items(
        self,
        request: live_20161101_models.DeletePlaylistItemsRequest,
    ) -> live_20161101_models.DeletePlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_playlist_items_with_options(request, runtime)

    async def delete_playlist_items_async(
        self,
        request: live_20161101_models.DeletePlaylistItemsRequest,
    ) -> live_20161101_models.DeletePlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_playlist_items_with_options_async(request, runtime)

    def delete_room_with_options(
        self,
        request: live_20161101_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_room_with_options_async(
        self,
        request: live_20161101_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_room(
        self,
        request: live_20161101_models.DeleteRoomRequest,
    ) -> live_20161101_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    async def delete_room_async(
        self,
        request: live_20161101_models.DeleteRoomRequest,
    ) -> live_20161101_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_room_with_options_async(request, runtime)

    def delete_snapshot_callback_auth_with_options(
        self,
        request: live_20161101_models.DeleteSnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteSnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_callback_auth_with_options_async(
        self,
        request: live_20161101_models.DeleteSnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteSnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotCallbackAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot_callback_auth(
        self,
        request: live_20161101_models.DeleteSnapshotCallbackAuthRequest,
    ) -> live_20161101_models.DeleteSnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_callback_auth_with_options(request, runtime)

    async def delete_snapshot_callback_auth_async(
        self,
        request: live_20161101_models.DeleteSnapshotCallbackAuthRequest,
    ) -> live_20161101_models.DeleteSnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_callback_auth_with_options_async(request, runtime)

    def delete_snapshot_files_with_options(
        self,
        request: live_20161101_models.DeleteSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteSnapshotFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.create_timestamp_list):
            query['CreateTimestampList'] = request.create_timestamp_list
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_files_with_options_async(
        self,
        request: live_20161101_models.DeleteSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteSnapshotFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.create_timestamp_list):
            query['CreateTimestampList'] = request.create_timestamp_list
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot_files(
        self,
        request: live_20161101_models.DeleteSnapshotFilesRequest,
    ) -> live_20161101_models.DeleteSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_files_with_options(request, runtime)

    async def delete_snapshot_files_async(
        self,
        request: live_20161101_models.DeleteSnapshotFilesRequest,
    ) -> live_20161101_models.DeleteSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_files_with_options_async(request, runtime)

    def delete_studio_layout_with_options(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_studio_layout_with_options_async(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteStudioLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_studio_layout(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_studio_layout_with_options(request, runtime)

    async def delete_studio_layout_async(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_studio_layout_with_options_async(request, runtime)

    def describe_auto_show_list_tasks_with_options(
        self,
        request: live_20161101_models.DescribeAutoShowListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeAutoShowListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoShowListTasks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeAutoShowListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_show_list_tasks_with_options_async(
        self,
        request: live_20161101_models.DescribeAutoShowListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeAutoShowListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoShowListTasks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeAutoShowListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_show_list_tasks(
        self,
        request: live_20161101_models.DescribeAutoShowListTasksRequest,
    ) -> live_20161101_models.DescribeAutoShowListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_show_list_tasks_with_options(request, runtime)

    async def describe_auto_show_list_tasks_async(
        self,
        request: live_20161101_models.DescribeAutoShowListTasksRequest,
    ) -> live_20161101_models.DescribeAutoShowListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_show_list_tasks_with_options_async(request, runtime)

    def describe_caster_channels_with_options(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterChannels',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_channels_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterChannels',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_channels(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_channels_with_options(request, runtime)

    async def describe_caster_channels_async(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_channels_with_options_async(request, runtime)

    def describe_caster_components_with_options(
        self,
        request: live_20161101_models.DescribeCasterComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterComponents',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_components_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterComponents',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_components(
        self,
        request: live_20161101_models.DescribeCasterComponentsRequest,
    ) -> live_20161101_models.DescribeCasterComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_components_with_options(request, runtime)

    async def describe_caster_components_async(
        self,
        request: live_20161101_models.DescribeCasterComponentsRequest,
    ) -> live_20161101_models.DescribeCasterComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_components_with_options_async(request, runtime)

    def describe_caster_config_with_options(
        self,
        request: live_20161101_models.DescribeCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_config_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_config(
        self,
        request: live_20161101_models.DescribeCasterConfigRequest,
    ) -> live_20161101_models.DescribeCasterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_config_with_options(request, runtime)

    async def describe_caster_config_async(
        self,
        request: live_20161101_models.DescribeCasterConfigRequest,
    ) -> live_20161101_models.DescribeCasterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_config_with_options_async(request, runtime)

    def describe_caster_layouts_with_options(
        self,
        request: live_20161101_models.DescribeCasterLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterLayoutsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_layouts_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterLayoutsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterLayoutsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_layouts(
        self,
        request: live_20161101_models.DescribeCasterLayoutsRequest,
    ) -> live_20161101_models.DescribeCasterLayoutsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_layouts_with_options(request, runtime)

    async def describe_caster_layouts_async(
        self,
        request: live_20161101_models.DescribeCasterLayoutsRequest,
    ) -> live_20161101_models.DescribeCasterLayoutsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_layouts_with_options_async(request, runtime)

    def describe_caster_program_with_options(
        self,
        request: live_20161101_models.DescribeCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_program_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_program(
        self,
        request: live_20161101_models.DescribeCasterProgramRequest,
    ) -> live_20161101_models.DescribeCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_program_with_options(request, runtime)

    async def describe_caster_program_async(
        self,
        request: live_20161101_models.DescribeCasterProgramRequest,
    ) -> live_20161101_models.DescribeCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_program_with_options_async(request, runtime)

    def describe_caster_scene_audio_with_options(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSceneAudioResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_scene_audio_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSceneAudioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_scene_audio(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scene_audio_with_options(request, runtime)

    async def describe_caster_scene_audio_async(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_scene_audio_with_options_async(request, runtime)

    def describe_caster_scenes_with_options(
        self,
        request: live_20161101_models.DescribeCasterScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterScenes',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_scenes_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterScenesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterScenes',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_scenes(
        self,
        request: live_20161101_models.DescribeCasterScenesRequest,
    ) -> live_20161101_models.DescribeCasterScenesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scenes_with_options(request, runtime)

    async def describe_caster_scenes_async(
        self,
        request: live_20161101_models.DescribeCasterScenesRequest,
    ) -> live_20161101_models.DescribeCasterScenesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_scenes_with_options_async(request, runtime)

    def describe_caster_stream_url_with_options(
        self,
        request: live_20161101_models.DescribeCasterStreamUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterStreamUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterStreamUrl',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterStreamUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_stream_url_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterStreamUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterStreamUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterStreamUrl',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterStreamUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_stream_url(
        self,
        request: live_20161101_models.DescribeCasterStreamUrlRequest,
    ) -> live_20161101_models.DescribeCasterStreamUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_stream_url_with_options(request, runtime)

    async def describe_caster_stream_url_async(
        self,
        request: live_20161101_models.DescribeCasterStreamUrlRequest,
    ) -> live_20161101_models.DescribeCasterStreamUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_stream_url_with_options_async(request, runtime)

    def describe_caster_sync_group_with_options(
        self,
        request: live_20161101_models.DescribeCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSyncGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_sync_group_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSyncGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_sync_group(
        self,
        request: live_20161101_models.DescribeCasterSyncGroupRequest,
    ) -> live_20161101_models.DescribeCasterSyncGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_sync_group_with_options(request, runtime)

    async def describe_caster_sync_group_async(
        self,
        request: live_20161101_models.DescribeCasterSyncGroupRequest,
    ) -> live_20161101_models.DescribeCasterSyncGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_sync_group_with_options_async(request, runtime)

    def describe_caster_video_resources_with_options(
        self,
        request: live_20161101_models.DescribeCasterVideoResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterVideoResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterVideoResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterVideoResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_caster_video_resources_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterVideoResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterVideoResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterVideoResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterVideoResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_caster_video_resources(
        self,
        request: live_20161101_models.DescribeCasterVideoResourcesRequest,
    ) -> live_20161101_models.DescribeCasterVideoResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_video_resources_with_options(request, runtime)

    async def describe_caster_video_resources_async(
        self,
        request: live_20161101_models.DescribeCasterVideoResourcesRequest,
    ) -> live_20161101_models.DescribeCasterVideoResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_video_resources_with_options_async(request, runtime)

    def describe_casters_with_options(
        self,
        request: live_20161101_models.DescribeCastersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCastersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.order_by_modify_asc):
            query['OrderByModifyAsc'] = request.order_by_modify_asc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasters',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCastersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_casters_with_options_async(
        self,
        request: live_20161101_models.DescribeCastersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCastersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.order_by_modify_asc):
            query['OrderByModifyAsc'] = request.order_by_modify_asc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasters',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCastersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_casters(
        self,
        request: live_20161101_models.DescribeCastersRequest,
    ) -> live_20161101_models.DescribeCastersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_casters_with_options(request, runtime)

    async def describe_casters_async(
        self,
        request: live_20161101_models.DescribeCastersRequest,
    ) -> live_20161101_models.DescribeCastersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_casters_with_options_async(request, runtime)

    def describe_domain_usage_data_with_options(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_usage_data_with_options_async(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_usage_data(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    async def describe_domain_usage_data_async(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_usage_data_with_options_async(request, runtime)

    def describe_domain_with_integrity_with_options(
        self,
        request: live_20161101_models.DescribeDomainWithIntegrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainWithIntegrityResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainWithIntegrity',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainWithIntegrityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_integrity_with_options_async(
        self,
        request: live_20161101_models.DescribeDomainWithIntegrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainWithIntegrityResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainWithIntegrity',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainWithIntegrityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_with_integrity(
        self,
        request: live_20161101_models.DescribeDomainWithIntegrityRequest,
    ) -> live_20161101_models.DescribeDomainWithIntegrityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_integrity_with_options(request, runtime)

    async def describe_domain_with_integrity_async(
        self,
        request: live_20161101_models.DescribeDomainWithIntegrityRequest,
    ) -> live_20161101_models.DescribeDomainWithIntegrityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_integrity_with_options_async(request, runtime)

    def describe_forbid_push_stream_room_list_with_options(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
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
            action='DescribeForbidPushStreamRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeForbidPushStreamRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_forbid_push_stream_room_list_with_options_async(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
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
            action='DescribeForbidPushStreamRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeForbidPushStreamRoomListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_forbid_push_stream_room_list(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_forbid_push_stream_room_list_with_options(request, runtime)

    async def describe_forbid_push_stream_room_list_async(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_forbid_push_stream_room_list_with_options_async(request, runtime)

    def describe_hls_live_stream_real_time_bps_data_with_options(
        self,
        request: live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHlsLiveStreamRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hls_live_stream_real_time_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHlsLiveStreamRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hls_live_stream_real_time_bps_data(
        self,
        request: live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataRequest,
    ) -> live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hls_live_stream_real_time_bps_data_with_options(request, runtime)

    async def describe_hls_live_stream_real_time_bps_data_async(
        self,
        request: live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataRequest,
    ) -> live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hls_live_stream_real_time_bps_data_with_options_async(request, runtime)

    def describe_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_audio_audit_config(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_config_with_options(request, runtime)

    async def describe_live_audio_audit_config_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_audio_audit_config_with_options_async(request, runtime)

    def describe_live_audio_audit_notify_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_audio_audit_notify_config(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_notify_config_with_options(request, runtime)

    async def describe_live_audio_audit_notify_config_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_audio_audit_notify_config_with_options_async(request, runtime)

    def describe_live_certificate_detail_with_options(
        self,
        request: live_20161101_models.DescribeLiveCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_certificate_detail_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_certificate_detail(
        self,
        request: live_20161101_models.DescribeLiveCertificateDetailRequest,
    ) -> live_20161101_models.DescribeLiveCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_detail_with_options(request, runtime)

    async def describe_live_certificate_detail_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateDetailRequest,
    ) -> live_20161101_models.DescribeLiveCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_certificate_detail_with_options_async(request, runtime)

    def describe_live_certificate_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_certificate_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_certificate_list(
        self,
        request: live_20161101_models.DescribeLiveCertificateListRequest,
    ) -> live_20161101_models.DescribeLiveCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_list_with_options(request, runtime)

    async def describe_live_certificate_list_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateListRequest,
    ) -> live_20161101_models.DescribeLiveCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_certificate_list_with_options_async(request, runtime)

    def describe_live_detect_notify_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_detect_notify_config(
        self,
        request: live_20161101_models.DescribeLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_notify_config_with_options(request, runtime)

    async def describe_live_detect_notify_config_async(
        self,
        request: live_20161101_models.DescribeLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_detect_notify_config_with_options_async(request, runtime)

    def describe_live_detect_porn_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDetectPornDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectPornDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fee):
            query['Fee'] = request.fee
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectPornData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectPornDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_detect_porn_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDetectPornDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectPornDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fee):
            query['Fee'] = request.fee
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectPornData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectPornDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_detect_porn_data(
        self,
        request: live_20161101_models.DescribeLiveDetectPornDataRequest,
    ) -> live_20161101_models.DescribeLiveDetectPornDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_porn_data_with_options(request, runtime)

    async def describe_live_detect_porn_data_async(
        self,
        request: live_20161101_models.DescribeLiveDetectPornDataRequest,
    ) -> live_20161101_models.DescribeLiveDetectPornDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_detect_porn_data_with_options_async(request, runtime)

    def describe_live_domain_bps_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_bps_data(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_with_options(request, runtime)

    async def describe_live_domain_bps_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_bps_data_with_options_async(request, runtime)

    def describe_live_domain_bps_data_by_layer_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByLayer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_bps_data_by_layer_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByLayerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByLayer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_bps_data_by_layer(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByLayerRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_live_domain_bps_data_by_layer_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByLayerRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_live_domain_bps_data_by_time_stamp_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByTimeStamp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByTimeStamp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_bps_data_by_time_stamp(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_by_time_stamp_with_options(request, runtime)

    async def describe_live_domain_bps_data_by_time_stamp_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_bps_data_by_time_stamp_with_options_async(request, runtime)

    def describe_live_domain_certificate_info_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainCertificateInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_certificate_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainCertificateInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_certificate_info(
        self,
        request: live_20161101_models.DescribeLiveDomainCertificateInfoRequest,
    ) -> live_20161101_models.DescribeLiveDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_certificate_info_with_options(request, runtime)

    async def describe_live_domain_certificate_info_async(
        self,
        request: live_20161101_models.DescribeLiveDomainCertificateInfoRequest,
    ) -> live_20161101_models.DescribeLiveDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_certificate_info_with_options_async(request, runtime)

    def describe_live_domain_configs_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_configs(
        self,
        request: live_20161101_models.DescribeLiveDomainConfigsRequest,
    ) -> live_20161101_models.DescribeLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_configs_with_options(request, runtime)

    async def describe_live_domain_configs_async(
        self,
        request: live_20161101_models.DescribeLiveDomainConfigsRequest,
    ) -> live_20161101_models.DescribeLiveDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_configs_with_options_async(request, runtime)

    def describe_live_domain_detail_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_detail_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_detail(
        self,
        request: live_20161101_models.DescribeLiveDomainDetailRequest,
    ) -> live_20161101_models.DescribeLiveDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_detail_with_options(request, runtime)

    async def describe_live_domain_detail_async(
        self,
        request: live_20161101_models.DescribeLiveDomainDetailRequest,
    ) -> live_20161101_models.DescribeLiveDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_detail_with_options_async(request, runtime)

    def describe_live_domain_frame_rate_and_bit_rate_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainFrameRateAndBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_frame_rate_and_bit_rate_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainFrameRateAndBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_frame_rate_and_bit_rate_data(
        self,
        request: live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_frame_rate_and_bit_rate_data_with_options(request, runtime)

    async def describe_live_domain_frame_rate_and_bit_rate_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_frame_rate_and_bit_rate_data_with_options_async(request, runtime)

    def describe_live_domain_limit_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLimit',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_limit_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLimit',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_limit(
        self,
        request: live_20161101_models.DescribeLiveDomainLimitRequest,
    ) -> live_20161101_models.DescribeLiveDomainLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_limit_with_options(request, runtime)

    async def describe_live_domain_limit_async(
        self,
        request: live_20161101_models.DescribeLiveDomainLimitRequest,
    ) -> live_20161101_models.DescribeLiveDomainLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_limit_with_options_async(request, runtime)

    def describe_live_domain_log_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLog',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_log_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLog',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_log(
        self,
        request: live_20161101_models.DescribeLiveDomainLogRequest,
    ) -> live_20161101_models.DescribeLiveDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_log_with_options(request, runtime)

    async def describe_live_domain_log_async(
        self,
        request: live_20161101_models.DescribeLiveDomainLogRequest,
    ) -> live_20161101_models.DescribeLiveDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_log_with_options_async(request, runtime)

    def describe_live_domain_mapping_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_mapping(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_mapping_with_options(request, runtime)

    async def describe_live_domain_mapping_async(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_mapping_with_options_async(request, runtime)

    def describe_live_domain_online_user_num_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainOnlineUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainOnlineUserNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainOnlineUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainOnlineUserNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_online_user_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainOnlineUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainOnlineUserNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainOnlineUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainOnlineUserNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_online_user_num(
        self,
        request: live_20161101_models.DescribeLiveDomainOnlineUserNumRequest,
    ) -> live_20161101_models.DescribeLiveDomainOnlineUserNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_online_user_num_with_options(request, runtime)

    async def describe_live_domain_online_user_num_async(
        self,
        request: live_20161101_models.DescribeLiveDomainOnlineUserNumRequest,
    ) -> live_20161101_models.DescribeLiveDomainOnlineUserNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_online_user_num_with_options_async(request, runtime)

    def describe_live_domain_push_bps_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainPushBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_push_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_push_bps_data(
        self,
        request: live_20161101_models.DescribeLiveDomainPushBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPushBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_bps_data_with_options(request, runtime)

    async def describe_live_domain_push_bps_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPushBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_push_bps_data_with_options_async(request, runtime)

    def describe_live_domain_push_traffic_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainPushTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_push_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_push_traffic_data(
        self,
        request: live_20161101_models.DescribeLiveDomainPushTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPushTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_traffic_data_with_options(request, runtime)

    async def describe_live_domain_push_traffic_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPushTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_push_traffic_data_with_options_async(request, runtime)

    def describe_live_domain_pv_uv_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainPvUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPvUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPvUvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPvUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_pv_uv_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPvUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPvUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPvUvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPvUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_pv_uv_data(
        self,
        request: live_20161101_models.DescribeLiveDomainPvUvDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPvUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_pv_uv_data_with_options(request, runtime)

    async def describe_live_domain_pv_uv_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPvUvDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainPvUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_pv_uv_data_with_options_async(request, runtime)

    def describe_live_domain_real_time_bps_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_real_time_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_real_time_bps_data(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_live_domain_real_time_bps_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeBpsDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_live_domain_real_time_http_code_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeHttpCodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_real_time_http_code_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeHttpCodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_real_time_http_code_data(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_live_domain_real_time_http_code_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_live_domain_real_time_traffic_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_real_time_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_real_time_traffic_data(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_live_domain_real_time_traffic_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_live_domain_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_realtime_log_delivery(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_realtime_log_delivery_with_options(request, runtime)

    async def describe_live_domain_realtime_log_delivery_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_realtime_log_delivery_with_options_async(request, runtime)

    def describe_live_domain_record_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_record_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_record_data(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_record_data_with_options(request, runtime)

    async def describe_live_domain_record_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_record_data_with_options_async(request, runtime)

    def describe_live_domain_record_usage_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_record_usage_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_record_usage_data(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRecordUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_record_usage_data_with_options(request, runtime)

    async def describe_live_domain_record_usage_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainRecordUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_record_usage_data_with_options_async(request, runtime)

    def describe_live_domain_snapshot_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainSnapshotData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainSnapshotDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_snapshot_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainSnapshotData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainSnapshotDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_snapshot_data(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_snapshot_data_with_options(request, runtime)

    async def describe_live_domain_snapshot_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_snapshot_data_with_options_async(request, runtime)

    def describe_live_domain_staging_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_staging_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_staging_config(
        self,
        request: live_20161101_models.DescribeLiveDomainStagingConfigRequest,
    ) -> live_20161101_models.DescribeLiveDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_staging_config_with_options(request, runtime)

    async def describe_live_domain_staging_config_async(
        self,
        request: live_20161101_models.DescribeLiveDomainStagingConfigRequest,
    ) -> live_20161101_models.DescribeLiveDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_staging_config_with_options_async(request, runtime)

    def describe_live_domain_stream_transcode_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split):
            query['Split'] = request.split
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStreamTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_stream_transcode_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split):
            query['Split'] = request.split
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStreamTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_stream_transcode_data(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_stream_transcode_data_with_options(request, runtime)

    async def describe_live_domain_stream_transcode_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_stream_transcode_data_with_options_async(request, runtime)

    def describe_live_domain_time_shift_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainTimeShiftDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTimeShiftDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTimeShiftData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTimeShiftDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_time_shift_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTimeShiftDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTimeShiftDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTimeShiftData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTimeShiftDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_time_shift_data(
        self,
        request: live_20161101_models.DescribeLiveDomainTimeShiftDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTimeShiftDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_time_shift_data_with_options(request, runtime)

    async def describe_live_domain_time_shift_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTimeShiftDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTimeShiftDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_time_shift_data_with_options_async(request, runtime)

    def describe_live_domain_traffic_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_traffic_data(
        self,
        request: live_20161101_models.DescribeLiveDomainTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_traffic_data_with_options(request, runtime)

    async def describe_live_domain_traffic_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTrafficDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_traffic_data_with_options_async(request, runtime)

    def describe_live_domain_transcode_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTranscodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_domain_transcode_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTranscodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTranscodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_domain_transcode_data(
        self,
        request: live_20161101_models.DescribeLiveDomainTranscodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_transcode_data_with_options(request, runtime)

    async def describe_live_domain_transcode_data_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTranscodeDataRequest,
    ) -> live_20161101_models.DescribeLiveDomainTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_domain_transcode_data_with_options_async(request, runtime)

    def describe_live_drm_usage_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDrmUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDrmUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDrmUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDrmUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_drm_usage_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDrmUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDrmUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDrmUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDrmUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_drm_usage_data(
        self,
        request: live_20161101_models.DescribeLiveDrmUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveDrmUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_drm_usage_data_with_options(request, runtime)

    async def describe_live_drm_usage_data_async(
        self,
        request: live_20161101_models.DescribeLiveDrmUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveDrmUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_drm_usage_data_with_options_async(request, runtime)

    def describe_live_edge_transfer_with_options(
        self,
        request: live_20161101_models.DescribeLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_edge_transfer_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveEdgeTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_edge_transfer(
        self,
        request: live_20161101_models.DescribeLiveEdgeTransferRequest,
    ) -> live_20161101_models.DescribeLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_edge_transfer_with_options(request, runtime)

    async def describe_live_edge_transfer_async(
        self,
        request: live_20161101_models.DescribeLiveEdgeTransferRequest,
    ) -> live_20161101_models.DescribeLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_edge_transfer_with_options_async(request, runtime)

    def describe_live_lazy_pull_stream_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveLazyPullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveLazyPullStreamConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_lazy_pull_stream_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveLazyPullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveLazyPullStreamConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_lazy_pull_stream_config(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_lazy_pull_stream_config_with_options(request, runtime)

    async def describe_live_lazy_pull_stream_config_async(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_lazy_pull_stream_config_with_options_async(request, runtime)

    def describe_live_producer_usage_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveProducerUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveProducerUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.app):
            query['app'] = request.app
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveProducerUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveProducerUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_producer_usage_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveProducerUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveProducerUsageDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.app):
            query['app'] = request.app
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveProducerUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveProducerUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_producer_usage_data(
        self,
        request: live_20161101_models.DescribeLiveProducerUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveProducerUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_producer_usage_data_with_options(request, runtime)

    async def describe_live_producer_usage_data_async(
        self,
        request: live_20161101_models.DescribeLiveProducerUsageDataRequest,
    ) -> live_20161101_models.DescribeLiveProducerUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_producer_usage_data_with_options_async(request, runtime)

    def describe_live_pull_stream_config_with_options(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLivePullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLivePullStreamConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_pull_stream_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLivePullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLivePullStreamConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_pull_stream_config(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_pull_stream_config_with_options(request, runtime)

    async def describe_live_pull_stream_config_async(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_pull_stream_config_with_options_async(request, runtime)

    def describe_live_realtime_delivery_acc_with_options(
        self,
        request: live_20161101_models.DescribeLiveRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeDeliveryAcc',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_realtime_delivery_acc_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeDeliveryAcc',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_realtime_delivery_acc(
        self,
        request: live_20161101_models.DescribeLiveRealtimeDeliveryAccRequest,
    ) -> live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_delivery_acc_with_options(request, runtime)

    async def describe_live_realtime_delivery_acc_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeDeliveryAccRequest,
    ) -> live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_realtime_delivery_acc_with_options_async(request, runtime)

    def describe_live_realtime_log_authorized_with_options(
        self,
        request: live_20161101_models.DescribeLiveRealtimeLogAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeLogAuthorized',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_realtime_log_authorized_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeLogAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeLogAuthorized',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_realtime_log_authorized(
        self,
        request: live_20161101_models.DescribeLiveRealtimeLogAuthorizedRequest,
    ) -> live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_log_authorized_with_options(request, runtime)

    async def describe_live_realtime_log_authorized_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeLogAuthorizedRequest,
    ) -> live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_realtime_log_authorized_with_options_async(request, runtime)

    def describe_live_record_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_record_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_record_config(
        self,
        request: live_20161101_models.DescribeLiveRecordConfigRequest,
    ) -> live_20161101_models.DescribeLiveRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_config_with_options(request, runtime)

    async def describe_live_record_config_async(
        self,
        request: live_20161101_models.DescribeLiveRecordConfigRequest,
    ) -> live_20161101_models.DescribeLiveRecordConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_record_config_with_options_async(request, runtime)

    def describe_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_record_notify_config(
        self,
        request: live_20161101_models.DescribeLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_notify_config_with_options(request, runtime)

    async def describe_live_record_notify_config_async(
        self,
        request: live_20161101_models.DescribeLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.DescribeLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_record_notify_config_with_options_async(request, runtime)

    def describe_live_record_vod_configs_with_options(
        self,
        request: live_20161101_models.DescribeLiveRecordVodConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordVodConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordVodConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordVodConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_record_vod_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordVodConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordVodConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordVodConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordVodConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_record_vod_configs(
        self,
        request: live_20161101_models.DescribeLiveRecordVodConfigsRequest,
    ) -> live_20161101_models.DescribeLiveRecordVodConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_vod_configs_with_options(request, runtime)

    async def describe_live_record_vod_configs_async(
        self,
        request: live_20161101_models.DescribeLiveRecordVodConfigsRequest,
    ) -> live_20161101_models.DescribeLiveRecordVodConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_record_vod_configs_with_options_async(request, runtime)

    def describe_live_shift_configs_with_options(
        self,
        request: live_20161101_models.DescribeLiveShiftConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveShiftConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveShiftConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveShiftConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_shift_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveShiftConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveShiftConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveShiftConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveShiftConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_shift_configs(
        self,
        request: live_20161101_models.DescribeLiveShiftConfigsRequest,
    ) -> live_20161101_models.DescribeLiveShiftConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_shift_configs_with_options(request, runtime)

    async def describe_live_shift_configs_async(
        self,
        request: live_20161101_models.DescribeLiveShiftConfigsRequest,
    ) -> live_20161101_models.DescribeLiveShiftConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_shift_configs_with_options_async(request, runtime)

    def describe_live_snapshot_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_snapshot_config(
        self,
        request: live_20161101_models.DescribeLiveSnapshotConfigRequest,
    ) -> live_20161101_models.DescribeLiveSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_config_with_options(request, runtime)

    async def describe_live_snapshot_config_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotConfigRequest,
    ) -> live_20161101_models.DescribeLiveSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_snapshot_config_with_options_async(request, runtime)

    def describe_live_snapshot_detect_porn_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_snapshot_detect_porn_config(
        self,
        request: live_20161101_models.DescribeLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_detect_porn_config_with_options(request, runtime)

    async def describe_live_snapshot_detect_porn_config_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_snapshot_detect_porn_config_with_options_async(request, runtime)

    def describe_live_stream_bit_rate_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamBitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamBitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_bit_rate_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamBitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamBitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_bit_rate_data(
        self,
        request: live_20161101_models.DescribeLiveStreamBitRateDataRequest,
    ) -> live_20161101_models.DescribeLiveStreamBitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_bit_rate_data_with_options(request, runtime)

    async def describe_live_stream_bit_rate_data_async(
        self,
        request: live_20161101_models.DescribeLiveStreamBitRateDataRequest,
    ) -> live_20161101_models.DescribeLiveStreamBitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_bit_rate_data_with_options_async(request, runtime)

    def describe_live_stream_count_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamCount',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_count_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamCount',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_count(
        self,
        request: live_20161101_models.DescribeLiveStreamCountRequest,
    ) -> live_20161101_models.DescribeLiveStreamCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_count_with_options(request, runtime)

    async def describe_live_stream_count_async(
        self,
        request: live_20161101_models.DescribeLiveStreamCountRequest,
    ) -> live_20161101_models.DescribeLiveStreamCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_count_with_options_async(request, runtime)

    def describe_live_stream_delay_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamDelayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_delay_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamDelayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_delay_config(
        self,
        request: live_20161101_models.DescribeLiveStreamDelayConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamDelayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_delay_config_with_options(request, runtime)

    async def describe_live_stream_delay_config_async(
        self,
        request: live_20161101_models.DescribeLiveStreamDelayConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamDelayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_delay_config_with_options_async(request, runtime)

    def describe_live_stream_history_user_num_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamHistoryUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamHistoryUserNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamHistoryUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamHistoryUserNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_history_user_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamHistoryUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamHistoryUserNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamHistoryUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamHistoryUserNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_history_user_num(
        self,
        request: live_20161101_models.DescribeLiveStreamHistoryUserNumRequest,
    ) -> live_20161101_models.DescribeLiveStreamHistoryUserNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_history_user_num_with_options(request, runtime)

    async def describe_live_stream_history_user_num_async(
        self,
        request: live_20161101_models.DescribeLiveStreamHistoryUserNumRequest,
    ) -> live_20161101_models.DescribeLiveStreamHistoryUserNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_history_user_num_with_options_async(request, runtime)

    def describe_live_stream_metric_detail_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamMetricDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamMetricDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamMetricDetailData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMetricDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_metric_detail_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamMetricDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamMetricDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamMetricDetailData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMetricDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_metric_detail_data(
        self,
        request: live_20161101_models.DescribeLiveStreamMetricDetailDataRequest,
    ) -> live_20161101_models.DescribeLiveStreamMetricDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_metric_detail_data_with_options(request, runtime)

    async def describe_live_stream_metric_detail_data_async(
        self,
        request: live_20161101_models.DescribeLiveStreamMetricDetailDataRequest,
    ) -> live_20161101_models.DescribeLiveStreamMetricDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_metric_detail_data_with_options_async(request, runtime)

    def describe_live_stream_monitor_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.order_rule):
            query['OrderRule'] = request.order_rule
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
            action='DescribeLiveStreamMonitorList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_monitor_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.order_rule):
            query['OrderRule'] = request.order_rule
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
            action='DescribeLiveStreamMonitorList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_monitor_list(
        self,
        request: live_20161101_models.DescribeLiveStreamMonitorListRequest,
    ) -> live_20161101_models.DescribeLiveStreamMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_monitor_list_with_options(request, runtime)

    async def describe_live_stream_monitor_list_async(
        self,
        request: live_20161101_models.DescribeLiveStreamMonitorListRequest,
    ) -> live_20161101_models.DescribeLiveStreamMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_monitor_list_with_options_async(request, runtime)

    def describe_live_stream_optimized_feature_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_optimized_feature_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_optimized_feature_config(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_optimized_feature_config_with_options(request, runtime)

    async def describe_live_stream_optimized_feature_config_async(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_optimized_feature_config_with_options_async(request, runtime)

    def describe_live_stream_record_content_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_record_content_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_record_content(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordContentRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_content_with_options(request, runtime)

    async def describe_live_stream_record_content_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordContentRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_record_content_with_options_async(request, runtime)

    def describe_live_stream_record_index_file_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFile',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_record_index_file_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFile',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_record_index_file(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFileRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_file_with_options(request, runtime)

    async def describe_live_stream_record_index_file_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFileRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_record_index_file_with_options_async(request, runtime)

    def describe_live_stream_record_index_files_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_record_index_files_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_record_index_files(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_files_with_options(request, runtime)

    async def describe_live_stream_record_index_files_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFilesRequest,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_record_index_files_with_options_async(request, runtime)

    def describe_live_stream_snapshot_info_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamSnapshotInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamSnapshotInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_snapshot_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamSnapshotInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamSnapshotInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_snapshot_info(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_snapshot_info_with_options(request, runtime)

    async def describe_live_stream_snapshot_info_async(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_snapshot_info_with_options_async(request, runtime)

    def describe_live_stream_state_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamState',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_state_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamState',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_state(
        self,
        request: live_20161101_models.DescribeLiveStreamStateRequest,
    ) -> live_20161101_models.DescribeLiveStreamStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_state_with_options(request, runtime)

    async def describe_live_stream_state_async(
        self,
        request: live_20161101_models.DescribeLiveStreamStateRequest,
    ) -> live_20161101_models.DescribeLiveStreamStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_state_with_options_async(request, runtime)

    def describe_live_stream_transcode_info_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_transcode_name):
            query['DomainTranscodeName'] = request.domain_transcode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_transcode_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_transcode_name):
            query['DomainTranscodeName'] = request.domain_transcode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_transcode_info(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_info_with_options(request, runtime)

    async def describe_live_stream_transcode_info_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_transcode_info_with_options_async(request, runtime)

    def describe_live_stream_transcode_stream_num_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeStreamNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeStreamNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_transcode_stream_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeStreamNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeStreamNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_transcode_stream_num(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeStreamNumRequest,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_stream_num_with_options(request, runtime)

    async def describe_live_stream_transcode_stream_num_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeStreamNumRequest,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_transcode_stream_num_with_options_async(request, runtime)

    def describe_live_stream_watermark_rules_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamWatermarkRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarkRules',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_watermark_rules_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarkRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamWatermarkRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarkRules',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarkRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_watermark_rules(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarkRulesRequest,
    ) -> live_20161101_models.DescribeLiveStreamWatermarkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_watermark_rules_with_options(request, runtime)

    async def describe_live_stream_watermark_rules_async(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarkRulesRequest,
    ) -> live_20161101_models.DescribeLiveStreamWatermarkRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_watermark_rules_with_options_async(request, runtime)

    def describe_live_stream_watermarks_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamWatermarksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_stream_watermarks_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamWatermarksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_stream_watermarks(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarksRequest,
    ) -> live_20161101_models.DescribeLiveStreamWatermarksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_watermarks_with_options(request, runtime)

    async def describe_live_stream_watermarks_async(
        self,
        request: live_20161101_models.DescribeLiveStreamWatermarksRequest,
    ) -> live_20161101_models.DescribeLiveStreamWatermarksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_stream_watermarks_with_options_async(request, runtime)

    def describe_live_streams_block_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsBlockList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_streams_block_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsBlockList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsBlockListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_streams_block_list(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_block_list_with_options(request, runtime)

    async def describe_live_streams_block_list_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_streams_block_list_with_options_async(request, runtime)

    def describe_live_streams_control_history_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsControlHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsControlHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsControlHistory',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsControlHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_streams_control_history_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsControlHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsControlHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsControlHistory',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsControlHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_streams_control_history(
        self,
        request: live_20161101_models.DescribeLiveStreamsControlHistoryRequest,
    ) -> live_20161101_models.DescribeLiveStreamsControlHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_control_history_with_options(request, runtime)

    async def describe_live_streams_control_history_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsControlHistoryRequest,
    ) -> live_20161101_models.DescribeLiveStreamsControlHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_streams_control_history_with_options_async(request, runtime)

    def describe_live_streams_notify_url_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_streams_notify_url_config(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_notify_url_config_with_options(request, runtime)

    async def describe_live_streams_notify_url_config_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_streams_notify_url_config_with_options_async(request, runtime)

    def describe_live_streams_online_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsOnlineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsOnlineListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.only_stream):
            query['OnlyStream'] = request.only_stream
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsOnlineList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsOnlineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_streams_online_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsOnlineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsOnlineListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.only_stream):
            query['OnlyStream'] = request.only_stream
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsOnlineList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsOnlineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_streams_online_list(
        self,
        request: live_20161101_models.DescribeLiveStreamsOnlineListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsOnlineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_online_list_with_options(request, runtime)

    async def describe_live_streams_online_list_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsOnlineListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsOnlineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_streams_online_list_with_options_async(request, runtime)

    def describe_live_streams_publish_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsPublishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsPublishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsPublishList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsPublishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_streams_publish_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsPublishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsPublishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsPublishList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsPublishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_streams_publish_list(
        self,
        request: live_20161101_models.DescribeLiveStreamsPublishListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsPublishListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_publish_list_with_options(request, runtime)

    async def describe_live_streams_publish_list_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsPublishListRequest,
    ) -> live_20161101_models.DescribeLiveStreamsPublishListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_streams_publish_list_with_options_async(request, runtime)

    def describe_live_tag_resources_with_options(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTagResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_tag_resources_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTagResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_tag_resources(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_tag_resources_with_options(request, runtime)

    async def describe_live_tag_resources_async(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_tag_resources_with_options_async(request, runtime)

    def describe_live_top_domains_by_flow_with_options(
        self,
        request: live_20161101_models.DescribeLiveTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTopDomainsByFlow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_top_domains_by_flow_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTopDomainsByFlow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_top_domains_by_flow(
        self,
        request: live_20161101_models.DescribeLiveTopDomainsByFlowRequest,
    ) -> live_20161101_models.DescribeLiveTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_top_domains_by_flow_with_options(request, runtime)

    async def describe_live_top_domains_by_flow_async(
        self,
        request: live_20161101_models.DescribeLiveTopDomainsByFlowRequest,
    ) -> live_20161101_models.DescribeLiveTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_top_domains_by_flow_with_options_async(request, runtime)

    def describe_live_user_bill_prediction_with_options(
        self,
        request: live_20161101_models.DescribeLiveUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserBillPredictionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserBillPrediction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserBillPredictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_user_bill_prediction_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveUserBillPredictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserBillPredictionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserBillPrediction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserBillPredictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_user_bill_prediction(
        self,
        request: live_20161101_models.DescribeLiveUserBillPredictionRequest,
    ) -> live_20161101_models.DescribeLiveUserBillPredictionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_bill_prediction_with_options(request, runtime)

    async def describe_live_user_bill_prediction_async(
        self,
        request: live_20161101_models.DescribeLiveUserBillPredictionRequest,
    ) -> live_20161101_models.DescribeLiveUserBillPredictionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_user_bill_prediction_with_options_async(request, runtime)

    def describe_live_user_domains_with_options(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_user_domains_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_user_domains(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_domains_with_options(request, runtime)

    async def describe_live_user_domains_async(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_user_domains_with_options_async(request, runtime)

    def describe_live_user_tags_with_options(
        self,
        request: live_20161101_models.DescribeLiveUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserTags',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_live_user_tags_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserTags',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_live_user_tags(
        self,
        request: live_20161101_models.DescribeLiveUserTagsRequest,
    ) -> live_20161101_models.DescribeLiveUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_tags_with_options(request, runtime)

    async def describe_live_user_tags_async(
        self,
        request: live_20161101_models.DescribeLiveUserTagsRequest,
    ) -> live_20161101_models.DescribeLiveUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_user_tags_with_options_async(request, runtime)

    def describe_meter_live_rtc_duration_with_options(
        self,
        request: live_20161101_models.DescribeMeterLiveRtcDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMeterLiveRtcDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterLiveRtcDuration',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMeterLiveRtcDurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_live_rtc_duration_with_options_async(
        self,
        request: live_20161101_models.DescribeMeterLiveRtcDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMeterLiveRtcDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterLiveRtcDuration',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMeterLiveRtcDurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_live_rtc_duration(
        self,
        request: live_20161101_models.DescribeMeterLiveRtcDurationRequest,
    ) -> live_20161101_models.DescribeMeterLiveRtcDurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_live_rtc_duration_with_options(request, runtime)

    async def describe_meter_live_rtc_duration_async(
        self,
        request: live_20161101_models.DescribeMeterLiveRtcDurationRequest,
    ) -> live_20161101_models.DescribeMeterLiveRtcDurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_live_rtc_duration_with_options_async(request, runtime)

    def describe_mix_stream_list_with_options(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMixStreamList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMixStreamListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mix_stream_list_with_options_async(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMixStreamList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMixStreamListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mix_stream_list(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mix_stream_list_with_options(request, runtime)

    async def describe_mix_stream_list_async(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mix_stream_list_with_options_async(request, runtime)

    def describe_rtsnative_sdkfirst_frame_cost_with_options(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKFirstFrameCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameCost',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtsnative_sdkfirst_frame_cost_with_options_async(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKFirstFrameCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameCost',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtsnative_sdkfirst_frame_cost(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKFirstFrameCostRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkfirst_frame_cost_with_options(request, runtime)

    async def describe_rtsnative_sdkfirst_frame_cost_async(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKFirstFrameCostRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtsnative_sdkfirst_frame_cost_with_options_async(request, runtime)

    def describe_rtsnative_sdkfirst_frame_delay_with_options(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameDelay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtsnative_sdkfirst_frame_delay_with_options_async(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameDelay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtsnative_sdkfirst_frame_delay(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkfirst_frame_delay_with_options(request, runtime)

    async def describe_rtsnative_sdkfirst_frame_delay_async(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtsnative_sdkfirst_frame_delay_with_options_async(request, runtime)

    def describe_rtsnative_sdkplay_fail_status_with_options(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKPlayFailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayFailStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayFailStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtsnative_sdkplay_fail_status_with_options_async(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKPlayFailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayFailStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayFailStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtsnative_sdkplay_fail_status(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKPlayFailStatusRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkplay_fail_status_with_options(request, runtime)

    async def describe_rtsnative_sdkplay_fail_status_async(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKPlayFailStatusRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtsnative_sdkplay_fail_status_with_options_async(request, runtime)

    def describe_rtsnative_sdkplay_time_with_options(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKPlayTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayTimeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayTime',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtsnative_sdkplay_time_with_options_async(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKPlayTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayTimeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayTime',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtsnative_sdkplay_time(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKPlayTimeRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkplay_time_with_options(request, runtime)

    async def describe_rtsnative_sdkplay_time_async(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKPlayTimeRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtsnative_sdkplay_time_with_options_async(request, runtime)

    def describe_rtsnative_sdkvv_data_with_options(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKVvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKVvDataResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKVvDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKVvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKVvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rtsnative_sdkvv_data_with_options_async(
        self,
        tmp_req: live_20161101_models.DescribeRTSNativeSDKVvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRTSNativeSDKVvDataResponse:
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKVvDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKVvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKVvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rtsnative_sdkvv_data(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKVvDataRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKVvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkvv_data_with_options(request, runtime)

    async def describe_rtsnative_sdkvv_data_async(
        self,
        request: live_20161101_models.DescribeRTSNativeSDKVvDataRequest,
    ) -> live_20161101_models.DescribeRTSNativeSDKVvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rtsnative_sdkvv_data_with_options_async(request, runtime)

    def describe_room_kickout_user_list_with_options(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomKickoutUserList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomKickoutUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_room_kickout_user_list_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomKickoutUserList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomKickoutUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_room_kickout_user_list(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_room_kickout_user_list_with_options(request, runtime)

    async def describe_room_kickout_user_list_async(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_room_kickout_user_list_with_options_async(request, runtime)

    def describe_room_list_with_options(
        self,
        request: live_20161101_models.DescribeRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_status):
            query['RoomStatus'] = request.room_status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_room_list_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_status):
            query['RoomStatus'] = request.room_status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_room_list(
        self,
        request: live_20161101_models.DescribeRoomListRequest,
    ) -> live_20161101_models.DescribeRoomListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_room_list_with_options(request, runtime)

    async def describe_room_list_async(
        self,
        request: live_20161101_models.DescribeRoomListRequest,
    ) -> live_20161101_models.DescribeRoomListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_room_list_with_options_async(request, runtime)

    def describe_room_status_with_options(
        self,
        request: live_20161101_models.DescribeRoomStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_room_status_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_room_status(
        self,
        request: live_20161101_models.DescribeRoomStatusRequest,
    ) -> live_20161101_models.DescribeRoomStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_room_status_with_options(request, runtime)

    async def describe_room_status_async(
        self,
        request: live_20161101_models.DescribeRoomStatusRequest,
    ) -> live_20161101_models.DescribeRoomStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_room_status_with_options_async(request, runtime)

    def describe_show_list_with_options(
        self,
        request: live_20161101_models.DescribeShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeShowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_show_list_with_options_async(
        self,
        request: live_20161101_models.DescribeShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeShowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_show_list(
        self,
        request: live_20161101_models.DescribeShowListRequest,
    ) -> live_20161101_models.DescribeShowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_show_list_with_options(request, runtime)

    async def describe_show_list_async(
        self,
        request: live_20161101_models.DescribeShowListRequest,
    ) -> live_20161101_models.DescribeShowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_show_list_with_options_async(request, runtime)

    def describe_studio_layouts_with_options(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStudioLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeStudioLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_studio_layouts_with_options_async(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStudioLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeStudioLayoutsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_studio_layouts(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_studio_layouts_with_options(request, runtime)

    async def describe_studio_layouts_async(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_studio_layouts_with_options_async(request, runtime)

    def describe_toutiao_live_play_with_options(
        self,
        request: live_20161101_models.DescribeToutiaoLivePlayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeToutiaoLivePlayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePlay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePlayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_toutiao_live_play_with_options_async(
        self,
        request: live_20161101_models.DescribeToutiaoLivePlayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeToutiaoLivePlayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePlay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePlayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_toutiao_live_play(
        self,
        request: live_20161101_models.DescribeToutiaoLivePlayRequest,
    ) -> live_20161101_models.DescribeToutiaoLivePlayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_toutiao_live_play_with_options(request, runtime)

    async def describe_toutiao_live_play_async(
        self,
        request: live_20161101_models.DescribeToutiaoLivePlayRequest,
    ) -> live_20161101_models.DescribeToutiaoLivePlayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_toutiao_live_play_with_options_async(request, runtime)

    def describe_toutiao_live_publish_with_options(
        self,
        request: live_20161101_models.DescribeToutiaoLivePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeToutiaoLivePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePublish',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_toutiao_live_publish_with_options_async(
        self,
        request: live_20161101_models.DescribeToutiaoLivePublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeToutiaoLivePublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePublish',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_toutiao_live_publish(
        self,
        request: live_20161101_models.DescribeToutiaoLivePublishRequest,
    ) -> live_20161101_models.DescribeToutiaoLivePublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_toutiao_live_publish_with_options(request, runtime)

    async def describe_toutiao_live_publish_async(
        self,
        request: live_20161101_models.DescribeToutiaoLivePublishRequest,
    ) -> live_20161101_models.DescribeToutiaoLivePublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_toutiao_live_publish_with_options_async(request, runtime)

    def describe_up_bps_peak_data_with_options(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_up_bps_peak_data_with_options_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_up_bps_peak_data(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_data_with_options(request, runtime)

    async def describe_up_bps_peak_data_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_up_bps_peak_data_with_options_async(request, runtime)

    def describe_up_bps_peak_of_line_with_options(
        self,
        request: live_20161101_models.DescribeUpBpsPeakOfLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakOfLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakOfLine',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakOfLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_up_bps_peak_of_line_with_options_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakOfLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakOfLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakOfLine',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakOfLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_up_bps_peak_of_line(
        self,
        request: live_20161101_models.DescribeUpBpsPeakOfLineRequest,
    ) -> live_20161101_models.DescribeUpBpsPeakOfLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_of_line_with_options(request, runtime)

    async def describe_up_bps_peak_of_line_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakOfLineRequest,
    ) -> live_20161101_models.DescribeUpBpsPeakOfLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_up_bps_peak_of_line_with_options_async(request, runtime)

    def describe_up_peak_publish_stream_data_with_options(
        self,
        request: live_20161101_models.DescribeUpPeakPublishStreamDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpPeakPublishStreamDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpPeakPublishStreamData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpPeakPublishStreamDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_up_peak_publish_stream_data_with_options_async(
        self,
        request: live_20161101_models.DescribeUpPeakPublishStreamDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpPeakPublishStreamDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpPeakPublishStreamData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpPeakPublishStreamDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_up_peak_publish_stream_data(
        self,
        request: live_20161101_models.DescribeUpPeakPublishStreamDataRequest,
    ) -> live_20161101_models.DescribeUpPeakPublishStreamDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_up_peak_publish_stream_data_with_options(request, runtime)

    async def describe_up_peak_publish_stream_data_async(
        self,
        request: live_20161101_models.DescribeUpPeakPublishStreamDataRequest,
    ) -> live_20161101_models.DescribeUpPeakPublishStreamDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_up_peak_publish_stream_data_with_options_async(request, runtime)

    def disable_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.DisableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DisableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DisableLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DisableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DisableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DisableLiveRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_live_realtime_log_delivery(
        self,
        request: live_20161101_models.DisableLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DisableLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_live_realtime_log_delivery_with_options(request, runtime)

    async def disable_live_realtime_log_delivery_async(
        self,
        request: live_20161101_models.DisableLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.DisableLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_live_realtime_log_delivery_with_options_async(request, runtime)

    def dynamic_update_water_mark_stream_rule_with_options(
        self,
        request: live_20161101_models.DynamicUpdateWaterMarkStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DynamicUpdateWaterMarkStreamRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def dynamic_update_water_mark_stream_rule_with_options_async(
        self,
        request: live_20161101_models.DynamicUpdateWaterMarkStreamRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DynamicUpdateWaterMarkStreamRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dynamic_update_water_mark_stream_rule(
        self,
        request: live_20161101_models.DynamicUpdateWaterMarkStreamRuleRequest,
    ) -> live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.dynamic_update_water_mark_stream_rule_with_options(request, runtime)

    async def dynamic_update_water_mark_stream_rule_async(
        self,
        request: live_20161101_models.DynamicUpdateWaterMarkStreamRuleRequest,
    ) -> live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dynamic_update_water_mark_stream_rule_with_options_async(request, runtime)

    def edit_playlist_with_options(
        self,
        request: live_20161101_models.EditPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_playlist_with_options_async(
        self,
        request: live_20161101_models.EditPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_playlist(
        self,
        request: live_20161101_models.EditPlaylistRequest,
    ) -> live_20161101_models.EditPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_playlist_with_options(request, runtime)

    async def edit_playlist_async(
        self,
        request: live_20161101_models.EditPlaylistRequest,
    ) -> live_20161101_models.EditPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_playlist_with_options_async(request, runtime)

    def edit_show_and_replace_with_options(
        self,
        request: live_20161101_models.EditShowAndReplaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditShowAndReplaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage_info):
            query['StorageInfo'] = request.storage_info
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditShowAndReplace',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditShowAndReplaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_show_and_replace_with_options_async(
        self,
        request: live_20161101_models.EditShowAndReplaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditShowAndReplaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage_info):
            query['StorageInfo'] = request.storage_info
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditShowAndReplace',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditShowAndReplaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_show_and_replace(
        self,
        request: live_20161101_models.EditShowAndReplaceRequest,
    ) -> live_20161101_models.EditShowAndReplaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_show_and_replace_with_options(request, runtime)

    async def edit_show_and_replace_async(
        self,
        request: live_20161101_models.EditShowAndReplaceRequest,
    ) -> live_20161101_models.EditShowAndReplaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_show_and_replace_with_options_async(request, runtime)

    def effect_caster_urgent_with_options(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterUrgent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterUrgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_caster_urgent_with_options_async(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterUrgent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterUrgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_caster_urgent(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_urgent_with_options(request, runtime)

    async def effect_caster_urgent_async(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.effect_caster_urgent_with_options_async(request, runtime)

    def effect_caster_video_resource_with_options(
        self,
        request: live_20161101_models.EffectCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.EffectCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterVideoResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_caster_video_resource(
        self,
        request: live_20161101_models.EffectCasterVideoResourceRequest,
    ) -> live_20161101_models.EffectCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_video_resource_with_options(request, runtime)

    async def effect_caster_video_resource_async(
        self,
        request: live_20161101_models.EffectCasterVideoResourceRequest,
    ) -> live_20161101_models.EffectCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.effect_caster_video_resource_with_options_async(request, runtime)

    def enable_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.EnableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EnableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EnableLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.EnableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EnableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EnableLiveRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_live_realtime_log_delivery(
        self,
        request: live_20161101_models.EnableLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.EnableLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_live_realtime_log_delivery_with_options(request, runtime)

    async def enable_live_realtime_log_delivery_async(
        self,
        request: live_20161101_models.EnableLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.EnableLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_live_realtime_log_delivery_with_options_async(request, runtime)

    def forbid_live_stream_with_options(
        self,
        request: live_20161101_models.ForbidLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidLiveStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidLiveStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def forbid_live_stream_with_options_async(
        self,
        request: live_20161101_models.ForbidLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidLiveStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidLiveStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def forbid_live_stream(
        self,
        request: live_20161101_models.ForbidLiveStreamRequest,
    ) -> live_20161101_models.ForbidLiveStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.forbid_live_stream_with_options(request, runtime)

    async def forbid_live_stream_async(
        self,
        request: live_20161101_models.ForbidLiveStreamRequest,
    ) -> live_20161101_models.ForbidLiveStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.forbid_live_stream_with_options_async(request, runtime)

    def forbid_push_stream_with_options(
        self,
        request: live_20161101_models.ForbidPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidPushStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidPushStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def forbid_push_stream_with_options_async(
        self,
        request: live_20161101_models.ForbidPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidPushStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidPushStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def forbid_push_stream(
        self,
        request: live_20161101_models.ForbidPushStreamRequest,
    ) -> live_20161101_models.ForbidPushStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.forbid_push_stream_with_options(request, runtime)

    async def forbid_push_stream_async(
        self,
        request: live_20161101_models.ForbidPushStreamRequest,
    ) -> live_20161101_models.ForbidPushStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.forbid_push_stream_with_options_async(request, runtime)

    def get_all_custom_templates_with_options(
        self,
        request: live_20161101_models.GetAllCustomTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetAllCustomTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllCustomTemplates',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetAllCustomTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_custom_templates_with_options_async(
        self,
        request: live_20161101_models.GetAllCustomTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetAllCustomTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllCustomTemplates',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetAllCustomTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_custom_templates(
        self,
        request: live_20161101_models.GetAllCustomTemplatesRequest,
    ) -> live_20161101_models.GetAllCustomTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_all_custom_templates_with_options(request, runtime)

    async def get_all_custom_templates_async(
        self,
        request: live_20161101_models.GetAllCustomTemplatesRequest,
    ) -> live_20161101_models.GetAllCustomTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_all_custom_templates_with_options_async(request, runtime)

    def get_custom_template_with_options(
        self,
        request: live_20161101_models.GetCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_template_with_options_async(
        self,
        request: live_20161101_models.GetCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_template(
        self,
        request: live_20161101_models.GetCustomTemplateRequest,
    ) -> live_20161101_models.GetCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_custom_template_with_options(request, runtime)

    async def get_custom_template_async(
        self,
        request: live_20161101_models.GetCustomTemplateRequest,
    ) -> live_20161101_models.GetCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_template_with_options_async(request, runtime)

    def get_editing_job_info_with_options(
        self,
        request: live_20161101_models.GetEditingJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetEditingJobInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingJobInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetEditingJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_editing_job_info_with_options_async(
        self,
        request: live_20161101_models.GetEditingJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetEditingJobInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingJobInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetEditingJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_editing_job_info(
        self,
        request: live_20161101_models.GetEditingJobInfoRequest,
    ) -> live_20161101_models.GetEditingJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_job_info_with_options(request, runtime)

    async def get_editing_job_info_async(
        self,
        request: live_20161101_models.GetEditingJobInfoRequest,
    ) -> live_20161101_models.GetEditingJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_job_info_with_options_async(request, runtime)

    def get_message_group_with_options(
        self,
        request: live_20161101_models.GetMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_group_with_options_async(
        self,
        request: live_20161101_models.GetMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_group(
        self,
        request: live_20161101_models.GetMessageGroupRequest,
    ) -> live_20161101_models.GetMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_group_with_options(request, runtime)

    async def get_message_group_async(
        self,
        request: live_20161101_models.GetMessageGroupRequest,
    ) -> live_20161101_models.GetMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_group_with_options_async(request, runtime)

    def get_message_token_with_options(
        self,
        request: live_20161101_models.GetMessageTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageToken',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_token_with_options_async(
        self,
        request: live_20161101_models.GetMessageTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageToken',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_token(
        self,
        request: live_20161101_models.GetMessageTokenRequest,
    ) -> live_20161101_models.GetMessageTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_token_with_options(request, runtime)

    async def get_message_token_async(
        self,
        request: live_20161101_models.GetMessageTokenRequest,
    ) -> live_20161101_models.GetMessageTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_token_with_options_async(request, runtime)

    def get_message_user_info_with_options(
        self,
        request: live_20161101_models.GetMessageUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageUserInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_uid):
            body['CloudUid'] = request.cloud_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageUserInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_user_info_with_options_async(
        self,
        request: live_20161101_models.GetMessageUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMessageUserInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_uid):
            body['CloudUid'] = request.cloud_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageUserInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_user_info(
        self,
        request: live_20161101_models.GetMessageUserInfoRequest,
    ) -> live_20161101_models.GetMessageUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_user_info_with_options(request, runtime)

    async def get_message_user_info_async(
        self,
        request: live_20161101_models.GetMessageUserInfoRequest,
    ) -> live_20161101_models.GetMessageUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_user_info_with_options_async(request, runtime)

    def get_multi_rate_config_with_options(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_rate_config(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_rate_config_with_options(request, runtime)

    async def get_multi_rate_config_async(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_rate_config_with_options_async(request, runtime)

    def get_multi_rate_config_list_with_options(
        self,
        request: live_20161101_models.GetMultiRateConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfigList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_rate_config_list_with_options_async(
        self,
        request: live_20161101_models.GetMultiRateConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfigList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_rate_config_list(
        self,
        request: live_20161101_models.GetMultiRateConfigListRequest,
    ) -> live_20161101_models.GetMultiRateConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multi_rate_config_list_with_options(request, runtime)

    async def get_multi_rate_config_list_async(
        self,
        request: live_20161101_models.GetMultiRateConfigListRequest,
    ) -> live_20161101_models.GetMultiRateConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_rate_config_list_with_options_async(request, runtime)

    def hot_live_rtc_stream_with_options(
        self,
        request: live_20161101_models.HotLiveRtcStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.HotLiveRtcStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.audio_msid):
            query['AudioMsid'] = request.audio_msid
        if not UtilClient.is_unset(request.connection_timeout):
            query['ConnectionTimeout'] = request.connection_timeout
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.media_timeout):
            query['MediaTimeout'] = request.media_timeout
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.video_msid):
            query['VideoMsid'] = request.video_msid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotLiveRtcStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.HotLiveRtcStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def hot_live_rtc_stream_with_options_async(
        self,
        request: live_20161101_models.HotLiveRtcStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.HotLiveRtcStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.audio_msid):
            query['AudioMsid'] = request.audio_msid
        if not UtilClient.is_unset(request.connection_timeout):
            query['ConnectionTimeout'] = request.connection_timeout
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.media_timeout):
            query['MediaTimeout'] = request.media_timeout
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.video_msid):
            query['VideoMsid'] = request.video_msid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotLiveRtcStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.HotLiveRtcStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hot_live_rtc_stream(
        self,
        request: live_20161101_models.HotLiveRtcStreamRequest,
    ) -> live_20161101_models.HotLiveRtcStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.hot_live_rtc_stream_with_options(request, runtime)

    async def hot_live_rtc_stream_async(
        self,
        request: live_20161101_models.HotLiveRtcStreamRequest,
    ) -> live_20161101_models.HotLiveRtcStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hot_live_rtc_stream_with_options_async(request, runtime)

    def initialize_auto_show_list_task_with_options(
        self,
        request: live_20161101_models.InitializeAutoShowListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.InitializeAutoShowListTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_back_url):
            query['CallBackUrl'] = request.call_back_url
        if not UtilClient.is_unset(request.caster_config):
            query['CasterConfig'] = request.caster_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeAutoShowListTask',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.InitializeAutoShowListTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_auto_show_list_task_with_options_async(
        self,
        request: live_20161101_models.InitializeAutoShowListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.InitializeAutoShowListTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_back_url):
            query['CallBackUrl'] = request.call_back_url
        if not UtilClient.is_unset(request.caster_config):
            query['CasterConfig'] = request.caster_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeAutoShowListTask',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.InitializeAutoShowListTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_auto_show_list_task(
        self,
        request: live_20161101_models.InitializeAutoShowListTaskRequest,
    ) -> live_20161101_models.InitializeAutoShowListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_auto_show_list_task_with_options(request, runtime)

    async def initialize_auto_show_list_task_async(
        self,
        request: live_20161101_models.InitializeAutoShowListTaskRequest,
    ) -> live_20161101_models.InitializeAutoShowListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_auto_show_list_task_with_options_async(request, runtime)

    def join_message_group_with_options(
        self,
        request: live_20161101_models.JoinMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.JoinMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.JoinMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_message_group_with_options_async(
        self,
        request: live_20161101_models.JoinMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.JoinMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.JoinMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_message_group(
        self,
        request: live_20161101_models.JoinMessageGroupRequest,
    ) -> live_20161101_models.JoinMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_message_group_with_options(request, runtime)

    async def join_message_group_async(
        self,
        request: live_20161101_models.JoinMessageGroupRequest,
    ) -> live_20161101_models.JoinMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_message_group_with_options_async(request, runtime)

    def leave_message_group_with_options(
        self,
        request: live_20161101_models.LeaveMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.LeaveMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LeaveMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.LeaveMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def leave_message_group_with_options_async(
        self,
        request: live_20161101_models.LeaveMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.LeaveMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LeaveMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.LeaveMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def leave_message_group(
        self,
        request: live_20161101_models.LeaveMessageGroupRequest,
    ) -> live_20161101_models.LeaveMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_message_group_with_options(request, runtime)

    async def leave_message_group_async(
        self,
        request: live_20161101_models.LeaveMessageGroupRequest,
    ) -> live_20161101_models.LeaveMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_message_group_with_options_async(request, runtime)

    def list_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_realtime_log_delivery(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_with_options(request, runtime)

    async def list_live_realtime_log_delivery_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_realtime_log_delivery_with_options_async(request, runtime)

    def list_live_realtime_log_delivery_domains_with_options(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_realtime_log_delivery_domains_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_realtime_log_delivery_domains(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryDomainsRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_domains_with_options(request, runtime)

    async def list_live_realtime_log_delivery_domains_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryDomainsRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_realtime_log_delivery_domains_with_options_async(request, runtime)

    def list_live_realtime_log_delivery_infos_with_options(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryInfos',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_realtime_log_delivery_infos_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryInfos',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_realtime_log_delivery_infos(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryInfosRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_infos_with_options(request, runtime)

    async def list_live_realtime_log_delivery_infos_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryInfosRequest,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_realtime_log_delivery_infos_with_options_async(request, runtime)

    def list_message_with_options(
        self,
        request: live_20161101_models.ListMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessage',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_with_options_async(
        self,
        request: live_20161101_models.ListMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessage',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message(
        self,
        request: live_20161101_models.ListMessageRequest,
    ) -> live_20161101_models.ListMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_message_with_options(request, runtime)

    async def list_message_async(
        self,
        request: live_20161101_models.ListMessageRequest,
    ) -> live_20161101_models.ListMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_message_with_options_async(request, runtime)

    def list_message_group_with_options(
        self,
        request: live_20161101_models.ListMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_group_with_options_async(
        self,
        request: live_20161101_models.ListMessageGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_group(
        self,
        request: live_20161101_models.ListMessageGroupRequest,
    ) -> live_20161101_models.ListMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_message_group_with_options(request, runtime)

    async def list_message_group_async(
        self,
        request: live_20161101_models.ListMessageGroupRequest,
    ) -> live_20161101_models.ListMessageGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_message_group_with_options_async(request, runtime)

    def list_message_group_user_with_options(
        self,
        request: live_20161101_models.ListMessageGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_message_group_user_with_options_async(
        self,
        request: live_20161101_models.ListMessageGroupUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListMessageGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_message_group_user(
        self,
        request: live_20161101_models.ListMessageGroupUserRequest,
    ) -> live_20161101_models.ListMessageGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_message_group_user_with_options(request, runtime)

    async def list_message_group_user_async(
        self,
        request: live_20161101_models.ListMessageGroupUserRequest,
    ) -> live_20161101_models.ListMessageGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_message_group_user_with_options_async(request, runtime)

    def list_playlist_with_options(
        self,
        request: live_20161101_models.ListPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_playlist_with_options_async(
        self,
        request: live_20161101_models.ListPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_playlist(
        self,
        request: live_20161101_models.ListPlaylistRequest,
    ) -> live_20161101_models.ListPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_playlist_with_options(request, runtime)

    async def list_playlist_async(
        self,
        request: live_20161101_models.ListPlaylistRequest,
    ) -> live_20161101_models.ListPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_playlist_with_options_async(request, runtime)

    def list_playlist_items_with_options(
        self,
        request: live_20161101_models.ListPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_playlist_items_with_options_async(
        self,
        request: live_20161101_models.ListPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_playlist_items(
        self,
        request: live_20161101_models.ListPlaylistItemsRequest,
    ) -> live_20161101_models.ListPlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_playlist_items_with_options(request, runtime)

    async def list_playlist_items_async(
        self,
        request: live_20161101_models.ListPlaylistItemsRequest,
    ) -> live_20161101_models.ListPlaylistItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_playlist_items_with_options_async(request, runtime)

    def modify_caster_component_with_options(
        self,
        request: live_20161101_models.ModifyCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_caster_component_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_caster_component(
        self,
        request: live_20161101_models.ModifyCasterComponentRequest,
    ) -> live_20161101_models.ModifyCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_component_with_options(request, runtime)

    async def modify_caster_component_async(
        self,
        request: live_20161101_models.ModifyCasterComponentRequest,
    ) -> live_20161101_models.ModifyCasterComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_caster_component_with_options_async(request, runtime)

    def modify_caster_episode_with_options(
        self,
        request: live_20161101_models.ModifyCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_caster_episode_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterEpisodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterEpisodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_caster_episode(
        self,
        request: live_20161101_models.ModifyCasterEpisodeRequest,
    ) -> live_20161101_models.ModifyCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_episode_with_options(request, runtime)

    async def modify_caster_episode_async(
        self,
        request: live_20161101_models.ModifyCasterEpisodeRequest,
    ) -> live_20161101_models.ModifyCasterEpisodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_caster_episode_with_options_async(request, runtime)

    def modify_caster_layout_with_options(
        self,
        request: live_20161101_models.ModifyCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_caster_layout_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_caster_layout(
        self,
        request: live_20161101_models.ModifyCasterLayoutRequest,
    ) -> live_20161101_models.ModifyCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_layout_with_options(request, runtime)

    async def modify_caster_layout_async(
        self,
        request: live_20161101_models.ModifyCasterLayoutRequest,
    ) -> live_20161101_models.ModifyCasterLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_caster_layout_with_options_async(request, runtime)

    def modify_caster_program_with_options(
        self,
        request: live_20161101_models.ModifyCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_caster_program_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterProgramResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterProgramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_caster_program(
        self,
        request: live_20161101_models.ModifyCasterProgramRequest,
    ) -> live_20161101_models.ModifyCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_program_with_options(request, runtime)

    async def modify_caster_program_async(
        self,
        request: live_20161101_models.ModifyCasterProgramRequest,
    ) -> live_20161101_models.ModifyCasterProgramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_caster_program_with_options_async(request, runtime)

    def modify_caster_video_resource_with_options(
        self,
        request: live_20161101_models.ModifyCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterVideoResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_caster_video_resource(
        self,
        request: live_20161101_models.ModifyCasterVideoResourceRequest,
    ) -> live_20161101_models.ModifyCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_video_resource_with_options(request, runtime)

    async def modify_caster_video_resource_async(
        self,
        request: live_20161101_models.ModifyCasterVideoResourceRequest,
    ) -> live_20161101_models.ModifyCasterVideoResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_caster_video_resource_with_options_async(request, runtime)

    def modify_live_domain_schdm_by_property_with_options(
        self,
        request: live_20161101_models.ModifyLiveDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveDomainSchdmByProperty',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_live_domain_schdm_by_property_with_options_async(
        self,
        request: live_20161101_models.ModifyLiveDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveDomainSchdmByProperty',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_live_domain_schdm_by_property(
        self,
        request: live_20161101_models.ModifyLiveDomainSchdmByPropertyRequest,
    ) -> live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_live_domain_schdm_by_property_with_options(request, runtime)

    async def modify_live_domain_schdm_by_property_async(
        self,
        request: live_20161101_models.ModifyLiveDomainSchdmByPropertyRequest,
    ) -> live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_live_domain_schdm_by_property_with_options_async(request, runtime)

    def modify_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.ModifyLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.ModifyLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_live_realtime_log_delivery(
        self,
        request: live_20161101_models.ModifyLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_live_realtime_log_delivery_with_options(request, runtime)

    async def modify_live_realtime_log_delivery_async(
        self,
        request: live_20161101_models.ModifyLiveRealtimeLogDeliveryRequest,
    ) -> live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_live_realtime_log_delivery_with_options_async(request, runtime)

    def modify_show_list_with_options(
        self,
        request: live_20161101_models.ModifyShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.high_priority_show_id):
            query['HighPriorityShowId'] = request.high_priority_show_id
        if not UtilClient.is_unset(request.high_priority_show_start_time):
            query['HighPriorityShowStartTime'] = request.high_priority_show_start_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyShowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_show_list_with_options_async(
        self,
        request: live_20161101_models.ModifyShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.high_priority_show_id):
            query['HighPriorityShowId'] = request.high_priority_show_id
        if not UtilClient.is_unset(request.high_priority_show_start_time):
            query['HighPriorityShowStartTime'] = request.high_priority_show_start_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyShowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_show_list(
        self,
        request: live_20161101_models.ModifyShowListRequest,
    ) -> live_20161101_models.ModifyShowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_show_list_with_options(request, runtime)

    async def modify_show_list_async(
        self,
        request: live_20161101_models.ModifyShowListRequest,
    ) -> live_20161101_models.ModifyShowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_show_list_with_options_async(request, runtime)

    def modify_studio_layout_with_options(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_studio_layout_with_options_async(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyStudioLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_studio_layout(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_studio_layout_with_options(request, runtime)

    async def modify_studio_layout_async(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_studio_layout_with_options_async(request, runtime)

    def open_live_shift_with_options(
        self,
        request: live_20161101_models.OpenLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.OpenLiveShiftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.ignore_transcode):
            query['IgnoreTranscode'] = request.ignore_transcode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vision):
            query['Vision'] = request.vision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.OpenLiveShiftResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_live_shift_with_options_async(
        self,
        request: live_20161101_models.OpenLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.OpenLiveShiftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.ignore_transcode):
            query['IgnoreTranscode'] = request.ignore_transcode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vision):
            query['Vision'] = request.vision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.OpenLiveShiftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_live_shift(
        self,
        request: live_20161101_models.OpenLiveShiftRequest,
    ) -> live_20161101_models.OpenLiveShiftResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_live_shift_with_options(request, runtime)

    async def open_live_shift_async(
        self,
        request: live_20161101_models.OpenLiveShiftRequest,
    ) -> live_20161101_models.OpenLiveShiftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_live_shift_with_options_async(request, runtime)

    def play_choosen_show_with_options(
        self,
        request: live_20161101_models.PlayChoosenShowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.PlayChoosenShowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlayChoosenShow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PlayChoosenShowResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_choosen_show_with_options_async(
        self,
        request: live_20161101_models.PlayChoosenShowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.PlayChoosenShowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlayChoosenShow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PlayChoosenShowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_choosen_show(
        self,
        request: live_20161101_models.PlayChoosenShowRequest,
    ) -> live_20161101_models.PlayChoosenShowResponse:
        runtime = util_models.RuntimeOptions()
        return self.play_choosen_show_with_options(request, runtime)

    async def play_choosen_show_async(
        self,
        request: live_20161101_models.PlayChoosenShowRequest,
    ) -> live_20161101_models.PlayChoosenShowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.play_choosen_show_with_options_async(request, runtime)

    def publish_live_staging_config_to_production_with_options(
        self,
        request: live_20161101_models.PublishLiveStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.PublishLiveStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishLiveStagingConfigToProduction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PublishLiveStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_live_staging_config_to_production_with_options_async(
        self,
        request: live_20161101_models.PublishLiveStagingConfigToProductionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.PublishLiveStagingConfigToProductionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishLiveStagingConfigToProduction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PublishLiveStagingConfigToProductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_live_staging_config_to_production(
        self,
        request: live_20161101_models.PublishLiveStagingConfigToProductionRequest,
    ) -> live_20161101_models.PublishLiveStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_live_staging_config_to_production_with_options(request, runtime)

    async def publish_live_staging_config_to_production_async(
        self,
        request: live_20161101_models.PublishLiveStagingConfigToProductionRequest,
    ) -> live_20161101_models.PublishLiveStagingConfigToProductionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_live_staging_config_to_production_with_options_async(request, runtime)

    def query_snapshot_callback_auth_with_options(
        self,
        request: live_20161101_models.QuerySnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.QuerySnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.QuerySnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_snapshot_callback_auth_with_options_async(
        self,
        request: live_20161101_models.QuerySnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.QuerySnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.QuerySnapshotCallbackAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_snapshot_callback_auth(
        self,
        request: live_20161101_models.QuerySnapshotCallbackAuthRequest,
    ) -> live_20161101_models.QuerySnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_snapshot_callback_auth_with_options(request, runtime)

    async def query_snapshot_callback_auth_async(
        self,
        request: live_20161101_models.QuerySnapshotCallbackAuthRequest,
    ) -> live_20161101_models.QuerySnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_snapshot_callback_auth_with_options_async(request, runtime)

    def real_time_record_command_with_options(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeRecordCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeRecordCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def real_time_record_command_with_options_async(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeRecordCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeRecordCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def real_time_record_command(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.real_time_record_command_with_options(request, runtime)

    async def real_time_record_command_async(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.real_time_record_command_with_options_async(request, runtime)

    def real_time_snapshot_command_with_options(
        self,
        request: live_20161101_models.RealTimeSnapshotCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeSnapshotCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeSnapshotCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeSnapshotCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def real_time_snapshot_command_with_options_async(
        self,
        request: live_20161101_models.RealTimeSnapshotCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeSnapshotCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeSnapshotCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeSnapshotCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def real_time_snapshot_command(
        self,
        request: live_20161101_models.RealTimeSnapshotCommandRequest,
    ) -> live_20161101_models.RealTimeSnapshotCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.real_time_snapshot_command_with_options(request, runtime)

    async def real_time_snapshot_command_async(
        self,
        request: live_20161101_models.RealTimeSnapshotCommandRequest,
    ) -> live_20161101_models.RealTimeSnapshotCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.real_time_snapshot_command_with_options_async(request, runtime)

    def remove_show_from_show_list_with_options(
        self,
        request: live_20161101_models.RemoveShowFromShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RemoveShowFromShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_id_list):
            query['showIdList'] = request.show_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveShowFromShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RemoveShowFromShowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_show_from_show_list_with_options_async(
        self,
        request: live_20161101_models.RemoveShowFromShowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RemoveShowFromShowListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_id_list):
            query['showIdList'] = request.show_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveShowFromShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RemoveShowFromShowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_show_from_show_list(
        self,
        request: live_20161101_models.RemoveShowFromShowListRequest,
    ) -> live_20161101_models.RemoveShowFromShowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_show_from_show_list_with_options(request, runtime)

    async def remove_show_from_show_list_async(
        self,
        request: live_20161101_models.RemoveShowFromShowListRequest,
    ) -> live_20161101_models.RemoveShowFromShowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_show_from_show_list_with_options_async(request, runtime)

    def resume_live_stream_with_options(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ResumeLiveStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_live_stream_with_options_async(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ResumeLiveStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_live_stream(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_live_stream_with_options(request, runtime)

    async def resume_live_stream_async(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_live_stream_with_options_async(request, runtime)

    def rollback_live_staging_config_with_options(
        self,
        request: live_20161101_models.RollbackLiveStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RollbackLiveStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackLiveStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RollbackLiveStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_live_staging_config_with_options_async(
        self,
        request: live_20161101_models.RollbackLiveStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RollbackLiveStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackLiveStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RollbackLiveStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_live_staging_config(
        self,
        request: live_20161101_models.RollbackLiveStagingConfigRequest,
    ) -> live_20161101_models.RollbackLiveStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_live_staging_config_with_options(request, runtime)

    async def rollback_live_staging_config_async(
        self,
        request: live_20161101_models.RollbackLiveStagingConfigRequest,
    ) -> live_20161101_models.RollbackLiveStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_live_staging_config_with_options_async(request, runtime)

    def send_room_notification_with_options(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_room_notification_with_options_async(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_room_notification(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_room_notification_with_options(request, runtime)

    async def send_room_notification_async(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_room_notification_with_options_async(request, runtime)

    def send_room_user_notification_with_options(
        self,
        request: live_20161101_models.SendRoomUserNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomUserNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.to_app_uid):
            query['ToAppUid'] = request.to_app_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomUserNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomUserNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_room_user_notification_with_options_async(
        self,
        request: live_20161101_models.SendRoomUserNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomUserNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.to_app_uid):
            query['ToAppUid'] = request.to_app_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomUserNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomUserNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_room_user_notification(
        self,
        request: live_20161101_models.SendRoomUserNotificationRequest,
    ) -> live_20161101_models.SendRoomUserNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_room_user_notification_with_options(request, runtime)

    async def send_room_user_notification_async(
        self,
        request: live_20161101_models.SendRoomUserNotificationRequest,
    ) -> live_20161101_models.SendRoomUserNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_room_user_notification_with_options_async(request, runtime)

    def set_caster_channel_with_options(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.face_beauty):
            query['FaceBeauty'] = request.face_beauty
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_status):
            query['PlayStatus'] = request.play_status
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.seek_offset):
            query['SeekOffset'] = request.seek_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterChannel',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_caster_channel_with_options_async(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.face_beauty):
            query['FaceBeauty'] = request.face_beauty
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_status):
            query['PlayStatus'] = request.play_status
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.seek_offset):
            query['SeekOffset'] = request.seek_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterChannel',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_caster_channel(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
    ) -> live_20161101_models.SetCasterChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_caster_channel_with_options(request, runtime)

    async def set_caster_channel_async(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
    ) -> live_20161101_models.SetCasterChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_caster_channel_with_options_async(request, runtime)

    def set_caster_config_with_options(
        self,
        request: live_20161101_models.SetCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.channel_enable):
            query['ChannelEnable'] = request.channel_enable
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_effect):
            query['ProgramEffect'] = request.program_effect
        if not UtilClient.is_unset(request.program_name):
            query['ProgramName'] = request.program_name
        if not UtilClient.is_unset(request.record_config):
            query['RecordConfig'] = request.record_config
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.side_output_url_list):
            query['SideOutputUrlList'] = request.side_output_url_list
        if not UtilClient.is_unset(request.sync_groups_config):
            query['SyncGroupsConfig'] = request.sync_groups_config
        if not UtilClient.is_unset(request.transcode_config):
            query['TranscodeConfig'] = request.transcode_config
        if not UtilClient.is_unset(request.urgent_live_stream_url):
            query['UrgentLiveStreamUrl'] = request.urgent_live_stream_url
        if not UtilClient.is_unset(request.urgent_material_id):
            query['UrgentMaterialId'] = request.urgent_material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_caster_config_with_options_async(
        self,
        request: live_20161101_models.SetCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.channel_enable):
            query['ChannelEnable'] = request.channel_enable
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_effect):
            query['ProgramEffect'] = request.program_effect
        if not UtilClient.is_unset(request.program_name):
            query['ProgramName'] = request.program_name
        if not UtilClient.is_unset(request.record_config):
            query['RecordConfig'] = request.record_config
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.side_output_url_list):
            query['SideOutputUrlList'] = request.side_output_url_list
        if not UtilClient.is_unset(request.sync_groups_config):
            query['SyncGroupsConfig'] = request.sync_groups_config
        if not UtilClient.is_unset(request.transcode_config):
            query['TranscodeConfig'] = request.transcode_config
        if not UtilClient.is_unset(request.urgent_live_stream_url):
            query['UrgentLiveStreamUrl'] = request.urgent_live_stream_url
        if not UtilClient.is_unset(request.urgent_material_id):
            query['UrgentMaterialId'] = request.urgent_material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_caster_config(
        self,
        request: live_20161101_models.SetCasterConfigRequest,
    ) -> live_20161101_models.SetCasterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_caster_config_with_options(request, runtime)

    async def set_caster_config_async(
        self,
        request: live_20161101_models.SetCasterConfigRequest,
    ) -> live_20161101_models.SetCasterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_caster_config_with_options_async(request, runtime)

    def set_caster_scene_config_with_options(
        self,
        request: live_20161101_models.SetCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.SetCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_caster_scene_config(
        self,
        request: live_20161101_models.SetCasterSceneConfigRequest,
    ) -> live_20161101_models.SetCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_caster_scene_config_with_options(request, runtime)

    async def set_caster_scene_config_async(
        self,
        request: live_20161101_models.SetCasterSceneConfigRequest,
    ) -> live_20161101_models.SetCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_caster_scene_config_with_options_async(request, runtime)

    def set_caster_sync_group_with_options(
        self,
        request: live_20161101_models.SetCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sync_group):
            query['SyncGroup'] = request.sync_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSyncGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_caster_sync_group_with_options_async(
        self,
        request: live_20161101_models.SetCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sync_group):
            query['SyncGroup'] = request.sync_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSyncGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_caster_sync_group(
        self,
        request: live_20161101_models.SetCasterSyncGroupRequest,
    ) -> live_20161101_models.SetCasterSyncGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_caster_sync_group_with_options(request, runtime)

    async def set_caster_sync_group_async(
        self,
        request: live_20161101_models.SetCasterSyncGroupRequest,
    ) -> live_20161101_models.SetCasterSyncGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_caster_sync_group_with_options_async(request, runtime)

    def set_caster_timed_event_with_options(
        self,
        request: live_20161101_models.SetCasterTimedEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterTimedEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterTimedEvent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterTimedEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_caster_timed_event_with_options_async(
        self,
        request: live_20161101_models.SetCasterTimedEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterTimedEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterTimedEvent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterTimedEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_caster_timed_event(
        self,
        request: live_20161101_models.SetCasterTimedEventRequest,
    ) -> live_20161101_models.SetCasterTimedEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_caster_timed_event_with_options(request, runtime)

    async def set_caster_timed_event_async(
        self,
        request: live_20161101_models.SetCasterTimedEventRequest,
    ) -> live_20161101_models.SetCasterTimedEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_caster_timed_event_with_options_async(request, runtime)

    def set_live_domain_certificate_with_options(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainCertificate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_domain_certificate_with_options_async(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainCertificate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_domain_certificate(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_domain_certificate_with_options(request, runtime)

    async def set_live_domain_certificate_async(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_domain_certificate_with_options_async(request, runtime)

    def set_live_domain_staging_config_with_options(
        self,
        request: live_20161101_models.SetLiveDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_domain_staging_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveDomainStagingConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainStagingConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainStagingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_domain_staging_config(
        self,
        request: live_20161101_models.SetLiveDomainStagingConfigRequest,
    ) -> live_20161101_models.SetLiveDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_domain_staging_config_with_options(request, runtime)

    async def set_live_domain_staging_config_async(
        self,
        request: live_20161101_models.SetLiveDomainStagingConfigRequest,
    ) -> live_20161101_models.SetLiveDomainStagingConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_domain_staging_config_with_options_async(request, runtime)

    def set_live_edge_transfer_with_options(
        self,
        request: live_20161101_models.SetLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_dns):
            query['HttpDns'] = request.http_dns
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.target_domain_list):
            query['TargetDomainList'] = request.target_domain_list
        if not UtilClient.is_unset(request.transfer_args):
            query['TransferArgs'] = request.transfer_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_edge_transfer_with_options_async(
        self,
        request: live_20161101_models.SetLiveEdgeTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveEdgeTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_dns):
            query['HttpDns'] = request.http_dns
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.target_domain_list):
            query['TargetDomainList'] = request.target_domain_list
        if not UtilClient.is_unset(request.transfer_args):
            query['TransferArgs'] = request.transfer_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveEdgeTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_edge_transfer(
        self,
        request: live_20161101_models.SetLiveEdgeTransferRequest,
    ) -> live_20161101_models.SetLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_edge_transfer_with_options(request, runtime)

    async def set_live_edge_transfer_async(
        self,
        request: live_20161101_models.SetLiveEdgeTransferRequest,
    ) -> live_20161101_models.SetLiveEdgeTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_edge_transfer_with_options_async(request, runtime)

    def set_live_lazy_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_app_name):
            query['PullAppName'] = request.pull_app_name
        if not UtilClient.is_unset(request.pull_domain_name):
            query['PullDomainName'] = request.pull_domain_name
        if not UtilClient.is_unset(request.pull_protocol):
            query['PullProtocol'] = request.pull_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_lazy_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_app_name):
            query['PullAppName'] = request.pull_app_name
        if not UtilClient.is_unset(request.pull_domain_name):
            query['PullDomainName'] = request.pull_domain_name
        if not UtilClient.is_unset(request.pull_protocol):
            query['PullProtocol'] = request.pull_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_lazy_pull_stream_info_config(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_lazy_pull_stream_info_config_with_options(request, runtime)

    async def set_live_lazy_pull_stream_info_config_async(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_lazy_pull_stream_info_config_with_options_async(request, runtime)

    def set_live_stream_delay_config_with_options(
        self,
        request: live_20161101_models.SetLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.flv_delay):
            query['FlvDelay'] = request.flv_delay
        if not UtilClient.is_unset(request.flv_level):
            query['FlvLevel'] = request.flv_level
        if not UtilClient.is_unset(request.hls_delay):
            query['HlsDelay'] = request.hls_delay
        if not UtilClient.is_unset(request.hls_level):
            query['HlsLevel'] = request.hls_level
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rtmp_delay):
            query['RtmpDelay'] = request.rtmp_delay
        if not UtilClient.is_unset(request.rtmp_level):
            query['RtmpLevel'] = request.rtmp_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamDelayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_stream_delay_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.flv_delay):
            query['FlvDelay'] = request.flv_delay
        if not UtilClient.is_unset(request.flv_level):
            query['FlvLevel'] = request.flv_level
        if not UtilClient.is_unset(request.hls_delay):
            query['HlsDelay'] = request.hls_delay
        if not UtilClient.is_unset(request.hls_level):
            query['HlsLevel'] = request.hls_level
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rtmp_delay):
            query['RtmpDelay'] = request.rtmp_delay
        if not UtilClient.is_unset(request.rtmp_level):
            query['RtmpLevel'] = request.rtmp_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamDelayConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_stream_delay_config(
        self,
        request: live_20161101_models.SetLiveStreamDelayConfigRequest,
    ) -> live_20161101_models.SetLiveStreamDelayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_delay_config_with_options(request, runtime)

    async def set_live_stream_delay_config_async(
        self,
        request: live_20161101_models.SetLiveStreamDelayConfigRequest,
    ) -> live_20161101_models.SetLiveStreamDelayConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_stream_delay_config_with_options_async(request, runtime)

    def set_live_stream_optimized_feature_config_with_options(
        self,
        request: live_20161101_models.SetLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_status):
            query['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_stream_optimized_feature_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_status):
            query['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_stream_optimized_feature_config(
        self,
        request: live_20161101_models.SetLiveStreamOptimizedFeatureConfigRequest,
    ) -> live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_optimized_feature_config_with_options(request, runtime)

    async def set_live_stream_optimized_feature_config_async(
        self,
        request: live_20161101_models.SetLiveStreamOptimizedFeatureConfigRequest,
    ) -> live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_stream_optimized_feature_config_with_options_async(request, runtime)

    def set_live_streams_notify_url_config_with_options(
        self,
        request: live_20161101_models.SetLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_auth_key):
            query['NotifyAuthKey'] = request.notify_auth_key
        if not UtilClient.is_unset(request.notify_req_auth):
            query['NotifyReqAuth'] = request.notify_req_auth
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_auth_key):
            query['NotifyAuthKey'] = request.notify_auth_key
        if not UtilClient.is_unset(request.notify_req_auth):
            query['NotifyReqAuth'] = request.notify_req_auth
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_live_streams_notify_url_config(
        self,
        request: live_20161101_models.SetLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_live_streams_notify_url_config_with_options(request, runtime)

    async def set_live_streams_notify_url_config_async(
        self,
        request: live_20161101_models.SetLiveStreamsNotifyUrlConfigRequest,
    ) -> live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_live_streams_notify_url_config_with_options_async(request, runtime)

    def set_snapshot_callback_auth_with_options(
        self,
        request: live_20161101_models.SetSnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetSnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_auth_key):
            query['CallbackAuthKey'] = request.callback_auth_key
        if not UtilClient.is_unset(request.callback_req_auth):
            query['CallbackReqAuth'] = request.callback_req_auth
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetSnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_snapshot_callback_auth_with_options_async(
        self,
        request: live_20161101_models.SetSnapshotCallbackAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetSnapshotCallbackAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_auth_key):
            query['CallbackAuthKey'] = request.callback_auth_key
        if not UtilClient.is_unset(request.callback_req_auth):
            query['CallbackReqAuth'] = request.callback_req_auth
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetSnapshotCallbackAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_snapshot_callback_auth(
        self,
        request: live_20161101_models.SetSnapshotCallbackAuthRequest,
    ) -> live_20161101_models.SetSnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_snapshot_callback_auth_with_options(request, runtime)

    async def set_snapshot_callback_auth_async(
        self,
        request: live_20161101_models.SetSnapshotCallbackAuthRequest,
    ) -> live_20161101_models.SetSnapshotCallbackAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_snapshot_callback_auth_with_options_async(request, runtime)

    def start_caster_with_options(
        self,
        request: live_20161101_models.StartCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_caster_with_options_async(
        self,
        request: live_20161101_models.StartCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_caster(
        self,
        request: live_20161101_models.StartCasterRequest,
    ) -> live_20161101_models.StartCasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_caster_with_options(request, runtime)

    async def start_caster_async(
        self,
        request: live_20161101_models.StartCasterRequest,
    ) -> live_20161101_models.StartCasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_caster_with_options_async(request, runtime)

    def start_caster_scene_with_options(
        self,
        request: live_20161101_models.StartCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_caster_scene_with_options_async(
        self,
        request: live_20161101_models.StartCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_caster_scene(
        self,
        request: live_20161101_models.StartCasterSceneRequest,
    ) -> live_20161101_models.StartCasterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_caster_scene_with_options(request, runtime)

    async def start_caster_scene_async(
        self,
        request: live_20161101_models.StartCasterSceneRequest,
    ) -> live_20161101_models.StartCasterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_caster_scene_with_options_async(request, runtime)

    def start_live_domain_with_options(
        self,
        request: live_20161101_models.StartLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_live_domain_with_options_async(
        self,
        request: live_20161101_models.StartLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_live_domain(
        self,
        request: live_20161101_models.StartLiveDomainRequest,
    ) -> live_20161101_models.StartLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_live_domain_with_options(request, runtime)

    async def start_live_domain_async(
        self,
        request: live_20161101_models.StartLiveDomainRequest,
    ) -> live_20161101_models.StartLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_live_domain_with_options_async(request, runtime)

    def start_live_stream_monitor_with_options(
        self,
        request: live_20161101_models.StartLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_live_stream_monitor_with_options_async(
        self,
        request: live_20161101_models.StartLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveStreamMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_live_stream_monitor(
        self,
        request: live_20161101_models.StartLiveStreamMonitorRequest,
    ) -> live_20161101_models.StartLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_live_stream_monitor_with_options(request, runtime)

    async def start_live_stream_monitor_async(
        self,
        request: live_20161101_models.StartLiveStreamMonitorRequest,
    ) -> live_20161101_models.StartLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_live_stream_monitor_with_options_async(request, runtime)

    def start_playlist_with_options(
        self,
        request: live_20161101_models.StartPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.resume_mode):
            query['ResumeMode'] = request.resume_mode
        if not UtilClient.is_unset(request.start_item_id):
            query['StartItemId'] = request.start_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_playlist_with_options_async(
        self,
        request: live_20161101_models.StartPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.resume_mode):
            query['ResumeMode'] = request.resume_mode
        if not UtilClient.is_unset(request.start_item_id):
            query['StartItemId'] = request.start_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_playlist(
        self,
        request: live_20161101_models.StartPlaylistRequest,
    ) -> live_20161101_models.StartPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_playlist_with_options(request, runtime)

    async def start_playlist_async(
        self,
        request: live_20161101_models.StartPlaylistRequest,
    ) -> live_20161101_models.StartPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_playlist_with_options_async(request, runtime)

    def stop_caster_with_options(
        self,
        request: live_20161101_models.StopCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_caster_with_options_async(
        self,
        request: live_20161101_models.StopCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_caster(
        self,
        request: live_20161101_models.StopCasterRequest,
    ) -> live_20161101_models.StopCasterResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_with_options(request, runtime)

    async def stop_caster_async(
        self,
        request: live_20161101_models.StopCasterRequest,
    ) -> live_20161101_models.StopCasterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_caster_with_options_async(request, runtime)

    def stop_caster_scene_with_options(
        self,
        request: live_20161101_models.StopCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_caster_scene_with_options_async(
        self,
        request: live_20161101_models.StopCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterSceneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_caster_scene(
        self,
        request: live_20161101_models.StopCasterSceneRequest,
    ) -> live_20161101_models.StopCasterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_scene_with_options(request, runtime)

    async def stop_caster_scene_async(
        self,
        request: live_20161101_models.StopCasterSceneRequest,
    ) -> live_20161101_models.StopCasterSceneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_caster_scene_with_options_async(request, runtime)

    def stop_live_domain_with_options(
        self,
        request: live_20161101_models.StopLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_domain_with_options_async(
        self,
        request: live_20161101_models.StopLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_live_domain(
        self,
        request: live_20161101_models.StopLiveDomainRequest,
    ) -> live_20161101_models.StopLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_domain_with_options(request, runtime)

    async def stop_live_domain_async(
        self,
        request: live_20161101_models.StopLiveDomainRequest,
    ) -> live_20161101_models.StopLiveDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_domain_with_options_async(request, runtime)

    def stop_live_stream_monitor_with_options(
        self,
        request: live_20161101_models.StopLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_stream_monitor_with_options_async(
        self,
        request: live_20161101_models.StopLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveStreamMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_live_stream_monitor(
        self,
        request: live_20161101_models.StopLiveStreamMonitorRequest,
    ) -> live_20161101_models.StopLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_stream_monitor_with_options(request, runtime)

    async def stop_live_stream_monitor_async(
        self,
        request: live_20161101_models.StopLiveStreamMonitorRequest,
    ) -> live_20161101_models.StopLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_stream_monitor_with_options_async(request, runtime)

    def stop_playlist_with_options(
        self,
        request: live_20161101_models.StopPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_playlist_with_options_async(
        self,
        request: live_20161101_models.StopPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopPlaylistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_playlist(
        self,
        request: live_20161101_models.StopPlaylistRequest,
    ) -> live_20161101_models.StopPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_playlist_with_options(request, runtime)

    async def stop_playlist_async(
        self,
        request: live_20161101_models.StopPlaylistRequest,
    ) -> live_20161101_models.StopPlaylistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_playlist_with_options_async(request, runtime)

    def tag_live_resources_with_options(
        self,
        request: live_20161101_models.TagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.TagLiveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.TagLiveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_live_resources_with_options_async(
        self,
        request: live_20161101_models.TagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.TagLiveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.TagLiveResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_live_resources(
        self,
        request: live_20161101_models.TagLiveResourcesRequest,
    ) -> live_20161101_models.TagLiveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_live_resources_with_options(request, runtime)

    async def tag_live_resources_async(
        self,
        request: live_20161101_models.TagLiveResourcesRequest,
    ) -> live_20161101_models.TagLiveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_live_resources_with_options_async(request, runtime)

    def un_tag_live_resources_with_options(
        self,
        request: live_20161101_models.UnTagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UnTagLiveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UnTagLiveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_live_resources_with_options_async(
        self,
        request: live_20161101_models.UnTagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UnTagLiveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UnTagLiveResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_live_resources(
        self,
        request: live_20161101_models.UnTagLiveResourcesRequest,
    ) -> live_20161101_models.UnTagLiveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_live_resources_with_options(request, runtime)

    async def un_tag_live_resources_async(
        self,
        request: live_20161101_models.UnTagLiveResourcesRequest,
    ) -> live_20161101_models.UnTagLiveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_live_resources_with_options_async(request, runtime)

    def update_caster_scene_audio_with_options(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.follow_enable):
            query['FollowEnable'] = request.follow_enable
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneAudioResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_caster_scene_audio_with_options_async(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.follow_enable):
            query['FollowEnable'] = request.follow_enable
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneAudioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_caster_scene_audio(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_audio_with_options(request, runtime)

    async def update_caster_scene_audio_async(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_caster_scene_audio_with_options_async(request, runtime)

    def update_caster_scene_config_with_options(
        self,
        request: live_20161101_models.UpdateCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.UpdateCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_caster_scene_config(
        self,
        request: live_20161101_models.UpdateCasterSceneConfigRequest,
    ) -> live_20161101_models.UpdateCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_config_with_options(request, runtime)

    async def update_caster_scene_config_async(
        self,
        request: live_20161101_models.UpdateCasterSceneConfigRequest,
    ) -> live_20161101_models.UpdateCasterSceneConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_caster_scene_config_with_options_async(request, runtime)

    def update_live_app_snapshot_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAppSnapshotConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_app_snapshot_config(
        self,
        request: live_20161101_models.UpdateLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.UpdateLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_app_snapshot_config_with_options(request, runtime)

    async def update_live_app_snapshot_config_async(
        self,
        request: live_20161101_models.UpdateLiveAppSnapshotConfigRequest,
    ) -> live_20161101_models.UpdateLiveAppSnapshotConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_app_snapshot_config_with_options_async(request, runtime)

    def update_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_audio_audit_config(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_config_with_options(request, runtime)

    async def update_live_audio_audit_config_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_audio_audit_config_with_options_async(request, runtime)

    def update_live_audio_audit_notify_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_audio_audit_notify_config(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_notify_config_with_options(request, runtime)

    async def update_live_audio_audit_notify_config_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_audio_audit_notify_config_with_options_async(request, runtime)

    def update_live_detect_notify_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveDetectNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_detect_notify_config(
        self,
        request: live_20161101_models.UpdateLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_detect_notify_config_with_options(request, runtime)

    async def update_live_detect_notify_config_async(
        self,
        request: live_20161101_models.UpdateLiveDetectNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveDetectNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_detect_notify_config_with_options_async(request, runtime)

    def update_live_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.UpdateLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLivePullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_pull_stream_info_config(
        self,
        request: live_20161101_models.UpdateLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.UpdateLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_pull_stream_info_config_with_options(request, runtime)

    async def update_live_pull_stream_info_config_async(
        self,
        request: live_20161101_models.UpdateLivePullStreamInfoConfigRequest,
    ) -> live_20161101_models.UpdateLivePullStreamInfoConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_pull_stream_info_config_with_options_async(request, runtime)

    def update_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveRecordNotifyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_record_notify_config(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_notify_config_with_options(request, runtime)

    async def update_live_record_notify_config_async(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_record_notify_config_with_options_async(request, runtime)

    def update_live_snapshot_detect_porn_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_snapshot_detect_porn_config(
        self,
        request: live_20161101_models.UpdateLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_snapshot_detect_porn_config_with_options(request, runtime)

    async def update_live_snapshot_detect_porn_config_async(
        self,
        request: live_20161101_models.UpdateLiveSnapshotDetectPornConfigRequest,
    ) -> live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_snapshot_detect_porn_config_with_options_async(request, runtime)

    def update_live_stream_monitor_with_options(
        self,
        request: live_20161101_models.UpdateLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_stream_monitor_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveStreamMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_stream_monitor(
        self,
        request: live_20161101_models.UpdateLiveStreamMonitorRequest,
    ) -> live_20161101_models.UpdateLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_monitor_with_options(request, runtime)

    async def update_live_stream_monitor_async(
        self,
        request: live_20161101_models.UpdateLiveStreamMonitorRequest,
    ) -> live_20161101_models.UpdateLiveStreamMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_stream_monitor_with_options_async(request, runtime)

    def update_live_stream_watermark_with_options(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_stream_watermark_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_stream_watermark(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRequest,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_watermark_with_options(request, runtime)

    async def update_live_stream_watermark_async(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRequest,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_stream_watermark_with_options_async(request, runtime)

    def update_live_stream_watermark_rule_with_options(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_stream_watermark_rule_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_stream_watermark_rule(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_watermark_rule_with_options(request, runtime)

    async def update_live_stream_watermark_rule_async(
        self,
        request: live_20161101_models.UpdateLiveStreamWatermarkRuleRequest,
    ) -> live_20161101_models.UpdateLiveStreamWatermarkRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_stream_watermark_rule_with_options_async(request, runtime)

    def update_live_top_level_domain_with_options(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTopLevelDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveTopLevelDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_top_level_domain_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTopLevelDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveTopLevelDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_top_level_domain(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_top_level_domain_with_options(request, runtime)

    async def update_live_top_level_domain_async(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_top_level_domain_with_options_async(request, runtime)

    def update_mix_stream_with_options(
        self,
        request: live_20161101_models.UpdateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mix_stream_with_options_async(
        self,
        request: live_20161101_models.UpdateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateMixStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateMixStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mix_stream(
        self,
        request: live_20161101_models.UpdateMixStreamRequest,
    ) -> live_20161101_models.UpdateMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mix_stream_with_options(request, runtime)

    async def update_mix_stream_async(
        self,
        request: live_20161101_models.UpdateMixStreamRequest,
    ) -> live_20161101_models.UpdateMixStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mix_stream_with_options_async(request, runtime)

    def verify_live_domain_owner_with_options(
        self,
        request: live_20161101_models.VerifyLiveDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.VerifyLiveDomainOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyLiveDomainOwner',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.VerifyLiveDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_live_domain_owner_with_options_async(
        self,
        request: live_20161101_models.VerifyLiveDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.VerifyLiveDomainOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyLiveDomainOwner',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.VerifyLiveDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_live_domain_owner(
        self,
        request: live_20161101_models.VerifyLiveDomainOwnerRequest,
    ) -> live_20161101_models.VerifyLiveDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_live_domain_owner_with_options(request, runtime)

    async def verify_live_domain_owner_async(
        self,
        request: live_20161101_models.VerifyLiveDomainOwnerRequest,
    ) -> live_20161101_models.VerifyLiveDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_live_domain_owner_with_options_async(request, runtime)

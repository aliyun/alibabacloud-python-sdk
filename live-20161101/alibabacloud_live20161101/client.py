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
            'ap-northeast-2-pop': 'live.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'live.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'live.ap-southeast-1.aliyuncs.com',
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
            'cn-yushanfang': 'live.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'live.aliyuncs.com',
            'cn-zhangjiakou': 'live.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'live.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'live.aliyuncs.com',
            'eu-west-1': 'live.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'live.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'live.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'live.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'live.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'live.ap-southeast-1.aliyuncs.com'
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterComponentResponse(),
            self.do_rpcrequest('AddCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_component_with_options_async(
        self,
        request: live_20161101_models.AddCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterComponentResponse(),
            await self.do_rpcrequest_async('AddCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeResponse(),
            self.do_rpcrequest('AddCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_episode_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeResponse(),
            await self.do_rpcrequest_async('AddCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupResponse(),
            self.do_rpcrequest('AddCasterEpisodeGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_episode_group_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupResponse(),
            await self.do_rpcrequest_async('AddCasterEpisodeGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupContentResponse(),
            self.do_rpcrequest('AddCasterEpisodeGroupContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_episode_group_content_with_options_async(
        self,
        request: live_20161101_models.AddCasterEpisodeGroupContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterEpisodeGroupContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupContentResponse(),
            await self.do_rpcrequest_async('AddCasterEpisodeGroupContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterLayoutResponse(),
            self.do_rpcrequest('AddCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_layout_with_options_async(
        self,
        request: live_20161101_models.AddCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterLayoutResponse(),
            await self.do_rpcrequest_async('AddCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterProgramResponse(),
            self.do_rpcrequest('AddCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_program_with_options_async(
        self,
        request: live_20161101_models.AddCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterProgramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterProgramResponse(),
            await self.do_rpcrequest_async('AddCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterVideoResourceResponse(),
            self.do_rpcrequest('AddCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.AddCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterVideoResourceResponse(),
            await self.do_rpcrequest_async('AddCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCustomLiveStreamTranscodeResponse(),
            self.do_rpcrequest('AddCustomLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_custom_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddCustomLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddCustomLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddCustomLiveStreamTranscodeResponse(),
            await self.do_rpcrequest_async('AddCustomLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_drmcertificate_with_options(
        self,
        request: live_20161101_models.AddDRMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddDRMCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddDRMCertificateResponse(),
            self.do_rpcrequest('AddDRMCertificate', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_drmcertificate_with_options_async(
        self,
        request: live_20161101_models.AddDRMCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddDRMCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddDRMCertificateResponse(),
            await self.do_rpcrequest_async('AddDRMCertificate', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_drmcertificate(
        self,
        request: live_20161101_models.AddDRMCertificateRequest,
    ) -> live_20161101_models.AddDRMCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_drmcertificate_with_options(request, runtime)

    async def add_drmcertificate_async(
        self,
        request: live_20161101_models.AddDRMCertificateRequest,
    ) -> live_20161101_models.AddDRMCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_drmcertificate_with_options_async(request, runtime)

    def add_live_app_record_config_with_options(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppRecordConfigResponse(),
            self.do_rpcrequest('AddLiveAppRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_app_record_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppRecordConfigResponse(),
            await self.do_rpcrequest_async('AddLiveAppRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppSnapshotConfigResponse(),
            self.do_rpcrequest('AddLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppSnapshotConfigResponse(),
            await self.do_rpcrequest_async('AddLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_live_asrconfig_with_options(
        self,
        request: live_20161101_models.AddLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveASRConfigResponse(),
            self.do_rpcrequest('AddLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_asrconfig_with_options_async(
        self,
        request: live_20161101_models.AddLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveASRConfigResponse(),
            await self.do_rpcrequest_async('AddLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_live_asrconfig(
        self,
        request: live_20161101_models.AddLiveASRConfigRequest,
    ) -> live_20161101_models.AddLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_live_asrconfig_with_options(request, runtime)

    async def add_live_asrconfig_async(
        self,
        request: live_20161101_models.AddLiveASRConfigRequest,
    ) -> live_20161101_models.AddLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_live_asrconfig_with_options_async(request, runtime)

    def add_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditConfigResponse(),
            self.do_rpcrequest('AddLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditConfigResponse(),
            await self.do_rpcrequest_async('AddLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditNotifyConfigResponse(),
            self.do_rpcrequest('AddLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditNotifyConfigResponse(),
            await self.do_rpcrequest_async('AddLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDetectNotifyConfigResponse(),
            self.do_rpcrequest('AddLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDetectNotifyConfigResponse(),
            await self.do_rpcrequest_async('AddLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainResponse(),
            self.do_rpcrequest('AddLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_domain_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainResponse(),
            await self.do_rpcrequest_async('AddLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainMappingResponse(),
            self.do_rpcrequest('AddLiveDomainMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainMappingResponse(),
            await self.do_rpcrequest_async('AddLiveDomainMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainPlayMappingResponse(),
            self.do_rpcrequest('AddLiveDomainPlayMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_domain_play_mapping_with_options_async(
        self,
        request: live_20161101_models.AddLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainPlayMappingResponse(),
            await self.do_rpcrequest_async('AddLiveDomainPlayMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLivePullStreamInfoConfigResponse(),
            self.do_rpcrequest('AddLivePullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.AddLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLivePullStreamInfoConfigResponse(),
            await self.do_rpcrequest_async('AddLivePullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordNotifyConfigResponse(),
            self.do_rpcrequest('AddLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordNotifyConfigResponse(),
            await self.do_rpcrequest_async('AddLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordVodConfigResponse(),
            self.do_rpcrequest('AddLiveRecordVodConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_record_vod_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordVodConfigResponse(),
            await self.do_rpcrequest_async('AddLiveRecordVodConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveSnapshotDetectPornConfigResponse(),
            self.do_rpcrequest('AddLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.AddLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveSnapshotDetectPornConfigResponse(),
            await self.do_rpcrequest_async('AddLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamTranscodeResponse(),
            self.do_rpcrequest('AddLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamTranscodeResponse(),
            await self.do_rpcrequest_async('AddLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_multi_rate_config_with_options(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddMultiRateConfigResponse(),
            self.do_rpcrequest('AddMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.AddMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddMultiRateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddMultiRateConfigResponse(),
            await self.do_rpcrequest_async('AddMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddPlaylistItemsResponse(),
            self.do_rpcrequest('AddPlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_playlist_items_with_options_async(
        self,
        request: live_20161101_models.AddPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddPlaylistItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddPlaylistItemsResponse(),
            await self.do_rpcrequest_async('AddPlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddRtsLiveStreamTranscodeResponse(),
            self.do_rpcrequest('AddRtsLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_rts_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.AddRtsLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddRtsLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddRtsLiveStreamTranscodeResponse(),
            await self.do_rpcrequest_async('AddRtsLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_studio_layout_with_options(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddStudioLayoutResponse(),
            self.do_rpcrequest('AddStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_studio_layout_with_options_async(
        self,
        request: live_20161101_models.AddStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddStudioLayoutResponse(),
            await self.do_rpcrequest_async('AddStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddTrancodeSEIResponse(),
            self.do_rpcrequest('AddTrancodeSEI', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_trancode_seiwith_options_async(
        self,
        request: live_20161101_models.AddTrancodeSEIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AddTrancodeSEIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AddTrancodeSEIResponse(),
            await self.do_rpcrequest_async('AddTrancodeSEI', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AllowPushStreamResponse(),
            self.do_rpcrequest('AllowPushStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allow_push_stream_with_options_async(
        self,
        request: live_20161101_models.AllowPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.AllowPushStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.AllowPushStreamResponse(),
            await self.do_rpcrequest_async('AllowPushStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def apply_board_token_with_options(
        self,
        request: live_20161101_models.ApplyBoardTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ApplyBoardTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ApplyBoardTokenResponse(),
            self.do_rpcrequest('ApplyBoardToken', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_board_token_with_options_async(
        self,
        request: live_20161101_models.ApplyBoardTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ApplyBoardTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ApplyBoardTokenResponse(),
            await self.do_rpcrequest_async('ApplyBoardToken', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_board_token(
        self,
        request: live_20161101_models.ApplyBoardTokenRequest,
    ) -> live_20161101_models.ApplyBoardTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_board_token_with_options(request, runtime)

    async def apply_board_token_async(
        self,
        request: live_20161101_models.ApplyBoardTokenRequest,
    ) -> live_20161101_models.ApplyBoardTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_board_token_with_options_async(request, runtime)

    def apply_record_token_with_options(
        self,
        request: live_20161101_models.ApplyRecordTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ApplyRecordTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ApplyRecordTokenResponse(),
            self.do_rpcrequest('ApplyRecordToken', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_record_token_with_options_async(
        self,
        request: live_20161101_models.ApplyRecordTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ApplyRecordTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ApplyRecordTokenResponse(),
            await self.do_rpcrequest_async('ApplyRecordToken', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_record_token(
        self,
        request: live_20161101_models.ApplyRecordTokenRequest,
    ) -> live_20161101_models.ApplyRecordTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_record_token_with_options(request, runtime)

    async def apply_record_token_async(
        self,
        request: live_20161101_models.ApplyRecordTokenRequest,
    ) -> live_20161101_models.ApplyRecordTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_record_token_with_options_async(request, runtime)

    def batch_delete_live_domain_configs_with_options(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.BatchDeleteLiveDomainConfigsResponse(),
            self.do_rpcrequest('BatchDeleteLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.BatchDeleteLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchDeleteLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.BatchDeleteLiveDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchDeleteLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.BatchSetLiveDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.BatchSetLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.BatchSetLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.BatchSetLiveDomainConfigsResponse(),
            await self.do_rpcrequest_async('BatchSetLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def check_service_for_role_with_options(
        self,
        request: live_20161101_models.CheckServiceForRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CheckServiceForRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CheckServiceForRoleResponse(),
            self.do_rpcrequest('CheckServiceForRole', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_for_role_with_options_async(
        self,
        request: live_20161101_models.CheckServiceForRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CheckServiceForRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CheckServiceForRoleResponse(),
            await self.do_rpcrequest_async('CheckServiceForRole', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_for_role(
        self,
        request: live_20161101_models.CheckServiceForRoleRequest,
    ) -> live_20161101_models.CheckServiceForRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_for_role_with_options(request, runtime)

    async def check_service_for_role_async(
        self,
        request: live_20161101_models.CheckServiceForRoleRequest,
    ) -> live_20161101_models.CheckServiceForRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_for_role_with_options_async(request, runtime)

    def close_live_shift_with_options(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CloseLiveShiftResponse(),
            self.do_rpcrequest('CloseLiveShift', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_live_shift_with_options_async(
        self,
        request: live_20161101_models.CloseLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CloseLiveShiftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CloseLiveShiftResponse(),
            await self.do_rpcrequest_async('CloseLiveShift', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def complete_board_with_options(
        self,
        request: live_20161101_models.CompleteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CompleteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CompleteBoardResponse(),
            self.do_rpcrequest('CompleteBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_board_with_options_async(
        self,
        request: live_20161101_models.CompleteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CompleteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CompleteBoardResponse(),
            await self.do_rpcrequest_async('CompleteBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_board(
        self,
        request: live_20161101_models.CompleteBoardRequest,
    ) -> live_20161101_models.CompleteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_board_with_options(request, runtime)

    async def complete_board_async(
        self,
        request: live_20161101_models.CompleteBoardRequest,
    ) -> live_20161101_models.CompleteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_board_with_options_async(request, runtime)

    def complete_board_record_with_options(
        self,
        request: live_20161101_models.CompleteBoardRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CompleteBoardRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CompleteBoardRecordResponse(),
            self.do_rpcrequest('CompleteBoardRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_board_record_with_options_async(
        self,
        request: live_20161101_models.CompleteBoardRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CompleteBoardRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CompleteBoardRecordResponse(),
            await self.do_rpcrequest_async('CompleteBoardRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_board_record(
        self,
        request: live_20161101_models.CompleteBoardRecordRequest,
    ) -> live_20161101_models.CompleteBoardRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_board_record_with_options(request, runtime)

    async def complete_board_record_async(
        self,
        request: live_20161101_models.CompleteBoardRecordRequest,
    ) -> live_20161101_models.CompleteBoardRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_board_record_with_options_async(request, runtime)

    def control_html_resource_with_options(
        self,
        request: live_20161101_models.ControlHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ControlHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ControlHtmlResourceResponse(),
            self.do_rpcrequest('ControlHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def control_html_resource_with_options_async(
        self,
        request: live_20161101_models.ControlHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ControlHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ControlHtmlResourceResponse(),
            await self.do_rpcrequest_async('ControlHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def control_html_resource(
        self,
        request: live_20161101_models.ControlHtmlResourceRequest,
    ) -> live_20161101_models.ControlHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.control_html_resource_with_options(request, runtime)

    async def control_html_resource_async(
        self,
        request: live_20161101_models.ControlHtmlResourceRequest,
    ) -> live_20161101_models.ControlHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.control_html_resource_with_options_async(request, runtime)

    def copy_caster_with_options(
        self,
        request: live_20161101_models.CopyCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterResponse(),
            self.do_rpcrequest('CopyCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_caster_with_options_async(
        self,
        request: live_20161101_models.CopyCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterResponse(),
            await self.do_rpcrequest_async('CopyCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterSceneConfigResponse(),
            self.do_rpcrequest('CopyCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.CopyCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CopyCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterSceneConfigResponse(),
            await self.do_rpcrequest_async('CopyCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_board_with_options(
        self,
        request: live_20161101_models.CreateBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateBoardResponse(),
            self.do_rpcrequest('CreateBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_board_with_options_async(
        self,
        request: live_20161101_models.CreateBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateBoardResponse(),
            await self.do_rpcrequest_async('CreateBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_board(
        self,
        request: live_20161101_models.CreateBoardRequest,
    ) -> live_20161101_models.CreateBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_board_with_options(request, runtime)

    async def create_board_async(
        self,
        request: live_20161101_models.CreateBoardRequest,
    ) -> live_20161101_models.CreateBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_board_with_options_async(request, runtime)

    def create_caster_with_options(
        self,
        request: live_20161101_models.CreateCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCasterResponse(),
            self.do_rpcrequest('CreateCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_caster_with_options_async(
        self,
        request: live_20161101_models.CreateCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCasterResponse(),
            await self.do_rpcrequest_async('CreateCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_live_real_time_log_delivery_with_options(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveRealTimeLogDeliveryResponse(),
            self.do_rpcrequest('CreateLiveRealTimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_live_real_time_log_delivery_with_options_async(
        self,
        request: live_20161101_models.CreateLiveRealTimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveRealTimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveRealTimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('CreateLiveRealTimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def create_live_stream_record_index_files_with_options(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamRecordIndexFilesResponse(),
            self.do_rpcrequest('CreateLiveStreamRecordIndexFiles', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_live_stream_record_index_files_with_options_async(
        self,
        request: live_20161101_models.CreateLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamRecordIndexFilesResponse(),
            await self.do_rpcrequest_async('CreateLiveStreamRecordIndexFiles', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_mix_stream_with_options(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMixStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMixStreamResponse(),
            self.do_rpcrequest('CreateMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mix_stream_with_options_async(
        self,
        request: live_20161101_models.CreateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateMixStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMixStreamResponse(),
            await self.do_rpcrequest_async('CreateMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_room_with_options(
        self,
        request: live_20161101_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_room_with_options_async(
        self,
        request: live_20161101_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.CreateRoomResponse(),
            await self.do_rpcrequest_async('CreateRoom', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(
        self,
        request: live_20161101_models.CreateRoomRequest,
    ) -> live_20161101_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: live_20161101_models.CreateRoomRequest,
    ) -> live_20161101_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)

    def delete_board_with_options(
        self,
        request: live_20161101_models.DeleteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteBoardResponse(),
            self.do_rpcrequest('DeleteBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_board_with_options_async(
        self,
        request: live_20161101_models.DeleteBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteBoardResponse(),
            await self.do_rpcrequest_async('DeleteBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_board(
        self,
        request: live_20161101_models.DeleteBoardRequest,
    ) -> live_20161101_models.DeleteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_board_with_options(request, runtime)

    async def delete_board_async(
        self,
        request: live_20161101_models.DeleteBoardRequest,
    ) -> live_20161101_models.DeleteBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_board_with_options_async(request, runtime)

    def delete_caster_with_options(
        self,
        request: live_20161101_models.DeleteCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterResponse(),
            self.do_rpcrequest('DeleteCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterResponse(),
            await self.do_rpcrequest_async('DeleteCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterComponentResponse(),
            self.do_rpcrequest('DeleteCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_component_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterComponentResponse(),
            await self.do_rpcrequest_async('DeleteCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeResponse(),
            self.do_rpcrequest('DeleteCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_episode_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeResponse(),
            await self.do_rpcrequest_async('DeleteCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeGroupResponse(),
            self.do_rpcrequest('DeleteCasterEpisodeGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_episode_group_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterEpisodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterEpisodeGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeGroupResponse(),
            await self.do_rpcrequest_async('DeleteCasterEpisodeGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterLayoutResponse(),
            self.do_rpcrequest('DeleteCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_layout_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterLayoutResponse(),
            await self.do_rpcrequest_async('DeleteCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterProgramResponse(),
            self.do_rpcrequest('DeleteCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_program_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterProgramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterProgramResponse(),
            await self.do_rpcrequest_async('DeleteCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterSceneConfigResponse(),
            self.do_rpcrequest('DeleteCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterSceneConfigResponse(),
            await self.do_rpcrequest_async('DeleteCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterVideoResourceResponse(),
            self.do_rpcrequest('DeleteCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.DeleteCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterVideoResourceResponse(),
            await self.do_rpcrequest_async('DeleteCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_html_resource_with_options(
        self,
        request: live_20161101_models.DeleteHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteHtmlResourceResponse(),
            self.do_rpcrequest('DeleteHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_html_resource_with_options_async(
        self,
        request: live_20161101_models.DeleteHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteHtmlResourceResponse(),
            await self.do_rpcrequest_async('DeleteHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_html_resource(
        self,
        request: live_20161101_models.DeleteHtmlResourceRequest,
    ) -> live_20161101_models.DeleteHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_html_resource_with_options(request, runtime)

    async def delete_html_resource_async(
        self,
        request: live_20161101_models.DeleteHtmlResourceRequest,
    ) -> live_20161101_models.DeleteHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_html_resource_with_options_async(request, runtime)

    def delete_live_app_record_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppRecordConfigResponse(),
            self.do_rpcrequest('DeleteLiveAppRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_app_record_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAppRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppRecordConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppRecordConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveAppRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppSnapshotConfigResponse(),
            self.do_rpcrequest('DeleteLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppSnapshotConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_live_asrconfig_with_options(
        self,
        request: live_20161101_models.DeleteLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveASRConfigResponse(),
            self.do_rpcrequest('DeleteLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_asrconfig_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveASRConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_live_asrconfig(
        self,
        request: live_20161101_models.DeleteLiveASRConfigRequest,
    ) -> live_20161101_models.DeleteLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_asrconfig_with_options(request, runtime)

    async def delete_live_asrconfig_async(
        self,
        request: live_20161101_models.DeleteLiveASRConfigRequest,
    ) -> live_20161101_models.DeleteLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_asrconfig_with_options_async(request, runtime)

    def delete_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditConfigResponse(),
            self.do_rpcrequest('DeleteLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse(),
            self.do_rpcrequest('DeleteLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDetectNotifyConfigResponse(),
            self.do_rpcrequest('DeleteLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDetectNotifyConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainResponse(),
            self.do_rpcrequest('DeleteLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_domain_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainResponse(),
            await self.do_rpcrequest_async('DeleteLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainMappingResponse(),
            self.do_rpcrequest('DeleteLiveDomainMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainMappingResponse(),
            await self.do_rpcrequest_async('DeleteLiveDomainMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainPlayMappingResponse(),
            self.do_rpcrequest('DeleteLiveDomainPlayMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_domain_play_mapping_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveDomainPlayMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveDomainPlayMappingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainPlayMappingResponse(),
            await self.do_rpcrequest_async('DeleteLiveDomainPlayMapping', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_live_lazy_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse(),
            self.do_rpcrequest('DeleteLiveLazyPullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_lazy_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveLazyPullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLivePullStreamInfoConfigResponse(),
            self.do_rpcrequest('DeleteLivePullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLivePullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLivePullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLivePullStreamInfoConfigResponse(),
            await self.do_rpcrequest_async('DeleteLivePullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DeleteLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DeleteLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def delete_live_real_time_log_logstore_with_options(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse(),
            self.do_rpcrequest('DeleteLiveRealTimeLogLogstore', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_live_real_time_log_logstore_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRealTimeLogLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse(),
            await self.do_rpcrequest_async('DeleteLiveRealTimeLogLogstore', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def delete_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordNotifyConfigResponse(),
            self.do_rpcrequest('DeleteLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordNotifyConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordVodConfigResponse(),
            self.do_rpcrequest('DeleteLiveRecordVodConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_record_vod_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveRecordVodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveRecordVodConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordVodConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveRecordVodConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse(),
            self.do_rpcrequest('DeleteLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_live_streams_notify_url_config_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('DeleteLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse(),
            await self.do_rpcrequest_async('DeleteLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_live_stream_transcode_with_options(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamTranscodeResponse(),
            self.do_rpcrequest('DeleteLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_live_stream_transcode_with_options_async(
        self,
        request: live_20161101_models.DeleteLiveStreamTranscodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteLiveStreamTranscodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamTranscodeResponse(),
            await self.do_rpcrequest_async('DeleteLiveStreamTranscode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_mix_stream_with_options(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMixStreamResponse(),
            self.do_rpcrequest('DeleteMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mix_stream_with_options_async(
        self,
        request: live_20161101_models.DeleteMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMixStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMixStreamResponse(),
            await self.do_rpcrequest_async('DeleteMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMultiRateConfigResponse(),
            self.do_rpcrequest('DeleteMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.DeleteMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteMultiRateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMultiRateConfigResponse(),
            await self.do_rpcrequest_async('DeleteMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistResponse(),
            self.do_rpcrequest('DeletePlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_playlist_with_options_async(
        self,
        request: live_20161101_models.DeletePlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistResponse(),
            await self.do_rpcrequest_async('DeletePlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistItemsResponse(),
            self.do_rpcrequest('DeletePlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_playlist_items_with_options_async(
        self,
        request: live_20161101_models.DeletePlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeletePlaylistItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistItemsResponse(),
            await self.do_rpcrequest_async('DeletePlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteRoomResponse(),
            self.do_rpcrequest('DeleteRoom', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_room_with_options_async(
        self,
        request: live_20161101_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteRoomResponse(),
            await self.do_rpcrequest_async('DeleteRoom', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_studio_layout_with_options(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteStudioLayoutResponse(),
            self.do_rpcrequest('DeleteStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_studio_layout_with_options_async(
        self,
        request: live_20161101_models.DeleteStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DeleteStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteStudioLayoutResponse(),
            await self.do_rpcrequest_async('DeleteStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_board_events_with_options(
        self,
        request: live_20161101_models.DescribeBoardEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardEventsResponse(),
            self.do_rpcrequest('DescribeBoardEvents', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_board_events_with_options_async(
        self,
        request: live_20161101_models.DescribeBoardEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardEventsResponse(),
            await self.do_rpcrequest_async('DescribeBoardEvents', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_board_events(
        self,
        request: live_20161101_models.DescribeBoardEventsRequest,
    ) -> live_20161101_models.DescribeBoardEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_board_events_with_options(request, runtime)

    async def describe_board_events_async(
        self,
        request: live_20161101_models.DescribeBoardEventsRequest,
    ) -> live_20161101_models.DescribeBoardEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_board_events_with_options_async(request, runtime)

    def describe_boards_with_options(
        self,
        request: live_20161101_models.DescribeBoardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardsResponse(),
            self.do_rpcrequest('DescribeBoards', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_boards_with_options_async(
        self,
        request: live_20161101_models.DescribeBoardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardsResponse(),
            await self.do_rpcrequest_async('DescribeBoards', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_boards(
        self,
        request: live_20161101_models.DescribeBoardsRequest,
    ) -> live_20161101_models.DescribeBoardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_boards_with_options(request, runtime)

    async def describe_boards_async(
        self,
        request: live_20161101_models.DescribeBoardsRequest,
    ) -> live_20161101_models.DescribeBoardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_boards_with_options_async(request, runtime)

    def describe_board_snapshot_with_options(
        self,
        request: live_20161101_models.DescribeBoardSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardSnapshotResponse(),
            self.do_rpcrequest('DescribeBoardSnapshot', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_board_snapshot_with_options_async(
        self,
        request: live_20161101_models.DescribeBoardSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeBoardSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeBoardSnapshotResponse(),
            await self.do_rpcrequest_async('DescribeBoardSnapshot', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_board_snapshot(
        self,
        request: live_20161101_models.DescribeBoardSnapshotRequest,
    ) -> live_20161101_models.DescribeBoardSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_board_snapshot_with_options(request, runtime)

    async def describe_board_snapshot_async(
        self,
        request: live_20161101_models.DescribeBoardSnapshotRequest,
    ) -> live_20161101_models.DescribeBoardSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_board_snapshot_with_options_async(request, runtime)

    def describe_caster_channels_with_options(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterChannelsResponse(),
            self.do_rpcrequest('DescribeCasterChannels', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_channels_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterChannelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterChannelsResponse(),
            await self.do_rpcrequest_async('DescribeCasterChannels', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterComponentsResponse(),
            self.do_rpcrequest('DescribeCasterComponents', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_components_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterComponentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterComponentsResponse(),
            await self.do_rpcrequest_async('DescribeCasterComponents', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterConfigResponse(),
            self.do_rpcrequest('DescribeCasterConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_config_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterConfigResponse(),
            await self.do_rpcrequest_async('DescribeCasterConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterLayoutsResponse(),
            self.do_rpcrequest('DescribeCasterLayouts', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_layouts_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterLayoutsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterLayoutsResponse(),
            await self.do_rpcrequest_async('DescribeCasterLayouts', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterProgramResponse(),
            self.do_rpcrequest('DescribeCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_program_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterProgramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterProgramResponse(),
            await self.do_rpcrequest_async('DescribeCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_caster_rtc_info_with_options(
        self,
        request: live_20161101_models.DescribeCasterRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterRtcInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterRtcInfoResponse(),
            self.do_rpcrequest('DescribeCasterRtcInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_rtc_info_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterRtcInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterRtcInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterRtcInfoResponse(),
            await self.do_rpcrequest_async('DescribeCasterRtcInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_caster_rtc_info(
        self,
        request: live_20161101_models.DescribeCasterRtcInfoRequest,
    ) -> live_20161101_models.DescribeCasterRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_rtc_info_with_options(request, runtime)

    async def describe_caster_rtc_info_async(
        self,
        request: live_20161101_models.DescribeCasterRtcInfoRequest,
    ) -> live_20161101_models.DescribeCasterRtcInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_caster_rtc_info_with_options_async(request, runtime)

    def describe_casters_with_options(
        self,
        request: live_20161101_models.DescribeCastersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCastersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCastersResponse(),
            self.do_rpcrequest('DescribeCasters', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_casters_with_options_async(
        self,
        request: live_20161101_models.DescribeCastersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCastersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCastersResponse(),
            await self.do_rpcrequest_async('DescribeCasters', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_caster_scene_audio_with_options(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSceneAudioResponse(),
            self.do_rpcrequest('DescribeCasterSceneAudio', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_scene_audio_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSceneAudioResponse(),
            await self.do_rpcrequest_async('DescribeCasterSceneAudio', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterScenesResponse(),
            self.do_rpcrequest('DescribeCasterScenes', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_scenes_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterScenesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterScenesResponse(),
            await self.do_rpcrequest_async('DescribeCasterScenes', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterStreamUrlResponse(),
            self.do_rpcrequest('DescribeCasterStreamUrl', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_stream_url_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterStreamUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterStreamUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterStreamUrlResponse(),
            await self.do_rpcrequest_async('DescribeCasterStreamUrl', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSyncGroupResponse(),
            self.do_rpcrequest('DescribeCasterSyncGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_sync_group_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSyncGroupResponse(),
            await self.do_rpcrequest_async('DescribeCasterSyncGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterVideoResourcesResponse(),
            self.do_rpcrequest('DescribeCasterVideoResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_caster_video_resources_with_options_async(
        self,
        request: live_20161101_models.DescribeCasterVideoResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeCasterVideoResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterVideoResourcesResponse(),
            await self.do_rpcrequest_async('DescribeCasterVideoResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_domain_usage_data_with_options(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainUsageDataResponse(),
            self.do_rpcrequest('DescribeDomainUsageData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_usage_data_with_options_async(
        self,
        request: live_20161101_models.DescribeDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainUsageDataResponse(),
            await self.do_rpcrequest_async('DescribeDomainUsageData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_drmcert_list_with_options(
        self,
        request: live_20161101_models.DescribeDRMCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDRMCertListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDRMCertListResponse(),
            self.do_rpcrequest('DescribeDRMCertList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drmcert_list_with_options_async(
        self,
        request: live_20161101_models.DescribeDRMCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeDRMCertListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDRMCertListResponse(),
            await self.do_rpcrequest_async('DescribeDRMCertList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drmcert_list(
        self,
        request: live_20161101_models.DescribeDRMCertListRequest,
    ) -> live_20161101_models.DescribeDRMCertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drmcert_list_with_options(request, runtime)

    async def describe_drmcert_list_async(
        self,
        request: live_20161101_models.DescribeDRMCertListRequest,
    ) -> live_20161101_models.DescribeDRMCertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drmcert_list_with_options_async(request, runtime)

    def describe_forbid_push_stream_room_list_with_options(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeForbidPushStreamRoomListResponse(),
            self.do_rpcrequest('DescribeForbidPushStreamRoomList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_forbid_push_stream_room_list_with_options_async(
        self,
        request: live_20161101_models.DescribeForbidPushStreamRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeForbidPushStreamRoomListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeForbidPushStreamRoomListResponse(),
            await self.do_rpcrequest_async('DescribeForbidPushStreamRoomList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse(),
            self.do_rpcrequest('DescribeHlsLiveStreamRealTimeBpsData', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_hls_live_stream_real_time_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeHlsLiveStreamRealTimeBpsData', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def describe_html_resource_with_options(
        self,
        request: live_20161101_models.DescribeHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHtmlResourceResponse(),
            self.do_rpcrequest('DescribeHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_html_resource_with_options_async(
        self,
        request: live_20161101_models.DescribeHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHtmlResourceResponse(),
            await self.do_rpcrequest_async('DescribeHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_html_resource(
        self,
        request: live_20161101_models.DescribeHtmlResourceRequest,
    ) -> live_20161101_models.DescribeHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_html_resource_with_options(request, runtime)

    async def describe_html_resource_async(
        self,
        request: live_20161101_models.DescribeHtmlResourceRequest,
    ) -> live_20161101_models.DescribeHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_html_resource_with_options_async(request, runtime)

    def describe_live_asr_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAsrConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAsrConfigResponse(),
            self.do_rpcrequest('DescribeLiveAsrConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_asr_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveAsrConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAsrConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAsrConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveAsrConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_live_asr_config(
        self,
        request: live_20161101_models.DescribeLiveAsrConfigRequest,
    ) -> live_20161101_models.DescribeLiveAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_asr_config_with_options(request, runtime)

    async def describe_live_asr_config_async(
        self,
        request: live_20161101_models.DescribeLiveAsrConfigRequest,
    ) -> live_20161101_models.DescribeLiveAsrConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_asr_config_with_options_async(request, runtime)

    def describe_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditConfigResponse(),
            self.do_rpcrequest('DescribeLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse(),
            self.do_rpcrequest('DescribeLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateDetailResponse(),
            self.do_rpcrequest('DescribeLiveCertificateDetail', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_certificate_detail_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateDetailResponse(),
            await self.do_rpcrequest_async('DescribeLiveCertificateDetail', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateListResponse(),
            self.do_rpcrequest('DescribeLiveCertificateList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_certificate_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateListResponse(),
            await self.do_rpcrequest_async('DescribeLiveCertificateList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectNotifyConfigResponse(),
            self.do_rpcrequest('DescribeLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectNotifyConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectPornDataResponse(),
            self.do_rpcrequest('DescribeLiveDetectPornData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_detect_porn_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDetectPornDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDetectPornDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectPornDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDetectPornData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainBpsData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainBpsData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_bps_data_by_time_stamp_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse(),
            self.do_rpcrequest('DescribeLiveDomainBpsDataByTimeStamp', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainBpsDataByTimeStamp', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainCertificateInfoResponse(),
            self.do_rpcrequest('DescribeLiveDomainCertificateInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_certificate_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainCertificateInfoResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainCertificateInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainConfigsResponse(),
            self.do_rpcrequest('DescribeLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainConfigsResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainDetailResponse(),
            self.do_rpcrequest('DescribeLiveDomainDetail', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_detail_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainDetailResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainDetail', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainFrameRateAndBitRateData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_frame_rate_and_bit_rate_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainFrameRateAndBitRateData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLimitResponse(),
            self.do_rpcrequest('DescribeLiveDomainLimit', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_limit_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLimitResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainLimit', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_mapping_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainMappingResponse(),
            self.do_rpcrequest('DescribeLiveDomainMapping', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_mapping_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainMappingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainMappingResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainMapping', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainOnlineUserNumResponse(),
            self.do_rpcrequest('DescribeLiveDomainOnlineUserNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_online_user_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainOnlineUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainOnlineUserNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainOnlineUserNumResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainOnlineUserNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushBpsDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainPushBpsData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_push_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainPushBpsData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushTrafficDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainPushTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_push_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPushTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPushTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainPushTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPvUvDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainPvUvData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_pv_uv_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainPvUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainPvUvDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPvUvDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainPvUvData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainRealTimeBpsData', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_real_time_bps_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainRealTimeBpsData', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainRealTimeHttpCodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_real_time_http_code_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainRealTimeHttpCodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DescribeLiveDomainRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def describe_live_domain_real_time_traffic_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainRealTimeTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_real_time_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRealTimeTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainRealTimeTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_record_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainRecordData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_record_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainRecordData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_snapshot_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainSnapshotDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainSnapshotData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_snapshot_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainSnapshotDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainSnapshotDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainSnapshotData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_domain_stream_transcode_data_with_options(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainStreamTranscodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_stream_transcode_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainStreamTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainStreamTranscodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTimeShiftDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainTimeShiftData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_time_shift_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTimeShiftDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTimeShiftDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTimeShiftDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainTimeShiftData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTrafficDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_traffic_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTrafficDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainTrafficData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTranscodeDataResponse(),
            self.do_rpcrequest('DescribeLiveDomainTranscodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_domain_transcode_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveDomainTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveDomainTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTranscodeDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveDomainTranscodeData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_lazy_pull_stream_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveLazyPullStreamConfigResponse(),
            self.do_rpcrequest('DescribeLiveLazyPullStreamConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_lazy_pull_stream_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveLazyPullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveLazyPullStreamConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveLazyPullStreamConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveLazyPullStreamConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_pull_stream_config_with_options(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLivePullStreamConfigResponse(),
            self.do_rpcrequest('DescribeLivePullStreamConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_pull_stream_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLivePullStreamConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLivePullStreamConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLivePullStreamConfigResponse(),
            await self.do_rpcrequest_async('DescribeLivePullStreamConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse(),
            self.do_rpcrequest('DescribeLiveRealtimeDeliveryAcc', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_realtime_delivery_acc_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeDeliveryAccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse(),
            await self.do_rpcrequest_async('DescribeLiveRealtimeDeliveryAcc', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse(),
            self.do_rpcrequest('DescribeLiveRealtimeLogAuthorized', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_live_realtime_log_authorized_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRealtimeLogAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse(),
            await self.do_rpcrequest_async('DescribeLiveRealtimeLogAuthorized', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordConfigResponse(),
            self.do_rpcrequest('DescribeLiveRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_record_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveRecordConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordNotifyConfigResponse(),
            self.do_rpcrequest('DescribeLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordNotifyConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordVodConfigsResponse(),
            self.do_rpcrequest('DescribeLiveRecordVodConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_record_vod_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveRecordVodConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveRecordVodConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordVodConfigsResponse(),
            await self.do_rpcrequest_async('DescribeLiveRecordVodConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveShiftConfigsResponse(),
            self.do_rpcrequest('DescribeLiveShiftConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_shift_configs_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveShiftConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveShiftConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveShiftConfigsResponse(),
            await self.do_rpcrequest_async('DescribeLiveShiftConfigs', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotConfigResponse(),
            self.do_rpcrequest('DescribeLiveSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse(),
            self.do_rpcrequest('DescribeLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamBitRateDataResponse(),
            self.do_rpcrequest('DescribeLiveStreamBitRateData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_bit_rate_data_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamBitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamBitRateDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamBitRateDataResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamBitRateData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamCountResponse(),
            self.do_rpcrequest('DescribeLiveStreamCount', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_count_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamCountResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamCount', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamDelayConfigResponse(),
            self.do_rpcrequest('DescribeLiveStreamDelayConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_delay_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamDelayConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamDelayConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamHistoryUserNumResponse(),
            self.do_rpcrequest('DescribeLiveStreamHistoryUserNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_history_user_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamHistoryUserNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamHistoryUserNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamHistoryUserNumResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamHistoryUserNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_stream_optimized_feature_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse(),
            self.do_rpcrequest('DescribeLiveStreamOptimizedFeatureConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_optimized_feature_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamOptimizedFeatureConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordContentResponse(),
            self.do_rpcrequest('DescribeLiveStreamRecordContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_record_content_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordContentResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamRecordContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFileResponse(),
            self.do_rpcrequest('DescribeLiveStreamRecordIndexFile', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_record_index_file_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFileResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamRecordIndexFile', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse(),
            self.do_rpcrequest('DescribeLiveStreamRecordIndexFiles', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_record_index_files_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamRecordIndexFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamRecordIndexFiles', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_streams_block_list_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsBlockListResponse(),
            self.do_rpcrequest('DescribeLiveStreamsBlockList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_streams_block_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsBlockListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsBlockListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsBlockListResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamsBlockList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsControlHistoryResponse(),
            self.do_rpcrequest('DescribeLiveStreamsControlHistory', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_streams_control_history_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsControlHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsControlHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsControlHistoryResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamsControlHistory', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_stream_snapshot_info_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamSnapshotInfoResponse(),
            self.do_rpcrequest('DescribeLiveStreamSnapshotInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_snapshot_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamSnapshotInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamSnapshotInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamSnapshotInfoResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamSnapshotInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_streams_notify_url_config_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('DescribeLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsOnlineListResponse(),
            self.do_rpcrequest('DescribeLiveStreamsOnlineList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_streams_online_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsOnlineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsOnlineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsOnlineListResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamsOnlineList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsPublishListResponse(),
            self.do_rpcrequest('DescribeLiveStreamsPublishList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_streams_publish_list_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamsPublishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamsPublishListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsPublishListResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamsPublishList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_stream_transcode_info_with_options(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeInfoResponse(),
            self.do_rpcrequest('DescribeLiveStreamTranscodeInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_transcode_info_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeInfoResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamTranscodeInfo', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse(),
            self.do_rpcrequest('DescribeLiveStreamTranscodeStreamNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_stream_transcode_stream_num_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveStreamTranscodeStreamNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse(),
            await self.do_rpcrequest_async('DescribeLiveStreamTranscodeStreamNum', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_tag_resources_with_options(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTagResourcesResponse(),
            self.do_rpcrequest('DescribeLiveTagResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_tag_resources_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTagResourcesResponse(),
            await self.do_rpcrequest_async('DescribeLiveTagResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTopDomainsByFlowResponse(),
            self.do_rpcrequest('DescribeLiveTopDomainsByFlow', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_top_domains_by_flow_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTopDomainsByFlowResponse(),
            await self.do_rpcrequest_async('DescribeLiveTopDomainsByFlow', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_user_domains_with_options(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserDomainsResponse(),
            self.do_rpcrequest('DescribeLiveUserDomains', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_user_domains_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserDomainsResponse(),
            await self.do_rpcrequest_async('DescribeLiveUserDomains', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserTagsResponse(),
            self.do_rpcrequest('DescribeLiveUserTags', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_user_tags_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserTagsResponse(),
            await self.do_rpcrequest_async('DescribeLiveUserTags', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_live_verify_content_with_options(
        self,
        request: live_20161101_models.DescribeLiveVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveVerifyContentResponse(),
            self.do_rpcrequest('DescribeLiveVerifyContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_live_verify_content_with_options_async(
        self,
        request: live_20161101_models.DescribeLiveVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeLiveVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveVerifyContentResponse(),
            await self.do_rpcrequest_async('DescribeLiveVerifyContent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_live_verify_content(
        self,
        request: live_20161101_models.DescribeLiveVerifyContentRequest,
    ) -> live_20161101_models.DescribeLiveVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_live_verify_content_with_options(request, runtime)

    async def describe_live_verify_content_async(
        self,
        request: live_20161101_models.DescribeLiveVerifyContentRequest,
    ) -> live_20161101_models.DescribeLiveVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_live_verify_content_with_options_async(request, runtime)

    def describe_mix_stream_list_with_options(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMixStreamListResponse(),
            self.do_rpcrequest('DescribeMixStreamList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mix_stream_list_with_options_async(
        self,
        request: live_20161101_models.DescribeMixStreamListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeMixStreamListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMixStreamListResponse(),
            await self.do_rpcrequest_async('DescribeMixStreamList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_record_with_options(
        self,
        request: live_20161101_models.DescribeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRecordResponse(),
            self.do_rpcrequest('DescribeRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_with_options_async(
        self,
        request: live_20161101_models.DescribeRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRecordResponse(),
            await self.do_rpcrequest_async('DescribeRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record(
        self,
        request: live_20161101_models.DescribeRecordRequest,
    ) -> live_20161101_models.DescribeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_with_options(request, runtime)

    async def describe_record_async(
        self,
        request: live_20161101_models.DescribeRecordRequest,
    ) -> live_20161101_models.DescribeRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_with_options_async(request, runtime)

    def describe_records_with_options(
        self,
        request: live_20161101_models.DescribeRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRecordsResponse(),
            self.do_rpcrequest('DescribeRecords', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_records_with_options_async(
        self,
        request: live_20161101_models.DescribeRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRecordsResponse(),
            await self.do_rpcrequest_async('DescribeRecords', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_records(
        self,
        request: live_20161101_models.DescribeRecordsRequest,
    ) -> live_20161101_models.DescribeRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    async def describe_records_async(
        self,
        request: live_20161101_models.DescribeRecordsRequest,
    ) -> live_20161101_models.DescribeRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_records_with_options_async(request, runtime)

    def describe_room_kickout_user_list_with_options(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomKickoutUserListResponse(),
            self.do_rpcrequest('DescribeRoomKickoutUserList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_room_kickout_user_list_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomKickoutUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomKickoutUserListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomKickoutUserListResponse(),
            await self.do_rpcrequest_async('DescribeRoomKickoutUserList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomListResponse(),
            self.do_rpcrequest('DescribeRoomList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_room_list_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomListResponse(),
            await self.do_rpcrequest_async('DescribeRoomList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomStatusResponse(),
            self.do_rpcrequest('DescribeRoomStatus', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_room_status_with_options_async(
        self,
        request: live_20161101_models.DescribeRoomStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeRoomStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomStatusResponse(),
            await self.do_rpcrequest_async('DescribeRoomStatus', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_studio_layouts_with_options(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeStudioLayoutsResponse(),
            self.do_rpcrequest('DescribeStudioLayouts', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_studio_layouts_with_options_async(
        self,
        request: live_20161101_models.DescribeStudioLayoutsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeStudioLayoutsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeStudioLayoutsResponse(),
            await self.do_rpcrequest_async('DescribeStudioLayouts', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_up_bps_peak_data_with_options(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakDataResponse(),
            self.do_rpcrequest('DescribeUpBpsPeakData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_up_bps_peak_data_with_options_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakDataResponse(),
            await self.do_rpcrequest_async('DescribeUpBpsPeakData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakOfLineResponse(),
            self.do_rpcrequest('DescribeUpBpsPeakOfLine', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_up_bps_peak_of_line_with_options_async(
        self,
        request: live_20161101_models.DescribeUpBpsPeakOfLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpBpsPeakOfLineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakOfLineResponse(),
            await self.do_rpcrequest_async('DescribeUpBpsPeakOfLine', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpPeakPublishStreamDataResponse(),
            self.do_rpcrequest('DescribeUpPeakPublishStreamData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_up_peak_publish_stream_data_with_options_async(
        self,
        request: live_20161101_models.DescribeUpPeakPublishStreamDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DescribeUpPeakPublishStreamDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpPeakPublishStreamDataResponse(),
            await self.do_rpcrequest_async('DescribeUpPeakPublishStreamData', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DisableLiveRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('DisableLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def disable_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.DisableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.DisableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.DisableLiveRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('DisableLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def edit_html_resource_with_options(
        self,
        request: live_20161101_models.EditHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EditHtmlResourceResponse(),
            self.do_rpcrequest('EditHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_html_resource_with_options_async(
        self,
        request: live_20161101_models.EditHtmlResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditHtmlResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EditHtmlResourceResponse(),
            await self.do_rpcrequest_async('EditHtmlResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_html_resource(
        self,
        request: live_20161101_models.EditHtmlResourceRequest,
    ) -> live_20161101_models.EditHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_html_resource_with_options(request, runtime)

    async def edit_html_resource_async(
        self,
        request: live_20161101_models.EditHtmlResourceRequest,
    ) -> live_20161101_models.EditHtmlResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_html_resource_with_options_async(request, runtime)

    def edit_playlist_with_options(
        self,
        request: live_20161101_models.EditPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EditPlaylistResponse(),
            self.do_rpcrequest('EditPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_playlist_with_options_async(
        self,
        request: live_20161101_models.EditPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EditPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EditPlaylistResponse(),
            await self.do_rpcrequest_async('EditPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def effect_caster_urgent_with_options(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterUrgentResponse(),
            self.do_rpcrequest('EffectCasterUrgent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def effect_caster_urgent_with_options_async(
        self,
        request: live_20161101_models.EffectCasterUrgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterUrgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterUrgentResponse(),
            await self.do_rpcrequest_async('EffectCasterUrgent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterVideoResourceResponse(),
            self.do_rpcrequest('EffectCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def effect_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.EffectCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EffectCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterVideoResourceResponse(),
            await self.do_rpcrequest_async('EffectCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.EnableLiveRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('EnableLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def enable_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.EnableLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.EnableLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.EnableLiveRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('EnableLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidLiveStreamResponse(),
            self.do_rpcrequest('ForbidLiveStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def forbid_live_stream_with_options_async(
        self,
        request: live_20161101_models.ForbidLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidLiveStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidLiveStreamResponse(),
            await self.do_rpcrequest_async('ForbidLiveStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidPushStreamResponse(),
            self.do_rpcrequest('ForbidPushStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def forbid_push_stream_with_options_async(
        self,
        request: live_20161101_models.ForbidPushStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ForbidPushStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidPushStreamResponse(),
            await self.do_rpcrequest_async('ForbidPushStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_multi_rate_config_with_options(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigResponse(),
            self.do_rpcrequest('GetMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multi_rate_config_with_options_async(
        self,
        request: live_20161101_models.GetMultiRateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigResponse(),
            await self.do_rpcrequest_async('GetMultiRateConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigListResponse(),
            self.do_rpcrequest('GetMultiRateConfigList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multi_rate_config_list_with_options_async(
        self,
        request: live_20161101_models.GetMultiRateConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.GetMultiRateConfigListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigListResponse(),
            await self.do_rpcrequest_async('GetMultiRateConfigList', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def join_board_with_options(
        self,
        request: live_20161101_models.JoinBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.JoinBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.JoinBoardResponse(),
            self.do_rpcrequest('JoinBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_board_with_options_async(
        self,
        request: live_20161101_models.JoinBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.JoinBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.JoinBoardResponse(),
            await self.do_rpcrequest_async('JoinBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_board(
        self,
        request: live_20161101_models.JoinBoardRequest,
    ) -> live_20161101_models.JoinBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_board_with_options(request, runtime)

    async def join_board_async(
        self,
        request: live_20161101_models.JoinBoardRequest,
    ) -> live_20161101_models.JoinBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_board_with_options_async(request, runtime)

    def list_live_realtime_log_delivery_with_options(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('ListLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('ListLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse(),
            self.do_rpcrequest('ListLiveRealtimeLogDeliveryDomains', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_live_realtime_log_delivery_domains_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse(),
            await self.do_rpcrequest_async('ListLiveRealtimeLogDeliveryDomains', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse(),
            self.do_rpcrequest('ListLiveRealtimeLogDeliveryInfos', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_live_realtime_log_delivery_infos_with_options_async(
        self,
        request: live_20161101_models.ListLiveRealtimeLogDeliveryInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse(),
            await self.do_rpcrequest_async('ListLiveRealtimeLogDeliveryInfos', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def list_playlist_with_options(
        self,
        request: live_20161101_models.ListPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistResponse(),
            self.do_rpcrequest('ListPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_playlist_with_options_async(
        self,
        request: live_20161101_models.ListPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistResponse(),
            await self.do_rpcrequest_async('ListPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistItemsResponse(),
            self.do_rpcrequest('ListPlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_playlist_items_with_options_async(
        self,
        request: live_20161101_models.ListPlaylistItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ListPlaylistItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistItemsResponse(),
            await self.do_rpcrequest_async('ListPlaylistItems', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterComponentResponse(),
            self.do_rpcrequest('ModifyCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_caster_component_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterComponentResponse(),
            await self.do_rpcrequest_async('ModifyCasterComponent', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterEpisodeResponse(),
            self.do_rpcrequest('ModifyCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_caster_episode_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterEpisodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterEpisodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterEpisodeResponse(),
            await self.do_rpcrequest_async('ModifyCasterEpisode', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterLayoutResponse(),
            self.do_rpcrequest('ModifyCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_caster_layout_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterLayoutResponse(),
            await self.do_rpcrequest_async('ModifyCasterLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterProgramResponse(),
            self.do_rpcrequest('ModifyCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_caster_program_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterProgramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterProgramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterProgramResponse(),
            await self.do_rpcrequest_async('ModifyCasterProgram', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterVideoResourceResponse(),
            self.do_rpcrequest('ModifyCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_caster_video_resource_with_options_async(
        self,
        request: live_20161101_models.ModifyCasterVideoResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyCasterVideoResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterVideoResourceResponse(),
            await self.do_rpcrequest_async('ModifyCasterVideoResource', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse(),
            self.do_rpcrequest('ModifyLiveDomainSchdmByProperty', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_live_domain_schdm_by_property_with_options_async(
        self,
        request: live_20161101_models.ModifyLiveDomainSchdmByPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse(),
            await self.do_rpcrequest_async('ModifyLiveDomainSchdmByProperty', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse(),
            self.do_rpcrequest('ModifyLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_live_realtime_log_delivery_with_options_async(
        self,
        request: live_20161101_models.ModifyLiveRealtimeLogDeliveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse(),
            await self.do_rpcrequest_async('ModifyLiveRealtimeLogDelivery', '2016-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def modify_studio_layout_with_options(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyStudioLayoutResponse(),
            self.do_rpcrequest('ModifyStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_studio_layout_with_options_async(
        self,
        request: live_20161101_models.ModifyStudioLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ModifyStudioLayoutResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyStudioLayoutResponse(),
            await self.do_rpcrequest_async('ModifyStudioLayout', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.OpenLiveShiftResponse(),
            self.do_rpcrequest('OpenLiveShift', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_live_shift_with_options_async(
        self,
        request: live_20161101_models.OpenLiveShiftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.OpenLiveShiftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.OpenLiveShiftResponse(),
            await self.do_rpcrequest_async('OpenLiveShift', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def real_time_record_command_with_options(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeRecordCommandResponse(),
            self.do_rpcrequest('RealTimeRecordCommand', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def real_time_record_command_with_options_async(
        self,
        request: live_20161101_models.RealTimeRecordCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeRecordCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeRecordCommandResponse(),
            await self.do_rpcrequest_async('RealTimeRecordCommand', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeSnapshotCommandResponse(),
            self.do_rpcrequest('RealTimeSnapshotCommand', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def real_time_snapshot_command_with_options_async(
        self,
        request: live_20161101_models.RealTimeSnapshotCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.RealTimeSnapshotCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeSnapshotCommandResponse(),
            await self.do_rpcrequest_async('RealTimeSnapshotCommand', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def resume_live_stream_with_options(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ResumeLiveStreamResponse(),
            self.do_rpcrequest('ResumeLiveStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_live_stream_with_options_async(
        self,
        request: live_20161101_models.ResumeLiveStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.ResumeLiveStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.ResumeLiveStreamResponse(),
            await self.do_rpcrequest_async('ResumeLiveStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def send_room_notification_with_options(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomNotificationResponse(),
            self.do_rpcrequest('SendRoomNotification', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_room_notification_with_options_async(
        self,
        request: live_20161101_models.SendRoomNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomNotificationResponse(),
            await self.do_rpcrequest_async('SendRoomNotification', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomUserNotificationResponse(),
            self.do_rpcrequest('SendRoomUserNotification', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_room_user_notification_with_options_async(
        self,
        request: live_20161101_models.SendRoomUserNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SendRoomUserNotificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomUserNotificationResponse(),
            await self.do_rpcrequest_async('SendRoomUserNotification', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_board_callback_with_options(
        self,
        request: live_20161101_models.SetBoardCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetBoardCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetBoardCallbackResponse(),
            self.do_rpcrequest('SetBoardCallback', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_board_callback_with_options_async(
        self,
        request: live_20161101_models.SetBoardCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetBoardCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetBoardCallbackResponse(),
            await self.do_rpcrequest_async('SetBoardCallback', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_board_callback(
        self,
        request: live_20161101_models.SetBoardCallbackRequest,
    ) -> live_20161101_models.SetBoardCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_board_callback_with_options(request, runtime)

    async def set_board_callback_async(
        self,
        request: live_20161101_models.SetBoardCallbackRequest,
    ) -> live_20161101_models.SetBoardCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_board_callback_with_options_async(request, runtime)

    def set_caster_channel_with_options(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterChannelResponse(),
            self.do_rpcrequest('SetCasterChannel', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_caster_channel_with_options_async(
        self,
        request: live_20161101_models.SetCasterChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterChannelResponse(),
            await self.do_rpcrequest_async('SetCasterChannel', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterConfigResponse(),
            self.do_rpcrequest('SetCasterConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_caster_config_with_options_async(
        self,
        request: live_20161101_models.SetCasterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterConfigResponse(),
            await self.do_rpcrequest_async('SetCasterConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSceneConfigResponse(),
            self.do_rpcrequest('SetCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.SetCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSceneConfigResponse(),
            await self.do_rpcrequest_async('SetCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSyncGroupResponse(),
            self.do_rpcrequest('SetCasterSyncGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_caster_sync_group_with_options_async(
        self,
        request: live_20161101_models.SetCasterSyncGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetCasterSyncGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSyncGroupResponse(),
            await self.do_rpcrequest_async('SetCasterSyncGroup', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_live_domain_certificate_with_options(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainCertificateResponse(),
            self.do_rpcrequest('SetLiveDomainCertificate', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_live_domain_certificate_with_options_async(
        self,
        request: live_20161101_models.SetLiveDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainCertificateResponse(),
            await self.do_rpcrequest_async('SetLiveDomainCertificate', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_live_lazy_pull_stream_info_config_with_options(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse(),
            self.do_rpcrequest('SetLiveLazyPullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_live_lazy_pull_stream_info_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveLazyPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse(),
            await self.do_rpcrequest_async('SetLiveLazyPullStreamInfoConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamDelayConfigResponse(),
            self.do_rpcrequest('SetLiveStreamDelayConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_live_stream_delay_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamDelayConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamDelayConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamDelayConfigResponse(),
            await self.do_rpcrequest_async('SetLiveStreamDelayConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse(),
            self.do_rpcrequest('SetLiveStreamOptimizedFeatureConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_live_stream_optimized_feature_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamOptimizedFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse(),
            await self.do_rpcrequest_async('SetLiveStreamOptimizedFeatureConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('SetLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_live_streams_notify_url_config_with_options_async(
        self,
        request: live_20161101_models.SetLiveStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse(),
            await self.do_rpcrequest_async('SetLiveStreamsNotifyUrlConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def start_board_record_with_options(
        self,
        request: live_20161101_models.StartBoardRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartBoardRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartBoardRecordResponse(),
            self.do_rpcrequest('StartBoardRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_board_record_with_options_async(
        self,
        request: live_20161101_models.StartBoardRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartBoardRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartBoardRecordResponse(),
            await self.do_rpcrequest_async('StartBoardRecord', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_board_record(
        self,
        request: live_20161101_models.StartBoardRecordRequest,
    ) -> live_20161101_models.StartBoardRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_board_record_with_options(request, runtime)

    async def start_board_record_async(
        self,
        request: live_20161101_models.StartBoardRecordRequest,
    ) -> live_20161101_models.StartBoardRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_board_record_with_options_async(request, runtime)

    def start_caster_with_options(
        self,
        request: live_20161101_models.StartCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterResponse(),
            self.do_rpcrequest('StartCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_caster_with_options_async(
        self,
        request: live_20161101_models.StartCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterResponse(),
            await self.do_rpcrequest_async('StartCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterSceneResponse(),
            self.do_rpcrequest('StartCasterScene', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_caster_scene_with_options_async(
        self,
        request: live_20161101_models.StartCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartCasterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterSceneResponse(),
            await self.do_rpcrequest_async('StartCasterScene', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveDomainResponse(),
            self.do_rpcrequest('StartLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_live_domain_with_options_async(
        self,
        request: live_20161101_models.StartLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveDomainResponse(),
            await self.do_rpcrequest_async('StartLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def start_live_index_with_options(
        self,
        request: live_20161101_models.StartLiveIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveIndexResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveIndexResponse(),
            self.do_rpcrequest('StartLiveIndex', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_live_index_with_options_async(
        self,
        request: live_20161101_models.StartLiveIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartLiveIndexResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveIndexResponse(),
            await self.do_rpcrequest_async('StartLiveIndex', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_live_index(
        self,
        request: live_20161101_models.StartLiveIndexRequest,
    ) -> live_20161101_models.StartLiveIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_live_index_with_options(request, runtime)

    async def start_live_index_async(
        self,
        request: live_20161101_models.StartLiveIndexRequest,
    ) -> live_20161101_models.StartLiveIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_live_index_with_options_async(request, runtime)

    def start_playlist_with_options(
        self,
        request: live_20161101_models.StartPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartPlaylistResponse(),
            self.do_rpcrequest('StartPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_playlist_with_options_async(
        self,
        request: live_20161101_models.StartPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StartPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StartPlaylistResponse(),
            await self.do_rpcrequest_async('StartPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterResponse(),
            self.do_rpcrequest('StopCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_caster_with_options_async(
        self,
        request: live_20161101_models.StopCasterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterResponse(),
            await self.do_rpcrequest_async('StopCaster', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterSceneResponse(),
            self.do_rpcrequest('StopCasterScene', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_caster_scene_with_options_async(
        self,
        request: live_20161101_models.StopCasterSceneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopCasterSceneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterSceneResponse(),
            await self.do_rpcrequest_async('StopCasterScene', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveDomainResponse(),
            self.do_rpcrequest('StopLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_live_domain_with_options_async(
        self,
        request: live_20161101_models.StopLiveDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveDomainResponse(),
            await self.do_rpcrequest_async('StopLiveDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def stop_live_index_with_options(
        self,
        request: live_20161101_models.StopLiveIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveIndexResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveIndexResponse(),
            self.do_rpcrequest('StopLiveIndex', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_live_index_with_options_async(
        self,
        request: live_20161101_models.StopLiveIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopLiveIndexResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveIndexResponse(),
            await self.do_rpcrequest_async('StopLiveIndex', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_live_index(
        self,
        request: live_20161101_models.StopLiveIndexRequest,
    ) -> live_20161101_models.StopLiveIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_index_with_options(request, runtime)

    async def stop_live_index_async(
        self,
        request: live_20161101_models.StopLiveIndexRequest,
    ) -> live_20161101_models.StopLiveIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_index_with_options_async(request, runtime)

    def stop_playlist_with_options(
        self,
        request: live_20161101_models.StopPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopPlaylistResponse(),
            self.do_rpcrequest('StopPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_playlist_with_options_async(
        self,
        request: live_20161101_models.StopPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.StopPlaylistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.StopPlaylistResponse(),
            await self.do_rpcrequest_async('StopPlaylist', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.TagLiveResourcesResponse(),
            self.do_rpcrequest('TagLiveResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_live_resources_with_options_async(
        self,
        request: live_20161101_models.TagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.TagLiveResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.TagLiveResourcesResponse(),
            await self.do_rpcrequest_async('TagLiveResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UnTagLiveResourcesResponse(),
            self.do_rpcrequest('UnTagLiveResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_live_resources_with_options_async(
        self,
        request: live_20161101_models.UnTagLiveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UnTagLiveResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UnTagLiveResourcesResponse(),
            await self.do_rpcrequest_async('UnTagLiveResources', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_board_with_options(
        self,
        request: live_20161101_models.UpdateBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateBoardResponse(),
            self.do_rpcrequest('UpdateBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_board_with_options_async(
        self,
        request: live_20161101_models.UpdateBoardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateBoardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateBoardResponse(),
            await self.do_rpcrequest_async('UpdateBoard', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_board(
        self,
        request: live_20161101_models.UpdateBoardRequest,
    ) -> live_20161101_models.UpdateBoardResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_board_with_options(request, runtime)

    async def update_board_async(
        self,
        request: live_20161101_models.UpdateBoardRequest,
    ) -> live_20161101_models.UpdateBoardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_board_with_options_async(request, runtime)

    def update_board_callback_with_options(
        self,
        request: live_20161101_models.UpdateBoardCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateBoardCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateBoardCallbackResponse(),
            self.do_rpcrequest('UpdateBoardCallback', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_board_callback_with_options_async(
        self,
        request: live_20161101_models.UpdateBoardCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateBoardCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateBoardCallbackResponse(),
            await self.do_rpcrequest_async('UpdateBoardCallback', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_board_callback(
        self,
        request: live_20161101_models.UpdateBoardCallbackRequest,
    ) -> live_20161101_models.UpdateBoardCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_board_callback_with_options(request, runtime)

    async def update_board_callback_async(
        self,
        request: live_20161101_models.UpdateBoardCallbackRequest,
    ) -> live_20161101_models.UpdateBoardCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_board_callback_with_options_async(request, runtime)

    def update_caster_scene_audio_with_options(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneAudioResponse(),
            self.do_rpcrequest('UpdateCasterSceneAudio', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_caster_scene_audio_with_options_async(
        self,
        request: live_20161101_models.UpdateCasterSceneAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneAudioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneAudioResponse(),
            await self.do_rpcrequest_async('UpdateCasterSceneAudio', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneConfigResponse(),
            self.do_rpcrequest('UpdateCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_caster_scene_config_with_options_async(
        self,
        request: live_20161101_models.UpdateCasterSceneConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateCasterSceneConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneConfigResponse(),
            await self.do_rpcrequest_async('UpdateCasterSceneConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAppSnapshotConfigResponse(),
            self.do_rpcrequest('UpdateLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_app_snapshot_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAppSnapshotConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAppSnapshotConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAppSnapshotConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveAppSnapshotConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_live_asrconfig_with_options(
        self,
        request: live_20161101_models.UpdateLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveASRConfigResponse(),
            self.do_rpcrequest('UpdateLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_asrconfig_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveASRConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveASRConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveASRConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveASRConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live_asrconfig(
        self,
        request: live_20161101_models.UpdateLiveASRConfigRequest,
    ) -> live_20161101_models.UpdateLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_asrconfig_with_options(request, runtime)

    async def update_live_asrconfig_async(
        self,
        request: live_20161101_models.UpdateLiveASRConfigRequest,
    ) -> live_20161101_models.UpdateLiveASRConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_asrconfig_with_options_async(request, runtime)

    def update_live_audio_audit_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditConfigResponse(),
            self.do_rpcrequest('UpdateLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_audio_audit_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveAudioAuditConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse(),
            self.do_rpcrequest('UpdateLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_audio_audit_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveAudioAuditNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveAudioAuditNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveDetectNotifyConfigResponse(),
            self.do_rpcrequest('UpdateLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_detect_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveDetectNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveDetectNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveDetectNotifyConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveDetectNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_live_record_notify_config_with_options(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveRecordNotifyConfigResponse(),
            self.do_rpcrequest('UpdateLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_record_notify_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveRecordNotifyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveRecordNotifyConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveRecordNotifyConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveRecordNotifyConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse(),
            self.do_rpcrequest('UpdateLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_snapshot_detect_porn_config_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveSnapshotDetectPornConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse(),
            await self.do_rpcrequest_async('UpdateLiveSnapshotDetectPornConfig', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_live_top_level_domain_with_options(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveTopLevelDomainResponse(),
            self.do_rpcrequest('UpdateLiveTopLevelDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_live_top_level_domain_with_options_async(
        self,
        request: live_20161101_models.UpdateLiveTopLevelDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateLiveTopLevelDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveTopLevelDomainResponse(),
            await self.do_rpcrequest_async('UpdateLiveTopLevelDomain', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateMixStreamResponse(),
            self.do_rpcrequest('UpdateMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mix_stream_with_options_async(
        self,
        request: live_20161101_models.UpdateMixStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.UpdateMixStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateMixStreamResponse(),
            await self.do_rpcrequest_async('UpdateMixStream', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.VerifyLiveDomainOwnerResponse(),
            self.do_rpcrequest('VerifyLiveDomainOwner', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_live_domain_owner_with_options_async(
        self,
        request: live_20161101_models.VerifyLiveDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_20161101_models.VerifyLiveDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_20161101_models.VerifyLiveDomainOwnerResponse(),
            await self.do_rpcrequest_async('VerifyLiveDomainOwner', '2016-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

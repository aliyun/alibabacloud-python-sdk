# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lvwangwatermark20210104 import models as lvwang_watermark_20210104_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('lvwangwatermark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_audio_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.AddAudioAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddAudioAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddAudioAsyncResponse(),
            self.do_rpcrequest('AddAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_audio_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.AddAudioAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddAudioAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddAudioAsyncResponse(),
            await self.do_rpcrequest_async('AddAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_audio_async(
        self,
        request: lvwang_watermark_20210104_models.AddAudioAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddAudioAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_audio_async_with_options(request, runtime)

    async def add_audio_async_async(
        self,
        request: lvwang_watermark_20210104_models.AddAudioAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddAudioAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_audio_async_with_options_async(request, runtime)

    def add_image_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.AddImageAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddImageAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddImageAsyncResponse(),
            self.do_rpcrequest('AddImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_image_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.AddImageAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddImageAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddImageAsyncResponse(),
            await self.do_rpcrequest_async('AddImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_image_async(
        self,
        request: lvwang_watermark_20210104_models.AddImageAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddImageAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_image_async_with_options(request, runtime)

    async def add_image_async_async(
        self,
        request: lvwang_watermark_20210104_models.AddImageAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddImageAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_image_async_with_options_async(request, runtime)

    def add_image_sync_with_options(
        self,
        request: lvwang_watermark_20210104_models.AddImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddImageSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddImageSyncResponse(),
            self.do_rpcrequest('AddImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_image_sync_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.AddImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddImageSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddImageSyncResponse(),
            await self.do_rpcrequest_async('AddImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_image_sync(
        self,
        request: lvwang_watermark_20210104_models.AddImageSyncRequest,
    ) -> lvwang_watermark_20210104_models.AddImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_image_sync_with_options(request, runtime)

    async def add_image_sync_async(
        self,
        request: lvwang_watermark_20210104_models.AddImageSyncRequest,
    ) -> lvwang_watermark_20210104_models.AddImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_image_sync_with_options_async(request, runtime)

    def add_video_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.AddVideoAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddVideoAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddVideoAsyncResponse(),
            self.do_rpcrequest('AddVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_video_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.AddVideoAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.AddVideoAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.AddVideoAsyncResponse(),
            await self.do_rpcrequest_async('AddVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_video_async(
        self,
        request: lvwang_watermark_20210104_models.AddVideoAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddVideoAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_video_async_with_options(request, runtime)

    async def add_video_async_async(
        self,
        request: lvwang_watermark_20210104_models.AddVideoAsyncRequest,
    ) -> lvwang_watermark_20210104_models.AddVideoAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_video_async_with_options_async(request, runtime)

    def get_audio_add_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAddRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioAddResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioAddResponse(),
            self.do_rpcrequest('GetAudioAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audio_add_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAddRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioAddResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioAddResponse(),
            await self.do_rpcrequest_async('GetAudioAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_add(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAddRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioAddResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_add_with_options(request, runtime)

    async def get_audio_add_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAddRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioAddResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_add_with_options_async(request, runtime)

    def get_audio_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioAsyncResponse(),
            self.do_rpcrequest('GetAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audio_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioAsyncResponse(),
            await self.do_rpcrequest_async('GetAudioAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_async_with_options(request, runtime)

    async def get_audio_async_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_async_with_options_async(request, runtime)

    def get_audio_extract_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetAudioExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioExtractResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioExtractResponse(),
            self.do_rpcrequest('GetAudioExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audio_extract_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioExtractResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioExtractResponse(),
            await self.do_rpcrequest_async('GetAudioExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_extract(
        self,
        request: lvwang_watermark_20210104_models.GetAudioExtractRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioExtractResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_extract_with_options(request, runtime)

    async def get_audio_extract_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioExtractRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioExtractResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_extract_with_options_async(request, runtime)

    def get_audio_trace_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetAudioTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioTraceResponse(),
            self.do_rpcrequest('GetAudioTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audio_trace_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetAudioTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetAudioTraceResponse(),
            await self.do_rpcrequest_async('GetAudioTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audio_trace(
        self,
        request: lvwang_watermark_20210104_models.GetAudioTraceRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audio_trace_with_options(request, runtime)

    async def get_audio_trace_async(
        self,
        request: lvwang_watermark_20210104_models.GetAudioTraceRequest,
    ) -> lvwang_watermark_20210104_models.GetAudioTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audio_trace_with_options_async(request, runtime)

    def get_image_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetImageAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetImageAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetImageAsyncResponse(),
            self.do_rpcrequest('GetImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetImageAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetImageAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetImageAsyncResponse(),
            await self.do_rpcrequest_async('GetImageAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_async(
        self,
        request: lvwang_watermark_20210104_models.GetImageAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetImageAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_async_with_options(request, runtime)

    async def get_image_async_async(
        self,
        request: lvwang_watermark_20210104_models.GetImageAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetImageAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_async_with_options_async(request, runtime)

    def get_image_sync_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetImageSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetImageSyncResponse(),
            self.do_rpcrequest('GetImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_sync_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetImageSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetImageSyncResponse(),
            await self.do_rpcrequest_async('GetImageSync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_sync(
        self,
        request: lvwang_watermark_20210104_models.GetImageSyncRequest,
    ) -> lvwang_watermark_20210104_models.GetImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_sync_with_options(request, runtime)

    async def get_image_sync_async(
        self,
        request: lvwang_watermark_20210104_models.GetImageSyncRequest,
    ) -> lvwang_watermark_20210104_models.GetImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_sync_with_options_async(request, runtime)

    def get_query_trace_file_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetQueryTraceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetQueryTraceFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetQueryTraceFileResponse(),
            self.do_rpcrequest('GetQueryTraceFile', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_query_trace_file_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetQueryTraceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetQueryTraceFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetQueryTraceFileResponse(),
            await self.do_rpcrequest_async('GetQueryTraceFile', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_query_trace_file(
        self,
        request: lvwang_watermark_20210104_models.GetQueryTraceFileRequest,
    ) -> lvwang_watermark_20210104_models.GetQueryTraceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_query_trace_file_with_options(request, runtime)

    async def get_query_trace_file_async(
        self,
        request: lvwang_watermark_20210104_models.GetQueryTraceFileRequest,
    ) -> lvwang_watermark_20210104_models.GetQueryTraceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_query_trace_file_with_options_async(request, runtime)

    def get_video_add_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAddRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoAddResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoAddResponse(),
            self.do_rpcrequest('GetVideoAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_add_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAddRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoAddResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoAddResponse(),
            await self.do_rpcrequest_async('GetVideoAdd', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_add(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAddRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoAddResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_add_with_options(request, runtime)

    async def get_video_add_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAddRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoAddResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_add_with_options_async(request, runtime)

    def get_video_async_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoAsyncResponse(),
            self.do_rpcrequest('GetVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_async_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoAsyncResponse(),
            await self.do_rpcrequest_async('GetVideoAsync', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_async_with_options(request, runtime)

    async def get_video_async_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoAsyncRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_async_with_options_async(request, runtime)

    def get_video_extract_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetVideoExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoExtractResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoExtractResponse(),
            self.do_rpcrequest('GetVideoExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_extract_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoExtractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoExtractResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoExtractResponse(),
            await self.do_rpcrequest_async('GetVideoExtract', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_extract(
        self,
        request: lvwang_watermark_20210104_models.GetVideoExtractRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoExtractResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_extract_with_options(request, runtime)

    async def get_video_extract_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoExtractRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoExtractResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_extract_with_options_async(request, runtime)

    def get_video_trace_with_options(
        self,
        request: lvwang_watermark_20210104_models.GetVideoTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoTraceResponse(),
            self.do_rpcrequest('GetVideoTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_trace_with_options_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lvwang_watermark_20210104_models.GetVideoTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            lvwang_watermark_20210104_models.GetVideoTraceResponse(),
            await self.do_rpcrequest_async('GetVideoTrace', '2021-01-04', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_trace(
        self,
        request: lvwang_watermark_20210104_models.GetVideoTraceRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_trace_with_options(request, runtime)

    async def get_video_trace_async(
        self,
        request: lvwang_watermark_20210104_models.GetVideoTraceRequest,
    ) -> lvwang_watermark_20210104_models.GetVideoTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_trace_with_options_async(request, runtime)

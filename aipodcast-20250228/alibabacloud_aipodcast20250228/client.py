# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aipodcast20250228 import models as aipodcast_20250228_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aipodcast', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def podcast_task_result_query_with_options(
        self,
        request: aipodcast_20250228_models.PodcastTaskResultQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aipodcast_20250228_models.PodcastTaskResultQueryResponse:
        """
        @summary ai播客生成任务结果查询
        
        @param request: PodcastTaskResultQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PodcastTaskResultQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PodcastTaskResultQuery',
            version='2025-02-28',
            protocol='HTTPS',
            pathname=f'/podcast/task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aipodcast_20250228_models.PodcastTaskResultQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def podcast_task_result_query_with_options_async(
        self,
        request: aipodcast_20250228_models.PodcastTaskResultQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aipodcast_20250228_models.PodcastTaskResultQueryResponse:
        """
        @summary ai播客生成任务结果查询
        
        @param request: PodcastTaskResultQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PodcastTaskResultQueryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PodcastTaskResultQuery',
            version='2025-02-28',
            protocol='HTTPS',
            pathname=f'/podcast/task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aipodcast_20250228_models.PodcastTaskResultQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def podcast_task_result_query(
        self,
        request: aipodcast_20250228_models.PodcastTaskResultQueryRequest,
    ) -> aipodcast_20250228_models.PodcastTaskResultQueryResponse:
        """
        @summary ai播客生成任务结果查询
        
        @param request: PodcastTaskResultQueryRequest
        @return: PodcastTaskResultQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.podcast_task_result_query_with_options(request, headers, runtime)

    async def podcast_task_result_query_async(
        self,
        request: aipodcast_20250228_models.PodcastTaskResultQueryRequest,
    ) -> aipodcast_20250228_models.PodcastTaskResultQueryResponse:
        """
        @summary ai播客生成任务结果查询
        
        @param request: PodcastTaskResultQueryRequest
        @return: PodcastTaskResultQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.podcast_task_result_query_with_options_async(request, headers, runtime)

    def podcast_task_submit_with_options(
        self,
        tmp_req: aipodcast_20250228_models.PodcastTaskSubmitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aipodcast_20250228_models.PodcastTaskSubmitResponse:
        """
        @summary ai播客生成任务提交
        
        @param tmp_req: PodcastTaskSubmitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PodcastTaskSubmitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aipodcast_20250228_models.PodcastTaskSubmitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_urls):
            request.file_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_urls, 'fileUrls', 'json')
        if not UtilClient.is_unset(tmp_req.voices):
            request.voices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.voices, 'voices', 'json')
        body = {}
        if not UtilClient.is_unset(request.counts):
            body['counts'] = request.counts
        if not UtilClient.is_unset(request.file_urls_shrink):
            body['fileUrls'] = request.file_urls_shrink
        if not UtilClient.is_unset(request.source_lang):
            body['sourceLang'] = request.source_lang
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.voices_shrink):
            body['voices'] = request.voices_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PodcastTaskSubmit',
            version='2025-02-28',
            protocol='HTTPS',
            pathname=f'/podcast/task/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aipodcast_20250228_models.PodcastTaskSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    async def podcast_task_submit_with_options_async(
        self,
        tmp_req: aipodcast_20250228_models.PodcastTaskSubmitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> aipodcast_20250228_models.PodcastTaskSubmitResponse:
        """
        @summary ai播客生成任务提交
        
        @param tmp_req: PodcastTaskSubmitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PodcastTaskSubmitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = aipodcast_20250228_models.PodcastTaskSubmitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_urls):
            request.file_urls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_urls, 'fileUrls', 'json')
        if not UtilClient.is_unset(tmp_req.voices):
            request.voices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.voices, 'voices', 'json')
        body = {}
        if not UtilClient.is_unset(request.counts):
            body['counts'] = request.counts
        if not UtilClient.is_unset(request.file_urls_shrink):
            body['fileUrls'] = request.file_urls_shrink
        if not UtilClient.is_unset(request.source_lang):
            body['sourceLang'] = request.source_lang
        if not UtilClient.is_unset(request.text):
            body['text'] = request.text
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.voices_shrink):
            body['voices'] = request.voices_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PodcastTaskSubmit',
            version='2025-02-28',
            protocol='HTTPS',
            pathname=f'/podcast/task/submit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aipodcast_20250228_models.PodcastTaskSubmitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def podcast_task_submit(
        self,
        request: aipodcast_20250228_models.PodcastTaskSubmitRequest,
    ) -> aipodcast_20250228_models.PodcastTaskSubmitResponse:
        """
        @summary ai播客生成任务提交
        
        @param request: PodcastTaskSubmitRequest
        @return: PodcastTaskSubmitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.podcast_task_submit_with_options(request, headers, runtime)

    async def podcast_task_submit_async(
        self,
        request: aipodcast_20250228_models.PodcastTaskSubmitRequest,
    ) -> aipodcast_20250228_models.PodcastTaskSubmitResponse:
        """
        @summary ai播客生成任务提交
        
        @param request: PodcastTaskSubmitRequest
        @return: PodcastTaskSubmitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.podcast_task_submit_with_options_async(request, headers, runtime)

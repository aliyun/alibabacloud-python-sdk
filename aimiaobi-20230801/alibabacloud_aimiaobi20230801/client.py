# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_aimiaobi20230801 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aimiaobi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_audit_terms_with_options(
        self,
        tmp_req: main_models.AddAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuditTermsResponse:
        tmp_req.validate()
        request = main_models.AddAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exception_word):
            request.exception_word_shrink = Utils.array_to_string_with_specified_style(tmp_req.exception_word, 'ExceptionWord', 'json')
        body = {}
        if not DaraCore.is_null(request.exception_word_shrink):
            body['ExceptionWord'] = request.exception_word_shrink
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.suggest_word):
            body['SuggestWord'] = request.suggest_word
        if not DaraCore.is_null(request.terms_desc):
            body['TermsDesc'] = request.terms_desc
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuditTermsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_audit_terms_with_options_async(
        self,
        tmp_req: main_models.AddAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAuditTermsResponse:
        tmp_req.validate()
        request = main_models.AddAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exception_word):
            request.exception_word_shrink = Utils.array_to_string_with_specified_style(tmp_req.exception_word, 'ExceptionWord', 'json')
        body = {}
        if not DaraCore.is_null(request.exception_word_shrink):
            body['ExceptionWord'] = request.exception_word_shrink
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.suggest_word):
            body['SuggestWord'] = request.suggest_word
        if not DaraCore.is_null(request.terms_desc):
            body['TermsDesc'] = request.terms_desc
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAuditTermsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_audit_terms(
        self,
        request: main_models.AddAuditTermsRequest,
    ) -> main_models.AddAuditTermsResponse:
        runtime = RuntimeOptions()
        return self.add_audit_terms_with_options(request, runtime)

    async def add_audit_terms_async(
        self,
        request: main_models.AddAuditTermsRequest,
    ) -> main_models.AddAuditTermsResponse:
        runtime = RuntimeOptions()
        return await self.add_audit_terms_with_options_async(request, runtime)

    def add_dataset_document_with_options(
        self,
        tmp_req: main_models.AddDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.AddDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document):
            request.document_shrink = Utils.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.document_shrink):
            body['Document'] = request.document_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dataset_document_with_options_async(
        self,
        tmp_req: main_models.AddDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.AddDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document):
            request.document_shrink = Utils.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.document_shrink):
            body['Document'] = request.document_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dataset_document(
        self,
        request: main_models.AddDatasetDocumentRequest,
    ) -> main_models.AddDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return self.add_dataset_document_with_options(request, runtime)

    async def add_dataset_document_async(
        self,
        request: main_models.AddDatasetDocumentRequest,
    ) -> main_models.AddDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return await self.add_dataset_document_with_options_async(request, runtime)

    def async_create_clips_task_with_options(
        self,
        tmp_req: main_models.AsyncCreateClipsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateClipsTaskResponse:
        tmp_req.validate()
        request = main_models.AsyncCreateClipsTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.color_words):
            request.color_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.color_words, 'ColorWords', 'json')
        if not DaraCore.is_null(tmp_req.stickers):
            request.stickers_shrink = Utils.array_to_string_with_specified_style(tmp_req.stickers, 'Stickers', 'json')
        body = {}
        if not DaraCore.is_null(request.close_music):
            body['CloseMusic'] = request.close_music
        if not DaraCore.is_null(request.close_subtitle):
            body['CloseSubtitle'] = request.close_subtitle
        if not DaraCore.is_null(request.close_voice):
            body['CloseVoice'] = request.close_voice
        if not DaraCore.is_null(request.color_words_shrink):
            body['ColorWords'] = request.color_words_shrink
        if not DaraCore.is_null(request.custom_voice_url):
            body['CustomVoiceUrl'] = request.custom_voice_url
        if not DaraCore.is_null(request.custom_voice_volume):
            body['CustomVoiceVolume'] = request.custom_voice_volume
        if not DaraCore.is_null(request.height):
            body['Height'] = request.height
        if not DaraCore.is_null(request.music_url):
            body['MusicUrl'] = request.music_url
        if not DaraCore.is_null(request.music_volume):
            body['MusicVolume'] = request.music_volume
        if not DaraCore.is_null(request.stickers_shrink):
            body['Stickers'] = request.stickers_shrink
        if not DaraCore.is_null(request.subtitle_font_size):
            body['SubtitleFontSize'] = request.subtitle_font_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.voice_style):
            body['VoiceStyle'] = request.voice_style
        if not DaraCore.is_null(request.voice_volume):
            body['VoiceVolume'] = request.voice_volume
        if not DaraCore.is_null(request.width):
            body['Width'] = request.width
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateClipsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateClipsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_create_clips_task_with_options_async(
        self,
        tmp_req: main_models.AsyncCreateClipsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateClipsTaskResponse:
        tmp_req.validate()
        request = main_models.AsyncCreateClipsTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.color_words):
            request.color_words_shrink = Utils.array_to_string_with_specified_style(tmp_req.color_words, 'ColorWords', 'json')
        if not DaraCore.is_null(tmp_req.stickers):
            request.stickers_shrink = Utils.array_to_string_with_specified_style(tmp_req.stickers, 'Stickers', 'json')
        body = {}
        if not DaraCore.is_null(request.close_music):
            body['CloseMusic'] = request.close_music
        if not DaraCore.is_null(request.close_subtitle):
            body['CloseSubtitle'] = request.close_subtitle
        if not DaraCore.is_null(request.close_voice):
            body['CloseVoice'] = request.close_voice
        if not DaraCore.is_null(request.color_words_shrink):
            body['ColorWords'] = request.color_words_shrink
        if not DaraCore.is_null(request.custom_voice_url):
            body['CustomVoiceUrl'] = request.custom_voice_url
        if not DaraCore.is_null(request.custom_voice_volume):
            body['CustomVoiceVolume'] = request.custom_voice_volume
        if not DaraCore.is_null(request.height):
            body['Height'] = request.height
        if not DaraCore.is_null(request.music_url):
            body['MusicUrl'] = request.music_url
        if not DaraCore.is_null(request.music_volume):
            body['MusicVolume'] = request.music_volume
        if not DaraCore.is_null(request.stickers_shrink):
            body['Stickers'] = request.stickers_shrink
        if not DaraCore.is_null(request.subtitle_font_size):
            body['SubtitleFontSize'] = request.subtitle_font_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.voice_style):
            body['VoiceStyle'] = request.voice_style
        if not DaraCore.is_null(request.voice_volume):
            body['VoiceVolume'] = request.voice_volume
        if not DaraCore.is_null(request.width):
            body['Width'] = request.width
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateClipsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateClipsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_create_clips_task(
        self,
        request: main_models.AsyncCreateClipsTaskRequest,
    ) -> main_models.AsyncCreateClipsTaskResponse:
        runtime = RuntimeOptions()
        return self.async_create_clips_task_with_options(request, runtime)

    async def async_create_clips_task_async(
        self,
        request: main_models.AsyncCreateClipsTaskRequest,
    ) -> main_models.AsyncCreateClipsTaskResponse:
        runtime = RuntimeOptions()
        return await self.async_create_clips_task_with_options_async(request, runtime)

    def async_create_clips_time_line_with_options(
        self,
        request: main_models.AsyncCreateClipsTimeLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateClipsTimeLineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_content):
            body['AdditionalContent'] = request.additional_content
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.no_ref_video):
            body['NoRefVideo'] = request.no_ref_video
        if not DaraCore.is_null(request.process_prompt):
            body['ProcessPrompt'] = request.process_prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateClipsTimeLine',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateClipsTimeLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_create_clips_time_line_with_options_async(
        self,
        request: main_models.AsyncCreateClipsTimeLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncCreateClipsTimeLineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_content):
            body['AdditionalContent'] = request.additional_content
        if not DaraCore.is_null(request.custom_content):
            body['CustomContent'] = request.custom_content
        if not DaraCore.is_null(request.no_ref_video):
            body['NoRefVideo'] = request.no_ref_video
        if not DaraCore.is_null(request.process_prompt):
            body['ProcessPrompt'] = request.process_prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncCreateClipsTimeLine',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncCreateClipsTimeLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_create_clips_time_line(
        self,
        request: main_models.AsyncCreateClipsTimeLineRequest,
    ) -> main_models.AsyncCreateClipsTimeLineResponse:
        runtime = RuntimeOptions()
        return self.async_create_clips_time_line_with_options(request, runtime)

    async def async_create_clips_time_line_async(
        self,
        request: main_models.AsyncCreateClipsTimeLineRequest,
    ) -> main_models.AsyncCreateClipsTimeLineResponse:
        runtime = RuntimeOptions()
        return await self.async_create_clips_time_line_with_options_async(request, runtime)

    def async_edit_timeline_with_options(
        self,
        tmp_req: main_models.AsyncEditTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncEditTimelineResponse:
        tmp_req.validate()
        request = main_models.AsyncEditTimelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.timelines):
            request.timelines_shrink = Utils.array_to_string_with_specified_style(tmp_req.timelines, 'Timelines', 'json')
        body = {}
        if not DaraCore.is_null(request.auto_clips):
            body['AutoClips'] = request.auto_clips
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.timelines_shrink):
            body['Timelines'] = request.timelines_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncEditTimeline',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncEditTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_edit_timeline_with_options_async(
        self,
        tmp_req: main_models.AsyncEditTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncEditTimelineResponse:
        tmp_req.validate()
        request = main_models.AsyncEditTimelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.timelines):
            request.timelines_shrink = Utils.array_to_string_with_specified_style(tmp_req.timelines, 'Timelines', 'json')
        body = {}
        if not DaraCore.is_null(request.auto_clips):
            body['AutoClips'] = request.auto_clips
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.timelines_shrink):
            body['Timelines'] = request.timelines_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncEditTimeline',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncEditTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_edit_timeline(
        self,
        request: main_models.AsyncEditTimelineRequest,
    ) -> main_models.AsyncEditTimelineResponse:
        runtime = RuntimeOptions()
        return self.async_edit_timeline_with_options(request, runtime)

    async def async_edit_timeline_async(
        self,
        request: main_models.AsyncEditTimelineRequest,
    ) -> main_models.AsyncEditTimelineResponse:
        runtime = RuntimeOptions()
        return await self.async_edit_timeline_with_options_async(request, runtime)

    def async_upload_tender_doc_with_options(
        self,
        request: main_models.AsyncUploadTenderDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncUploadTenderDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.tender_doc_name):
            body['TenderDocName'] = request.tender_doc_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncUploadTenderDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncUploadTenderDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_upload_tender_doc_with_options_async(
        self,
        request: main_models.AsyncUploadTenderDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncUploadTenderDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.tender_doc_name):
            body['TenderDocName'] = request.tender_doc_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncUploadTenderDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncUploadTenderDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_upload_tender_doc(
        self,
        request: main_models.AsyncUploadTenderDocRequest,
    ) -> main_models.AsyncUploadTenderDocResponse:
        runtime = RuntimeOptions()
        return self.async_upload_tender_doc_with_options(request, runtime)

    async def async_upload_tender_doc_async(
        self,
        request: main_models.AsyncUploadTenderDocRequest,
    ) -> main_models.AsyncUploadTenderDocResponse:
        runtime = RuntimeOptions()
        return await self.async_upload_tender_doc_with_options_async(request, runtime)

    def async_upload_video_with_options(
        self,
        tmp_req: main_models.AsyncUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncUploadVideoResponse:
        tmp_req.validate()
        request = main_models.AsyncUploadVideoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_video):
            request.reference_video_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_video, 'ReferenceVideo', 'json')
        if not DaraCore.is_null(tmp_req.source_videos):
            request.source_videos_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_videos, 'SourceVideos', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'VideoRoles', 'json')
        body = {}
        if not DaraCore.is_null(request.anlysis_prompt):
            body['AnlysisPrompt'] = request.anlysis_prompt
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['FaceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.reference_video_shrink):
            body['ReferenceVideo'] = request.reference_video_shrink
        if not DaraCore.is_null(request.remove_subtitle):
            body['RemoveSubtitle'] = request.remove_subtitle
        if not DaraCore.is_null(request.source_videos_shrink):
            body['SourceVideos'] = request.source_videos_shrink
        if not DaraCore.is_null(request.split_interval):
            body['SplitInterval'] = request.split_interval
        if not DaraCore.is_null(request.video_roles_shrink):
            body['VideoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['VideoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncUploadVideo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncUploadVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_upload_video_with_options_async(
        self,
        tmp_req: main_models.AsyncUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncUploadVideoResponse:
        tmp_req.validate()
        request = main_models.AsyncUploadVideoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_video):
            request.reference_video_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_video, 'ReferenceVideo', 'json')
        if not DaraCore.is_null(tmp_req.source_videos):
            request.source_videos_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_videos, 'SourceVideos', 'json')
        if not DaraCore.is_null(tmp_req.video_roles):
            request.video_roles_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_roles, 'VideoRoles', 'json')
        body = {}
        if not DaraCore.is_null(request.anlysis_prompt):
            body['AnlysisPrompt'] = request.anlysis_prompt
        if not DaraCore.is_null(request.face_identity_similarity_min_score):
            body['FaceIdentitySimilarityMinScore'] = request.face_identity_similarity_min_score
        if not DaraCore.is_null(request.reference_video_shrink):
            body['ReferenceVideo'] = request.reference_video_shrink
        if not DaraCore.is_null(request.remove_subtitle):
            body['RemoveSubtitle'] = request.remove_subtitle
        if not DaraCore.is_null(request.source_videos_shrink):
            body['SourceVideos'] = request.source_videos_shrink
        if not DaraCore.is_null(request.split_interval):
            body['SplitInterval'] = request.split_interval
        if not DaraCore.is_null(request.video_roles_shrink):
            body['VideoRoles'] = request.video_roles_shrink
        if not DaraCore.is_null(request.video_shot_face_identity_count):
            body['VideoShotFaceIdentityCount'] = request.video_shot_face_identity_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncUploadVideo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncUploadVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_upload_video(
        self,
        request: main_models.AsyncUploadVideoRequest,
    ) -> main_models.AsyncUploadVideoResponse:
        runtime = RuntimeOptions()
        return self.async_upload_video_with_options(request, runtime)

    async def async_upload_video_async(
        self,
        request: main_models.AsyncUploadVideoRequest,
    ) -> main_models.AsyncUploadVideoResponse:
        runtime = RuntimeOptions()
        return await self.async_upload_video_with_options_async(request, runtime)

    def async_writing_bidding_doc_with_options(
        self,
        request: main_models.AsyncWritingBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncWritingBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.company_keyword):
            body['CompanyKeyword'] = request.company_keyword
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncWritingBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncWritingBiddingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def async_writing_bidding_doc_with_options_async(
        self,
        request: main_models.AsyncWritingBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AsyncWritingBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.company_keyword):
            body['CompanyKeyword'] = request.company_keyword
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AsyncWritingBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AsyncWritingBiddingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def async_writing_bidding_doc(
        self,
        request: main_models.AsyncWritingBiddingDocRequest,
    ) -> main_models.AsyncWritingBiddingDocResponse:
        runtime = RuntimeOptions()
        return self.async_writing_bidding_doc_with_options(request, runtime)

    async def async_writing_bidding_doc_async(
        self,
        request: main_models.AsyncWritingBiddingDocRequest,
    ) -> main_models.AsyncWritingBiddingDocResponse:
        runtime = RuntimeOptions()
        return await self.async_writing_bidding_doc_with_options_async(request, runtime)

    def bind_ppt_artifact_with_options(
        self,
        request: main_models.BindPptArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPptArtifactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.artifact_id):
            body['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindPptArtifact',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPptArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_ppt_artifact_with_options_async(
        self,
        request: main_models.BindPptArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPptArtifactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.artifact_id):
            body['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindPptArtifact',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPptArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_ppt_artifact(
        self,
        request: main_models.BindPptArtifactRequest,
    ) -> main_models.BindPptArtifactResponse:
        runtime = RuntimeOptions()
        return self.bind_ppt_artifact_with_options(request, runtime)

    async def bind_ppt_artifact_async(
        self,
        request: main_models.BindPptArtifactRequest,
    ) -> main_models.BindPptArtifactResponse:
        runtime = RuntimeOptions()
        return await self.bind_ppt_artifact_with_options_async(request, runtime)

    def cancel_async_task_with_options(
        self,
        request: main_models.CancelAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_async_task_with_options_async(
        self,
        request: main_models.CancelAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_async_task(
        self,
        request: main_models.CancelAsyncTaskRequest,
    ) -> main_models.CancelAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_async_task_with_options(request, runtime)

    async def cancel_async_task_async(
        self,
        request: main_models.CancelAsyncTaskRequest,
    ) -> main_models.CancelAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_async_task_with_options_async(request, runtime)

    def cancel_audit_task_with_options(
        self,
        request: main_models.CancelAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content_audit_task_id):
            body['ContentAuditTaskId'] = request.content_audit_task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAuditTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_audit_task_with_options_async(
        self,
        request: main_models.CancelAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content_audit_task_id):
            body['ContentAuditTaskId'] = request.content_audit_task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAuditTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_audit_task(
        self,
        request: main_models.CancelAuditTaskRequest,
    ) -> main_models.CancelAuditTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_audit_task_with_options(request, runtime)

    async def cancel_audit_task_async(
        self,
        request: main_models.CancelAuditTaskRequest,
    ) -> main_models.CancelAuditTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_audit_task_with_options_async(request, runtime)

    def cancel_deep_write_task_with_options(
        self,
        request: main_models.CancelDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDeepWriteTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDeepWriteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_deep_write_task_with_options_async(
        self,
        request: main_models.CancelDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDeepWriteTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDeepWriteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_deep_write_task(
        self,
        request: main_models.CancelDeepWriteTaskRequest,
    ) -> main_models.CancelDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_deep_write_task_with_options(request, runtime)

    async def cancel_deep_write_task_async(
        self,
        request: main_models.CancelDeepWriteTaskRequest,
    ) -> main_models.CancelDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_deep_write_task_with_options_async(request, runtime)

    def clear_intervenes_with_options(
        self,
        request: main_models.ClearIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_intervenes_with_options_async(
        self,
        request: main_models.ClearIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_intervenes(
        self,
        request: main_models.ClearIntervenesRequest,
    ) -> main_models.ClearIntervenesResponse:
        runtime = RuntimeOptions()
        return self.clear_intervenes_with_options(request, runtime)

    async def clear_intervenes_async(
        self,
        request: main_models.ClearIntervenesRequest,
    ) -> main_models.ClearIntervenesResponse:
        runtime = RuntimeOptions()
        return await self.clear_intervenes_with_options_async(request, runtime)

    def confirm_and_post_process_audit_note_with_options(
        self,
        request: main_models.ConfirmAndPostProcessAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmAndPostProcessAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmAndPostProcessAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmAndPostProcessAuditNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_and_post_process_audit_note_with_options_async(
        self,
        request: main_models.ConfirmAndPostProcessAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmAndPostProcessAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmAndPostProcessAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmAndPostProcessAuditNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_and_post_process_audit_note(
        self,
        request: main_models.ConfirmAndPostProcessAuditNoteRequest,
    ) -> main_models.ConfirmAndPostProcessAuditNoteResponse:
        runtime = RuntimeOptions()
        return self.confirm_and_post_process_audit_note_with_options(request, runtime)

    async def confirm_and_post_process_audit_note_async(
        self,
        request: main_models.ConfirmAndPostProcessAuditNoteRequest,
    ) -> main_models.ConfirmAndPostProcessAuditNoteResponse:
        runtime = RuntimeOptions()
        return await self.confirm_and_post_process_audit_note_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.document_handle_config):
            request.document_handle_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_handle_config, 'DocumentHandleConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.document_handle_config_shrink):
            body['DocumentHandleConfig'] = request.document_handle_config_shrink
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.document_handle_config):
            request.document_handle_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_handle_config, 'DocumentHandleConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.document_handle_config_shrink):
            body['DocumentHandleConfig'] = request.document_handle_config_shrink
        if not DaraCore.is_null(request.invoke_type):
            body['InvokeType'] = request.invoke_type
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_general_config_with_options(
        self,
        request: main_models.CreateGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGeneralConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_general_config_with_options_async(
        self,
        request: main_models.CreateGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGeneralConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_general_config(
        self,
        request: main_models.CreateGeneralConfigRequest,
    ) -> main_models.CreateGeneralConfigResponse:
        runtime = RuntimeOptions()
        return self.create_general_config_with_options(request, runtime)

    async def create_general_config_async(
        self,
        request: main_models.CreateGeneralConfigRequest,
    ) -> main_models.CreateGeneralConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_general_config_with_options_async(request, runtime)

    def create_generated_content_with_options(
        self,
        tmp_req: main_models.CreateGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGeneratedContentResponse:
        tmp_req.validate()
        request = main_models.CreateGeneratedContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not DaraCore.is_null(request.content_text):
            body['ContentText'] = request.content_text
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_generated_content_with_options_async(
        self,
        tmp_req: main_models.CreateGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGeneratedContentResponse:
        tmp_req.validate()
        request = main_models.CreateGeneratedContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not DaraCore.is_null(request.content_text):
            body['ContentText'] = request.content_text
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_generated_content(
        self,
        request: main_models.CreateGeneratedContentRequest,
    ) -> main_models.CreateGeneratedContentResponse:
        runtime = RuntimeOptions()
        return self.create_generated_content_with_options(request, runtime)

    async def create_generated_content_async(
        self,
        request: main_models.CreateGeneratedContentRequest,
    ) -> main_models.CreateGeneratedContentResponse:
        runtime = RuntimeOptions()
        return await self.create_generated_content_with_options_async(request, runtime)

    def create_token_with_options(
        self,
        request: main_models.CreateTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateToken',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_with_options_async(
        self,
        request: main_models.CreateTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateToken',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token(
        self,
        request: main_models.CreateTokenRequest,
    ) -> main_models.CreateTokenResponse:
        runtime = RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    async def create_token_async(
        self,
        request: main_models.CreateTokenRequest,
    ) -> main_models.CreateTokenResponse:
        runtime = RuntimeOptions()
        return await self.create_token_with_options_async(request, runtime)

    def delete_audit_note_with_options(
        self,
        request: main_models.DeleteAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuditNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_audit_note_with_options_async(
        self,
        request: main_models.DeleteAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuditNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_audit_note(
        self,
        request: main_models.DeleteAuditNoteRequest,
    ) -> main_models.DeleteAuditNoteResponse:
        runtime = RuntimeOptions()
        return self.delete_audit_note_with_options(request, runtime)

    async def delete_audit_note_async(
        self,
        request: main_models.DeleteAuditNoteRequest,
    ) -> main_models.DeleteAuditNoteResponse:
        runtime = RuntimeOptions()
        return await self.delete_audit_note_with_options_async(request, runtime)

    def delete_audit_terms_with_options(
        self,
        tmp_req: main_models.DeleteAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuditTermsResponse:
        tmp_req.validate()
        request = main_models.DeleteAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'IdList', 'json')
        body = {}
        if not DaraCore.is_null(request.id_list_shrink):
            body['IdList'] = request.id_list_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuditTermsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_audit_terms_with_options_async(
        self,
        tmp_req: main_models.DeleteAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAuditTermsResponse:
        tmp_req.validate()
        request = main_models.DeleteAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'IdList', 'json')
        body = {}
        if not DaraCore.is_null(request.id_list_shrink):
            body['IdList'] = request.id_list_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAuditTermsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_audit_terms(
        self,
        request: main_models.DeleteAuditTermsRequest,
    ) -> main_models.DeleteAuditTermsResponse:
        runtime = RuntimeOptions()
        return self.delete_audit_terms_with_options(request, runtime)

    async def delete_audit_terms_async(
        self,
        request: main_models.DeleteAuditTermsRequest,
    ) -> main_models.DeleteAuditTermsResponse:
        runtime = RuntimeOptions()
        return await self.delete_audit_terms_with_options_async(request, runtime)

    def delete_custom_text_with_options(
        self,
        request: main_models.DeleteCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_text_with_options_async(
        self,
        request: main_models.DeleteCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_text(
        self,
        request: main_models.DeleteCustomTextRequest,
    ) -> main_models.DeleteCustomTextResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_text_with_options(request, runtime)

    async def delete_custom_text_async(
        self,
        request: main_models.DeleteCustomTextRequest,
    ) -> main_models.DeleteCustomTextResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_text_with_options_async(request, runtime)

    def delete_custom_topic_by_topic_with_options(
        self,
        request: main_models.DeleteCustomTopicByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTopicByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomTopicByTopic',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTopicByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_by_topic_with_options_async(
        self,
        request: main_models.DeleteCustomTopicByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTopicByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomTopicByTopic',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTopicByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_by_topic(
        self,
        request: main_models.DeleteCustomTopicByTopicRequest,
    ) -> main_models.DeleteCustomTopicByTopicResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_topic_by_topic_with_options(request, runtime)

    async def delete_custom_topic_by_topic_async(
        self,
        request: main_models.DeleteCustomTopicByTopicRequest,
    ) -> main_models.DeleteCustomTopicByTopicResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_topic_by_topic_with_options_async(request, runtime)

    def delete_custom_topic_view_point_by_id_with_options(
        self,
        request: main_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTopicViewPointByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomTopicViewPointById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTopicViewPointByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_topic_view_point_by_id_with_options_async(
        self,
        request: main_models.DeleteCustomTopicViewPointByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomTopicViewPointByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomTopicViewPointById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomTopicViewPointByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_topic_view_point_by_id(
        self,
        request: main_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> main_models.DeleteCustomTopicViewPointByIdResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_topic_view_point_by_id_with_options(request, runtime)

    async def delete_custom_topic_view_point_by_id_async(
        self,
        request: main_models.DeleteCustomTopicViewPointByIdRequest,
    ) -> main_models.DeleteCustomTopicViewPointByIdResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_topic_view_point_by_id_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_dataset_document_with_options(
        self,
        request: main_models.DeleteDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_document_with_options_async(
        self,
        request: main_models.DeleteDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset_document(
        self,
        request: main_models.DeleteDatasetDocumentRequest,
    ) -> main_models.DeleteDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_document_with_options(request, runtime)

    async def delete_dataset_document_async(
        self,
        request: main_models.DeleteDatasetDocumentRequest,
    ) -> main_models.DeleteDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_document_with_options_async(request, runtime)

    def delete_docs_with_options(
        self,
        tmp_req: main_models.DeleteDocsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocsResponse:
        tmp_req.validate()
        request = main_models.DeleteDocsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_docs_with_options_async(
        self,
        tmp_req: main_models.DeleteDocsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocsResponse:
        tmp_req.validate()
        request = main_models.DeleteDocsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_docs(
        self,
        request: main_models.DeleteDocsRequest,
    ) -> main_models.DeleteDocsResponse:
        runtime = RuntimeOptions()
        return self.delete_docs_with_options(request, runtime)

    async def delete_docs_async(
        self,
        request: main_models.DeleteDocsRequest,
    ) -> main_models.DeleteDocsResponse:
        runtime = RuntimeOptions()
        return await self.delete_docs_with_options_async(request, runtime)

    def delete_fact_audit_url_with_options(
        self,
        request: main_models.DeleteFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFactAuditUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fact_audit_url_with_options_async(
        self,
        request: main_models.DeleteFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFactAuditUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fact_audit_url(
        self,
        request: main_models.DeleteFactAuditUrlRequest,
    ) -> main_models.DeleteFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return self.delete_fact_audit_url_with_options(request, runtime)

    async def delete_fact_audit_url_async(
        self,
        request: main_models.DeleteFactAuditUrlRequest,
    ) -> main_models.DeleteFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return await self.delete_fact_audit_url_with_options_async(request, runtime)

    def delete_general_config_with_options(
        self,
        request: main_models.DeleteGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGeneralConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_general_config_with_options_async(
        self,
        request: main_models.DeleteGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGeneralConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_general_config(
        self,
        request: main_models.DeleteGeneralConfigRequest,
    ) -> main_models.DeleteGeneralConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_general_config_with_options(request, runtime)

    async def delete_general_config_async(
        self,
        request: main_models.DeleteGeneralConfigRequest,
    ) -> main_models.DeleteGeneralConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_general_config_with_options_async(request, runtime)

    def delete_generated_content_with_options(
        self,
        request: main_models.DeleteGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_generated_content_with_options_async(
        self,
        request: main_models.DeleteGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_generated_content(
        self,
        request: main_models.DeleteGeneratedContentRequest,
    ) -> main_models.DeleteGeneratedContentResponse:
        runtime = RuntimeOptions()
        return self.delete_generated_content_with_options(request, runtime)

    async def delete_generated_content_async(
        self,
        request: main_models.DeleteGeneratedContentRequest,
    ) -> main_models.DeleteGeneratedContentResponse:
        runtime = RuntimeOptions()
        return await self.delete_generated_content_with_options_async(request, runtime)

    def delete_intervene_rule_with_options(
        self,
        request: main_models.DeleteInterveneRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInterveneRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInterveneRule',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_intervene_rule_with_options_async(
        self,
        request: main_models.DeleteInterveneRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInterveneRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInterveneRule',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_intervene_rule(
        self,
        request: main_models.DeleteInterveneRuleRequest,
    ) -> main_models.DeleteInterveneRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_intervene_rule_with_options(request, runtime)

    async def delete_intervene_rule_async(
        self,
        request: main_models.DeleteInterveneRuleRequest,
    ) -> main_models.DeleteInterveneRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_intervene_rule_with_options_async(request, runtime)

    def delete_material_by_id_with_options(
        self,
        request: main_models.DeleteMaterialByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_by_id_with_options_async(
        self,
        request: main_models.DeleteMaterialByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMaterialByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMaterialById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material_by_id(
        self,
        request: main_models.DeleteMaterialByIdRequest,
    ) -> main_models.DeleteMaterialByIdResponse:
        runtime = RuntimeOptions()
        return self.delete_material_by_id_with_options(request, runtime)

    async def delete_material_by_id_async(
        self,
        request: main_models.DeleteMaterialByIdRequest,
    ) -> main_models.DeleteMaterialByIdResponse:
        runtime = RuntimeOptions()
        return await self.delete_material_by_id_with_options_async(request, runtime)

    def delete_style_learning_result_with_options(
        self,
        request: main_models.DeleteStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_style_learning_result_with_options_async(
        self,
        request: main_models.DeleteStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_style_learning_result(
        self,
        request: main_models.DeleteStyleLearningResultRequest,
    ) -> main_models.DeleteStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return self.delete_style_learning_result_with_options(request, runtime)

    async def delete_style_learning_result_async(
        self,
        request: main_models.DeleteStyleLearningResultRequest,
    ) -> main_models.DeleteStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return await self.delete_style_learning_result_with_options_async(request, runtime)

    def document_extraction_with_options(
        self,
        tmp_req: main_models.DocumentExtractionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentExtractionResponse:
        tmp_req.validate()
        request = main_models.DocumentExtractionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.urls):
            request.urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocumentExtraction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentExtractionResponse(),
            self.call_api(params, req, runtime)
        )

    async def document_extraction_with_options_async(
        self,
        tmp_req: main_models.DocumentExtractionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentExtractionResponse:
        tmp_req.validate()
        request = main_models.DocumentExtractionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.urls):
            request.urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.urls, 'Urls', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.urls_shrink):
            body['Urls'] = request.urls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocumentExtraction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentExtractionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def document_extraction(
        self,
        request: main_models.DocumentExtractionRequest,
    ) -> main_models.DocumentExtractionResponse:
        runtime = RuntimeOptions()
        return self.document_extraction_with_options(request, runtime)

    async def document_extraction_async(
        self,
        request: main_models.DocumentExtractionRequest,
    ) -> main_models.DocumentExtractionResponse:
        runtime = RuntimeOptions()
        return await self.document_extraction_with_options_async(request, runtime)

    def download_audit_note_with_options(
        self,
        request: main_models.DownloadAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadAuditNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_audit_note_with_options_async(
        self,
        request: main_models.DownloadAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadAuditNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_audit_note(
        self,
        request: main_models.DownloadAuditNoteRequest,
    ) -> main_models.DownloadAuditNoteResponse:
        runtime = RuntimeOptions()
        return self.download_audit_note_with_options(request, runtime)

    async def download_audit_note_async(
        self,
        request: main_models.DownloadAuditNoteRequest,
    ) -> main_models.DownloadAuditNoteResponse:
        runtime = RuntimeOptions()
        return await self.download_audit_note_with_options_async(request, runtime)

    def download_bidding_doc_with_options(
        self,
        request: main_models.DownloadBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadBiddingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_bidding_doc_with_options_async(
        self,
        request: main_models.DownloadBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DownloadBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadBiddingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_bidding_doc(
        self,
        request: main_models.DownloadBiddingDocRequest,
    ) -> main_models.DownloadBiddingDocResponse:
        runtime = RuntimeOptions()
        return self.download_bidding_doc_with_options(request, runtime)

    async def download_bidding_doc_async(
        self,
        request: main_models.DownloadBiddingDocRequest,
    ) -> main_models.DownloadBiddingDocResponse:
        runtime = RuntimeOptions()
        return await self.download_bidding_doc_with_options_async(request, runtime)

    def edit_audit_terms_with_options(
        self,
        tmp_req: main_models.EditAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditAuditTermsResponse:
        tmp_req.validate()
        request = main_models.EditAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exception_word):
            request.exception_word_shrink = Utils.array_to_string_with_specified_style(tmp_req.exception_word, 'ExceptionWord', 'json')
        body = {}
        if not DaraCore.is_null(request.exception_word_shrink):
            body['ExceptionWord'] = request.exception_word_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.suggest_word):
            body['SuggestWord'] = request.suggest_word
        if not DaraCore.is_null(request.terms_desc):
            body['TermsDesc'] = request.terms_desc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditAuditTermsResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_audit_terms_with_options_async(
        self,
        tmp_req: main_models.EditAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditAuditTermsResponse:
        tmp_req.validate()
        request = main_models.EditAuditTermsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exception_word):
            request.exception_word_shrink = Utils.array_to_string_with_specified_style(tmp_req.exception_word, 'ExceptionWord', 'json')
        body = {}
        if not DaraCore.is_null(request.exception_word_shrink):
            body['ExceptionWord'] = request.exception_word_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.suggest_word):
            body['SuggestWord'] = request.suggest_word
        if not DaraCore.is_null(request.terms_desc):
            body['TermsDesc'] = request.terms_desc
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditAuditTermsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_audit_terms(
        self,
        request: main_models.EditAuditTermsRequest,
    ) -> main_models.EditAuditTermsResponse:
        runtime = RuntimeOptions()
        return self.edit_audit_terms_with_options(request, runtime)

    async def edit_audit_terms_async(
        self,
        request: main_models.EditAuditTermsRequest,
    ) -> main_models.EditAuditTermsResponse:
        runtime = RuntimeOptions()
        return await self.edit_audit_terms_with_options_async(request, runtime)

    def edit_bidding_doc_with_options(
        self,
        request: main_models.EditBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_format):
            body['ContentFormat'] = request.content_format
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditBiddingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_bidding_doc_with_options_async(
        self,
        request: main_models.EditBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_format):
            body['ContentFormat'] = request.content_format
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditBiddingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_bidding_doc(
        self,
        request: main_models.EditBiddingDocRequest,
    ) -> main_models.EditBiddingDocResponse:
        runtime = RuntimeOptions()
        return self.edit_bidding_doc_with_options(request, runtime)

    async def edit_bidding_doc_async(
        self,
        request: main_models.EditBiddingDocRequest,
    ) -> main_models.EditBiddingDocResponse:
        runtime = RuntimeOptions()
        return await self.edit_bidding_doc_with_options_async(request, runtime)

    def export_analysis_tag_detail_by_task_id_with_options(
        self,
        tmp_req: main_models.ExportAnalysisTagDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnalysisTagDetailByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_analysis_tag_detail_by_task_id_with_options_async(
        self,
        tmp_req: main_models.ExportAnalysisTagDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ExportAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnalysisTagDetailByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_analysis_tag_detail_by_task_id(
        self,
        request: main_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.export_analysis_tag_detail_by_task_id_with_options(request, runtime)

    async def export_analysis_tag_detail_by_task_id_async(
        self,
        request: main_models.ExportAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ExportAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.export_analysis_tag_detail_by_task_id_with_options_async(request, runtime)

    def export_audit_content_result_with_options(
        self,
        request: main_models.ExportAuditContentResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAuditContentResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAuditContentResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAuditContentResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_audit_content_result_with_options_async(
        self,
        request: main_models.ExportAuditContentResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAuditContentResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAuditContentResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAuditContentResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_audit_content_result(
        self,
        request: main_models.ExportAuditContentResultRequest,
    ) -> main_models.ExportAuditContentResultResponse:
        runtime = RuntimeOptions()
        return self.export_audit_content_result_with_options(request, runtime)

    async def export_audit_content_result_async(
        self,
        request: main_models.ExportAuditContentResultRequest,
    ) -> main_models.ExportAuditContentResultResponse:
        runtime = RuntimeOptions()
        return await self.export_audit_content_result_with_options_async(request, runtime)

    def export_custom_source_analysis_task_with_options(
        self,
        request: main_models.ExportCustomSourceAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomSourceAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomSourceAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomSourceAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_custom_source_analysis_task_with_options_async(
        self,
        request: main_models.ExportCustomSourceAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomSourceAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomSourceAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomSourceAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_custom_source_analysis_task(
        self,
        request: main_models.ExportCustomSourceAnalysisTaskRequest,
    ) -> main_models.ExportCustomSourceAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.export_custom_source_analysis_task_with_options(request, runtime)

    async def export_custom_source_analysis_task_async(
        self,
        request: main_models.ExportCustomSourceAnalysisTaskRequest,
    ) -> main_models.ExportCustomSourceAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.export_custom_source_analysis_task_with_options_async(request, runtime)

    def export_generated_content_with_options(
        self,
        request: main_models.ExportGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_generated_content_with_options_async(
        self,
        request: main_models.ExportGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_generated_content(
        self,
        request: main_models.ExportGeneratedContentRequest,
    ) -> main_models.ExportGeneratedContentResponse:
        runtime = RuntimeOptions()
        return self.export_generated_content_with_options(request, runtime)

    async def export_generated_content_async(
        self,
        request: main_models.ExportGeneratedContentRequest,
    ) -> main_models.ExportGeneratedContentResponse:
        runtime = RuntimeOptions()
        return await self.export_generated_content_with_options_async(request, runtime)

    def export_hot_topic_planning_proposals_with_options(
        self,
        tmp_req: main_models.ExportHotTopicPlanningProposalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportHotTopicPlanningProposalsResponse:
        tmp_req.validate()
        request = main_models.ExportHotTopicPlanningProposalsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not DaraCore.is_null(tmp_req.titles):
            request.titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportHotTopicPlanningProposals',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHotTopicPlanningProposalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_hot_topic_planning_proposals_with_options_async(
        self,
        tmp_req: main_models.ExportHotTopicPlanningProposalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportHotTopicPlanningProposalsResponse:
        tmp_req.validate()
        request = main_models.ExportHotTopicPlanningProposalsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not DaraCore.is_null(tmp_req.titles):
            request.titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportHotTopicPlanningProposals',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHotTopicPlanningProposalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_hot_topic_planning_proposals(
        self,
        request: main_models.ExportHotTopicPlanningProposalsRequest,
    ) -> main_models.ExportHotTopicPlanningProposalsResponse:
        runtime = RuntimeOptions()
        return self.export_hot_topic_planning_proposals_with_options(request, runtime)

    async def export_hot_topic_planning_proposals_async(
        self,
        request: main_models.ExportHotTopicPlanningProposalsRequest,
    ) -> main_models.ExportHotTopicPlanningProposalsResponse:
        runtime = RuntimeOptions()
        return await self.export_hot_topic_planning_proposals_with_options_async(request, runtime)

    def export_intervenes_with_options(
        self,
        request: main_models.ExportIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_intervenes_with_options_async(
        self,
        request: main_models.ExportIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_intervenes(
        self,
        request: main_models.ExportIntervenesRequest,
    ) -> main_models.ExportIntervenesResponse:
        runtime = RuntimeOptions()
        return self.export_intervenes_with_options(request, runtime)

    async def export_intervenes_async(
        self,
        request: main_models.ExportIntervenesRequest,
    ) -> main_models.ExportIntervenesResponse:
        runtime = RuntimeOptions()
        return await self.export_intervenes_with_options_async(request, runtime)

    def feedback_dialogue_with_options(
        self,
        tmp_req: main_models.FeedbackDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackDialogueResponse:
        tmp_req.validate()
        request = main_models.FeedbackDialogueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rating_tags):
            request.rating_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not DaraCore.is_null(request.good_text):
            body['GoodText'] = request.good_text
        if not DaraCore.is_null(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not DaraCore.is_null(request.rating):
            body['Rating'] = request.rating
        if not DaraCore.is_null(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackDialogue',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_dialogue_with_options_async(
        self,
        tmp_req: main_models.FeedbackDialogueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackDialogueResponse:
        tmp_req.validate()
        request = main_models.FeedbackDialogueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rating_tags):
            request.rating_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.rating_tags, 'RatingTags', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.customer_response):
            body['CustomerResponse'] = request.customer_response
        if not DaraCore.is_null(request.good_text):
            body['GoodText'] = request.good_text
        if not DaraCore.is_null(request.modified_response):
            body['ModifiedResponse'] = request.modified_response
        if not DaraCore.is_null(request.rating):
            body['Rating'] = request.rating
        if not DaraCore.is_null(request.rating_tags_shrink):
            body['RatingTags'] = request.rating_tags_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackDialogue',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_dialogue(
        self,
        request: main_models.FeedbackDialogueRequest,
    ) -> main_models.FeedbackDialogueResponse:
        runtime = RuntimeOptions()
        return self.feedback_dialogue_with_options(request, runtime)

    async def feedback_dialogue_async(
        self,
        request: main_models.FeedbackDialogueRequest,
    ) -> main_models.FeedbackDialogueResponse:
        runtime = RuntimeOptions()
        return await self.feedback_dialogue_with_options_async(request, runtime)

    def fetch_export_terms_task_with_options(
        self,
        request: main_models.FetchExportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchExportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchExportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchExportTermsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_export_terms_task_with_options_async(
        self,
        request: main_models.FetchExportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchExportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchExportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchExportTermsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_export_terms_task(
        self,
        request: main_models.FetchExportTermsTaskRequest,
    ) -> main_models.FetchExportTermsTaskResponse:
        runtime = RuntimeOptions()
        return self.fetch_export_terms_task_with_options(request, runtime)

    async def fetch_export_terms_task_async(
        self,
        request: main_models.FetchExportTermsTaskRequest,
    ) -> main_models.FetchExportTermsTaskResponse:
        runtime = RuntimeOptions()
        return await self.fetch_export_terms_task_with_options_async(request, runtime)

    def fetch_export_word_task_with_options(
        self,
        request: main_models.FetchExportWordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchExportWordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchExportWordTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchExportWordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_export_word_task_with_options_async(
        self,
        request: main_models.FetchExportWordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchExportWordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchExportWordTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchExportWordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_export_word_task(
        self,
        request: main_models.FetchExportWordTaskRequest,
    ) -> main_models.FetchExportWordTaskResponse:
        runtime = RuntimeOptions()
        return self.fetch_export_word_task_with_options(request, runtime)

    async def fetch_export_word_task_async(
        self,
        request: main_models.FetchExportWordTaskRequest,
    ) -> main_models.FetchExportWordTaskResponse:
        runtime = RuntimeOptions()
        return await self.fetch_export_word_task_with_options_async(request, runtime)

    def fetch_image_task_with_options(
        self,
        tmp_req: main_models.FetchImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchImageTaskResponse:
        tmp_req.validate()
        request = main_models.FetchImageTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not DaraCore.is_null(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchImageTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_image_task_with_options_async(
        self,
        tmp_req: main_models.FetchImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchImageTaskResponse:
        tmp_req.validate()
        request = main_models.FetchImageTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'TaskIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not DaraCore.is_null(request.task_id_list_shrink):
            body['TaskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchImageTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_image_task(
        self,
        request: main_models.FetchImageTaskRequest,
    ) -> main_models.FetchImageTaskResponse:
        runtime = RuntimeOptions()
        return self.fetch_image_task_with_options(request, runtime)

    async def fetch_image_task_async(
        self,
        request: main_models.FetchImageTaskRequest,
    ) -> main_models.FetchImageTaskResponse:
        runtime = RuntimeOptions()
        return await self.fetch_image_task_with_options_async(request, runtime)

    def fetch_import_terms_task_with_options(
        self,
        request: main_models.FetchImportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchImportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchImportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchImportTermsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_import_terms_task_with_options_async(
        self,
        request: main_models.FetchImportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FetchImportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FetchImportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FetchImportTermsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_import_terms_task(
        self,
        request: main_models.FetchImportTermsTaskRequest,
    ) -> main_models.FetchImportTermsTaskResponse:
        runtime = RuntimeOptions()
        return self.fetch_import_terms_task_with_options(request, runtime)

    async def fetch_import_terms_task_async(
        self,
        request: main_models.FetchImportTermsTaskRequest,
    ) -> main_models.FetchImportTermsTaskResponse:
        runtime = RuntimeOptions()
        return await self.fetch_import_terms_task_with_options_async(request, runtime)

    def generate_export_word_task_with_options(
        self,
        request: main_models.GenerateExportWordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateExportWordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generated_content_id):
            body['GeneratedContentId'] = request.generated_content_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateExportWordTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateExportWordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_export_word_task_with_options_async(
        self,
        request: main_models.GenerateExportWordTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateExportWordTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generated_content_id):
            body['GeneratedContentId'] = request.generated_content_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateExportWordTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateExportWordTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_export_word_task(
        self,
        request: main_models.GenerateExportWordTaskRequest,
    ) -> main_models.GenerateExportWordTaskResponse:
        runtime = RuntimeOptions()
        return self.generate_export_word_task_with_options(request, runtime)

    async def generate_export_word_task_async(
        self,
        request: main_models.GenerateExportWordTaskRequest,
    ) -> main_models.GenerateExportWordTaskResponse:
        runtime = RuntimeOptions()
        return await self.generate_export_word_task_with_options_async(request, runtime)

    def generate_file_url_by_key_with_options(
        self,
        request: main_models.GenerateFileUrlByKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileUrlByKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileUrlByKey',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateFileUrlByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_file_url_by_key_with_options_async(
        self,
        request: main_models.GenerateFileUrlByKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileUrlByKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileUrlByKey',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateFileUrlByKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_file_url_by_key(
        self,
        request: main_models.GenerateFileUrlByKeyRequest,
    ) -> main_models.GenerateFileUrlByKeyResponse:
        runtime = RuntimeOptions()
        return self.generate_file_url_by_key_with_options(request, runtime)

    async def generate_file_url_by_key_async(
        self,
        request: main_models.GenerateFileUrlByKeyRequest,
    ) -> main_models.GenerateFileUrlByKeyResponse:
        runtime = RuntimeOptions()
        return await self.generate_file_url_by_key_with_options_async(request, runtime)

    def generate_image_task_with_options(
        self,
        tmp_req: main_models.GenerateImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateImageTaskResponse:
        tmp_req.validate()
        request = main_models.GenerateImageTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.paragraph_list):
            request.paragraph_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not DaraCore.is_null(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateImageTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_image_task_with_options_async(
        self,
        tmp_req: main_models.GenerateImageTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateImageTaskResponse:
        tmp_req.validate()
        request = main_models.GenerateImageTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.paragraph_list):
            request.paragraph_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.paragraph_list, 'ParagraphList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.article_task_id):
            body['ArticleTaskId'] = request.article_task_id
        if not DaraCore.is_null(request.paragraph_list_shrink):
            body['ParagraphList'] = request.paragraph_list_shrink
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateImageTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_image_task(
        self,
        request: main_models.GenerateImageTaskRequest,
    ) -> main_models.GenerateImageTaskResponse:
        runtime = RuntimeOptions()
        return self.generate_image_task_with_options(request, runtime)

    async def generate_image_task_async(
        self,
        request: main_models.GenerateImageTaskRequest,
    ) -> main_models.GenerateImageTaskResponse:
        runtime = RuntimeOptions()
        return await self.generate_image_task_with_options_async(request, runtime)

    def generate_upload_config_with_options(
        self,
        request: main_models.GenerateUploadConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_config_with_options_async(
        self,
        request: main_models.GenerateUploadConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.parent_dir):
            body['ParentDir'] = request.parent_dir
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_config(
        self,
        request: main_models.GenerateUploadConfigRequest,
    ) -> main_models.GenerateUploadConfigResponse:
        runtime = RuntimeOptions()
        return self.generate_upload_config_with_options(request, runtime)

    async def generate_upload_config_async(
        self,
        request: main_models.GenerateUploadConfigRequest,
    ) -> main_models.GenerateUploadConfigResponse:
        runtime = RuntimeOptions()
        return await self.generate_upload_config_with_options_async(request, runtime)

    def generate_view_point_with_options(
        self,
        tmp_req: main_models.GenerateViewPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateViewPointResponse:
        tmp_req.validate()
        request = main_models.GenerateViewPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateViewPoint',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateViewPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_view_point_with_options_async(
        self,
        tmp_req: main_models.GenerateViewPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateViewPointResponse:
        tmp_req.validate()
        request = main_models.GenerateViewPointShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateViewPoint',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateViewPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_view_point(
        self,
        request: main_models.GenerateViewPointRequest,
    ) -> main_models.GenerateViewPointResponse:
        runtime = RuntimeOptions()
        return self.generate_view_point_with_options(request, runtime)

    async def generate_view_point_async(
        self,
        request: main_models.GenerateViewPointRequest,
    ) -> main_models.GenerateViewPointResponse:
        runtime = RuntimeOptions()
        return await self.generate_view_point_with_options_async(request, runtime)

    def get_audit_note_post_processing_status_with_options(
        self,
        request: main_models.GetAuditNotePostProcessingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditNotePostProcessingStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditNotePostProcessingStatus',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditNotePostProcessingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_note_post_processing_status_with_options_async(
        self,
        request: main_models.GetAuditNotePostProcessingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditNotePostProcessingStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditNotePostProcessingStatus',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditNotePostProcessingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_note_post_processing_status(
        self,
        request: main_models.GetAuditNotePostProcessingStatusRequest,
    ) -> main_models.GetAuditNotePostProcessingStatusResponse:
        runtime = RuntimeOptions()
        return self.get_audit_note_post_processing_status_with_options(request, runtime)

    async def get_audit_note_post_processing_status_async(
        self,
        request: main_models.GetAuditNotePostProcessingStatusRequest,
    ) -> main_models.GetAuditNotePostProcessingStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_note_post_processing_status_with_options_async(request, runtime)

    def get_audit_note_processing_status_with_options(
        self,
        request: main_models.GetAuditNoteProcessingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditNoteProcessingStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditNoteProcessingStatus',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditNoteProcessingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_note_processing_status_with_options_async(
        self,
        request: main_models.GetAuditNoteProcessingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditNoteProcessingStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditNoteProcessingStatus',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditNoteProcessingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_note_processing_status(
        self,
        request: main_models.GetAuditNoteProcessingStatusRequest,
    ) -> main_models.GetAuditNoteProcessingStatusResponse:
        runtime = RuntimeOptions()
        return self.get_audit_note_processing_status_with_options(request, runtime)

    async def get_audit_note_processing_status_async(
        self,
        request: main_models.GetAuditNoteProcessingStatusRequest,
    ) -> main_models.GetAuditNoteProcessingStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_note_processing_status_with_options_async(request, runtime)

    def get_auto_clips_task_info_with_options(
        self,
        request: main_models.GetAutoClipsTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoClipsTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoClipsTaskInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoClipsTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_clips_task_info_with_options_async(
        self,
        request: main_models.GetAutoClipsTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoClipsTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoClipsTaskInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoClipsTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_clips_task_info(
        self,
        request: main_models.GetAutoClipsTaskInfoRequest,
    ) -> main_models.GetAutoClipsTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_auto_clips_task_info_with_options(request, runtime)

    async def get_auto_clips_task_info_async(
        self,
        request: main_models.GetAutoClipsTaskInfoRequest,
    ) -> main_models.GetAutoClipsTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_clips_task_info_with_options_async(request, runtime)

    def get_available_audit_notes_with_options(
        self,
        request: main_models.GetAvailableAuditNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailableAuditNotesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailableAuditNotes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailableAuditNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_available_audit_notes_with_options_async(
        self,
        request: main_models.GetAvailableAuditNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailableAuditNotesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailableAuditNotes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailableAuditNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_available_audit_notes(
        self,
        request: main_models.GetAvailableAuditNotesRequest,
    ) -> main_models.GetAvailableAuditNotesResponse:
        runtime = RuntimeOptions()
        return self.get_available_audit_notes_with_options(request, runtime)

    async def get_available_audit_notes_async(
        self,
        request: main_models.GetAvailableAuditNotesRequest,
    ) -> main_models.GetAvailableAuditNotesResponse:
        runtime = RuntimeOptions()
        return await self.get_available_audit_notes_with_options_async(request, runtime)

    def get_bidding_doc_info_with_options(
        self,
        request: main_models.GetBiddingDocInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBiddingDocInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBiddingDocInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBiddingDocInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bidding_doc_info_with_options_async(
        self,
        request: main_models.GetBiddingDocInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBiddingDocInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBiddingDocInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBiddingDocInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bidding_doc_info(
        self,
        request: main_models.GetBiddingDocInfoRequest,
    ) -> main_models.GetBiddingDocInfoResponse:
        runtime = RuntimeOptions()
        return self.get_bidding_doc_info_with_options(request, runtime)

    async def get_bidding_doc_info_async(
        self,
        request: main_models.GetBiddingDocInfoRequest,
    ) -> main_models.GetBiddingDocInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_bidding_doc_info_with_options_async(request, runtime)

    def get_bidding_remain_limit_num_with_options(
        self,
        request: main_models.GetBiddingRemainLimitNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBiddingRemainLimitNumResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_name):
            body['ApiName'] = request.api_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBiddingRemainLimitNum',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBiddingRemainLimitNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bidding_remain_limit_num_with_options_async(
        self,
        request: main_models.GetBiddingRemainLimitNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBiddingRemainLimitNumResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_name):
            body['ApiName'] = request.api_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBiddingRemainLimitNum',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBiddingRemainLimitNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bidding_remain_limit_num(
        self,
        request: main_models.GetBiddingRemainLimitNumRequest,
    ) -> main_models.GetBiddingRemainLimitNumResponse:
        runtime = RuntimeOptions()
        return self.get_bidding_remain_limit_num_with_options(request, runtime)

    async def get_bidding_remain_limit_num_async(
        self,
        request: main_models.GetBiddingRemainLimitNumRequest,
    ) -> main_models.GetBiddingRemainLimitNumResponse:
        runtime = RuntimeOptions()
        return await self.get_bidding_remain_limit_num_with_options_async(request, runtime)

    def get_categories_by_task_id_with_options(
        self,
        request: main_models.GetCategoriesByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCategoriesByTaskIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCategoriesByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCategoriesByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_categories_by_task_id_with_options_async(
        self,
        request: main_models.GetCategoriesByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCategoriesByTaskIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCategoriesByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCategoriesByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_categories_by_task_id(
        self,
        request: main_models.GetCategoriesByTaskIdRequest,
    ) -> main_models.GetCategoriesByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_categories_by_task_id_with_options(request, runtime)

    async def get_categories_by_task_id_async(
        self,
        request: main_models.GetCategoriesByTaskIdRequest,
    ) -> main_models.GetCategoriesByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_categories_by_task_id_with_options_async(request, runtime)

    def get_custom_hot_topic_broadcast_job_with_options(
        self,
        request: main_models.GetCustomHotTopicBroadcastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomHotTopicBroadcastJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomHotTopicBroadcastJob',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomHotTopicBroadcastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_hot_topic_broadcast_job_with_options_async(
        self,
        request: main_models.GetCustomHotTopicBroadcastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomHotTopicBroadcastJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomHotTopicBroadcastJob',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomHotTopicBroadcastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_hot_topic_broadcast_job(
        self,
        request: main_models.GetCustomHotTopicBroadcastJobRequest,
    ) -> main_models.GetCustomHotTopicBroadcastJobResponse:
        runtime = RuntimeOptions()
        return self.get_custom_hot_topic_broadcast_job_with_options(request, runtime)

    async def get_custom_hot_topic_broadcast_job_async(
        self,
        request: main_models.GetCustomHotTopicBroadcastJobRequest,
    ) -> main_models.GetCustomHotTopicBroadcastJobResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_hot_topic_broadcast_job_with_options_async(request, runtime)

    def get_custom_source_topic_analysis_task_with_options(
        self,
        request: main_models.GetCustomSourceTopicAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomSourceTopicAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomSourceTopicAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomSourceTopicAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_source_topic_analysis_task_with_options_async(
        self,
        request: main_models.GetCustomSourceTopicAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomSourceTopicAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomSourceTopicAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomSourceTopicAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_source_topic_analysis_task(
        self,
        request: main_models.GetCustomSourceTopicAnalysisTaskRequest,
    ) -> main_models.GetCustomSourceTopicAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.get_custom_source_topic_analysis_task_with_options(request, runtime)

    async def get_custom_source_topic_analysis_task_async(
        self,
        request: main_models.GetCustomSourceTopicAnalysisTaskRequest,
    ) -> main_models.GetCustomSourceTopicAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_source_topic_analysis_task_with_options_async(request, runtime)

    def get_custom_text_with_options(
        self,
        request: main_models.GetCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_text_with_options_async(
        self,
        request: main_models.GetCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_text(
        self,
        request: main_models.GetCustomTextRequest,
    ) -> main_models.GetCustomTextResponse:
        runtime = RuntimeOptions()
        return self.get_custom_text_with_options(request, runtime)

    async def get_custom_text_async(
        self,
        request: main_models.GetCustomTextRequest,
    ) -> main_models.GetCustomTextResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_text_with_options_async(request, runtime)

    def get_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        request: main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_topic_selection_perspective_analysis_task(
        self,
        request: main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.get_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.GetCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def get_data_source_order_config_with_options(
        self,
        request: main_models.GetDataSourceOrderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceOrderConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generate_technology):
            body['GenerateTechnology'] = request.generate_technology
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceOrderConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_order_config_with_options_async(
        self,
        request: main_models.GetDataSourceOrderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceOrderConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generate_technology):
            body['GenerateTechnology'] = request.generate_technology
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceOrderConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_order_config(
        self,
        request: main_models.GetDataSourceOrderConfigRequest,
    ) -> main_models.GetDataSourceOrderConfigResponse:
        runtime = RuntimeOptions()
        return self.get_data_source_order_config_with_options(request, runtime)

    async def get_data_source_order_config_async(
        self,
        request: main_models.GetDataSourceOrderConfigRequest,
    ) -> main_models.GetDataSourceOrderConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_data_source_order_config_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_dataset_document_with_options(
        self,
        tmp_req: main_models.GetDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.GetDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.include_fields):
            request.include_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not DaraCore.is_null(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_document_with_options_async(
        self,
        tmp_req: main_models.GetDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.GetDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.include_fields):
            request.include_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.doc_uuid):
            body['DocUuid'] = request.doc_uuid
        if not DaraCore.is_null(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_document(
        self,
        request: main_models.GetDatasetDocumentRequest,
    ) -> main_models.GetDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return self.get_dataset_document_with_options(request, runtime)

    async def get_dataset_document_async(
        self,
        request: main_models.GetDatasetDocumentRequest,
    ) -> main_models.GetDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return await self.get_dataset_document_with_options_async(request, runtime)

    def get_deep_write_task_with_options(
        self,
        request: main_models.GetDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeepWriteTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeepWriteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deep_write_task_with_options_async(
        self,
        request: main_models.GetDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeepWriteTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeepWriteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deep_write_task(
        self,
        request: main_models.GetDeepWriteTaskRequest,
    ) -> main_models.GetDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return self.get_deep_write_task_with_options(request, runtime)

    async def get_deep_write_task_async(
        self,
        request: main_models.GetDeepWriteTaskRequest,
    ) -> main_models.GetDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_deep_write_task_with_options_async(request, runtime)

    def get_deep_write_task_result_with_options(
        self,
        request: main_models.GetDeepWriteTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeepWriteTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeepWriteTaskResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeepWriteTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deep_write_task_result_with_options_async(
        self,
        request: main_models.GetDeepWriteTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeepWriteTaskResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDeepWriteTaskResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeepWriteTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deep_write_task_result(
        self,
        request: main_models.GetDeepWriteTaskResultRequest,
    ) -> main_models.GetDeepWriteTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_deep_write_task_result_with_options(request, runtime)

    async def get_deep_write_task_result_async(
        self,
        request: main_models.GetDeepWriteTaskResultRequest,
    ) -> main_models.GetDeepWriteTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_deep_write_task_result_with_options_async(request, runtime)

    def get_doc_cluster_task_with_options(
        self,
        request: main_models.GetDocClusterTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocClusterTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocClusterTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_cluster_task_with_options_async(
        self,
        request: main_models.GetDocClusterTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocClusterTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocClusterTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_cluster_task(
        self,
        request: main_models.GetDocClusterTaskRequest,
    ) -> main_models.GetDocClusterTaskResponse:
        runtime = RuntimeOptions()
        return self.get_doc_cluster_task_with_options(request, runtime)

    async def get_doc_cluster_task_async(
        self,
        request: main_models.GetDocClusterTaskRequest,
    ) -> main_models.GetDocClusterTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_doc_cluster_task_with_options_async(request, runtime)

    def get_doc_info_with_options(
        self,
        request: main_models.GetDocInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_info_with_options_async(
        self,
        request: main_models.GetDocInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDocInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_info(
        self,
        request: main_models.GetDocInfoRequest,
    ) -> main_models.GetDocInfoResponse:
        runtime = RuntimeOptions()
        return self.get_doc_info_with_options(request, runtime)

    async def get_doc_info_async(
        self,
        request: main_models.GetDocInfoRequest,
    ) -> main_models.GetDocInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_doc_info_with_options_async(request, runtime)

    def get_enterprise_voc_analysis_task_with_options(
        self,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseVocAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_voc_analysis_task_with_options_async(
        self,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseVocAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_voc_analysis_task(
        self,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.get_enterprise_voc_analysis_task_with_options(request, runtime)

    async def get_enterprise_voc_analysis_task_async(
        self,
        request: main_models.GetEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.GetEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_enterprise_voc_analysis_task_with_options_async(request, runtime)

    def get_fact_audit_url_with_options(
        self,
        request: main_models.GetFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFactAuditUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fact_audit_url_with_options_async(
        self,
        request: main_models.GetFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFactAuditUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fact_audit_url(
        self,
        request: main_models.GetFactAuditUrlRequest,
    ) -> main_models.GetFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return self.get_fact_audit_url_with_options(request, runtime)

    async def get_fact_audit_url_async(
        self,
        request: main_models.GetFactAuditUrlRequest,
    ) -> main_models.GetFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_fact_audit_url_with_options_async(request, runtime)

    def get_file_content_length_with_options(
        self,
        request: main_models.GetFileContentLengthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileContentLengthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileContentLength',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileContentLengthResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_content_length_with_options_async(
        self,
        request: main_models.GetFileContentLengthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileContentLengthResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFileContentLength',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileContentLengthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_content_length(
        self,
        request: main_models.GetFileContentLengthRequest,
    ) -> main_models.GetFileContentLengthResponse:
        runtime = RuntimeOptions()
        return self.get_file_content_length_with_options(request, runtime)

    async def get_file_content_length_async(
        self,
        request: main_models.GetFileContentLengthRequest,
    ) -> main_models.GetFileContentLengthResponse:
        runtime = RuntimeOptions()
        return await self.get_file_content_length_with_options_async(request, runtime)

    def get_general_config_with_options(
        self,
        request: main_models.GetGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGeneralConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_general_config_with_options_async(
        self,
        request: main_models.GetGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGeneralConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_general_config(
        self,
        request: main_models.GetGeneralConfigRequest,
    ) -> main_models.GetGeneralConfigResponse:
        runtime = RuntimeOptions()
        return self.get_general_config_with_options(request, runtime)

    async def get_general_config_async(
        self,
        request: main_models.GetGeneralConfigRequest,
    ) -> main_models.GetGeneralConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_general_config_with_options_async(request, runtime)

    def get_generated_content_with_options(
        self,
        request: main_models.GetGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_generated_content_with_options_async(
        self,
        request: main_models.GetGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGeneratedContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_generated_content(
        self,
        request: main_models.GetGeneratedContentRequest,
    ) -> main_models.GetGeneratedContentResponse:
        runtime = RuntimeOptions()
        return self.get_generated_content_with_options(request, runtime)

    async def get_generated_content_async(
        self,
        request: main_models.GetGeneratedContentRequest,
    ) -> main_models.GetGeneratedContentResponse:
        runtime = RuntimeOptions()
        return await self.get_generated_content_with_options_async(request, runtime)

    def get_hot_topic_broadcast_with_options(
        self,
        tmp_req: main_models.GetHotTopicBroadcastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotTopicBroadcastResponse:
        tmp_req.validate()
        request = main_models.GetHotTopicBroadcastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.locations):
            request.locations_shrink = Utils.array_to_string_with_specified_style(tmp_req.locations, 'Locations', 'json')
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'StepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.step_for_news_broadcast_content_config):
            request.step_for_news_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_news_broadcast_content_config, 'StepForNewsBroadcastContentConfig', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.calc_total_token):
            body['CalcTotalToken'] = request.calc_total_token
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.location_query):
            body['LocationQuery'] = request.location_query
        if not DaraCore.is_null(request.locations_shrink):
            body['Locations'] = request.locations_shrink
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['StepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.step_for_news_broadcast_content_config_shrink):
            body['StepForNewsBroadcastContentConfig'] = request.step_for_news_broadcast_content_config_shrink
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotTopicBroadcast',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotTopicBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hot_topic_broadcast_with_options_async(
        self,
        tmp_req: main_models.GetHotTopicBroadcastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotTopicBroadcastResponse:
        tmp_req.validate()
        request = main_models.GetHotTopicBroadcastShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.locations):
            request.locations_shrink = Utils.array_to_string_with_specified_style(tmp_req.locations, 'Locations', 'json')
        if not DaraCore.is_null(tmp_req.step_for_custom_summary_style_config):
            request.step_for_custom_summary_style_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_custom_summary_style_config, 'StepForCustomSummaryStyleConfig', 'json')
        if not DaraCore.is_null(tmp_req.step_for_news_broadcast_content_config):
            request.step_for_news_broadcast_content_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.step_for_news_broadcast_content_config, 'StepForNewsBroadcastContentConfig', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.calc_total_token):
            body['CalcTotalToken'] = request.calc_total_token
        if not DaraCore.is_null(request.category):
            body['Category'] = request.category
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.location_query):
            body['LocationQuery'] = request.location_query
        if not DaraCore.is_null(request.locations_shrink):
            body['Locations'] = request.locations_shrink
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.step_for_custom_summary_style_config_shrink):
            body['StepForCustomSummaryStyleConfig'] = request.step_for_custom_summary_style_config_shrink
        if not DaraCore.is_null(request.step_for_news_broadcast_content_config_shrink):
            body['StepForNewsBroadcastContentConfig'] = request.step_for_news_broadcast_content_config_shrink
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetHotTopicBroadcast',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotTopicBroadcastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hot_topic_broadcast(
        self,
        request: main_models.GetHotTopicBroadcastRequest,
    ) -> main_models.GetHotTopicBroadcastResponse:
        runtime = RuntimeOptions()
        return self.get_hot_topic_broadcast_with_options(request, runtime)

    async def get_hot_topic_broadcast_async(
        self,
        request: main_models.GetHotTopicBroadcastRequest,
    ) -> main_models.GetHotTopicBroadcastResponse:
        runtime = RuntimeOptions()
        return await self.get_hot_topic_broadcast_with_options_async(request, runtime)

    def get_intervene_global_reply_with_options(
        self,
        request: main_models.GetInterveneGlobalReplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneGlobalReplyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneGlobalReply',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_global_reply_with_options_async(
        self,
        request: main_models.GetInterveneGlobalReplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneGlobalReplyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneGlobalReply',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_global_reply(
        self,
        request: main_models.GetInterveneGlobalReplyRequest,
    ) -> main_models.GetInterveneGlobalReplyResponse:
        runtime = RuntimeOptions()
        return self.get_intervene_global_reply_with_options(request, runtime)

    async def get_intervene_global_reply_async(
        self,
        request: main_models.GetInterveneGlobalReplyRequest,
    ) -> main_models.GetInterveneGlobalReplyResponse:
        runtime = RuntimeOptions()
        return await self.get_intervene_global_reply_with_options_async(request, runtime)

    def get_intervene_import_task_info_with_options(
        self,
        request: main_models.GetInterveneImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneImportTaskInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_import_task_info_with_options_async(
        self,
        request: main_models.GetInterveneImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneImportTaskInfo',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_import_task_info(
        self,
        request: main_models.GetInterveneImportTaskInfoRequest,
    ) -> main_models.GetInterveneImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_intervene_import_task_info_with_options(request, runtime)

    async def get_intervene_import_task_info_async(
        self,
        request: main_models.GetInterveneImportTaskInfoRequest,
    ) -> main_models.GetInterveneImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_intervene_import_task_info_with_options_async(request, runtime)

    def get_intervene_rule_detail_with_options(
        self,
        request: main_models.GetInterveneRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneRuleDetail',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_rule_detail_with_options_async(
        self,
        request: main_models.GetInterveneRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneRuleDetail',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_rule_detail(
        self,
        request: main_models.GetInterveneRuleDetailRequest,
    ) -> main_models.GetInterveneRuleDetailResponse:
        runtime = RuntimeOptions()
        return self.get_intervene_rule_detail_with_options(request, runtime)

    async def get_intervene_rule_detail_async(
        self,
        request: main_models.GetInterveneRuleDetailRequest,
    ) -> main_models.GetInterveneRuleDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_intervene_rule_detail_with_options_async(request, runtime)

    def get_intervene_template_file_url_with_options(
        self,
        request: main_models.GetInterveneTemplateFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneTemplateFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneTemplateFileUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneTemplateFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intervene_template_file_url_with_options_async(
        self,
        request: main_models.GetInterveneTemplateFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInterveneTemplateFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInterveneTemplateFileUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInterveneTemplateFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intervene_template_file_url(
        self,
        request: main_models.GetInterveneTemplateFileUrlRequest,
    ) -> main_models.GetInterveneTemplateFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_intervene_template_file_url_with_options(request, runtime)

    async def get_intervene_template_file_url_async(
        self,
        request: main_models.GetInterveneTemplateFileUrlRequest,
    ) -> main_models.GetInterveneTemplateFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_intervene_template_file_url_with_options_async(request, runtime)

    def get_material_by_id_with_options(
        self,
        request: main_models.GetMaterialByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaterialByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMaterialById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaterialByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_material_by_id_with_options_async(
        self,
        request: main_models.GetMaterialByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMaterialByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMaterialById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMaterialByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_material_by_id(
        self,
        request: main_models.GetMaterialByIdRequest,
    ) -> main_models.GetMaterialByIdResponse:
        runtime = RuntimeOptions()
        return self.get_material_by_id_with_options(request, runtime)

    async def get_material_by_id_async(
        self,
        request: main_models.GetMaterialByIdRequest,
    ) -> main_models.GetMaterialByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_material_by_id_with_options_async(request, runtime)

    def get_ppt_config_with_options(
        self,
        request: main_models.GetPptConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPptConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPptConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPptConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ppt_config_with_options_async(
        self,
        request: main_models.GetPptConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPptConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPptConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPptConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ppt_config(
        self,
        request: main_models.GetPptConfigRequest,
    ) -> main_models.GetPptConfigResponse:
        runtime = RuntimeOptions()
        return self.get_ppt_config_with_options(request, runtime)

    async def get_ppt_config_async(
        self,
        request: main_models.GetPptConfigRequest,
    ) -> main_models.GetPptConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_ppt_config_with_options_async(request, runtime)

    def get_properties_with_options(
        self,
        request: main_models.GetPropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProperties',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_properties_with_options_async(
        self,
        request: main_models.GetPropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProperties',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_properties(
        self,
        request: main_models.GetPropertiesRequest,
    ) -> main_models.GetPropertiesResponse:
        runtime = RuntimeOptions()
        return self.get_properties_with_options(request, runtime)

    async def get_properties_async(
        self,
        request: main_models.GetPropertiesRequest,
    ) -> main_models.GetPropertiesResponse:
        runtime = RuntimeOptions()
        return await self.get_properties_with_options_async(request, runtime)

    def get_smart_audit_result_with_options(
        self,
        request: main_models.GetSmartAuditResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAuditResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAuditResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAuditResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_audit_result_with_options_async(
        self,
        request: main_models.GetSmartAuditResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartAuditResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartAuditResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartAuditResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_audit_result(
        self,
        request: main_models.GetSmartAuditResultRequest,
    ) -> main_models.GetSmartAuditResultResponse:
        runtime = RuntimeOptions()
        return self.get_smart_audit_result_with_options(request, runtime)

    async def get_smart_audit_result_async(
        self,
        request: main_models.GetSmartAuditResultRequest,
    ) -> main_models.GetSmartAuditResultResponse:
        runtime = RuntimeOptions()
        return await self.get_smart_audit_result_with_options_async(request, runtime)

    def get_smart_clip_task_with_options(
        self,
        request: main_models.GetSmartClipTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartClipTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartClipTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_clip_task_with_options_async(
        self,
        request: main_models.GetSmartClipTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmartClipTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSmartClipTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmartClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_clip_task(
        self,
        request: main_models.GetSmartClipTaskRequest,
    ) -> main_models.GetSmartClipTaskResponse:
        runtime = RuntimeOptions()
        return self.get_smart_clip_task_with_options(request, runtime)

    async def get_smart_clip_task_async(
        self,
        request: main_models.GetSmartClipTaskRequest,
    ) -> main_models.GetSmartClipTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_smart_clip_task_with_options_async(request, runtime)

    def get_style_learning_result_with_options(
        self,
        request: main_models.GetStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_style_learning_result_with_options_async(
        self,
        request: main_models.GetStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_style_learning_result(
        self,
        request: main_models.GetStyleLearningResultRequest,
    ) -> main_models.GetStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return self.get_style_learning_result_with_options(request, runtime)

    async def get_style_learning_result_async(
        self,
        request: main_models.GetStyleLearningResultRequest,
    ) -> main_models.GetStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return await self.get_style_learning_result_with_options_async(request, runtime)

    def get_topic_by_id_with_options(
        self,
        request: main_models.GetTopicByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_by_id_with_options_async(
        self,
        request: main_models.GetTopicByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicById',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_by_id(
        self,
        request: main_models.GetTopicByIdRequest,
    ) -> main_models.GetTopicByIdResponse:
        runtime = RuntimeOptions()
        return self.get_topic_by_id_with_options(request, runtime)

    async def get_topic_by_id_async(
        self,
        request: main_models.GetTopicByIdRequest,
    ) -> main_models.GetTopicByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_by_id_with_options_async(request, runtime)

    def get_topic_selection_perspective_analysis_task_with_options(
        self,
        request: main_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_selection_perspective_analysis_task_with_options_async(
        self,
        request: main_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_selection_perspective_analysis_task(
        self,
        request: main_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.get_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def get_topic_selection_perspective_analysis_task_async(
        self,
        request: main_models.GetTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.GetTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def import_intervene_file_with_options(
        self,
        request: main_models.ImportInterveneFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportInterveneFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportInterveneFile',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportInterveneFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_with_options_async(
        self,
        request: main_models.ImportInterveneFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportInterveneFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportInterveneFile',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportInterveneFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file(
        self,
        request: main_models.ImportInterveneFileRequest,
    ) -> main_models.ImportInterveneFileResponse:
        runtime = RuntimeOptions()
        return self.import_intervene_file_with_options(request, runtime)

    async def import_intervene_file_async(
        self,
        request: main_models.ImportInterveneFileRequest,
    ) -> main_models.ImportInterveneFileResponse:
        runtime = RuntimeOptions()
        return await self.import_intervene_file_with_options_async(request, runtime)

    def import_intervene_file_async_with_options(
        self,
        request: main_models.ImportInterveneFileAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportInterveneFileAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportInterveneFileAsync',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportInterveneFileAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_intervene_file_async_with_options_async(
        self,
        request: main_models.ImportInterveneFileAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportInterveneFileAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportInterveneFileAsync',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportInterveneFileAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_intervene_file_async(
        self,
        request: main_models.ImportInterveneFileAsyncRequest,
    ) -> main_models.ImportInterveneFileAsyncResponse:
        runtime = RuntimeOptions()
        return self.import_intervene_file_async_with_options(request, runtime)

    async def import_intervene_file_async_async(
        self,
        request: main_models.ImportInterveneFileAsyncRequest,
    ) -> main_models.ImportInterveneFileAsyncResponse:
        runtime = RuntimeOptions()
        return await self.import_intervene_file_async_with_options_async(request, runtime)

    def initiate_ppt_creation_with_options(
        self,
        request: main_models.InitiatePptCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitiatePptCreationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.outline):
            body['Outline'] = request.outline
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitiatePptCreation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitiatePptCreationResponse(),
            self.call_api(params, req, runtime)
        )

    async def initiate_ppt_creation_with_options_async(
        self,
        request: main_models.InitiatePptCreationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitiatePptCreationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.outline):
            body['Outline'] = request.outline
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InitiatePptCreation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitiatePptCreationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initiate_ppt_creation(
        self,
        request: main_models.InitiatePptCreationRequest,
    ) -> main_models.InitiatePptCreationResponse:
        runtime = RuntimeOptions()
        return self.initiate_ppt_creation_with_options(request, runtime)

    async def initiate_ppt_creation_async(
        self,
        request: main_models.InitiatePptCreationRequest,
    ) -> main_models.InitiatePptCreationResponse:
        runtime = RuntimeOptions()
        return await self.initiate_ppt_creation_with_options_async(request, runtime)

    def insert_intervene_global_reply_with_options(
        self,
        tmp_req: main_models.InsertInterveneGlobalReplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertInterveneGlobalReplyResponse:
        tmp_req.validate()
        request = main_models.InsertInterveneGlobalReplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertInterveneGlobalReply',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertInterveneGlobalReplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_global_reply_with_options_async(
        self,
        tmp_req: main_models.InsertInterveneGlobalReplyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertInterveneGlobalReplyResponse:
        tmp_req.validate()
        request = main_models.InsertInterveneGlobalReplyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reply_messag_list):
            request.reply_messag_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.reply_messag_list, 'ReplyMessagList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.reply_messag_list_shrink):
            body['ReplyMessagList'] = request.reply_messag_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertInterveneGlobalReply',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertInterveneGlobalReplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_global_reply(
        self,
        request: main_models.InsertInterveneGlobalReplyRequest,
    ) -> main_models.InsertInterveneGlobalReplyResponse:
        runtime = RuntimeOptions()
        return self.insert_intervene_global_reply_with_options(request, runtime)

    async def insert_intervene_global_reply_async(
        self,
        request: main_models.InsertInterveneGlobalReplyRequest,
    ) -> main_models.InsertInterveneGlobalReplyResponse:
        runtime = RuntimeOptions()
        return await self.insert_intervene_global_reply_with_options_async(request, runtime)

    def insert_intervene_rule_with_options(
        self,
        tmp_req: main_models.InsertInterveneRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertInterveneRuleResponse:
        tmp_req.validate()
        request = main_models.InsertInterveneRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertInterveneRule',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertInterveneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_intervene_rule_with_options_async(
        self,
        tmp_req: main_models.InsertInterveneRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InsertInterveneRuleResponse:
        tmp_req.validate()
        request = main_models.InsertInterveneRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.intervene_rule_config):
            request.intervene_rule_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.intervene_rule_config, 'InterveneRuleConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.intervene_rule_config_shrink):
            body['InterveneRuleConfig'] = request.intervene_rule_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InsertInterveneRule',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertInterveneRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_intervene_rule(
        self,
        request: main_models.InsertInterveneRuleRequest,
    ) -> main_models.InsertInterveneRuleResponse:
        runtime = RuntimeOptions()
        return self.insert_intervene_rule_with_options(request, runtime)

    async def insert_intervene_rule_async(
        self,
        request: main_models.InsertInterveneRuleRequest,
    ) -> main_models.InsertInterveneRuleResponse:
        runtime = RuntimeOptions()
        return await self.insert_intervene_rule_with_options_async(request, runtime)

    def list_analysis_tag_detail_by_task_id_with_options(
        self,
        tmp_req: main_models.ListAnalysisTagDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ListAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisTagDetailByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisTagDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_analysis_tag_detail_by_task_id_with_options_async(
        self,
        tmp_req: main_models.ListAnalysisTagDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        tmp_req.validate()
        request = main_models.ListAnalysisTagDetailByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.categories):
            request.categories_shrink = Utils.array_to_string_with_specified_style(tmp_req.categories, 'Categories', 'json')
        body = {}
        if not DaraCore.is_null(request.categories_shrink):
            body['Categories'] = request.categories_shrink
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAnalysisTagDetailByTaskId',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnalysisTagDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_analysis_tag_detail_by_task_id(
        self,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.list_analysis_tag_detail_by_task_id_with_options(request, runtime)

    async def list_analysis_tag_detail_by_task_id_async(
        self,
        request: main_models.ListAnalysisTagDetailByTaskIdRequest,
    ) -> main_models.ListAnalysisTagDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.list_analysis_tag_detail_by_task_id_with_options_async(request, runtime)

    def list_async_tasks_with_options(
        self,
        tmp_req: main_models.ListAsyncTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        tmp_req.validate()
        request = main_models.ListAsyncTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_status_list):
            request.task_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not DaraCore.is_null(tmp_req.task_type_list):
            request.task_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_code):
            body['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_async_tasks_with_options_async(
        self,
        tmp_req: main_models.ListAsyncTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsyncTasksResponse:
        tmp_req.validate()
        request = main_models.ListAsyncTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_status_list):
            request.task_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_status_list, 'TaskStatusList', 'json')
        if not DaraCore.is_null(tmp_req.task_type_list):
            request.task_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_type_list, 'TaskTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.task_code):
            body['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_status_list_shrink):
            body['TaskStatusList'] = request.task_status_list_shrink
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.task_type_list_shrink):
            body['TaskTypeList'] = request.task_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAsyncTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsyncTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_async_tasks(
        self,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        return self.list_async_tasks_with_options(request, runtime)

    async def list_async_tasks_async(
        self,
        request: main_models.ListAsyncTasksRequest,
    ) -> main_models.ListAsyncTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_async_tasks_with_options_async(request, runtime)

    def list_audit_content_error_types_with_options(
        self,
        request: main_models.ListAuditContentErrorTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditContentErrorTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditContentErrorTypes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditContentErrorTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audit_content_error_types_with_options_async(
        self,
        request: main_models.ListAuditContentErrorTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditContentErrorTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditContentErrorTypes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditContentErrorTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audit_content_error_types(
        self,
        request: main_models.ListAuditContentErrorTypesRequest,
    ) -> main_models.ListAuditContentErrorTypesResponse:
        runtime = RuntimeOptions()
        return self.list_audit_content_error_types_with_options(request, runtime)

    async def list_audit_content_error_types_async(
        self,
        request: main_models.ListAuditContentErrorTypesRequest,
    ) -> main_models.ListAuditContentErrorTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_audit_content_error_types_with_options_async(request, runtime)

    def list_audit_terms_with_options(
        self,
        request: main_models.ListAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditTermsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditTermsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audit_terms_with_options_async(
        self,
        request: main_models.ListAuditTermsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditTermsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditTerms',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditTermsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audit_terms(
        self,
        request: main_models.ListAuditTermsRequest,
    ) -> main_models.ListAuditTermsResponse:
        runtime = RuntimeOptions()
        return self.list_audit_terms_with_options(request, runtime)

    async def list_audit_terms_async(
        self,
        request: main_models.ListAuditTermsRequest,
    ) -> main_models.ListAuditTermsResponse:
        runtime = RuntimeOptions()
        return await self.list_audit_terms_with_options_async(request, runtime)

    def list_bidding_doc_with_options(
        self,
        request: main_models.ListBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBiddingDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bidding_doc_with_options_async(
        self,
        request: main_models.ListBiddingDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBiddingDocResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            body['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBiddingDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBiddingDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bidding_doc(
        self,
        request: main_models.ListBiddingDocRequest,
    ) -> main_models.ListBiddingDocResponse:
        runtime = RuntimeOptions()
        return self.list_bidding_doc_with_options(request, runtime)

    async def list_bidding_doc_async(
        self,
        request: main_models.ListBiddingDocRequest,
    ) -> main_models.ListBiddingDocResponse:
        runtime = RuntimeOptions()
        return await self.list_bidding_doc_with_options_async(request, runtime)

    def list_build_configs_with_options(
        self,
        request: main_models.ListBuildConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBuildConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBuildConfigs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBuildConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_build_configs_with_options_async(
        self,
        request: main_models.ListBuildConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBuildConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBuildConfigs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBuildConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_build_configs(
        self,
        request: main_models.ListBuildConfigsRequest,
    ) -> main_models.ListBuildConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_build_configs_with_options(request, runtime)

    async def list_build_configs_async(
        self,
        request: main_models.ListBuildConfigsRequest,
    ) -> main_models.ListBuildConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_build_configs_with_options_async(request, runtime)

    def list_custom_text_with_options(
        self,
        request: main_models.ListCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_text_with_options_async(
        self,
        request: main_models.ListCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_text(
        self,
        request: main_models.ListCustomTextRequest,
    ) -> main_models.ListCustomTextResponse:
        runtime = RuntimeOptions()
        return self.list_custom_text_with_options(request, runtime)

    async def list_custom_text_async(
        self,
        request: main_models.ListCustomTextRequest,
    ) -> main_models.ListCustomTextResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_text_with_options_async(request, runtime)

    def list_custom_view_points_with_options(
        self,
        tmp_req: main_models.ListCustomViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomViewPointsResponse:
        tmp_req.validate()
        request = main_models.ListCustomViewPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attitudes):
            request.attitudes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.attitude):
            body['Attitude'] = request.attitude
        if not DaraCore.is_null(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_view_points_with_options_async(
        self,
        tmp_req: main_models.ListCustomViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomViewPointsResponse:
        tmp_req.validate()
        request = main_models.ListCustomViewPointsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attitudes):
            request.attitudes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attitudes, 'Attitudes', 'json')
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.attitude):
            body['Attitude'] = request.attitude
        if not DaraCore.is_null(request.attitudes_shrink):
            body['Attitudes'] = request.attitudes_shrink
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_view_points(
        self,
        request: main_models.ListCustomViewPointsRequest,
    ) -> main_models.ListCustomViewPointsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_view_points_with_options(request, runtime)

    async def list_custom_view_points_async(
        self,
        request: main_models.ListCustomViewPointsRequest,
    ) -> main_models.ListCustomViewPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_view_points_with_options_async(request, runtime)

    def list_dataset_documents_with_options(
        self,
        tmp_req: main_models.ListDatasetDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListDatasetDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_fields):
            request.exclude_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_fields, 'ExcludeFields', 'json')
        if not DaraCore.is_null(tmp_req.include_fields):
            request.include_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.exclude_fields_shrink):
            body['ExcludeFields'] = request.exclude_fields_shrink
        if not DaraCore.is_null(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_documents_with_options_async(
        self,
        tmp_req: main_models.ListDatasetDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListDatasetDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_fields):
            request.exclude_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_fields, 'ExcludeFields', 'json')
        if not DaraCore.is_null(tmp_req.include_fields):
            request.include_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.include_fields, 'IncludeFields', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.exclude_fields_shrink):
            body['ExcludeFields'] = request.exclude_fields_shrink
        if not DaraCore.is_null(request.include_fields_shrink):
            body['IncludeFields'] = request.include_fields_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasetDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_documents(
        self,
        request: main_models.ListDatasetDocumentsRequest,
    ) -> main_models.ListDatasetDocumentsResponse:
        runtime = RuntimeOptions()
        return self.list_dataset_documents_with_options(request, runtime)

    async def list_dataset_documents_async(
        self,
        request: main_models.ListDatasetDocumentsRequest,
    ) -> main_models.ListDatasetDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.list_dataset_documents_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.include_config):
            body['IncludeConfig'] = request.include_config
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.dataset_type):
            body['DatasetType'] = request.dataset_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.include_config):
            body['IncludeConfig'] = request.include_config
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_dialogues_with_options(
        self,
        request: main_models.ListDialoguesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialoguesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogues',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialoguesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dialogues_with_options_async(
        self,
        request: main_models.ListDialoguesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDialoguesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.dialogue_type):
            body['DialogueType'] = request.dialogue_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDialogues',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDialoguesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dialogues(
        self,
        request: main_models.ListDialoguesRequest,
    ) -> main_models.ListDialoguesResponse:
        runtime = RuntimeOptions()
        return self.list_dialogues_with_options(request, runtime)

    async def list_dialogues_async(
        self,
        request: main_models.ListDialoguesRequest,
    ) -> main_models.ListDialoguesResponse:
        runtime = RuntimeOptions()
        return await self.list_dialogues_with_options_async(request, runtime)

    def list_docs_with_options(
        self,
        tmp_req: main_models.ListDocsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocsResponse:
        tmp_req.validate()
        request = main_models.ListDocsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.statuses_shrink):
            body['Statuses'] = request.statuses_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_docs_with_options_async(
        self,
        tmp_req: main_models.ListDocsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocsResponse:
        tmp_req.validate()
        request = main_models.ListDocsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.doc_name):
            body['DocName'] = request.doc_name
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.statuses_shrink):
            body['Statuses'] = request.statuses_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_docs(
        self,
        request: main_models.ListDocsRequest,
    ) -> main_models.ListDocsResponse:
        runtime = RuntimeOptions()
        return self.list_docs_with_options(request, runtime)

    async def list_docs_async(
        self,
        request: main_models.ListDocsRequest,
    ) -> main_models.ListDocsResponse:
        runtime = RuntimeOptions()
        return await self.list_docs_with_options_async(request, runtime)

    def list_document_retrieve_with_options(
        self,
        request: main_models.ListDocumentRetrieveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentRetrieveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.element_scope):
            body['ElementScope'] = request.element_scope
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office):
            body['Office'] = request.office
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_content_type):
            body['SubContentType'] = request.sub_content_type
        if not DaraCore.is_null(request.subject_classify):
            body['SubjectClassify'] = request.subject_classify
        if not DaraCore.is_null(request.word_size):
            body['WordSize'] = request.word_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentRetrieve',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentRetrieveResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_document_retrieve_with_options_async(
        self,
        request: main_models.ListDocumentRetrieveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentRetrieveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.element_scope):
            body['ElementScope'] = request.element_scope
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.office):
            body['Office'] = request.office
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.region):
            body['Region'] = request.region
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_content_type):
            body['SubContentType'] = request.sub_content_type
        if not DaraCore.is_null(request.subject_classify):
            body['SubjectClassify'] = request.subject_classify
        if not DaraCore.is_null(request.word_size):
            body['WordSize'] = request.word_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentRetrieve',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentRetrieveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_document_retrieve(
        self,
        request: main_models.ListDocumentRetrieveRequest,
    ) -> main_models.ListDocumentRetrieveResponse:
        runtime = RuntimeOptions()
        return self.list_document_retrieve_with_options(request, runtime)

    async def list_document_retrieve_async(
        self,
        request: main_models.ListDocumentRetrieveRequest,
    ) -> main_models.ListDocumentRetrieveResponse:
        runtime = RuntimeOptions()
        return await self.list_document_retrieve_with_options_async(request, runtime)

    def list_fresh_view_points_with_options(
        self,
        request: main_models.ListFreshViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreshViewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreshViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreshViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fresh_view_points_with_options_async(
        self,
        request: main_models.ListFreshViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreshViewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreshViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreshViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fresh_view_points(
        self,
        request: main_models.ListFreshViewPointsRequest,
    ) -> main_models.ListFreshViewPointsResponse:
        runtime = RuntimeOptions()
        return self.list_fresh_view_points_with_options(request, runtime)

    async def list_fresh_view_points_async(
        self,
        request: main_models.ListFreshViewPointsRequest,
    ) -> main_models.ListFreshViewPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_fresh_view_points_with_options_async(request, runtime)

    def list_general_configs_with_options(
        self,
        request: main_models.ListGeneralConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGeneralConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGeneralConfigs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGeneralConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_general_configs_with_options_async(
        self,
        request: main_models.ListGeneralConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGeneralConfigsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGeneralConfigs',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGeneralConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_general_configs(
        self,
        request: main_models.ListGeneralConfigsRequest,
    ) -> main_models.ListGeneralConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_general_configs_with_options(request, runtime)

    async def list_general_configs_async(
        self,
        request: main_models.ListGeneralConfigsRequest,
    ) -> main_models.ListGeneralConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_general_configs_with_options_async(request, runtime)

    def list_generated_contents_with_options(
        self,
        request: main_models.ListGeneratedContentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGeneratedContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGeneratedContents',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGeneratedContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_generated_contents_with_options_async(
        self,
        request: main_models.ListGeneratedContentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGeneratedContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content_domain):
            body['ContentDomain'] = request.content_domain
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.data_type):
            body['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGeneratedContents',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGeneratedContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_generated_contents(
        self,
        request: main_models.ListGeneratedContentsRequest,
    ) -> main_models.ListGeneratedContentsResponse:
        runtime = RuntimeOptions()
        return self.list_generated_contents_with_options(request, runtime)

    async def list_generated_contents_async(
        self,
        request: main_models.ListGeneratedContentsRequest,
    ) -> main_models.ListGeneratedContentsResponse:
        runtime = RuntimeOptions()
        return await self.list_generated_contents_with_options_async(request, runtime)

    def list_hot_news_with_type_with_options(
        self,
        tmp_req: main_models.ListHotNewsWithTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotNewsWithTypeResponse:
        tmp_req.validate()
        request = main_models.ListHotNewsWithTypeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.news_types):
            request.news_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.news_type):
            body['NewsType'] = request.news_type
        if not DaraCore.is_null(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotNewsWithType',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotNewsWithTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_news_with_type_with_options_async(
        self,
        tmp_req: main_models.ListHotNewsWithTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotNewsWithTypeResponse:
        tmp_req.validate()
        request = main_models.ListHotNewsWithTypeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.news_types):
            request.news_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.news_types, 'NewsTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.news_type):
            body['NewsType'] = request.news_type
        if not DaraCore.is_null(request.news_types_shrink):
            body['NewsTypes'] = request.news_types_shrink
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotNewsWithType',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotNewsWithTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_news_with_type(
        self,
        request: main_models.ListHotNewsWithTypeRequest,
    ) -> main_models.ListHotNewsWithTypeResponse:
        runtime = RuntimeOptions()
        return self.list_hot_news_with_type_with_options(request, runtime)

    async def list_hot_news_with_type_async(
        self,
        request: main_models.ListHotNewsWithTypeRequest,
    ) -> main_models.ListHotNewsWithTypeResponse:
        runtime = RuntimeOptions()
        return await self.list_hot_news_with_type_with_options_async(request, runtime)

    def list_hot_sources_with_options(
        self,
        request: main_models.ListHotSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotSources',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_sources_with_options_async(
        self,
        request: main_models.ListHotSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotSources',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_sources(
        self,
        request: main_models.ListHotSourcesRequest,
    ) -> main_models.ListHotSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_hot_sources_with_options(request, runtime)

    async def list_hot_sources_async(
        self,
        request: main_models.ListHotSourcesRequest,
    ) -> main_models.ListHotSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_hot_sources_with_options_async(request, runtime)

    def list_hot_topics_with_options(
        self,
        tmp_req: main_models.ListHotTopicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotTopicsResponse:
        tmp_req.validate()
        request = main_models.ListHotTopicsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not DaraCore.is_null(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotTopics',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_topics_with_options_async(
        self,
        tmp_req: main_models.ListHotTopicsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotTopicsResponse:
        tmp_req.validate()
        request = main_models.ListHotTopicsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topic_ids):
            request.topic_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.topic_ids, 'TopicIds', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic_ids_shrink):
            body['TopicIds'] = request.topic_ids_shrink
        if not DaraCore.is_null(request.topic_query):
            body['TopicQuery'] = request.topic_query
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.with_news):
            body['WithNews'] = request.with_news
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotTopics',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_topics(
        self,
        request: main_models.ListHotTopicsRequest,
    ) -> main_models.ListHotTopicsResponse:
        runtime = RuntimeOptions()
        return self.list_hot_topics_with_options(request, runtime)

    async def list_hot_topics_async(
        self,
        request: main_models.ListHotTopicsRequest,
    ) -> main_models.ListHotTopicsResponse:
        runtime = RuntimeOptions()
        return await self.list_hot_topics_with_options_async(request, runtime)

    def list_hot_view_points_with_options(
        self,
        request: main_models.ListHotViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotViewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotViewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_view_points_with_options_async(
        self,
        request: main_models.ListHotViewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotViewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHotViewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotViewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_view_points(
        self,
        request: main_models.ListHotViewPointsRequest,
    ) -> main_models.ListHotViewPointsResponse:
        runtime = RuntimeOptions()
        return self.list_hot_view_points_with_options(request, runtime)

    async def list_hot_view_points_async(
        self,
        request: main_models.ListHotViewPointsRequest,
    ) -> main_models.ListHotViewPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_hot_view_points_with_options_async(request, runtime)

    def list_intervene_cnt_with_options(
        self,
        request: main_models.ListInterveneCntRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneCntResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneCnt',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneCntResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_cnt_with_options_async(
        self,
        request: main_models.ListInterveneCntRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneCntResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneCnt',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneCntResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_cnt(
        self,
        request: main_models.ListInterveneCntRequest,
    ) -> main_models.ListInterveneCntResponse:
        runtime = RuntimeOptions()
        return self.list_intervene_cnt_with_options(request, runtime)

    async def list_intervene_cnt_async(
        self,
        request: main_models.ListInterveneCntRequest,
    ) -> main_models.ListInterveneCntResponse:
        runtime = RuntimeOptions()
        return await self.list_intervene_cnt_with_options_async(request, runtime)

    def list_intervene_import_tasks_with_options(
        self,
        request: main_models.ListInterveneImportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneImportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneImportTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneImportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_import_tasks_with_options_async(
        self,
        request: main_models.ListInterveneImportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneImportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneImportTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneImportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_import_tasks(
        self,
        request: main_models.ListInterveneImportTasksRequest,
    ) -> main_models.ListInterveneImportTasksResponse:
        runtime = RuntimeOptions()
        return self.list_intervene_import_tasks_with_options(request, runtime)

    async def list_intervene_import_tasks_async(
        self,
        request: main_models.ListInterveneImportTasksRequest,
    ) -> main_models.ListInterveneImportTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_intervene_import_tasks_with_options_async(request, runtime)

    def list_intervene_rules_with_options(
        self,
        request: main_models.ListInterveneRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneRules',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervene_rules_with_options_async(
        self,
        request: main_models.ListInterveneRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInterveneRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInterveneRules',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInterveneRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervene_rules(
        self,
        request: main_models.ListInterveneRulesRequest,
    ) -> main_models.ListInterveneRulesResponse:
        runtime = RuntimeOptions()
        return self.list_intervene_rules_with_options(request, runtime)

    async def list_intervene_rules_async(
        self,
        request: main_models.ListInterveneRulesRequest,
    ) -> main_models.ListInterveneRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_intervene_rules_with_options_async(request, runtime)

    def list_intervenes_with_options(
        self,
        request: main_models.ListIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_intervenes_with_options_async(
        self,
        request: main_models.ListIntervenesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntervenesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.intervene_type):
            body['InterveneType'] = request.intervene_type
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIntervenes',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntervenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_intervenes(
        self,
        request: main_models.ListIntervenesRequest,
    ) -> main_models.ListIntervenesResponse:
        runtime = RuntimeOptions()
        return self.list_intervenes_with_options(request, runtime)

    async def list_intervenes_async(
        self,
        request: main_models.ListIntervenesRequest,
    ) -> main_models.ListIntervenesResponse:
        runtime = RuntimeOptions()
        return await self.list_intervenes_with_options_async(request, runtime)

    def list_material_documents_with_options(
        self,
        tmp_req: main_models.ListMaterialDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterialDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListMaterialDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_type_list):
            request.doc_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not DaraCore.is_null(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not DaraCore.is_null(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterialDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterialDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_material_documents_with_options_async(
        self,
        tmp_req: main_models.ListMaterialDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMaterialDocumentsResponse:
        tmp_req.validate()
        request = main_models.ListMaterialDocumentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_type_list):
            request.doc_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_type_list, 'DocTypeList', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.doc_type_list_shrink):
            body['DocTypeList'] = request.doc_type_list_shrink
        if not DaraCore.is_null(request.generate_public_url):
            body['GeneratePublicUrl'] = request.generate_public_url
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.update_time_end):
            body['UpdateTimeEnd'] = request.update_time_end
        if not DaraCore.is_null(request.update_time_start):
            body['UpdateTimeStart'] = request.update_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMaterialDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMaterialDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_material_documents(
        self,
        request: main_models.ListMaterialDocumentsRequest,
    ) -> main_models.ListMaterialDocumentsResponse:
        runtime = RuntimeOptions()
        return self.list_material_documents_with_options(request, runtime)

    async def list_material_documents_async(
        self,
        request: main_models.ListMaterialDocumentsRequest,
    ) -> main_models.ListMaterialDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.list_material_documents_with_options_async(request, runtime)

    def list_planning_proposal_with_options(
        self,
        tmp_req: main_models.ListPlanningProposalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlanningProposalResponse:
        tmp_req.validate()
        request = main_models.ListPlanningProposalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not DaraCore.is_null(tmp_req.titles):
            request.titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlanningProposal',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlanningProposalResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_planning_proposal_with_options_async(
        self,
        tmp_req: main_models.ListPlanningProposalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPlanningProposalResponse:
        tmp_req.validate()
        request = main_models.ListPlanningProposalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_view_point_ids):
            request.custom_view_point_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_view_point_ids, 'CustomViewPointIds', 'json')
        if not DaraCore.is_null(tmp_req.titles):
            request.titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.titles, 'Titles', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.custom_view_point_id):
            body['CustomViewPointId'] = request.custom_view_point_id
        if not DaraCore.is_null(request.custom_view_point_ids_shrink):
            body['CustomViewPointIds'] = request.custom_view_point_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.titles_shrink):
            body['Titles'] = request.titles_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.view_point_type):
            body['ViewPointType'] = request.view_point_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPlanningProposal',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPlanningProposalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_planning_proposal(
        self,
        request: main_models.ListPlanningProposalRequest,
    ) -> main_models.ListPlanningProposalResponse:
        runtime = RuntimeOptions()
        return self.list_planning_proposal_with_options(request, runtime)

    async def list_planning_proposal_async(
        self,
        request: main_models.ListPlanningProposalRequest,
    ) -> main_models.ListPlanningProposalResponse:
        runtime = RuntimeOptions()
        return await self.list_planning_proposal_with_options_async(request, runtime)

    def list_search_task_dialogue_datas_with_options(
        self,
        request: main_models.ListSearchTaskDialogueDatasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTaskDialogueDatasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.multimodal_search_type):
            body['MultimodalSearchType'] = request.multimodal_search_type
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.search_model):
            body['SearchModel'] = request.search_model
        if not DaraCore.is_null(request.search_model_data_value):
            body['SearchModelDataValue'] = request.search_model_data_value
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTaskDialogueDatas',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTaskDialogueDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_task_dialogue_datas_with_options_async(
        self,
        request: main_models.ListSearchTaskDialogueDatasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTaskDialogueDatasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.multimodal_search_type):
            body['MultimodalSearchType'] = request.multimodal_search_type
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.search_model):
            body['SearchModel'] = request.search_model
        if not DaraCore.is_null(request.search_model_data_value):
            body['SearchModelDataValue'] = request.search_model_data_value
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTaskDialogueDatas',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTaskDialogueDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_task_dialogue_datas(
        self,
        request: main_models.ListSearchTaskDialogueDatasRequest,
    ) -> main_models.ListSearchTaskDialogueDatasResponse:
        runtime = RuntimeOptions()
        return self.list_search_task_dialogue_datas_with_options(request, runtime)

    async def list_search_task_dialogue_datas_async(
        self,
        request: main_models.ListSearchTaskDialogueDatasRequest,
    ) -> main_models.ListSearchTaskDialogueDatasResponse:
        runtime = RuntimeOptions()
        return await self.list_search_task_dialogue_datas_with_options_async(request, runtime)

    def list_search_task_dialogues_with_options(
        self,
        request: main_models.ListSearchTaskDialoguesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTaskDialoguesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTaskDialogues',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTaskDialoguesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_task_dialogues_with_options_async(
        self,
        request: main_models.ListSearchTaskDialoguesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTaskDialoguesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTaskDialogues',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTaskDialoguesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_task_dialogues(
        self,
        request: main_models.ListSearchTaskDialoguesRequest,
    ) -> main_models.ListSearchTaskDialoguesResponse:
        runtime = RuntimeOptions()
        return self.list_search_task_dialogues_with_options(request, runtime)

    async def list_search_task_dialogues_async(
        self,
        request: main_models.ListSearchTaskDialoguesRequest,
    ) -> main_models.ListSearchTaskDialoguesResponse:
        runtime = RuntimeOptions()
        return await self.list_search_task_dialogues_with_options_async(request, runtime)

    def list_search_tasks_with_options(
        self,
        tmp_req: main_models.ListSearchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTasksResponse:
        tmp_req.validate()
        request = main_models.ListSearchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dialogue_types):
            request.dialogue_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.dialogue_types, 'DialogueTypes', 'json')
        body = {}
        if not DaraCore.is_null(request.dialogue_types_shrink):
            body['DialogueTypes'] = request.dialogue_types_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_tasks_with_options_async(
        self,
        tmp_req: main_models.ListSearchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchTasksResponse:
        tmp_req.validate()
        request = main_models.ListSearchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dialogue_types):
            request.dialogue_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.dialogue_types, 'DialogueTypes', 'json')
        body = {}
        if not DaraCore.is_null(request.dialogue_types_shrink):
            body['DialogueTypes'] = request.dialogue_types_shrink
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchTasks',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_tasks(
        self,
        request: main_models.ListSearchTasksRequest,
    ) -> main_models.ListSearchTasksResponse:
        runtime = RuntimeOptions()
        return self.list_search_tasks_with_options(request, runtime)

    async def list_search_tasks_async(
        self,
        request: main_models.ListSearchTasksRequest,
    ) -> main_models.ListSearchTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_search_tasks_with_options_async(request, runtime)

    def list_style_learning_result_with_options(
        self,
        request: main_models.ListStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_style_learning_result_with_options_async(
        self,
        request: main_models.ListStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStyleLearningResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.current):
            body['Current'] = request.current
        if not DaraCore.is_null(request.size):
            body['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_style_learning_result(
        self,
        request: main_models.ListStyleLearningResultRequest,
    ) -> main_models.ListStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return self.list_style_learning_result_with_options(request, runtime)

    async def list_style_learning_result_async(
        self,
        request: main_models.ListStyleLearningResultRequest,
    ) -> main_models.ListStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return await self.list_style_learning_result_with_options_async(request, runtime)

    def list_timed_view_attitude_with_options(
        self,
        request: main_models.ListTimedViewAttitudeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTimedViewAttitudeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTimedViewAttitude',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTimedViewAttitudeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_timed_view_attitude_with_options_async(
        self,
        request: main_models.ListTimedViewAttitudeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTimedViewAttitudeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTimedViewAttitude',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTimedViewAttitudeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_timed_view_attitude(
        self,
        request: main_models.ListTimedViewAttitudeRequest,
    ) -> main_models.ListTimedViewAttitudeResponse:
        runtime = RuntimeOptions()
        return self.list_timed_view_attitude_with_options(request, runtime)

    async def list_timed_view_attitude_async(
        self,
        request: main_models.ListTimedViewAttitudeRequest,
    ) -> main_models.ListTimedViewAttitudeResponse:
        runtime = RuntimeOptions()
        return await self.list_timed_view_attitude_with_options_async(request, runtime)

    def list_topic_recommend_event_list_with_options(
        self,
        request: main_models.ListTopicRecommendEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicRecommendEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTopicRecommendEventList',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_recommend_event_list_with_options_async(
        self,
        request: main_models.ListTopicRecommendEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicRecommendEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTopicRecommendEventList',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_recommend_event_list(
        self,
        request: main_models.ListTopicRecommendEventListRequest,
    ) -> main_models.ListTopicRecommendEventListResponse:
        runtime = RuntimeOptions()
        return self.list_topic_recommend_event_list_with_options(request, runtime)

    async def list_topic_recommend_event_list_async(
        self,
        request: main_models.ListTopicRecommendEventListRequest,
    ) -> main_models.ListTopicRecommendEventListResponse:
        runtime = RuntimeOptions()
        return await self.list_topic_recommend_event_list_with_options_async(request, runtime)

    def list_topic_view_point_recommend_event_list_with_options(
        self,
        request: main_models.ListTopicViewPointRecommendEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicViewPointRecommendEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTopicViewPointRecommendEventList',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicViewPointRecommendEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_view_point_recommend_event_list_with_options_async(
        self,
        request: main_models.ListTopicViewPointRecommendEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicViewPointRecommendEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTopicViewPointRecommendEventList',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicViewPointRecommendEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_view_point_recommend_event_list(
        self,
        request: main_models.ListTopicViewPointRecommendEventListRequest,
    ) -> main_models.ListTopicViewPointRecommendEventListResponse:
        runtime = RuntimeOptions()
        return self.list_topic_view_point_recommend_event_list_with_options(request, runtime)

    async def list_topic_view_point_recommend_event_list_async(
        self,
        request: main_models.ListTopicViewPointRecommendEventListRequest,
    ) -> main_models.ListTopicViewPointRecommendEventListResponse:
        runtime = RuntimeOptions()
        return await self.list_topic_view_point_recommend_event_list_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: main_models.ListVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVersions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: main_models.ListVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVersions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_versions(
        self,
        request: main_models.ListVersionsRequest,
    ) -> main_models.ListVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: main_models.ListVersionsRequest,
    ) -> main_models.ListVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def list_web_review_points_with_options(
        self,
        request: main_models.ListWebReviewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWebReviewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWebReviewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebReviewPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_review_points_with_options_async(
        self,
        request: main_models.ListWebReviewPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWebReviewPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWebReviewPoints',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebReviewPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_review_points(
        self,
        request: main_models.ListWebReviewPointsRequest,
    ) -> main_models.ListWebReviewPointsResponse:
        runtime = RuntimeOptions()
        return self.list_web_review_points_with_options(request, runtime)

    async def list_web_review_points_async(
        self,
        request: main_models.ListWebReviewPointsRequest,
    ) -> main_models.ListWebReviewPointsResponse:
        runtime = RuntimeOptions()
        return await self.list_web_review_points_with_options_async(request, runtime)

    def list_writing_styles_with_options(
        self,
        request: main_models.ListWritingStylesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWritingStylesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWritingStyles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWritingStylesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_writing_styles_with_options_async(
        self,
        request: main_models.ListWritingStylesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWritingStylesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListWritingStyles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWritingStylesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_writing_styles(
        self,
        request: main_models.ListWritingStylesRequest,
    ) -> main_models.ListWritingStylesResponse:
        runtime = RuntimeOptions()
        return self.list_writing_styles_with_options(request, runtime)

    async def list_writing_styles_async(
        self,
        request: main_models.ListWritingStylesRequest,
    ) -> main_models.ListWritingStylesResponse:
        runtime = RuntimeOptions()
        return await self.list_writing_styles_with_options_async(request, runtime)

    def query_async_task_with_options(
        self,
        request: main_models.QueryAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_async_task_with_options_async(
        self,
        request: main_models.QueryAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_async_task(
        self,
        request: main_models.QueryAsyncTaskRequest,
    ) -> main_models.QueryAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.query_async_task_with_options(request, runtime)

    async def query_async_task_async(
        self,
        request: main_models.QueryAsyncTaskRequest,
    ) -> main_models.QueryAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.query_async_task_with_options_async(request, runtime)

    def query_audit_task_with_options(
        self,
        request: main_models.QueryAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content_audit_task_id):
            body['ContentAuditTaskId'] = request.content_audit_task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuditTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_audit_task_with_options_async(
        self,
        request: main_models.QueryAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content_audit_task_id):
            body['ContentAuditTaskId'] = request.content_audit_task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuditTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_audit_task(
        self,
        request: main_models.QueryAuditTaskRequest,
    ) -> main_models.QueryAuditTaskResponse:
        runtime = RuntimeOptions()
        return self.query_audit_task_with_options(request, runtime)

    async def query_audit_task_async(
        self,
        request: main_models.QueryAuditTaskRequest,
    ) -> main_models.QueryAuditTaskResponse:
        runtime = RuntimeOptions()
        return await self.query_audit_task_with_options_async(request, runtime)

    def run_abbreviation_content_with_sse(
        self,
        request: main_models.RunAbbreviationContentRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunAbbreviationContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAbbreviationContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAbbreviationContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_abbreviation_content_with_sse_async(
        self,
        request: main_models.RunAbbreviationContentRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunAbbreviationContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAbbreviationContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAbbreviationContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_abbreviation_content_with_options(
        self,
        request: main_models.RunAbbreviationContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunAbbreviationContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAbbreviationContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAbbreviationContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_abbreviation_content_with_options_async(
        self,
        request: main_models.RunAbbreviationContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunAbbreviationContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAbbreviationContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAbbreviationContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_abbreviation_content(
        self,
        request: main_models.RunAbbreviationContentRequest,
    ) -> main_models.RunAbbreviationContentResponse:
        runtime = RuntimeOptions()
        return self.run_abbreviation_content_with_options(request, runtime)

    async def run_abbreviation_content_async(
        self,
        request: main_models.RunAbbreviationContentRequest,
    ) -> main_models.RunAbbreviationContentResponse:
        runtime = RuntimeOptions()
        return await self.run_abbreviation_content_with_options_async(request, runtime)

    def run_ai_helper_writing_with_sse(
        self,
        tmp_req: main_models.RunAiHelperWritingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunAiHelperWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunAiHelperWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAiHelperWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAiHelperWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_ai_helper_writing_with_sse_async(
        self,
        tmp_req: main_models.RunAiHelperWritingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunAiHelperWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunAiHelperWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAiHelperWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunAiHelperWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_ai_helper_writing_with_options(
        self,
        tmp_req: main_models.RunAiHelperWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunAiHelperWritingResponse:
        tmp_req.validate()
        request = main_models.RunAiHelperWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAiHelperWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAiHelperWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ai_helper_writing_with_options_async(
        self,
        tmp_req: main_models.RunAiHelperWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunAiHelperWritingResponse:
        tmp_req.validate()
        request = main_models.RunAiHelperWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunAiHelperWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunAiHelperWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ai_helper_writing(
        self,
        request: main_models.RunAiHelperWritingRequest,
    ) -> main_models.RunAiHelperWritingResponse:
        runtime = RuntimeOptions()
        return self.run_ai_helper_writing_with_options(request, runtime)

    async def run_ai_helper_writing_async(
        self,
        request: main_models.RunAiHelperWritingRequest,
    ) -> main_models.RunAiHelperWritingResponse:
        runtime = RuntimeOptions()
        return await self.run_ai_helper_writing_with_options_async(request, runtime)

    def run_book_brainmap_with_sse(
        self,
        request: main_models.RunBookBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunBookBrainmapResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookBrainmapResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_book_brainmap_with_sse_async(
        self,
        request: main_models.RunBookBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunBookBrainmapResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookBrainmapResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_book_brainmap_with_options(
        self,
        request: main_models.RunBookBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookBrainmapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookBrainmapResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_book_brainmap_with_options_async(
        self,
        request: main_models.RunBookBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookBrainmapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookBrainmapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_book_brainmap(
        self,
        request: main_models.RunBookBrainmapRequest,
    ) -> main_models.RunBookBrainmapResponse:
        runtime = RuntimeOptions()
        return self.run_book_brainmap_with_options(request, runtime)

    async def run_book_brainmap_async(
        self,
        request: main_models.RunBookBrainmapRequest,
    ) -> main_models.RunBookBrainmapResponse:
        runtime = RuntimeOptions()
        return await self.run_book_brainmap_with_options_async(request, runtime)

    def run_book_introduction_with_sse(
        self,
        request: main_models.RunBookIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunBookIntroductionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_book_introduction_with_sse_async(
        self,
        request: main_models.RunBookIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunBookIntroductionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_book_introduction_with_options(
        self,
        request: main_models.RunBookIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookIntroductionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_book_introduction_with_options_async(
        self,
        request: main_models.RunBookIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookIntroductionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_book_introduction(
        self,
        request: main_models.RunBookIntroductionRequest,
    ) -> main_models.RunBookIntroductionResponse:
        runtime = RuntimeOptions()
        return self.run_book_introduction_with_options(request, runtime)

    async def run_book_introduction_async(
        self,
        request: main_models.RunBookIntroductionRequest,
    ) -> main_models.RunBookIntroductionResponse:
        runtime = RuntimeOptions()
        return await self.run_book_introduction_with_options_async(request, runtime)

    def run_book_smart_card_with_sse(
        self,
        request: main_models.RunBookSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunBookSmartCardResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookSmartCardResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_book_smart_card_with_sse_async(
        self,
        request: main_models.RunBookSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunBookSmartCardResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunBookSmartCardResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_book_smart_card_with_options(
        self,
        request: main_models.RunBookSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookSmartCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookSmartCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_book_smart_card_with_options_async(
        self,
        request: main_models.RunBookSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunBookSmartCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunBookSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunBookSmartCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_book_smart_card(
        self,
        request: main_models.RunBookSmartCardRequest,
    ) -> main_models.RunBookSmartCardResponse:
        runtime = RuntimeOptions()
        return self.run_book_smart_card_with_options(request, runtime)

    async def run_book_smart_card_async(
        self,
        request: main_models.RunBookSmartCardRequest,
    ) -> main_models.RunBookSmartCardResponse:
        runtime = RuntimeOptions()
        return await self.run_book_smart_card_with_options_async(request, runtime)

    def run_comment_generation_with_sse(
        self,
        tmp_req: main_models.RunCommentGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunCommentGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunCommentGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.length_range):
            request.length_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not DaraCore.is_null(tmp_req.sentiment):
            request.sentiment_shrink = Utils.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not DaraCore.is_null(tmp_req.type):
            request.type_shrink = Utils.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.num_comments):
            body['NumComments'] = request.num_comments
        if not DaraCore.is_null(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        if not DaraCore.is_null(request.type_shrink):
            body['Type'] = request.type_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommentGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCommentGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_comment_generation_with_sse_async(
        self,
        tmp_req: main_models.RunCommentGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunCommentGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunCommentGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.length_range):
            request.length_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not DaraCore.is_null(tmp_req.sentiment):
            request.sentiment_shrink = Utils.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not DaraCore.is_null(tmp_req.type):
            request.type_shrink = Utils.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.num_comments):
            body['NumComments'] = request.num_comments
        if not DaraCore.is_null(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        if not DaraCore.is_null(request.type_shrink):
            body['Type'] = request.type_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommentGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCommentGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_comment_generation_with_options(
        self,
        tmp_req: main_models.RunCommentGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommentGenerationResponse:
        tmp_req.validate()
        request = main_models.RunCommentGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.length_range):
            request.length_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not DaraCore.is_null(tmp_req.sentiment):
            request.sentiment_shrink = Utils.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not DaraCore.is_null(tmp_req.type):
            request.type_shrink = Utils.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.num_comments):
            body['NumComments'] = request.num_comments
        if not DaraCore.is_null(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        if not DaraCore.is_null(request.type_shrink):
            body['Type'] = request.type_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommentGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommentGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_comment_generation_with_options_async(
        self,
        tmp_req: main_models.RunCommentGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommentGenerationResponse:
        tmp_req.validate()
        request = main_models.RunCommentGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.length_range):
            request.length_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.length_range, 'LengthRange', 'json')
        if not DaraCore.is_null(tmp_req.sentiment):
            request.sentiment_shrink = Utils.array_to_string_with_specified_style(tmp_req.sentiment, 'Sentiment', 'json')
        if not DaraCore.is_null(tmp_req.type):
            request.type_shrink = Utils.array_to_string_with_specified_style(tmp_req.type, 'Type', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_emoji):
            body['AllowEmoji'] = request.allow_emoji
        if not DaraCore.is_null(request.extra_info):
            body['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.length_range_shrink):
            body['LengthRange'] = request.length_range_shrink
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.num_comments):
            body['NumComments'] = request.num_comments
        if not DaraCore.is_null(request.sentiment_shrink):
            body['Sentiment'] = request.sentiment_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_material):
            body['SourceMaterial'] = request.source_material
        if not DaraCore.is_null(request.style):
            body['Style'] = request.style
        if not DaraCore.is_null(request.type_shrink):
            body['Type'] = request.type_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommentGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommentGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_comment_generation(
        self,
        request: main_models.RunCommentGenerationRequest,
    ) -> main_models.RunCommentGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_comment_generation_with_options(request, runtime)

    async def run_comment_generation_async(
        self,
        request: main_models.RunCommentGenerationRequest,
    ) -> main_models.RunCommentGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_comment_generation_with_options_async(request, runtime)

    def run_continue_content_with_sse(
        self,
        request: main_models.RunContinueContentRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunContinueContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContinueContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContinueContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_continue_content_with_sse_async(
        self,
        request: main_models.RunContinueContentRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunContinueContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContinueContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunContinueContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_continue_content_with_options(
        self,
        request: main_models.RunContinueContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunContinueContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContinueContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContinueContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_continue_content_with_options_async(
        self,
        request: main_models.RunContinueContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunContinueContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunContinueContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunContinueContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_continue_content(
        self,
        request: main_models.RunContinueContentRequest,
    ) -> main_models.RunContinueContentResponse:
        runtime = RuntimeOptions()
        return self.run_continue_content_with_options(request, runtime)

    async def run_continue_content_async(
        self,
        request: main_models.RunContinueContentRequest,
    ) -> main_models.RunContinueContentResponse:
        runtime = RuntimeOptions()
        return await self.run_continue_content_with_options_async(request, runtime)

    def run_custom_hot_topic_analysis_with_sse(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunCustomHotTopicAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCustomHotTopicAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_custom_hot_topic_analysis_with_sse_async(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunCustomHotTopicAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCustomHotTopicAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_custom_hot_topic_analysis_with_options(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCustomHotTopicAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCustomHotTopicAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_analysis_with_options_async(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCustomHotTopicAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.force_analysis_exists_topic):
            body['ForceAnalysisExistsTopic'] = request.force_analysis_exists_topic
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCustomHotTopicAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_analysis(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
    ) -> main_models.RunCustomHotTopicAnalysisResponse:
        runtime = RuntimeOptions()
        return self.run_custom_hot_topic_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_analysis_async(
        self,
        request: main_models.RunCustomHotTopicAnalysisRequest,
    ) -> main_models.RunCustomHotTopicAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.run_custom_hot_topic_analysis_with_options_async(request, runtime)

    def run_custom_hot_topic_view_point_analysis_with_sse(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunCustomHotTopicViewPointAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_query):
            body['SearchQuery'] = request.search_query
        if not DaraCore.is_null(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicViewPointAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCustomHotTopicViewPointAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_custom_hot_topic_view_point_analysis_with_sse_async(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunCustomHotTopicViewPointAnalysisResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_query):
            body['SearchQuery'] = request.search_query
        if not DaraCore.is_null(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicViewPointAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunCustomHotTopicViewPointAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_custom_hot_topic_view_point_analysis_with_options(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCustomHotTopicViewPointAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_query):
            body['SearchQuery'] = request.search_query
        if not DaraCore.is_null(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicViewPointAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCustomHotTopicViewPointAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_custom_hot_topic_view_point_analysis_with_options_async(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCustomHotTopicViewPointAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ask_user):
            body['AskUser'] = request.ask_user
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_query):
            body['SearchQuery'] = request.search_query
        if not DaraCore.is_null(request.skip_ask_user):
            body['SkipAskUser'] = request.skip_ask_user
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.topic_id):
            body['TopicId'] = request.topic_id
        if not DaraCore.is_null(request.topic_source):
            body['TopicSource'] = request.topic_source
        if not DaraCore.is_null(request.topic_version):
            body['TopicVersion'] = request.topic_version
        if not DaraCore.is_null(request.user_back):
            body['UserBack'] = request.user_back
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCustomHotTopicViewPointAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCustomHotTopicViewPointAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_custom_hot_topic_view_point_analysis(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> main_models.RunCustomHotTopicViewPointAnalysisResponse:
        runtime = RuntimeOptions()
        return self.run_custom_hot_topic_view_point_analysis_with_options(request, runtime)

    async def run_custom_hot_topic_view_point_analysis_async(
        self,
        request: main_models.RunCustomHotTopicViewPointAnalysisRequest,
    ) -> main_models.RunCustomHotTopicViewPointAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.run_custom_hot_topic_view_point_analysis_with_options_async(request, runtime)

    def run_deep_writing_with_sse(
        self,
        request: main_models.RunDeepWritingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDeepWritingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDeepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDeepWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_deep_writing_with_sse_async(
        self,
        request: main_models.RunDeepWritingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDeepWritingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDeepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDeepWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_deep_writing_with_options(
        self,
        request: main_models.RunDeepWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDeepWritingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDeepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDeepWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_deep_writing_with_options_async(
        self,
        request: main_models.RunDeepWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDeepWritingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDeepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDeepWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_deep_writing(
        self,
        request: main_models.RunDeepWritingRequest,
    ) -> main_models.RunDeepWritingResponse:
        runtime = RuntimeOptions()
        return self.run_deep_writing_with_options(request, runtime)

    async def run_deep_writing_async(
        self,
        request: main_models.RunDeepWritingRequest,
    ) -> main_models.RunDeepWritingResponse:
        runtime = RuntimeOptions()
        return await self.run_deep_writing_with_options_async(request, runtime)

    def run_doc_brainmap_with_sse(
        self,
        request: main_models.RunDocBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocBrainmapResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocBrainmapResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_brainmap_with_sse_async(
        self,
        request: main_models.RunDocBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocBrainmapResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocBrainmapResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_brainmap_with_options(
        self,
        request: main_models.RunDocBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocBrainmapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocBrainmapResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_brainmap_with_options_async(
        self,
        request: main_models.RunDocBrainmapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocBrainmapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.node_number):
            body['NodeNumber'] = request.node_number
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocBrainmap',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocBrainmapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_brainmap(
        self,
        request: main_models.RunDocBrainmapRequest,
    ) -> main_models.RunDocBrainmapResponse:
        runtime = RuntimeOptions()
        return self.run_doc_brainmap_with_options(request, runtime)

    async def run_doc_brainmap_async(
        self,
        request: main_models.RunDocBrainmapRequest,
    ) -> main_models.RunDocBrainmapResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_brainmap_with_options_async(request, runtime)

    def run_doc_introduction_with_sse(
        self,
        request: main_models.RunDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocIntroductionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_introduction_with_sse_async(
        self,
        request: main_models.RunDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocIntroductionResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_introduction_with_options(
        self,
        request: main_models.RunDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocIntroductionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_introduction_with_options_async(
        self,
        request: main_models.RunDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocIntroductionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.introduction_prompt):
            body['IntroductionPrompt'] = request.introduction_prompt
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.reference_content):
            body['referenceContent'] = request.reference_content
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_introduction(
        self,
        request: main_models.RunDocIntroductionRequest,
    ) -> main_models.RunDocIntroductionResponse:
        runtime = RuntimeOptions()
        return self.run_doc_introduction_with_options(request, runtime)

    async def run_doc_introduction_async(
        self,
        request: main_models.RunDocIntroductionRequest,
    ) -> main_models.RunDocIntroductionResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_introduction_with_options_async(request, runtime)

    def run_doc_qa_with_sse(
        self,
        tmp_req: main_models.RunDocQaRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocQaResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunDocQaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.search_source):
            body['SearchSource'] = request.search_source
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocQa',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocQaResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_qa_with_sse_async(
        self,
        tmp_req: main_models.RunDocQaRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocQaResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunDocQaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.search_source):
            body['SearchSource'] = request.search_source
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocQa',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocQaResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_qa_with_options(
        self,
        tmp_req: main_models.RunDocQaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocQaResponse:
        tmp_req.validate()
        request = main_models.RunDocQaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.search_source):
            body['SearchSource'] = request.search_source
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocQa',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocQaResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_qa_with_options_async(
        self,
        tmp_req: main_models.RunDocQaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocQaResponse:
        tmp_req.validate()
        request = main_models.RunDocQaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.conversation_contexts):
            request.conversation_contexts_shrink = Utils.array_to_string_with_specified_style(tmp_req.conversation_contexts, 'ConversationContexts', 'json')
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            body['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.conversation_contexts_shrink):
            body['ConversationContexts'] = request.conversation_contexts_shrink
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.search_source):
            body['SearchSource'] = request.search_source
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocQa',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocQaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_qa(
        self,
        request: main_models.RunDocQaRequest,
    ) -> main_models.RunDocQaResponse:
        runtime = RuntimeOptions()
        return self.run_doc_qa_with_options(request, runtime)

    async def run_doc_qa_async(
        self,
        request: main_models.RunDocQaRequest,
    ) -> main_models.RunDocQaResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_qa_with_options_async(request, runtime)

    def run_doc_smart_card_with_sse(
        self,
        request: main_models.RunDocSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocSmartCardResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocSmartCardResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_smart_card_with_sse_async(
        self,
        request: main_models.RunDocSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocSmartCardResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocSmartCardResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_smart_card_with_options(
        self,
        request: main_models.RunDocSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocSmartCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocSmartCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_smart_card_with_options_async(
        self,
        request: main_models.RunDocSmartCardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocSmartCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSmartCard',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocSmartCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_smart_card(
        self,
        request: main_models.RunDocSmartCardRequest,
    ) -> main_models.RunDocSmartCardResponse:
        runtime = RuntimeOptions()
        return self.run_doc_smart_card_with_options(request, runtime)

    async def run_doc_smart_card_async(
        self,
        request: main_models.RunDocSmartCardRequest,
    ) -> main_models.RunDocSmartCardResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_smart_card_with_options_async(request, runtime)

    def run_doc_summary_with_sse(
        self,
        request: main_models.RunDocSummaryRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocSummaryResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSummary',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocSummaryResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_summary_with_sse_async(
        self,
        request: main_models.RunDocSummaryRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocSummaryResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSummary',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocSummaryResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_summary_with_options(
        self,
        request: main_models.RunDocSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSummary',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_summary_with_options_async(
        self,
        request: main_models.RunDocSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocSummaryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocSummary',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_summary(
        self,
        request: main_models.RunDocSummaryRequest,
    ) -> main_models.RunDocSummaryResponse:
        runtime = RuntimeOptions()
        return self.run_doc_summary_with_options(request, runtime)

    async def run_doc_summary_async(
        self,
        request: main_models.RunDocSummaryRequest,
    ) -> main_models.RunDocSummaryResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_summary_with_options_async(request, runtime)

    def run_doc_translation_with_sse(
        self,
        request: main_models.RunDocTranslationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocTranslationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.trans_type):
            body['TransType'] = request.trans_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocTranslation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocTranslationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_translation_with_sse_async(
        self,
        request: main_models.RunDocTranslationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocTranslationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.trans_type):
            body['TransType'] = request.trans_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocTranslation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocTranslationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_translation_with_options(
        self,
        request: main_models.RunDocTranslationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocTranslationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.trans_type):
            body['TransType'] = request.trans_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocTranslation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocTranslationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_translation_with_options_async(
        self,
        request: main_models.RunDocTranslationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocTranslationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clean_cache):
            body['CleanCache'] = request.clean_cache
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.recommend_content):
            body['RecommendContent'] = request.recommend_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.trans_type):
            body['TransType'] = request.trans_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocTranslation',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocTranslationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_translation(
        self,
        request: main_models.RunDocTranslationRequest,
    ) -> main_models.RunDocTranslationResponse:
        runtime = RuntimeOptions()
        return self.run_doc_translation_with_options(request, runtime)

    async def run_doc_translation_async(
        self,
        request: main_models.RunDocTranslationRequest,
    ) -> main_models.RunDocTranslationResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_translation_with_options_async(request, runtime)

    def run_doc_washing_with_sse(
        self,
        request: main_models.RunDocWashingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunDocWashingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not DaraCore.is_null(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocWashing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocWashingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_doc_washing_with_sse_async(
        self,
        request: main_models.RunDocWashingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunDocWashingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not DaraCore.is_null(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocWashing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunDocWashingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_doc_washing_with_options(
        self,
        request: main_models.RunDocWashingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocWashingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not DaraCore.is_null(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocWashing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocWashingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_doc_washing_with_options_async(
        self,
        request: main_models.RunDocWashingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunDocWashingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        if not DaraCore.is_null(request.word_number):
            body['WordNumber'] = request.word_number
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_type_name):
            body['WritingTypeName'] = request.writing_type_name
        if not DaraCore.is_null(request.writing_type_ref_doc):
            body['WritingTypeRefDoc'] = request.writing_type_ref_doc
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunDocWashing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunDocWashingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_doc_washing(
        self,
        request: main_models.RunDocWashingRequest,
    ) -> main_models.RunDocWashingResponse:
        runtime = RuntimeOptions()
        return self.run_doc_washing_with_options(request, runtime)

    async def run_doc_washing_async(
        self,
        request: main_models.RunDocWashingRequest,
    ) -> main_models.RunDocWashingResponse:
        runtime = RuntimeOptions()
        return await self.run_doc_washing_with_options_async(request, runtime)

    def run_expand_content_with_sse(
        self,
        request: main_models.RunExpandContentRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunExpandContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunExpandContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunExpandContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_expand_content_with_sse_async(
        self,
        request: main_models.RunExpandContentRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunExpandContentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunExpandContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunExpandContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_expand_content_with_options(
        self,
        request: main_models.RunExpandContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunExpandContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunExpandContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunExpandContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_expand_content_with_options_async(
        self,
        request: main_models.RunExpandContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunExpandContentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunExpandContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunExpandContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_expand_content(
        self,
        request: main_models.RunExpandContentRequest,
    ) -> main_models.RunExpandContentResponse:
        runtime = RuntimeOptions()
        return self.run_expand_content_with_options(request, runtime)

    async def run_expand_content_async(
        self,
        request: main_models.RunExpandContentRequest,
    ) -> main_models.RunExpandContentResponse:
        runtime = RuntimeOptions()
        return await self.run_expand_content_with_options_async(request, runtime)

    def run_generate_questions_with_sse(
        self,
        request: main_models.RunGenerateQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunGenerateQuestionsResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunGenerateQuestions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunGenerateQuestionsResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_generate_questions_with_sse_async(
        self,
        request: main_models.RunGenerateQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunGenerateQuestionsResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunGenerateQuestions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunGenerateQuestionsResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_generate_questions_with_options(
        self,
        request: main_models.RunGenerateQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunGenerateQuestionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunGenerateQuestions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunGenerateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_generate_questions_with_options_async(
        self,
        request: main_models.RunGenerateQuestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunGenerateQuestionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunGenerateQuestions',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunGenerateQuestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_generate_questions(
        self,
        request: main_models.RunGenerateQuestionsRequest,
    ) -> main_models.RunGenerateQuestionsResponse:
        runtime = RuntimeOptions()
        return self.run_generate_questions_with_options(request, runtime)

    async def run_generate_questions_async(
        self,
        request: main_models.RunGenerateQuestionsRequest,
    ) -> main_models.RunGenerateQuestionsResponse:
        runtime = RuntimeOptions()
        return await self.run_generate_questions_with_options_async(request, runtime)

    def run_hotword_with_sse(
        self,
        request: main_models.RunHotwordRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunHotwordResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotword',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotwordResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_hotword_with_sse_async(
        self,
        request: main_models.RunHotwordRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunHotwordResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotword',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunHotwordResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_hotword_with_options(
        self,
        request: main_models.RunHotwordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunHotwordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotword',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotwordResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_hotword_with_options_async(
        self,
        request: main_models.RunHotwordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunHotwordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_id):
            body['DocId'] = request.doc_id
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_content):
            body['ReferenceContent'] = request.reference_content
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunHotword',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunHotwordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_hotword(
        self,
        request: main_models.RunHotwordRequest,
    ) -> main_models.RunHotwordResponse:
        runtime = RuntimeOptions()
        return self.run_hotword_with_options(request, runtime)

    async def run_hotword_async(
        self,
        request: main_models.RunHotwordRequest,
    ) -> main_models.RunHotwordResponse:
        runtime = RuntimeOptions()
        return await self.run_hotword_with_options_async(request, runtime)

    def run_keywords_extraction_generation_with_sse(
        self,
        tmp_req: main_models.RunKeywordsExtractionGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunKeywordsExtractionGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunKeywordsExtractionGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunKeywordsExtractionGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunKeywordsExtractionGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_keywords_extraction_generation_with_sse_async(
        self,
        tmp_req: main_models.RunKeywordsExtractionGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunKeywordsExtractionGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunKeywordsExtractionGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunKeywordsExtractionGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunKeywordsExtractionGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_keywords_extraction_generation_with_options(
        self,
        tmp_req: main_models.RunKeywordsExtractionGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunKeywordsExtractionGenerationResponse:
        tmp_req.validate()
        request = main_models.RunKeywordsExtractionGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunKeywordsExtractionGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunKeywordsExtractionGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_keywords_extraction_generation_with_options_async(
        self,
        tmp_req: main_models.RunKeywordsExtractionGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunKeywordsExtractionGenerationResponse:
        tmp_req.validate()
        request = main_models.RunKeywordsExtractionGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunKeywordsExtractionGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunKeywordsExtractionGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_keywords_extraction_generation(
        self,
        request: main_models.RunKeywordsExtractionGenerationRequest,
    ) -> main_models.RunKeywordsExtractionGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_keywords_extraction_generation_with_options(request, runtime)

    async def run_keywords_extraction_generation_async(
        self,
        request: main_models.RunKeywordsExtractionGenerationRequest,
    ) -> main_models.RunKeywordsExtractionGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_keywords_extraction_generation_with_options_async(request, runtime)

    def run_multi_doc_introduction_with_sse(
        self,
        tmp_req: main_models.RunMultiDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunMultiDocIntroductionResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunMultiDocIntroductionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMultiDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMultiDocIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_multi_doc_introduction_with_sse_async(
        self,
        tmp_req: main_models.RunMultiDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunMultiDocIntroductionResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunMultiDocIntroductionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMultiDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunMultiDocIntroductionResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_multi_doc_introduction_with_options(
        self,
        tmp_req: main_models.RunMultiDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunMultiDocIntroductionResponse:
        tmp_req.validate()
        request = main_models.RunMultiDocIntroductionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMultiDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMultiDocIntroductionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_multi_doc_introduction_with_options_async(
        self,
        tmp_req: main_models.RunMultiDocIntroductionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunMultiDocIntroductionResponse:
        tmp_req.validate()
        request = main_models.RunMultiDocIntroductionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_ids):
            request.doc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_ids, 'DocIds', 'json')
        body = {}
        if not DaraCore.is_null(request.doc_ids_shrink):
            body['DocIds'] = request.doc_ids_shrink
        if not DaraCore.is_null(request.key_point_prompt):
            body['KeyPointPrompt'] = request.key_point_prompt
        if not DaraCore.is_null(request.model_name):
            body['ModelName'] = request.model_name
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.summary_prompt):
            body['SummaryPrompt'] = request.summary_prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunMultiDocIntroduction',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunMultiDocIntroductionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_multi_doc_introduction(
        self,
        request: main_models.RunMultiDocIntroductionRequest,
    ) -> main_models.RunMultiDocIntroductionResponse:
        runtime = RuntimeOptions()
        return self.run_multi_doc_introduction_with_options(request, runtime)

    async def run_multi_doc_introduction_async(
        self,
        request: main_models.RunMultiDocIntroductionRequest,
    ) -> main_models.RunMultiDocIntroductionResponse:
        runtime = RuntimeOptions()
        return await self.run_multi_doc_introduction_with_options_async(request, runtime)

    def run_ppt_outline_generation_with_sse(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunPptOutlineGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPptOutlineGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunPptOutlineGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_ppt_outline_generation_with_sse_async(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunPptOutlineGenerationResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPptOutlineGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunPptOutlineGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_ppt_outline_generation_with_options(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunPptOutlineGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPptOutlineGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPptOutlineGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_ppt_outline_generation_with_options_async(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunPptOutlineGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunPptOutlineGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPptOutlineGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_ppt_outline_generation(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
    ) -> main_models.RunPptOutlineGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_ppt_outline_generation_with_options(request, runtime)

    async def run_ppt_outline_generation_async(
        self,
        request: main_models.RunPptOutlineGenerationRequest,
    ) -> main_models.RunPptOutlineGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_ppt_outline_generation_with_options_async(request, runtime)

    def run_quick_writing_with_sse(
        self,
        tmp_req: main_models.RunQuickWritingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunQuickWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunQuickWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunQuickWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunQuickWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_quick_writing_with_sse_async(
        self,
        tmp_req: main_models.RunQuickWritingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunQuickWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunQuickWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunQuickWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunQuickWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_quick_writing_with_options(
        self,
        tmp_req: main_models.RunQuickWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunQuickWritingResponse:
        tmp_req.validate()
        request = main_models.RunQuickWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunQuickWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunQuickWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_quick_writing_with_options_async(
        self,
        tmp_req: main_models.RunQuickWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunQuickWritingResponse:
        tmp_req.validate()
        request = main_models.RunQuickWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunQuickWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunQuickWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_quick_writing(
        self,
        request: main_models.RunQuickWritingRequest,
    ) -> main_models.RunQuickWritingResponse:
        runtime = RuntimeOptions()
        return self.run_quick_writing_with_options(request, runtime)

    async def run_quick_writing_async(
        self,
        request: main_models.RunQuickWritingRequest,
    ) -> main_models.RunQuickWritingResponse:
        runtime = RuntimeOptions()
        return await self.run_quick_writing_with_options_async(request, runtime)

    def run_search_generation_with_sse(
        self,
        tmp_req: main_models.RunSearchGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunSearchGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunSearchGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_context):
            request.agent_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSearchGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_search_generation_with_sse_async(
        self,
        tmp_req: main_models.RunSearchGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunSearchGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunSearchGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_context):
            request.agent_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSearchGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_search_generation_with_options(
        self,
        tmp_req: main_models.RunSearchGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchGenerationResponse:
        tmp_req.validate()
        request = main_models.RunSearchGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_context):
            request.agent_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_generation_with_options_async(
        self,
        tmp_req: main_models.RunSearchGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchGenerationResponse:
        tmp_req.validate()
        request = main_models.RunSearchGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_context):
            request.agent_context_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_context, 'AgentContext', 'json')
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_context_shrink):
            body['AgentContext'] = request.agent_context_shrink
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.original_session_id):
            body['OriginalSessionId'] = request.original_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_generation(
        self,
        request: main_models.RunSearchGenerationRequest,
    ) -> main_models.RunSearchGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_search_generation_with_options(request, runtime)

    async def run_search_generation_async(
        self,
        request: main_models.RunSearchGenerationRequest,
    ) -> main_models.RunSearchGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_search_generation_with_options_async(request, runtime)

    def run_search_similar_articles_with_sse(
        self,
        tmp_req: main_models.RunSearchSimilarArticlesRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunSearchSimilarArticlesResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunSearchSimilarArticlesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchSimilarArticles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSearchSimilarArticlesResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_search_similar_articles_with_sse_async(
        self,
        tmp_req: main_models.RunSearchSimilarArticlesRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunSearchSimilarArticlesResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunSearchSimilarArticlesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchSimilarArticles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSearchSimilarArticlesResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_search_similar_articles_with_options(
        self,
        tmp_req: main_models.RunSearchSimilarArticlesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchSimilarArticlesResponse:
        tmp_req.validate()
        request = main_models.RunSearchSimilarArticlesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchSimilarArticles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchSimilarArticlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_similar_articles_with_options_async(
        self,
        tmp_req: main_models.RunSearchSimilarArticlesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSearchSimilarArticlesResponse:
        tmp_req.validate()
        request = main_models.RunSearchSimilarArticlesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chat_config):
            request.chat_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.chat_config, 'ChatConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.chat_config_shrink):
            body['ChatConfig'] = request.chat_config_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSearchSimilarArticles',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSearchSimilarArticlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_similar_articles(
        self,
        request: main_models.RunSearchSimilarArticlesRequest,
    ) -> main_models.RunSearchSimilarArticlesResponse:
        runtime = RuntimeOptions()
        return self.run_search_similar_articles_with_options(request, runtime)

    async def run_search_similar_articles_async(
        self,
        request: main_models.RunSearchSimilarArticlesRequest,
    ) -> main_models.RunSearchSimilarArticlesResponse:
        runtime = RuntimeOptions()
        return await self.run_search_similar_articles_with_options_async(request, runtime)

    def run_step_by_step_writing_with_sse(
        self,
        tmp_req: main_models.RunStepByStepWritingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunStepByStepWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStepByStepWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStepByStepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStepByStepWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_step_by_step_writing_with_sse_async(
        self,
        tmp_req: main_models.RunStepByStepWritingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunStepByStepWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStepByStepWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStepByStepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStepByStepWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_step_by_step_writing_with_options(
        self,
        tmp_req: main_models.RunStepByStepWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunStepByStepWritingResponse:
        tmp_req.validate()
        request = main_models.RunStepByStepWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStepByStepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStepByStepWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_step_by_step_writing_with_options_async(
        self,
        tmp_req: main_models.RunStepByStepWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunStepByStepWritingResponse:
        tmp_req.validate()
        request = main_models.RunStepByStepWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStepByStepWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStepByStepWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_step_by_step_writing(
        self,
        request: main_models.RunStepByStepWritingRequest,
    ) -> main_models.RunStepByStepWritingResponse:
        runtime = RuntimeOptions()
        return self.run_step_by_step_writing_with_options(request, runtime)

    async def run_step_by_step_writing_async(
        self,
        request: main_models.RunStepByStepWritingRequest,
    ) -> main_models.RunStepByStepWritingResponse:
        runtime = RuntimeOptions()
        return await self.run_step_by_step_writing_with_options_async(request, runtime)

    def run_style_feature_analysis_with_sse(
        self,
        tmp_req: main_models.RunStyleFeatureAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunStyleFeatureAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStyleFeatureAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.material_ids):
            request.material_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleFeatureAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStyleFeatureAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_style_feature_analysis_with_sse_async(
        self,
        tmp_req: main_models.RunStyleFeatureAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunStyleFeatureAnalysisResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunStyleFeatureAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.material_ids):
            request.material_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleFeatureAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunStyleFeatureAnalysisResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_style_feature_analysis_with_options(
        self,
        tmp_req: main_models.RunStyleFeatureAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunStyleFeatureAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunStyleFeatureAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.material_ids):
            request.material_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleFeatureAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStyleFeatureAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_style_feature_analysis_with_options_async(
        self,
        tmp_req: main_models.RunStyleFeatureAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunStyleFeatureAnalysisResponse:
        tmp_req.validate()
        request = main_models.RunStyleFeatureAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.material_ids):
            request.material_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_ids, 'MaterialIds', 'json')
        body = {}
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.material_ids_shrink):
            body['MaterialIds'] = request.material_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunStyleFeatureAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunStyleFeatureAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_style_feature_analysis(
        self,
        request: main_models.RunStyleFeatureAnalysisRequest,
    ) -> main_models.RunStyleFeatureAnalysisResponse:
        runtime = RuntimeOptions()
        return self.run_style_feature_analysis_with_options(request, runtime)

    async def run_style_feature_analysis_async(
        self,
        request: main_models.RunStyleFeatureAnalysisRequest,
    ) -> main_models.RunStyleFeatureAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.run_style_feature_analysis_with_options_async(request, runtime)

    def run_summary_generate_with_sse(
        self,
        request: main_models.RunSummaryGenerateRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunSummaryGenerateResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSummaryGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSummaryGenerateResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_summary_generate_with_sse_async(
        self,
        request: main_models.RunSummaryGenerateRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunSummaryGenerateResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSummaryGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunSummaryGenerateResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_summary_generate_with_options(
        self,
        request: main_models.RunSummaryGenerateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSummaryGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSummaryGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSummaryGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_summary_generate_with_options_async(
        self,
        request: main_models.RunSummaryGenerateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSummaryGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunSummaryGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSummaryGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_summary_generate(
        self,
        request: main_models.RunSummaryGenerateRequest,
    ) -> main_models.RunSummaryGenerateResponse:
        runtime = RuntimeOptions()
        return self.run_summary_generate_with_options(request, runtime)

    async def run_summary_generate_async(
        self,
        request: main_models.RunSummaryGenerateRequest,
    ) -> main_models.RunSummaryGenerateResponse:
        runtime = RuntimeOptions()
        return await self.run_summary_generate_with_options_async(request, runtime)

    def run_text_polishing_with_sse(
        self,
        request: main_models.RunTextPolishingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunTextPolishingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.origin_content):
            body['OriginContent'] = request.origin_content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTextPolishing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTextPolishingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_text_polishing_with_sse_async(
        self,
        request: main_models.RunTextPolishingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunTextPolishingResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.origin_content):
            body['OriginContent'] = request.origin_content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTextPolishing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTextPolishingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_text_polishing_with_options(
        self,
        request: main_models.RunTextPolishingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTextPolishingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.origin_content):
            body['OriginContent'] = request.origin_content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTextPolishing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTextPolishingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_text_polishing_with_options_async(
        self,
        request: main_models.RunTextPolishingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTextPolishingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.origin_content):
            body['OriginContent'] = request.origin_content
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTextPolishing',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTextPolishingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_text_polishing(
        self,
        request: main_models.RunTextPolishingRequest,
    ) -> main_models.RunTextPolishingResponse:
        runtime = RuntimeOptions()
        return self.run_text_polishing_with_options(request, runtime)

    async def run_text_polishing_async(
        self,
        request: main_models.RunTextPolishingRequest,
    ) -> main_models.RunTextPolishingResponse:
        runtime = RuntimeOptions()
        return await self.run_text_polishing_with_options_async(request, runtime)

    def run_title_generation_with_sse(
        self,
        tmp_req: main_models.RunTitleGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunTitleGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTitleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title_count):
            body['TitleCount'] = request.title_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTitleGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTitleGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_title_generation_with_sse_async(
        self,
        tmp_req: main_models.RunTitleGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunTitleGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTitleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title_count):
            body['TitleCount'] = request.title_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTitleGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTitleGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_title_generation_with_options(
        self,
        tmp_req: main_models.RunTitleGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTitleGenerationResponse:
        tmp_req.validate()
        request = main_models.RunTitleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title_count):
            body['TitleCount'] = request.title_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTitleGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTitleGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_title_generation_with_options_async(
        self,
        tmp_req: main_models.RunTitleGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTitleGenerationResponse:
        tmp_req.validate()
        request = main_models.RunTitleGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.deduplicated_titles):
            request.deduplicated_titles_shrink = Utils.array_to_string_with_specified_style(tmp_req.deduplicated_titles, 'DeduplicatedTitles', 'json')
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.deduplicated_titles_shrink):
            body['DeduplicatedTitles'] = request.deduplicated_titles_shrink
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.title_count):
            body['TitleCount'] = request.title_count
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTitleGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTitleGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_title_generation(
        self,
        request: main_models.RunTitleGenerationRequest,
    ) -> main_models.RunTitleGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_title_generation_with_options(request, runtime)

    async def run_title_generation_async(
        self,
        request: main_models.RunTitleGenerationRequest,
    ) -> main_models.RunTitleGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_title_generation_with_options_async(request, runtime)

    def run_topic_selection_merge_with_sse(
        self,
        tmp_req: main_models.RunTopicSelectionMergeRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunTopicSelectionMergeResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTopicSelectionMergeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTopicSelectionMerge',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTopicSelectionMergeResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_topic_selection_merge_with_sse_async(
        self,
        tmp_req: main_models.RunTopicSelectionMergeRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunTopicSelectionMergeResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTopicSelectionMergeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTopicSelectionMerge',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTopicSelectionMergeResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_topic_selection_merge_with_options(
        self,
        tmp_req: main_models.RunTopicSelectionMergeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTopicSelectionMergeResponse:
        tmp_req.validate()
        request = main_models.RunTopicSelectionMergeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTopicSelectionMerge',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTopicSelectionMergeResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_topic_selection_merge_with_options_async(
        self,
        tmp_req: main_models.RunTopicSelectionMergeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTopicSelectionMergeResponse:
        tmp_req.validate()
        request = main_models.RunTopicSelectionMergeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTopicSelectionMerge',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTopicSelectionMergeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_topic_selection_merge(
        self,
        request: main_models.RunTopicSelectionMergeRequest,
    ) -> main_models.RunTopicSelectionMergeResponse:
        runtime = RuntimeOptions()
        return self.run_topic_selection_merge_with_options(request, runtime)

    async def run_topic_selection_merge_async(
        self,
        request: main_models.RunTopicSelectionMergeRequest,
    ) -> main_models.RunTopicSelectionMergeResponse:
        runtime = RuntimeOptions()
        return await self.run_topic_selection_merge_with_options_async(request, runtime)

    def run_translate_generation_with_sse(
        self,
        tmp_req: main_models.RunTranslateGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunTranslateGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTranslateGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTranslateGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTranslateGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_translate_generation_with_sse_async(
        self,
        tmp_req: main_models.RunTranslateGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunTranslateGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunTranslateGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTranslateGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunTranslateGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_translate_generation_with_options(
        self,
        tmp_req: main_models.RunTranslateGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTranslateGenerationResponse:
        tmp_req.validate()
        request = main_models.RunTranslateGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTranslateGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTranslateGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_translate_generation_with_options_async(
        self,
        tmp_req: main_models.RunTranslateGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunTranslateGenerationResponse:
        tmp_req.validate()
        request = main_models.RunTranslateGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunTranslateGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunTranslateGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_translate_generation(
        self,
        request: main_models.RunTranslateGenerationRequest,
    ) -> main_models.RunTranslateGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_translate_generation_with_options(request, runtime)

    async def run_translate_generation_async(
        self,
        request: main_models.RunTranslateGenerationRequest,
    ) -> main_models.RunTranslateGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_translate_generation_with_options_async(request, runtime)

    def run_video_script_generate_with_sse(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunVideoScriptGenerateResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.script_length):
            body['ScriptLength'] = request.script_length
        if not DaraCore.is_null(request.script_number):
            body['ScriptNumber'] = request.script_number
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoScriptGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoScriptGenerateResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_video_script_generate_with_sse_async(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunVideoScriptGenerateResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.script_length):
            body['ScriptLength'] = request.script_length
        if not DaraCore.is_null(request.script_number):
            body['ScriptNumber'] = request.script_number
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoScriptGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunVideoScriptGenerateResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_video_script_generate_with_options(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoScriptGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.script_length):
            body['ScriptLength'] = request.script_length
        if not DaraCore.is_null(request.script_number):
            body['ScriptNumber'] = request.script_number
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoScriptGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoScriptGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_video_script_generate_with_options_async(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunVideoScriptGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.script_length):
            body['ScriptLength'] = request.script_length
        if not DaraCore.is_null(request.script_number):
            body['ScriptNumber'] = request.script_number
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunVideoScriptGenerate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunVideoScriptGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_video_script_generate(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
    ) -> main_models.RunVideoScriptGenerateResponse:
        runtime = RuntimeOptions()
        return self.run_video_script_generate_with_options(request, runtime)

    async def run_video_script_generate_async(
        self,
        request: main_models.RunVideoScriptGenerateRequest,
    ) -> main_models.RunVideoScriptGenerateResponse:
        runtime = RuntimeOptions()
        return await self.run_video_script_generate_with_options_async(request, runtime)

    def run_write_tone_generation_with_sse(
        self,
        tmp_req: main_models.RunWriteToneGenerationRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunWriteToneGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunWriteToneGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriteToneGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWriteToneGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_write_tone_generation_with_sse_async(
        self,
        tmp_req: main_models.RunWriteToneGenerationRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunWriteToneGenerationResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunWriteToneGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriteToneGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWriteToneGenerationResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_write_tone_generation_with_options(
        self,
        tmp_req: main_models.RunWriteToneGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunWriteToneGenerationResponse:
        tmp_req.validate()
        request = main_models.RunWriteToneGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriteToneGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWriteToneGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_write_tone_generation_with_options_async(
        self,
        tmp_req: main_models.RunWriteToneGenerationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunWriteToneGenerationResponse:
        tmp_req.validate()
        request = main_models.RunWriteToneGenerationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        body = {}
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriteToneGeneration',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWriteToneGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_write_tone_generation(
        self,
        request: main_models.RunWriteToneGenerationRequest,
    ) -> main_models.RunWriteToneGenerationResponse:
        runtime = RuntimeOptions()
        return self.run_write_tone_generation_with_options(request, runtime)

    async def run_write_tone_generation_async(
        self,
        request: main_models.RunWriteToneGenerationRequest,
    ) -> main_models.RunWriteToneGenerationResponse:
        runtime = RuntimeOptions()
        return await self.run_write_tone_generation_with_options_async(request, runtime)

    def run_writing_with_sse(
        self,
        tmp_req: main_models.RunWritingRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_writing_with_sse_async(
        self,
        tmp_req: main_models.RunWritingRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunWritingResponse, None, None]:
        tmp_req.validate()
        request = main_models.RunWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWritingResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_writing_with_options(
        self,
        tmp_req: main_models.RunWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunWritingResponse:
        tmp_req.validate()
        request = main_models.RunWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWritingResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_writing_with_options_async(
        self,
        tmp_req: main_models.RunWritingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunWritingResponse:
        tmp_req.validate()
        request = main_models.RunWritingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.reference_data):
            request.reference_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.reference_data, 'ReferenceData', 'json')
        if not DaraCore.is_null(tmp_req.writing_config):
            request.writing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_config, 'WritingConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.origin_session_id):
            body['OriginSessionId'] = request.origin_session_id
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.reference_data_shrink):
            body['ReferenceData'] = request.reference_data_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_config_shrink):
            body['WritingConfig'] = request.writing_config_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWriting',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWritingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_writing(
        self,
        request: main_models.RunWritingRequest,
    ) -> main_models.RunWritingResponse:
        runtime = RuntimeOptions()
        return self.run_writing_with_options(request, runtime)

    async def run_writing_async(
        self,
        request: main_models.RunWritingRequest,
    ) -> main_models.RunWritingResponse:
        runtime = RuntimeOptions()
        return await self.run_writing_with_options_async(request, runtime)

    def run_writing_v2with_sse(
        self,
        tmp_req: main_models.RunWritingV2Request,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.RunWritingV2Response, None, None]:
        tmp_req.validate()
        request = main_models.RunWritingV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        if not DaraCore.is_null(tmp_req.mini_docs):
            request.mini_docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.mini_docs, 'MiniDocs', 'json')
        if not DaraCore.is_null(tmp_req.outline_list):
            request.outline_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outline_list, 'OutlineList', 'json')
        if not DaraCore.is_null(tmp_req.outlines):
            request.outlines_shrink = Utils.array_to_string_with_specified_style(tmp_req.outlines, 'Outlines', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.gc_number_size):
            body['GcNumberSize'] = request.gc_number_size
        if not DaraCore.is_null(request.gc_number_size_tag):
            body['GcNumberSizeTag'] = request.gc_number_size_tag
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.mini_docs_shrink):
            body['MiniDocs'] = request.mini_docs_shrink
        if not DaraCore.is_null(request.outline_list_shrink):
            body['OutlineList'] = request.outline_list_shrink
        if not DaraCore.is_null(request.outlines_shrink):
            body['Outlines'] = request.outlines_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_trace_method):
            body['SourceTraceMethod'] = request.source_trace_method
        if not DaraCore.is_null(request.step):
            body['Step'] = request.step
        if not DaraCore.is_null(request.summarization_shrink):
            body['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWritingV2',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWritingV2Response(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def run_writing_v2with_sse_async(
        self,
        tmp_req: main_models.RunWritingV2Request,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.RunWritingV2Response, None, None]:
        tmp_req.validate()
        request = main_models.RunWritingV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        if not DaraCore.is_null(tmp_req.mini_docs):
            request.mini_docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.mini_docs, 'MiniDocs', 'json')
        if not DaraCore.is_null(tmp_req.outline_list):
            request.outline_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outline_list, 'OutlineList', 'json')
        if not DaraCore.is_null(tmp_req.outlines):
            request.outlines_shrink = Utils.array_to_string_with_specified_style(tmp_req.outlines, 'Outlines', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.gc_number_size):
            body['GcNumberSize'] = request.gc_number_size
        if not DaraCore.is_null(request.gc_number_size_tag):
            body['GcNumberSizeTag'] = request.gc_number_size_tag
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.mini_docs_shrink):
            body['MiniDocs'] = request.mini_docs_shrink
        if not DaraCore.is_null(request.outline_list_shrink):
            body['OutlineList'] = request.outline_list_shrink
        if not DaraCore.is_null(request.outlines_shrink):
            body['Outlines'] = request.outlines_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_trace_method):
            body['SourceTraceMethod'] = request.source_trace_method
        if not DaraCore.is_null(request.step):
            body['Step'] = request.step
        if not DaraCore.is_null(request.summarization_shrink):
            body['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWritingV2',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.RunWritingV2Response(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def run_writing_v2with_options(
        self,
        tmp_req: main_models.RunWritingV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.RunWritingV2Response:
        tmp_req.validate()
        request = main_models.RunWritingV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        if not DaraCore.is_null(tmp_req.mini_docs):
            request.mini_docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.mini_docs, 'MiniDocs', 'json')
        if not DaraCore.is_null(tmp_req.outline_list):
            request.outline_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outline_list, 'OutlineList', 'json')
        if not DaraCore.is_null(tmp_req.outlines):
            request.outlines_shrink = Utils.array_to_string_with_specified_style(tmp_req.outlines, 'Outlines', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.gc_number_size):
            body['GcNumberSize'] = request.gc_number_size
        if not DaraCore.is_null(request.gc_number_size_tag):
            body['GcNumberSizeTag'] = request.gc_number_size_tag
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.mini_docs_shrink):
            body['MiniDocs'] = request.mini_docs_shrink
        if not DaraCore.is_null(request.outline_list_shrink):
            body['OutlineList'] = request.outline_list_shrink
        if not DaraCore.is_null(request.outlines_shrink):
            body['Outlines'] = request.outlines_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_trace_method):
            body['SourceTraceMethod'] = request.source_trace_method
        if not DaraCore.is_null(request.step):
            body['Step'] = request.step
        if not DaraCore.is_null(request.summarization_shrink):
            body['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWritingV2',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWritingV2Response(),
            self.call_api(params, req, runtime)
        )

    async def run_writing_v2with_options_async(
        self,
        tmp_req: main_models.RunWritingV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.RunWritingV2Response:
        tmp_req.validate()
        request = main_models.RunWritingV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.articles):
            request.articles_shrink = Utils.array_to_string_with_specified_style(tmp_req.articles, 'Articles', 'json')
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        if not DaraCore.is_null(tmp_req.mini_docs):
            request.mini_docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.mini_docs, 'MiniDocs', 'json')
        if not DaraCore.is_null(tmp_req.outline_list):
            request.outline_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.outline_list, 'OutlineList', 'json')
        if not DaraCore.is_null(tmp_req.outlines):
            request.outlines_shrink = Utils.array_to_string_with_specified_style(tmp_req.outlines, 'Outlines', 'json')
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        if not DaraCore.is_null(tmp_req.summarization):
            request.summarization_shrink = Utils.array_to_string_with_specified_style(tmp_req.summarization, 'Summarization', 'json')
        if not DaraCore.is_null(tmp_req.writing_params):
            request.writing_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.writing_params, 'WritingParams', 'json')
        body = {}
        if not DaraCore.is_null(request.articles_shrink):
            body['Articles'] = request.articles_shrink
        if not DaraCore.is_null(request.distribute_writing):
            body['DistributeWriting'] = request.distribute_writing
        if not DaraCore.is_null(request.gc_number_size):
            body['GcNumberSize'] = request.gc_number_size
        if not DaraCore.is_null(request.gc_number_size_tag):
            body['GcNumberSizeTag'] = request.gc_number_size_tag
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.language):
            body['Language'] = request.language
        if not DaraCore.is_null(request.mini_docs_shrink):
            body['MiniDocs'] = request.mini_docs_shrink
        if not DaraCore.is_null(request.outline_list_shrink):
            body['OutlineList'] = request.outline_list_shrink
        if not DaraCore.is_null(request.outlines_shrink):
            body['Outlines'] = request.outlines_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.prompt_mode):
            body['PromptMode'] = request.prompt_mode
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.source_trace_method):
            body['SourceTraceMethod'] = request.source_trace_method
        if not DaraCore.is_null(request.step):
            body['Step'] = request.step
        if not DaraCore.is_null(request.summarization_shrink):
            body['Summarization'] = request.summarization_shrink
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.use_search):
            body['UseSearch'] = request.use_search
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.writing_params_shrink):
            body['WritingParams'] = request.writing_params_shrink
        if not DaraCore.is_null(request.writing_scene):
            body['WritingScene'] = request.writing_scene
        if not DaraCore.is_null(request.writing_style):
            body['WritingStyle'] = request.writing_style
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunWritingV2',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunWritingV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def run_writing_v2(
        self,
        request: main_models.RunWritingV2Request,
    ) -> main_models.RunWritingV2Response:
        runtime = RuntimeOptions()
        return self.run_writing_v2with_options(request, runtime)

    async def run_writing_v2_async(
        self,
        request: main_models.RunWritingV2Request,
    ) -> main_models.RunWritingV2Response:
        runtime = RuntimeOptions()
        return await self.run_writing_v2with_options_async(request, runtime)

    def save_custom_text_with_options(
        self,
        request: main_models.SaveCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_custom_text_with_options_async(
        self,
        request: main_models.SaveCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_custom_text(
        self,
        request: main_models.SaveCustomTextRequest,
    ) -> main_models.SaveCustomTextResponse:
        runtime = RuntimeOptions()
        return self.save_custom_text_with_options(request, runtime)

    async def save_custom_text_async(
        self,
        request: main_models.SaveCustomTextRequest,
    ) -> main_models.SaveCustomTextResponse:
        runtime = RuntimeOptions()
        return await self.save_custom_text_with_options_async(request, runtime)

    def save_data_source_order_config_with_options(
        self,
        tmp_req: main_models.SaveDataSourceOrderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDataSourceOrderConfigResponse:
        tmp_req.validate()
        request = main_models.SaveDataSourceOrderConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generate_technology):
            body['GenerateTechnology'] = request.generate_technology
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveDataSourceOrderConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDataSourceOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_data_source_order_config_with_options_async(
        self,
        tmp_req: main_models.SaveDataSourceOrderConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveDataSourceOrderConfigResponse:
        tmp_req.validate()
        request = main_models.SaveDataSourceOrderConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_config_data_source_list):
            request.user_config_data_source_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_config_data_source_list, 'UserConfigDataSourceList', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.generate_technology):
            body['GenerateTechnology'] = request.generate_technology
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.user_config_data_source_list_shrink):
            body['UserConfigDataSourceList'] = request.user_config_data_source_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveDataSourceOrderConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveDataSourceOrderConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_data_source_order_config(
        self,
        request: main_models.SaveDataSourceOrderConfigRequest,
    ) -> main_models.SaveDataSourceOrderConfigResponse:
        runtime = RuntimeOptions()
        return self.save_data_source_order_config_with_options(request, runtime)

    async def save_data_source_order_config_async(
        self,
        request: main_models.SaveDataSourceOrderConfigRequest,
    ) -> main_models.SaveDataSourceOrderConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_data_source_order_config_with_options_async(request, runtime)

    def save_material_document_with_options(
        self,
        tmp_req: main_models.SaveMaterialDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMaterialDocumentResponse:
        tmp_req.validate()
        request = main_models.SaveMaterialDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_keywords):
            request.doc_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not DaraCore.is_null(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.pub_time):
            body['PubTime'] = request.pub_time
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.src_from):
            body['SrcFrom'] = request.src_from
        if not DaraCore.is_null(request.summary):
            body['Summary'] = request.summary
        if not DaraCore.is_null(request.text_content):
            body['TextContent'] = request.text_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveMaterialDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_material_document_with_options_async(
        self,
        tmp_req: main_models.SaveMaterialDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveMaterialDocumentResponse:
        tmp_req.validate()
        request = main_models.SaveMaterialDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_keywords):
            request.doc_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.both_save_private_and_share):
            body['BothSavePrivateAndShare'] = request.both_save_private_and_share
        if not DaraCore.is_null(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.pub_time):
            body['PubTime'] = request.pub_time
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.src_from):
            body['SrcFrom'] = request.src_from
        if not DaraCore.is_null(request.summary):
            body['Summary'] = request.summary
        if not DaraCore.is_null(request.text_content):
            body['TextContent'] = request.text_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveMaterialDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_material_document(
        self,
        request: main_models.SaveMaterialDocumentRequest,
    ) -> main_models.SaveMaterialDocumentResponse:
        runtime = RuntimeOptions()
        return self.save_material_document_with_options(request, runtime)

    async def save_material_document_async(
        self,
        request: main_models.SaveMaterialDocumentRequest,
    ) -> main_models.SaveMaterialDocumentResponse:
        runtime = RuntimeOptions()
        return await self.save_material_document_with_options_async(request, runtime)

    def save_style_learning_result_with_options(
        self,
        tmp_req: main_models.SaveStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveStyleLearningResultResponse:
        tmp_req.validate()
        request = main_models.SaveStyleLearningResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_text_id_list):
            request.custom_text_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_text_id_list, 'CustomTextIdList', 'json')
        if not DaraCore.is_null(tmp_req.material_id_list):
            request.material_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_id_list, 'MaterialIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.aigc_result):
            body['AigcResult'] = request.aigc_result
        if not DaraCore.is_null(request.custom_text_id_list_shrink):
            body['CustomTextIdList'] = request.custom_text_id_list_shrink
        if not DaraCore.is_null(request.material_id_list_shrink):
            body['MaterialIdList'] = request.material_id_list_shrink
        if not DaraCore.is_null(request.rewrite_result):
            body['RewriteResult'] = request.rewrite_result
        if not DaraCore.is_null(request.style_name):
            body['StyleName'] = request.style_name
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveStyleLearningResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_style_learning_result_with_options_async(
        self,
        tmp_req: main_models.SaveStyleLearningResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveStyleLearningResultResponse:
        tmp_req.validate()
        request = main_models.SaveStyleLearningResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_text_id_list):
            request.custom_text_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_text_id_list, 'CustomTextIdList', 'json')
        if not DaraCore.is_null(tmp_req.material_id_list):
            request.material_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.material_id_list, 'MaterialIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.aigc_result):
            body['AigcResult'] = request.aigc_result
        if not DaraCore.is_null(request.custom_text_id_list_shrink):
            body['CustomTextIdList'] = request.custom_text_id_list_shrink
        if not DaraCore.is_null(request.material_id_list_shrink):
            body['MaterialIdList'] = request.material_id_list_shrink
        if not DaraCore.is_null(request.rewrite_result):
            body['RewriteResult'] = request.rewrite_result
        if not DaraCore.is_null(request.style_name):
            body['StyleName'] = request.style_name
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveStyleLearningResult',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveStyleLearningResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_style_learning_result(
        self,
        request: main_models.SaveStyleLearningResultRequest,
    ) -> main_models.SaveStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return self.save_style_learning_result_with_options(request, runtime)

    async def save_style_learning_result_async(
        self,
        request: main_models.SaveStyleLearningResultRequest,
    ) -> main_models.SaveStyleLearningResultResponse:
        runtime = RuntimeOptions()
        return await self.save_style_learning_result_with_options_async(request, runtime)

    def search_dataset_documents_with_options(
        self,
        request: main_models.SearchDatasetDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchDatasetDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.extend_1):
            body['Extend1'] = request.extend_1
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDatasetDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDatasetDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_dataset_documents_with_options_async(
        self,
        request: main_models.SearchDatasetDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchDatasetDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.extend_1):
            body['Extend1'] = request.extend_1
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDatasetDocuments',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDatasetDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_dataset_documents(
        self,
        request: main_models.SearchDatasetDocumentsRequest,
    ) -> main_models.SearchDatasetDocumentsResponse:
        runtime = RuntimeOptions()
        return self.search_dataset_documents_with_options(request, runtime)

    async def search_dataset_documents_async(
        self,
        request: main_models.SearchDatasetDocumentsRequest,
    ) -> main_models.SearchDatasetDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.search_dataset_documents_with_options_async(request, runtime)

    def search_news_with_options(
        self,
        tmp_req: main_models.SearchNewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchNewsResponse:
        tmp_req.validate()
        request = main_models.SearchNewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchNews',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchNewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_news_with_options_async(
        self,
        tmp_req: main_models.SearchNewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchNewsResponse:
        tmp_req.validate()
        request = main_models.SearchNewsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.search_sources):
            request.search_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_sources, 'SearchSources', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.filter_not_null):
            body['FilterNotNull'] = request.filter_not_null
        if not DaraCore.is_null(request.include_content):
            body['IncludeContent'] = request.include_content
        if not DaraCore.is_null(request.page):
            body['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.search_sources_shrink):
            body['SearchSources'] = request.search_sources_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchNews',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchNewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_news(
        self,
        request: main_models.SearchNewsRequest,
    ) -> main_models.SearchNewsResponse:
        runtime = RuntimeOptions()
        return self.search_news_with_options(request, runtime)

    async def search_news_async(
        self,
        request: main_models.SearchNewsRequest,
    ) -> main_models.SearchNewsResponse:
        runtime = RuntimeOptions()
        return await self.search_news_with_options_async(request, runtime)

    def submit_async_task_with_options(
        self,
        request: main_models.SubmitAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_code):
            body['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_async_task_with_options_async(
        self,
        request: main_models.SubmitAsyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAsyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.task_code):
            body['TaskCode'] = request.task_code
        if not DaraCore.is_null(request.task_execute_time):
            body['TaskExecuteTime'] = request.task_execute_time
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_param):
            body['TaskParam'] = request.task_param
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAsyncTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_async_task(
        self,
        request: main_models.SubmitAsyncTaskRequest,
    ) -> main_models.SubmitAsyncTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_async_task_with_options(request, runtime)

    async def submit_async_task_async(
        self,
        request: main_models.SubmitAsyncTaskRequest,
    ) -> main_models.SubmitAsyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_async_task_with_options_async(request, runtime)

    def submit_audit_note_with_options(
        self,
        request: main_models.SubmitAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAuditNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_audit_note_with_options_async(
        self,
        request: main_models.SubmitAuditNoteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAuditNoteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAuditNote',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAuditNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_audit_note(
        self,
        request: main_models.SubmitAuditNoteRequest,
    ) -> main_models.SubmitAuditNoteResponse:
        runtime = RuntimeOptions()
        return self.submit_audit_note_with_options(request, runtime)

    async def submit_audit_note_async(
        self,
        request: main_models.SubmitAuditNoteRequest,
    ) -> main_models.SubmitAuditNoteResponse:
        runtime = RuntimeOptions()
        return await self.submit_audit_note_with_options_async(request, runtime)

    def submit_audit_task_with_options(
        self,
        request: main_models.SubmitAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAuditTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_audit_task_with_options_async(
        self,
        request: main_models.SubmitAuditTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAuditTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['ArticleId'] = request.article_id
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAuditTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAuditTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_audit_task(
        self,
        request: main_models.SubmitAuditTaskRequest,
    ) -> main_models.SubmitAuditTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_audit_task_with_options(request, runtime)

    async def submit_audit_task_async(
        self,
        request: main_models.SubmitAuditTaskRequest,
    ) -> main_models.SubmitAuditTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_audit_task_with_options_async(request, runtime)

    def submit_custom_hot_topic_broadcast_job_with_options(
        self,
        tmp_req: main_models.SubmitCustomHotTopicBroadcastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomHotTopicBroadcastJobResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomHotTopicBroadcastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hot_topic_broadcast_config):
            request.hot_topic_broadcast_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topic_broadcast_config, 'HotTopicBroadcastConfig', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_broadcast_config_shrink):
            body['HotTopicBroadcastConfig'] = request.hot_topic_broadcast_config_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomHotTopicBroadcastJob',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomHotTopicBroadcastJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_hot_topic_broadcast_job_with_options_async(
        self,
        tmp_req: main_models.SubmitCustomHotTopicBroadcastJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomHotTopicBroadcastJobResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomHotTopicBroadcastJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.hot_topic_broadcast_config):
            request.hot_topic_broadcast_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.hot_topic_broadcast_config, 'HotTopicBroadcastConfig', 'json')
        if not DaraCore.is_null(tmp_req.topics):
            request.topics_shrink = Utils.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        body = {}
        if not DaraCore.is_null(request.hot_topic_broadcast_config_shrink):
            body['HotTopicBroadcastConfig'] = request.hot_topic_broadcast_config_shrink
        if not DaraCore.is_null(request.hot_topic_version):
            body['HotTopicVersion'] = request.hot_topic_version
        if not DaraCore.is_null(request.topics_shrink):
            body['Topics'] = request.topics_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomHotTopicBroadcastJob',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomHotTopicBroadcastJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_hot_topic_broadcast_job(
        self,
        request: main_models.SubmitCustomHotTopicBroadcastJobRequest,
    ) -> main_models.SubmitCustomHotTopicBroadcastJobResponse:
        runtime = RuntimeOptions()
        return self.submit_custom_hot_topic_broadcast_job_with_options(request, runtime)

    async def submit_custom_hot_topic_broadcast_job_async(
        self,
        request: main_models.SubmitCustomHotTopicBroadcastJobRequest,
    ) -> main_models.SubmitCustomHotTopicBroadcastJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_custom_hot_topic_broadcast_job_with_options_async(request, runtime)

    def submit_custom_source_topic_analysis_with_options(
        self,
        tmp_req: main_models.SubmitCustomSourceTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomSourceTopicAnalysisResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomSourceTopicAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.analysis_types):
            request.analysis_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.analysis_types, 'AnalysisTypes', 'json')
        if not DaraCore.is_null(tmp_req.news):
            request.news_shrink = Utils.array_to_string_with_specified_style(tmp_req.news, 'News', 'json')
        body = {}
        if not DaraCore.is_null(request.analysis_types_shrink):
            body['AnalysisTypes'] = request.analysis_types_shrink
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.max_topic_size):
            body['MaxTopicSize'] = request.max_topic_size
        if not DaraCore.is_null(request.news_shrink):
            body['News'] = request.news_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomSourceTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomSourceTopicAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_source_topic_analysis_with_options_async(
        self,
        tmp_req: main_models.SubmitCustomSourceTopicAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomSourceTopicAnalysisResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomSourceTopicAnalysisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.analysis_types):
            request.analysis_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.analysis_types, 'AnalysisTypes', 'json')
        if not DaraCore.is_null(tmp_req.news):
            request.news_shrink = Utils.array_to_string_with_specified_style(tmp_req.news, 'News', 'json')
        body = {}
        if not DaraCore.is_null(request.analysis_types_shrink):
            body['AnalysisTypes'] = request.analysis_types_shrink
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.max_topic_size):
            body['MaxTopicSize'] = request.max_topic_size
        if not DaraCore.is_null(request.news_shrink):
            body['News'] = request.news_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomSourceTopicAnalysis',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomSourceTopicAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_source_topic_analysis(
        self,
        request: main_models.SubmitCustomSourceTopicAnalysisRequest,
    ) -> main_models.SubmitCustomSourceTopicAnalysisResponse:
        runtime = RuntimeOptions()
        return self.submit_custom_source_topic_analysis_with_options(request, runtime)

    async def submit_custom_source_topic_analysis_async(
        self,
        request: main_models.SubmitCustomSourceTopicAnalysisRequest,
    ) -> main_models.SubmitCustomSourceTopicAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.submit_custom_source_topic_analysis_with_options_async(request, runtime)

    def submit_custom_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_custom_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCustomTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_custom_topic_selection_perspective_analysis_task(
        self,
        request: main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_custom_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_custom_topic_selection_perspective_analysis_task_async(
        self,
        request: main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_custom_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def submit_deep_write_task_with_options(
        self,
        tmp_req: main_models.SubmitDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDeepWriteTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDeepWriteTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_orchestration):
            request.agent_orchestration_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_orchestration, 'AgentOrchestration', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_orchestration_shrink):
            query['AgentOrchestration'] = request.agent_orchestration_shrink
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.instructions):
            body['Instructions'] = request.instructions
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDeepWriteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_deep_write_task_with_options_async(
        self,
        tmp_req: main_models.SubmitDeepWriteTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDeepWriteTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDeepWriteTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.agent_orchestration):
            request.agent_orchestration_shrink = Utils.array_to_string_with_specified_style(tmp_req.agent_orchestration, 'AgentOrchestration', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_orchestration_shrink):
            query['AgentOrchestration'] = request.agent_orchestration_shrink
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.input):
            body['Input'] = request.input
        if not DaraCore.is_null(request.instructions):
            body['Instructions'] = request.instructions
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDeepWriteTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDeepWriteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_deep_write_task(
        self,
        request: main_models.SubmitDeepWriteTaskRequest,
    ) -> main_models.SubmitDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_deep_write_task_with_options(request, runtime)

    async def submit_deep_write_task_async(
        self,
        request: main_models.SubmitDeepWriteTaskRequest,
    ) -> main_models.SubmitDeepWriteTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_deep_write_task_with_options_async(request, runtime)

    def submit_doc_cluster_task_with_options(
        self,
        tmp_req: main_models.SubmitDocClusterTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocClusterTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDocClusterTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not DaraCore.is_null(request.title_length):
            body['TitleLength'] = request.title_length
        if not DaraCore.is_null(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocClusterTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocClusterTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_cluster_task_with_options_async(
        self,
        tmp_req: main_models.SubmitDocClusterTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDocClusterTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitDocClusterTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.summary_length):
            body['SummaryLength'] = request.summary_length
        if not DaraCore.is_null(request.title_length):
            body['TitleLength'] = request.title_length
        if not DaraCore.is_null(request.topic_count):
            body['TopicCount'] = request.topic_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDocClusterTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDocClusterTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_cluster_task(
        self,
        request: main_models.SubmitDocClusterTaskRequest,
    ) -> main_models.SubmitDocClusterTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_doc_cluster_task_with_options(request, runtime)

    async def submit_doc_cluster_task_async(
        self,
        request: main_models.SubmitDocClusterTaskRequest,
    ) -> main_models.SubmitDocClusterTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_doc_cluster_task_with_options_async(request, runtime)

    def submit_enterprise_voc_analysis_task_with_options(
        self,
        tmp_req: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content_tags):
            request.content_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.content_tags, 'ContentTags', 'json')
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'FilterTags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.content_tags_shrink):
            body['ContentTags'] = request.content_tags_shrink
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['FilterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.material_type):
            body['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.positive_sample):
            body['PositiveSample'] = request.positive_sample
        if not DaraCore.is_null(request.positive_sample_file_key):
            body['PositiveSampleFileKey'] = request.positive_sample_file_key
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseVocAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_enterprise_voc_analysis_task_with_options_async(
        self,
        tmp_req: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitEnterpriseVocAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.content_tags):
            request.content_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.content_tags, 'ContentTags', 'json')
        if not DaraCore.is_null(tmp_req.contents):
            request.contents_shrink = Utils.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not DaraCore.is_null(tmp_req.filter_tags):
            request.filter_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_tags, 'FilterTags', 'json')
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.content_tags_shrink):
            body['ContentTags'] = request.content_tags_shrink
        if not DaraCore.is_null(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.filter_tags_shrink):
            body['FilterTags'] = request.filter_tags_shrink
        if not DaraCore.is_null(request.material_type):
            body['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.model_id):
            body['ModelId'] = request.model_id
        if not DaraCore.is_null(request.positive_sample):
            body['PositiveSample'] = request.positive_sample
        if not DaraCore.is_null(request.positive_sample_file_key):
            body['PositiveSampleFileKey'] = request.positive_sample_file_key
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseVocAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseVocAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_enterprise_voc_analysis_task(
        self,
        request: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_enterprise_voc_analysis_task_with_options(request, runtime)

    async def submit_enterprise_voc_analysis_task_async(
        self,
        request: main_models.SubmitEnterpriseVocAnalysisTaskRequest,
    ) -> main_models.SubmitEnterpriseVocAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_enterprise_voc_analysis_task_with_options_async(request, runtime)

    def submit_export_terms_task_with_options(
        self,
        request: main_models.SubmitExportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitExportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitExportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitExportTermsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_export_terms_task_with_options_async(
        self,
        request: main_models.SubmitExportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitExportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitExportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitExportTermsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_export_terms_task(
        self,
        request: main_models.SubmitExportTermsTaskRequest,
    ) -> main_models.SubmitExportTermsTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_export_terms_task_with_options(request, runtime)

    async def submit_export_terms_task_async(
        self,
        request: main_models.SubmitExportTermsTaskRequest,
    ) -> main_models.SubmitExportTermsTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_export_terms_task_with_options_async(request, runtime)

    def submit_fact_audit_url_with_options(
        self,
        request: main_models.SubmitFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFactAuditUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fact_audit_url_with_options_async(
        self,
        request: main_models.SubmitFactAuditUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFactAuditUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFactAuditUrl',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFactAuditUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fact_audit_url(
        self,
        request: main_models.SubmitFactAuditUrlRequest,
    ) -> main_models.SubmitFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return self.submit_fact_audit_url_with_options(request, runtime)

    async def submit_fact_audit_url_async(
        self,
        request: main_models.SubmitFactAuditUrlRequest,
    ) -> main_models.SubmitFactAuditUrlResponse:
        runtime = RuntimeOptions()
        return await self.submit_fact_audit_url_with_options_async(request, runtime)

    def submit_import_terms_task_with_options(
        self,
        request: main_models.SubmitImportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImportTermsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_import_terms_task_with_options_async(
        self,
        request: main_models.SubmitImportTermsTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImportTermsTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImportTermsTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImportTermsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_import_terms_task(
        self,
        request: main_models.SubmitImportTermsTaskRequest,
    ) -> main_models.SubmitImportTermsTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_import_terms_task_with_options(request, runtime)

    async def submit_import_terms_task_async(
        self,
        request: main_models.SubmitImportTermsTaskRequest,
    ) -> main_models.SubmitImportTermsTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_import_terms_task_with_options_async(request, runtime)

    def submit_smart_audit_with_options(
        self,
        tmp_req: main_models.SubmitSmartAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmartAuditResponse:
        tmp_req.validate()
        request = main_models.SubmitSmartAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_url_list):
            request.image_url_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_url_list, 'ImageUrlList', 'json')
        if not DaraCore.is_null(tmp_req.sub_codes):
            request.sub_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_codes, 'SubCodes', 'json')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'imageUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.image_url_list_shrink):
            body['ImageUrlList'] = request.image_url_list_shrink
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.sub_codes_shrink):
            body['SubCodes'] = request.sub_codes_shrink
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.image_urls_shrink):
            body['imageUrls'] = request.image_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmartAudit',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmartAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smart_audit_with_options_async(
        self,
        tmp_req: main_models.SubmitSmartAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmartAuditResponse:
        tmp_req.validate()
        request = main_models.SubmitSmartAuditShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_url_list):
            request.image_url_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_url_list, 'ImageUrlList', 'json')
        if not DaraCore.is_null(tmp_req.sub_codes):
            request.sub_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.sub_codes, 'SubCodes', 'json')
        if not DaraCore.is_null(tmp_req.image_urls):
            request.image_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_urls, 'imageUrls', 'json')
        body = {}
        if not DaraCore.is_null(request.image_url_list_shrink):
            body['ImageUrlList'] = request.image_url_list_shrink
        if not DaraCore.is_null(request.note_id):
            body['NoteId'] = request.note_id
        if not DaraCore.is_null(request.sub_codes_shrink):
            body['SubCodes'] = request.sub_codes_shrink
        if not DaraCore.is_null(request.terms_name):
            body['TermsName'] = request.terms_name
        if not DaraCore.is_null(request.text):
            body['Text'] = request.text
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.image_urls_shrink):
            body['imageUrls'] = request.image_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmartAudit',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmartAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smart_audit(
        self,
        request: main_models.SubmitSmartAuditRequest,
    ) -> main_models.SubmitSmartAuditResponse:
        runtime = RuntimeOptions()
        return self.submit_smart_audit_with_options(request, runtime)

    async def submit_smart_audit_async(
        self,
        request: main_models.SubmitSmartAuditRequest,
    ) -> main_models.SubmitSmartAuditResponse:
        runtime = RuntimeOptions()
        return await self.submit_smart_audit_with_options_async(request, runtime)

    def submit_smart_clip_task_with_options(
        self,
        tmp_req: main_models.SubmitSmartClipTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmartClipTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitSmartClipTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.editing_config):
            request.editing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.editing_config, 'EditingConfig', 'json')
        if not DaraCore.is_null(tmp_req.input_config):
            request.input_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_config, 'InputConfig', 'json')
        if not DaraCore.is_null(tmp_req.output_config):
            request.output_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.output_config, 'OutputConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.editing_config_shrink):
            body['EditingConfig'] = request.editing_config_shrink
        if not DaraCore.is_null(request.extend_param):
            body['ExtendParam'] = request.extend_param
        if not DaraCore.is_null(request.input_config_shrink):
            body['InputConfig'] = request.input_config_shrink
        if not DaraCore.is_null(request.output_config_shrink):
            body['OutputConfig'] = request.output_config_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmartClipTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmartClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smart_clip_task_with_options_async(
        self,
        tmp_req: main_models.SubmitSmartClipTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmartClipTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitSmartClipTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.editing_config):
            request.editing_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.editing_config, 'EditingConfig', 'json')
        if not DaraCore.is_null(tmp_req.input_config):
            request.input_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.input_config, 'InputConfig', 'json')
        if not DaraCore.is_null(tmp_req.output_config):
            request.output_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.output_config, 'OutputConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.editing_config_shrink):
            body['EditingConfig'] = request.editing_config_shrink
        if not DaraCore.is_null(request.extend_param):
            body['ExtendParam'] = request.extend_param
        if not DaraCore.is_null(request.input_config_shrink):
            body['InputConfig'] = request.input_config_shrink
        if not DaraCore.is_null(request.output_config_shrink):
            body['OutputConfig'] = request.output_config_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmartClipTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmartClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smart_clip_task(
        self,
        request: main_models.SubmitSmartClipTaskRequest,
    ) -> main_models.SubmitSmartClipTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_smart_clip_task_with_options(request, runtime)

    async def submit_smart_clip_task_async(
        self,
        request: main_models.SubmitSmartClipTaskRequest,
    ) -> main_models.SubmitSmartClipTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_smart_clip_task_with_options_async(request, runtime)

    def submit_topic_selection_perspective_analysis_task_with_options(
        self,
        tmp_req: main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not DaraCore.is_null(tmp_req.perspective_types):
            request.perspective_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_topic_selection_perspective_analysis_task_with_options_async(
        self,
        tmp_req: main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.documents):
            request.documents_shrink = Utils.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        if not DaraCore.is_null(tmp_req.perspective_types):
            request.perspective_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.perspective_types, 'PerspectiveTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not DaraCore.is_null(request.perspective_types_shrink):
            body['PerspectiveTypes'] = request.perspective_types_shrink
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTopicSelectionPerspectiveAnalysisTask',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_topic_selection_perspective_analysis_task(
        self,
        request: main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_topic_selection_perspective_analysis_task_with_options(request, runtime)

    async def submit_topic_selection_perspective_analysis_task_async(
        self,
        request: main_models.SubmitTopicSelectionPerspectiveAnalysisTaskRequest,
    ) -> main_models.SubmitTopicSelectionPerspectiveAnalysisTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_topic_selection_perspective_analysis_task_with_options_async(request, runtime)

    def update_custom_text_with_options(
        self,
        request: main_models.UpdateCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_text_with_options_async(
        self,
        request: main_models.UpdateCustomTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomText',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_text(
        self,
        request: main_models.UpdateCustomTextRequest,
    ) -> main_models.UpdateCustomTextResponse:
        runtime = RuntimeOptions()
        return self.update_custom_text_with_options(request, runtime)

    async def update_custom_text_async(
        self,
        request: main_models.UpdateCustomTextRequest,
    ) -> main_models.UpdateCustomTextResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_text_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        tmp_req: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        tmp_req: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            body['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_description):
            body['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.search_dataset_enable):
            body['SearchDatasetEnable'] = request.search_dataset_enable
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_dataset_document_with_options(
        self,
        tmp_req: main_models.UpdateDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document):
            request.document_shrink = Utils.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.document_shrink):
            body['Document'] = request.document_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_document_with_options_async(
        self,
        tmp_req: main_models.UpdateDatasetDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetDocumentResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document):
            request.document_shrink = Utils.array_to_string_with_specified_style(tmp_req.document, 'Document', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.document_shrink):
            body['Document'] = request.document_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDatasetDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset_document(
        self,
        request: main_models.UpdateDatasetDocumentRequest,
    ) -> main_models.UpdateDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return self.update_dataset_document_with_options(request, runtime)

    async def update_dataset_document_async(
        self,
        request: main_models.UpdateDatasetDocumentRequest,
    ) -> main_models.UpdateDatasetDocumentResponse:
        runtime = RuntimeOptions()
        return await self.update_dataset_document_with_options_async(request, runtime)

    def update_general_config_with_options(
        self,
        request: main_models.UpdateGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGeneralConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_general_config_with_options_async(
        self,
        request: main_models.UpdateGeneralConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGeneralConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config_key):
            body['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            body['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGeneralConfig',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGeneralConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_general_config(
        self,
        request: main_models.UpdateGeneralConfigRequest,
    ) -> main_models.UpdateGeneralConfigResponse:
        runtime = RuntimeOptions()
        return self.update_general_config_with_options(request, runtime)

    async def update_general_config_async(
        self,
        request: main_models.UpdateGeneralConfigRequest,
    ) -> main_models.UpdateGeneralConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_general_config_with_options_async(request, runtime)

    def update_generated_content_with_options(
        self,
        tmp_req: main_models.UpdateGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGeneratedContentResponse:
        tmp_req.validate()
        request = main_models.UpdateGeneratedContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_text):
            body['ContentText'] = request.content_text
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGeneratedContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_generated_content_with_options_async(
        self,
        tmp_req: main_models.UpdateGeneratedContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGeneratedContentResponse:
        tmp_req.validate()
        request = main_models.UpdateGeneratedContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.keywords):
            request.keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.keywords, 'Keywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_text):
            body['ContentText'] = request.content_text
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.keywords_shrink):
            body['Keywords'] = request.keywords_shrink
        if not DaraCore.is_null(request.prompt):
            body['Prompt'] = request.prompt
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGeneratedContent',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGeneratedContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_generated_content(
        self,
        request: main_models.UpdateGeneratedContentRequest,
    ) -> main_models.UpdateGeneratedContentResponse:
        runtime = RuntimeOptions()
        return self.update_generated_content_with_options(request, runtime)

    async def update_generated_content_async(
        self,
        request: main_models.UpdateGeneratedContentRequest,
    ) -> main_models.UpdateGeneratedContentResponse:
        runtime = RuntimeOptions()
        return await self.update_generated_content_with_options_async(request, runtime)

    def update_material_document_with_options(
        self,
        tmp_req: main_models.UpdateMaterialDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaterialDocumentResponse:
        tmp_req.validate()
        request = main_models.UpdateMaterialDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_keywords):
            request.doc_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.pub_time):
            body['PubTime'] = request.pub_time
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.src_from):
            body['SrcFrom'] = request.src_from
        if not DaraCore.is_null(request.summary):
            body['Summary'] = request.summary
        if not DaraCore.is_null(request.text_content):
            body['TextContent'] = request.text_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaterialDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMaterialDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_material_document_with_options_async(
        self,
        tmp_req: main_models.UpdateMaterialDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMaterialDocumentResponse:
        tmp_req.validate()
        request = main_models.UpdateMaterialDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.doc_keywords):
            request.doc_keywords_shrink = Utils.array_to_string_with_specified_style(tmp_req.doc_keywords, 'DocKeywords', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.doc_keywords_shrink):
            body['DocKeywords'] = request.doc_keywords_shrink
        if not DaraCore.is_null(request.doc_type):
            body['DocType'] = request.doc_type
        if not DaraCore.is_null(request.external_url):
            body['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.html_content):
            body['HtmlContent'] = request.html_content
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.pub_time):
            body['PubTime'] = request.pub_time
        if not DaraCore.is_null(request.share_attr):
            body['ShareAttr'] = request.share_attr
        if not DaraCore.is_null(request.src_from):
            body['SrcFrom'] = request.src_from
        if not DaraCore.is_null(request.summary):
            body['Summary'] = request.summary
        if not DaraCore.is_null(request.text_content):
            body['TextContent'] = request.text_content
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMaterialDocument',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMaterialDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_material_document(
        self,
        request: main_models.UpdateMaterialDocumentRequest,
    ) -> main_models.UpdateMaterialDocumentResponse:
        runtime = RuntimeOptions()
        return self.update_material_document_with_options(request, runtime)

    async def update_material_document_async(
        self,
        request: main_models.UpdateMaterialDocumentRequest,
    ) -> main_models.UpdateMaterialDocumentResponse:
        runtime = RuntimeOptions()
        return await self.update_material_document_with_options_async(request, runtime)

    def upload_book_with_options(
        self,
        tmp_req: main_models.UploadBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadBookResponse:
        tmp_req.validate()
        request = main_models.UploadBookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.docs):
            request.docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadBook',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_book_with_options_async(
        self,
        tmp_req: main_models.UploadBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadBookResponse:
        tmp_req.validate()
        request = main_models.UploadBookShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.docs):
            request.docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadBook',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_book(
        self,
        request: main_models.UploadBookRequest,
    ) -> main_models.UploadBookResponse:
        runtime = RuntimeOptions()
        return self.upload_book_with_options(request, runtime)

    async def upload_book_async(
        self,
        request: main_models.UploadBookRequest,
    ) -> main_models.UploadBookResponse:
        runtime = RuntimeOptions()
        return await self.upload_book_with_options_async(request, runtime)

    def upload_doc_with_options(
        self,
        tmp_req: main_models.UploadDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocResponse:
        tmp_req.validate()
        request = main_models.UploadDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.docs):
            request.docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_doc_with_options_async(
        self,
        tmp_req: main_models.UploadDocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocResponse:
        tmp_req.validate()
        request = main_models.UploadDocShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.docs):
            request.docs_shrink = Utils.array_to_string_with_specified_style(tmp_req.docs, 'Docs', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.docs_shrink):
            body['Docs'] = request.docs_shrink
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDoc',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_doc(
        self,
        request: main_models.UploadDocRequest,
    ) -> main_models.UploadDocResponse:
        runtime = RuntimeOptions()
        return self.upload_doc_with_options(request, runtime)

    async def upload_doc_async(
        self,
        request: main_models.UploadDocRequest,
    ) -> main_models.UploadDocResponse:
        runtime = RuntimeOptions()
        return await self.upload_doc_with_options_async(request, runtime)

    def validate_upload_template_with_options(
        self,
        request: main_models.ValidateUploadTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateUploadTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateUploadTemplate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateUploadTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_upload_template_with_options_async(
        self,
        request: main_models.ValidateUploadTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateUploadTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_key):
            body['FileKey'] = request.file_key
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateUploadTemplate',
            version = '2023-08-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateUploadTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_upload_template(
        self,
        request: main_models.ValidateUploadTemplateRequest,
    ) -> main_models.ValidateUploadTemplateResponse:
        runtime = RuntimeOptions()
        return self.validate_upload_template_with_options(request, runtime)

    async def validate_upload_template_async(
        self,
        request: main_models.ValidateUploadTemplateRequest,
    ) -> main_models.ValidateUploadTemplateResponse:
        runtime = RuntimeOptions()
        return await self.validate_upload_template_with_options_async(request, runtime)

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_searchplat20240529 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._product_id = 'Searchplat'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''

    def create_audio_asr_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateAudioAsrTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAudioAsrTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudioAsrTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/audio-asr/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAudioAsrTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_audio_asr_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateAudioAsrTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAudioAsrTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudioAsrTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/audio-asr/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAudioAsrTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_audio_asr_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateAudioAsrTaskRequest,
    ) -> main_models.CreateAudioAsrTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_audio_asr_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_audio_asr_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateAudioAsrTaskRequest,
    ) -> main_models.CreateAudioAsrTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_audio_asr_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_document_analyze_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateDocumentAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocumentAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocumentAnalyzeTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocumentAnalyzeTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_document_analyze_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateDocumentAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDocumentAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDocumentAnalyzeTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDocumentAnalyzeTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_document_analyze_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateDocumentAnalyzeTaskRequest,
    ) -> main_models.CreateDocumentAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_document_analyze_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_document_analyze_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateDocumentAnalyzeTaskRequest,
    ) -> main_models.CreateDocumentAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_document_analyze_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_image_analyze_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateImageAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageAnalyzeTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageAnalyzeTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_image_analyze_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateImageAnalyzeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageAnalyzeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageAnalyzeTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageAnalyzeTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_image_analyze_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateImageAnalyzeTaskRequest,
    ) -> main_models.CreateImageAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_image_analyze_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_image_analyze_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateImageAnalyzeTaskRequest,
    ) -> main_models.CreateImageAnalyzeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_image_analyze_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_video_segmentation_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSegmentationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSegmentationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSegmentationTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-segmentation/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSegmentationTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_video_segmentation_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSegmentationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSegmentationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSegmentationTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-segmentation/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSegmentationTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_video_segmentation_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSegmentationTaskRequest,
    ) -> main_models.CreateVideoSegmentationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_video_segmentation_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_video_segmentation_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSegmentationTaskRequest,
    ) -> main_models.CreateVideoSegmentationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_video_segmentation_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_video_snapshot_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSnapshotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSnapshotTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSnapshotTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-snapshot/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSnapshotTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_video_snapshot_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSnapshotTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSnapshotTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSnapshotTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-snapshot/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSnapshotTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_video_snapshot_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSnapshotTaskRequest,
    ) -> main_models.CreateVideoSnapshotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_video_snapshot_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_video_snapshot_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSnapshotTaskRequest,
    ) -> main_models.CreateVideoSnapshotTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_video_snapshot_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def create_video_summarization_task_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSummarizationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSummarizationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSummarizationTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-summarization/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSummarizationTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_video_summarization_task_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSummarizationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoSummarizationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.output):
            body['output'] = request.output
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoSummarizationTask',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-summarization/{service_id}/async',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoSummarizationTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_video_summarization_task(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSummarizationTaskRequest,
    ) -> main_models.CreateVideoSummarizationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_video_summarization_task_with_options(workspace_name, service_id, request, headers, runtime)

    async def create_video_summarization_task_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.CreateVideoSummarizationTaskRequest,
    ) -> main_models.CreateVideoSummarizationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_video_summarization_task_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_audio_asr_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetAudioAsrTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioAsrTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioAsrTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/audio-asr/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioAsrTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_audio_asr_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetAudioAsrTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAudioAsrTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAudioAsrTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/audio-asr/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAudioAsrTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_audio_asr_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetAudioAsrTaskStatusRequest,
    ) -> main_models.GetAudioAsrTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_audio_asr_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_audio_asr_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetAudioAsrTaskStatusRequest,
    ) -> main_models.GetAudioAsrTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_audio_asr_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_analyze_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentAnalyzeTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentAnalyzeTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentAnalyzeTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_analyze_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentAnalyzeTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentAnalyzeTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-analyze/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentAnalyzeTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_analyze_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentAnalyzeTaskStatusRequest,
    ) -> main_models.GetDocumentAnalyzeTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_analyze_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_analyze_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentAnalyzeTaskStatusRequest,
    ) -> main_models.GetDocumentAnalyzeTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_analyze_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_rank_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentRankResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.docs):
            body['docs'] = request.docs
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentRank',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/ranker/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentRankResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_rank_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentRankRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentRankResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.docs):
            body['docs'] = request.docs
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentRank',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/ranker/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentRankResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_rank(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentRankRequest,
    ) -> main_models.GetDocumentRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_rank_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_rank_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentRankRequest,
    ) -> main_models.GetDocumentRankResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_rank_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_document_split_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentSplitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentSplitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentSplit',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-split/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentSplitResponse(),
            self.execute(params, req, runtime)
        )

    async def get_document_split_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentSplitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDocumentSplitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDocumentSplit',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/document-split/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDocumentSplitResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_document_split(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentSplitRequest,
    ) -> main_models.GetDocumentSplitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_document_split_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_document_split_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetDocumentSplitRequest,
    ) -> main_models.GetDocumentSplitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_document_split_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_embedding_tuning_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetEmbeddingTuningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmbeddingTuningResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmbeddingTuning',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/embedding-tuning/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmbeddingTuningResponse(),
            self.execute(params, req, runtime)
        )

    async def get_embedding_tuning_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetEmbeddingTuningRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmbeddingTuningResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetEmbeddingTuning',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/embedding-tuning/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmbeddingTuningResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_embedding_tuning(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetEmbeddingTuningRequest,
    ) -> main_models.GetEmbeddingTuningResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_embedding_tuning_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_embedding_tuning_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetEmbeddingTuningRequest,
    ) -> main_models.GetEmbeddingTuningResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_embedding_tuning_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_image_analyze_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageAnalyzeTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageAnalyzeTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageAnalyzeTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_image_analyze_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageAnalyzeTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageAnalyzeTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageAnalyzeTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-analyze/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageAnalyzeTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_image_analyze_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageAnalyzeTaskStatusRequest,
    ) -> main_models.GetImageAnalyzeTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_image_analyze_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_image_analyze_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageAnalyzeTaskStatusRequest,
    ) -> main_models.GetImageAnalyzeTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_image_analyze_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_image_object_detection_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageObjectDetectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageObjectDetectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageObjectDetection',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-object-detection/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageObjectDetectionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_image_object_detection_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageObjectDetectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetImageObjectDetectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image):
            body['image'] = request.image
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetImageObjectDetection',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/image-object-detection/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageObjectDetectionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_image_object_detection(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageObjectDetectionRequest,
    ) -> main_models.GetImageObjectDetectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_image_object_detection_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_image_object_detection_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetImageObjectDetectionRequest,
    ) -> main_models.GetImageObjectDetectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_image_object_detection_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_multi_modal_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiModalEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiModalEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/multi-modal-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiModalEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_multi_modal_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiModalEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiModalEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/multi-modal-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiModalEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_multi_modal_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalEmbeddingRequest,
    ) -> main_models.GetMultiModalEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_multi_modal_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_multi_modal_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalEmbeddingRequest,
    ) -> main_models.GetMultiModalEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_multi_modal_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_multi_modal_reranker_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalRerankerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiModalRerankerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.docs):
            body['docs'] = request.docs
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiModalReranker',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/multi-modal-reranker/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiModalRerankerResponse(),
            self.execute(params, req, runtime)
        )

    async def get_multi_modal_reranker_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalRerankerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiModalRerankerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.docs):
            body['docs'] = request.docs
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiModalReranker',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/multi-modal-reranker/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiModalRerankerResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_multi_modal_reranker(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalRerankerRequest,
    ) -> main_models.GetMultiModalRerankerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_multi_modal_reranker_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_multi_modal_reranker_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetMultiModalRerankerRequest,
    ) -> main_models.GetMultiModalRerankerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_multi_modal_reranker_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_prediction_with_options(
        self,
        deployment_id: str,
        request: main_models.GetPredictionRequest,
        headers: main_models.GetPredictionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPredictionResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.token):
            real_headers['Token'] = str(headers.token)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'GetPrediction',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/deployments/{deployment_id}/predict',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GetPredictionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_prediction_with_options_async(
        self,
        deployment_id: str,
        request: main_models.GetPredictionRequest,
        headers: main_models.GetPredictionHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetPredictionResponse:
        request.validate()
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.token):
            real_headers['Token'] = str(headers.token)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'GetPrediction',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/deployments/{deployment_id}/predict',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.GetPredictionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_prediction(
        self,
        deployment_id: str,
        request: main_models.GetPredictionRequest,
    ) -> main_models.GetPredictionResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPredictionHeaders()
        return self.get_prediction_with_options(deployment_id, request, headers, runtime)

    async def get_prediction_async(
        self,
        deployment_id: str,
        request: main_models.GetPredictionRequest,
    ) -> main_models.GetPredictionResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetPredictionHeaders()
        return await self.get_prediction_with_options_async(deployment_id, request, headers, runtime)

    def get_query_analysis_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetQueryAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.functions):
            body['functions'] = request.functions
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryAnalysis',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/query-analyze/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryAnalysisResponse(),
            self.execute(params, req, runtime)
        )

    async def get_query_analysis_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetQueryAnalysisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQueryAnalysisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.functions):
            body['functions'] = request.functions
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetQueryAnalysis',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/query-analyze/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueryAnalysisResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_query_analysis(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetQueryAnalysisRequest,
    ) -> main_models.GetQueryAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_query_analysis_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_query_analysis_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetQueryAnalysisRequest,
    ) -> main_models.GetQueryAnalysisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_query_analysis_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.input_type):
            body['input_type'] = request.input_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.input_type):
            body['input_type'] = request.input_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextEmbeddingRequest,
    ) -> main_models.GetTextEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextEmbeddingRequest,
    ) -> main_models.GetTextEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_generation_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.csi_level):
            body['csi_level'] = request.csi_level
        if not DaraCore.is_null(request.enable_search):
            body['enable_search'] = request.enable_search
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextGeneration',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-generation/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextGenerationResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_generation_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextGenerationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextGenerationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.csi_level):
            body['csi_level'] = request.csi_level
        if not DaraCore.is_null(request.enable_search):
            body['enable_search'] = request.enable_search
        if not DaraCore.is_null(request.messages):
            body['messages'] = request.messages
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.stream):
            body['stream'] = request.stream
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextGeneration',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-generation/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextGenerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_generation(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextGenerationRequest,
    ) -> main_models.GetTextGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_generation_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_generation_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextGenerationRequest,
    ) -> main_models.GetTextGenerationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_generation_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_text_sparse_embedding_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextSparseEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextSparseEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.input_type):
            body['input_type'] = request.input_type
        if not DaraCore.is_null(request.return_token):
            body['return_token'] = request.return_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextSparseEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-sparse-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextSparseEmbeddingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_text_sparse_embedding_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextSparseEmbeddingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextSparseEmbeddingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.input):
            body['input'] = request.input
        if not DaraCore.is_null(request.input_type):
            body['input_type'] = request.input_type
        if not DaraCore.is_null(request.return_token):
            body['return_token'] = request.return_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextSparseEmbedding',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/text-sparse-embedding/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextSparseEmbeddingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_text_sparse_embedding(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextSparseEmbeddingRequest,
    ) -> main_models.GetTextSparseEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_sparse_embedding_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_text_sparse_embedding_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetTextSparseEmbeddingRequest,
    ) -> main_models.GetTextSparseEmbeddingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_sparse_embedding_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_video_segmentation_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSegmentationTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSegmentationTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSegmentationTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-segmentation/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSegmentationTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_segmentation_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSegmentationTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSegmentationTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSegmentationTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-segmentation/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSegmentationTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_segmentation_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSegmentationTaskStatusRequest,
    ) -> main_models.GetVideoSegmentationTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_segmentation_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_video_segmentation_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSegmentationTaskStatusRequest,
    ) -> main_models.GetVideoSegmentationTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_segmentation_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_video_snapshot_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSnapshotTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSnapshotTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSnapshotTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-snapshot/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSnapshotTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_snapshot_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSnapshotTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSnapshotTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSnapshotTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-snapshot/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSnapshotTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_snapshot_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSnapshotTaskStatusRequest,
    ) -> main_models.GetVideoSnapshotTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_snapshot_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_video_snapshot_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSnapshotTaskStatusRequest,
    ) -> main_models.GetVideoSnapshotTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_snapshot_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_video_summarization_task_status_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSummarizationTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSummarizationTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSummarizationTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-summarization/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSummarizationTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_summarization_task_status_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSummarizationTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoSummarizationTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoSummarizationTaskStatus',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/video-summarization/{service_id}/async/task-status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoSummarizationTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_summarization_task_status(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSummarizationTaskStatusRequest,
    ) -> main_models.GetVideoSummarizationTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_summarization_task_status_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_video_summarization_task_status_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetVideoSummarizationTaskStatusRequest,
    ) -> main_models.GetVideoSummarizationTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_summarization_task_status_with_options_async(workspace_name, service_id, request, headers, runtime)

    def get_web_search_with_options(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetWebSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['content_type'] = request.content_type
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_rewrite):
            body['query_rewrite'] = request.query_rewrite
        if not DaraCore.is_null(request.top_k):
            body['top_k'] = request.top_k
        if not DaraCore.is_null(request.way):
            body['way'] = request.way
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWebSearch',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/web-search/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def get_web_search_with_options_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetWebSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_type):
            body['content_type'] = request.content_type
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.query_rewrite):
            body['query_rewrite'] = request.query_rewrite
        if not DaraCore.is_null(request.top_k):
            body['top_k'] = request.top_k
        if not DaraCore.is_null(request.way):
            body['way'] = request.way
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetWebSearch',
            version = '2024-05-29',
            protocol = 'HTTPS',
            pathname = f'/v3/openapi/workspaces/{workspace_name}/web-search/{service_id}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_web_search(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetWebSearchRequest,
    ) -> main_models.GetWebSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_web_search_with_options(workspace_name, service_id, request, headers, runtime)

    async def get_web_search_async(
        self,
        workspace_name: str,
        service_id: str,
        request: main_models.GetWebSearchRequest,
    ) -> main_models.GetWebSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_web_search_with_options_async(workspace_name, service_id, request, headers, runtime)

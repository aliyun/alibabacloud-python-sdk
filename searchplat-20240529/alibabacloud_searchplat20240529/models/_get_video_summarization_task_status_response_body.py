# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetVideoSummarizationTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetVideoSummarizationTaskStatusResponseBodyResult = None,
        usage: main_models.GetVideoSummarizationTaskStatusResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency is not None:
            result['latency'] = self.latency

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('result') is not None:
            temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetVideoSummarizationTaskStatusResponseBodyUsage(DaraModel):
    def __init__(
        self,
        audio_token: int = None,
        image_token: int = None,
        input_token: int = None,
        output_token: int = None,
    ):
        self.audio_token = audio_token
        self.image_token = image_token
        self.input_token = input_token
        self.output_token = output_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_token is not None:
            result['audio_token'] = self.audio_token

        if self.image_token is not None:
            result['image_token'] = self.image_token

        if self.input_token is not None:
            result['input_token'] = self.input_token

        if self.output_token is not None:
            result['output_token'] = self.output_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audio_token') is not None:
            self.audio_token = m.get('audio_token')

        if m.get('image_token') is not None:
            self.image_token = m.get('image_token')

        if m.get('input_token') is not None:
            self.input_token = m.get('input_token')

        if m.get('output_token') is not None:
            self.output_token = m.get('output_token')

        return self

class GetVideoSummarizationTaskStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: main_models.GetVideoSummarizationTaskStatusResponseBodyResultData = None,
        error: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.data = data
        self.error = error
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error is not None:
            result['error'] = self.error

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyResultData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class GetVideoSummarizationTaskStatusResponseBodyResultData(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataChunks] = None,
        video_metadata: main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataVideoMetadata = None,
    ):
        self.chunks = chunks
        self.video_metadata = video_metadata

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()
        if self.video_metadata:
            self.video_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['chunks'].append(k1.to_map() if k1 else None)

        if self.video_metadata is not None:
            result['video_metadata'] = self.video_metadata.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataChunks()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('video_metadata') is not None:
            temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataVideoMetadata()
            self.video_metadata = temp_model.from_map(m.get('video_metadata'))

        return self

class GetVideoSummarizationTaskStatusResponseBodyResultDataVideoMetadata(DaraModel):
    def __init__(
        self,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
    ):
        self.summary = summary
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary is not None:
            result['summary'] = self.summary

        if self.tags is not None:
            result['tags'] = self.tags

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class GetVideoSummarizationTaskStatusResponseBodyResultDataChunks(DaraModel):
    def __init__(
        self,
        enhanced_transcript: str = None,
        index: int = None,
        metadata: main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataChunksMetadata = None,
    ):
        self.enhanced_transcript = enhanced_transcript
        self.index = index
        self.metadata = metadata

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enhanced_transcript is not None:
            result['enhanced_transcript'] = self.enhanced_transcript

        if self.index is not None:
            result['index'] = self.index

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enhanced_transcript') is not None:
            self.enhanced_transcript = m.get('enhanced_transcript')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('metadata') is not None:
            temp_model = main_models.GetVideoSummarizationTaskStatusResponseBodyResultDataChunksMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        return self

class GetVideoSummarizationTaskStatusResponseBodyResultDataChunksMetadata(DaraModel):
    def __init__(
        self,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
    ):
        self.summary = summary
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary is not None:
            result['summary'] = self.summary

        if self.tags is not None:
            result['tags'] = self.tags

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetVideoSegmentationTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetVideoSegmentationTaskStatusResponseBodyResult = None,
        usage: main_models.GetVideoSegmentationTaskStatusResponseBodyUsage = None,
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
            temp_model = main_models.GetVideoSegmentationTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetVideoSegmentationTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetVideoSegmentationTaskStatusResponseBodyUsage(DaraModel):
    def __init__(
        self,
        audio_token: int = None,
        image_token: int = None,
    ):
        self.audio_token = audio_token
        self.image_token = image_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audio_token') is not None:
            self.audio_token = m.get('audio_token')

        if m.get('image_token') is not None:
            self.image_token = m.get('image_token')

        return self

class GetVideoSegmentationTaskStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetVideoSegmentationTaskStatusResponseBodyResultData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error is not None:
            result['error'] = self.error

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetVideoSegmentationTaskStatusResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class GetVideoSegmentationTaskStatusResponseBodyResultData(DaraModel):
    def __init__(
        self,
        chunk_index: int = None,
        end_time: float = None,
        snapshots: List[main_models.GetVideoSegmentationTaskStatusResponseBodyResultDataSnapshots] = None,
        start_time: float = None,
        transcript: str = None,
    ):
        self.chunk_index = chunk_index
        self.end_time = end_time
        self.snapshots = snapshots
        self.start_time = start_time
        self.transcript = transcript

    def validate(self):
        if self.snapshots:
            for v1 in self.snapshots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_index is not None:
            result['chunk_index'] = self.chunk_index

        if self.end_time is not None:
            result['end_time'] = self.end_time

        result['snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['snapshots'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.transcript is not None:
            result['transcript'] = self.transcript

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunk_index') is not None:
            self.chunk_index = m.get('chunk_index')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        self.snapshots = []
        if m.get('snapshots') is not None:
            for k1 in m.get('snapshots'):
                temp_model = main_models.GetVideoSegmentationTaskStatusResponseBodyResultDataSnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('transcript') is not None:
            self.transcript = m.get('transcript')

        return self

class GetVideoSegmentationTaskStatusResponseBodyResultDataSnapshots(DaraModel):
    def __init__(
        self,
        frame_index: int = None,
        frame_time: float = None,
        path: str = None,
    ):
        self.frame_index = frame_index
        self.frame_time = frame_time
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_index is not None:
            result['frame_index'] = self.frame_index

        if self.frame_time is not None:
            result['frame_time'] = self.frame_time

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('frame_index') is not None:
            self.frame_index = m.get('frame_index')

        if m.get('frame_time') is not None:
            self.frame_time = m.get('frame_time')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self


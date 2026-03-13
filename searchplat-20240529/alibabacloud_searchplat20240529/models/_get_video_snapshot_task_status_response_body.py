# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetVideoSnapshotTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetVideoSnapshotTaskStatusResponseBodyResult = None,
        usage: main_models.GetVideoSnapshotTaskStatusResponseBodyUsage = None,
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
            temp_model = main_models.GetVideoSnapshotTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetVideoSnapshotTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetVideoSnapshotTaskStatusResponseBodyUsage(DaraModel):
    def __init__(
        self,
        image_count: int = None,
    ):
        self.image_count = image_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_count is not None:
            result['image_count'] = self.image_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')

        return self

class GetVideoSnapshotTaskStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetVideoSnapshotTaskStatusResponseBodyResultData] = None,
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
                temp_model = main_models.GetVideoSnapshotTaskStatusResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class GetVideoSnapshotTaskStatusResponseBodyResultData(DaraModel):
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


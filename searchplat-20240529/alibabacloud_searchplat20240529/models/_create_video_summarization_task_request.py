# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateVideoSummarizationTaskRequest(DaraModel):
    def __init__(
        self,
        input: main_models.CreateVideoSummarizationTaskRequestInput = None,
        output: main_models.CreateVideoSummarizationTaskRequestOutput = None,
        parameters: Dict[str, Any] = None,
    ):
        self.input = input
        self.output = output
        self.parameters = parameters

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input.to_map()

        if self.output is not None:
            result['output'] = self.output.to_map()

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            temp_model = main_models.CreateVideoSummarizationTaskRequestInput()
            self.input = temp_model.from_map(m.get('input'))

        if m.get('output') is not None:
            temp_model = main_models.CreateVideoSummarizationTaskRequestOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

class CreateVideoSummarizationTaskRequestOutput(DaraModel):
    def __init__(
        self,
        oss: str = None,
        type: str = None,
    ):
        self.oss = oss
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss is not None:
            result['oss'] = self.oss

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oss') is not None:
            self.oss = m.get('oss')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateVideoSummarizationTaskRequestInput(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.CreateVideoSummarizationTaskRequestInputChunks] = None,
        file_name: str = None,
        oss: str = None,
        url: str = None,
    ):
        self.chunks = chunks
        self.file_name = file_name
        self.oss = oss
        self.url = url

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['chunks'].append(k1.to_map() if k1 else None)

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.oss is not None:
            result['oss'] = self.oss

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.CreateVideoSummarizationTaskRequestInputChunks()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('oss') is not None:
            self.oss = m.get('oss')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class CreateVideoSummarizationTaskRequestInputChunks(DaraModel):
    def __init__(
        self,
        end_time: float = None,
        snapshots: List[main_models.CreateVideoSummarizationTaskRequestInputChunksSnapshots] = None,
        start_time: float = None,
        transcript: str = None,
    ):
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
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        self.snapshots = []
        if m.get('snapshots') is not None:
            for k1 in m.get('snapshots'):
                temp_model = main_models.CreateVideoSummarizationTaskRequestInputChunksSnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('transcript') is not None:
            self.transcript = m.get('transcript')

        return self

class CreateVideoSummarizationTaskRequestInputChunksSnapshots(DaraModel):
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


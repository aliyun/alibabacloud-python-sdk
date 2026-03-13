# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateAudioAsrTaskRequest(DaraModel):
    def __init__(
        self,
        input: main_models.CreateAudioAsrTaskRequestInput = None,
        output: main_models.CreateAudioAsrTaskRequestOutput = None,
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
            temp_model = main_models.CreateAudioAsrTaskRequestInput()
            self.input = temp_model.from_map(m.get('input'))

        if m.get('output') is not None:
            temp_model = main_models.CreateAudioAsrTaskRequestOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

class CreateAudioAsrTaskRequestOutput(DaraModel):
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



class CreateAudioAsrTaskRequestInput(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        oss: str = None,
        url: str = None,
    ):
        self.content = content
        self.file_name = file_name
        self.oss = oss
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.oss is not None:
            result['oss'] = self.oss

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('oss') is not None:
            self.oss = m.get('oss')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


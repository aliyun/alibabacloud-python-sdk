# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class VideoGenerationRequest(DaraModel):
    def __init__(
        self,
        input: main_models.VideoGenerationRequestInput = None,
        intent: main_models.VideoGenerationRequestIntent = None,
        output: main_models.VideoGenerationRequestOutput = None,
    ):
        # This parameter is required.
        self.input = input
        self.intent = intent
        # This parameter is required.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()
        if self.intent:
            self.intent.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.intent is not None:
            result['Intent'] = self.intent.to_map()

        if self.output is not None:
            result['Output'] = self.output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.VideoGenerationRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Intent') is not None:
            temp_model = main_models.VideoGenerationRequestIntent()
            self.intent = temp_model.from_map(m.get('Intent'))

        if m.get('Output') is not None:
            temp_model = main_models.VideoGenerationRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        return self

class VideoGenerationRequestOutput(DaraModel):
    def __init__(
        self,
        duration: int = None,
        quality: str = None,
        ratio: str = None,
    ):
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.quality = quality
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

class VideoGenerationRequestIntent(DaraModel):
    def __init__(
        self,
        channel: str = None,
        goal: str = None,
    ):
        self.channel = channel
        self.goal = goal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.goal is not None:
            result['Goal'] = self.goal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Goal') is not None:
            self.goal = m.get('Goal')

        return self

class VideoGenerationRequestInput(DaraModel):
    def __init__(
        self,
        extra: Dict[str, Any] = None,
        images: List[str] = None,
        title: str = None,
    ):
        self.extra = extra
        # This parameter is required.
        self.images = images
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.images is not None:
            result['Images'] = self.images

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lingmou20250527 import models as main_models
from darabonba.model import DaraModel

class CreateBroadcastVideoFromTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_id: str = None,
        variables: List[main_models.TemplateVariable] = None,
        video_options: main_models.CreateBroadcastVideoFromTemplateRequestVideoOptions = None,
    ):
        self.name = name
        self.template_id = template_id
        self.variables = variables
        self.video_options = video_options

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()
        if self.video_options:
            self.video_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.template_id is not None:
            result['templateId'] = self.template_id

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        if self.video_options is not None:
            result['videoOptions'] = self.video_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.TemplateVariable()
                self.variables.append(temp_model.from_map(k1))

        if m.get('videoOptions') is not None:
            temp_model = main_models.CreateBroadcastVideoFromTemplateRequestVideoOptions()
            self.video_options = temp_model.from_map(m.get('videoOptions'))

        return self

class CreateBroadcastVideoFromTemplateRequestVideoOptions(DaraModel):
    def __init__(
        self,
        fps: int = None,
        resolution: str = None,
        watermark: bool = None,
    ):
        self.fps = fps
        self.resolution = resolution
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fps is not None:
            result['fps'] = self.fps

        if self.resolution is not None:
            result['resolution'] = self.resolution

        if self.watermark is not None:
            result['watermark'] = self.watermark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fps') is not None:
            self.fps = m.get('fps')

        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')

        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')

        return self


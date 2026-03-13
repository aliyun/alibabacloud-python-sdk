# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetImageObjectDetectionRequest(DaraModel):
    def __init__(
        self,
        image: main_models.GetImageObjectDetectionRequestImage = None,
        options: Dict[str, Any] = None,
    ):
        self.image = image
        self.options = options

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image.to_map()

        if self.options is not None:
            result['options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            temp_model = main_models.GetImageObjectDetectionRequestImage()
            self.image = temp_model.from_map(m.get('image'))

        if m.get('options') is not None:
            self.options = m.get('options')

        return self

class GetImageObjectDetectionRequestImage(DaraModel):
    def __init__(
        self,
        content: str = None,
        url: str = None,
    ):
        self.content = content
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

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetImageObjectDetectionResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetImageObjectDetectionResponseBodyResult = None,
        usage: main_models.GetImageObjectDetectionResponseBodyUsage = None,
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
            temp_model = main_models.GetImageObjectDetectionResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetImageObjectDetectionResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetImageObjectDetectionResponseBodyUsage(DaraModel):
    def __init__(
        self,
        image: int = None,
    ):
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        return self

class GetImageObjectDetectionResponseBodyResult(DaraModel):
    def __init__(
        self,
        objects: List[main_models.GetImageObjectDetectionResponseBodyResultObjects] = None,
    ):
        self.objects = objects

    def validate(self):
        if self.objects:
            for v1 in self.objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objects'] = []
        if self.objects is not None:
            for k1 in self.objects:
                result['objects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.objects = []
        if m.get('objects') is not None:
            for k1 in m.get('objects'):
                temp_model = main_models.GetImageObjectDetectionResponseBodyResultObjects()
                self.objects.append(temp_model.from_map(k1))

        return self

class GetImageObjectDetectionResponseBodyResultObjects(DaraModel):
    def __init__(
        self,
        confidence: str = None,
        location: main_models.GetImageObjectDetectionResponseBodyResultObjectsLocation = None,
    ):
        self.confidence = confidence
        self.location = location

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.location is not None:
            result['location'] = self.location.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('location') is not None:
            temp_model = main_models.GetImageObjectDetectionResponseBodyResultObjectsLocation()
            self.location = temp_model.from_map(m.get('location'))

        return self

class GetImageObjectDetectionResponseBodyResultObjectsLocation(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
        height: int = None,
        width: int = None,
    ):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.height is not None:
            result['height'] = self.height

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self


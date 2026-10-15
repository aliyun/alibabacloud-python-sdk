# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class StorefrontSceneRecognitionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.StorefrontSceneRecognitionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The scene recognition result.
        self.data = data
        # The returned message or failure description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.StorefrontSceneRecognitionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class StorefrontSceneRecognitionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.StorefrontSceneRecognitionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The scene recognition result details.
        self.result = result
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.StorefrontSceneRecognitionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class StorefrontSceneRecognitionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        details: List[main_models.StorefrontSceneRecognitionResponseBodyDataResultDetails] = None,
        grounding: main_models.StorefrontSceneRecognitionResponseBodyDataResultGrounding = None,
        scenes: List[str] = None,
    ):
        # The classification details. This can be an empty array.
        self.details = details
        # The localization information.
        self.grounding = grounding
        # The non-empty scene classification array.
        self.scenes = scenes

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.grounding:
            self.grounding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.grounding is not None:
            result['Grounding'] = self.grounding.to_map()

        if self.scenes is not None:
            result['Scenes'] = self.scenes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.StorefrontSceneRecognitionResponseBodyDataResultDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('Grounding') is not None:
            temp_model = main_models.StorefrontSceneRecognitionResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')

        return self

class StorefrontSceneRecognitionResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.StorefrontSceneRecognitionResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage.
        self.coverage = coverage
        # The region list.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.StorefrontSceneRecognitionResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class StorefrontSceneRecognitionResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[float] = None,
        label: str = None,
        text: str = None,
    ):
        # The bounding box coordinates.
        self.bbox_2d = bbox_2d
        # The label.
        self.label = label
        # The recognized text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox_2d is not None:
            result['Bbox2d'] = self.bbox_2d

        if self.label is not None:
            result['Label'] = self.label

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox2d') is not None:
            self.bbox_2d = m.get('Bbox2d')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class StorefrontSceneRecognitionResponseBodyDataResultDetails(DaraModel):
    def __init__(
        self,
        clazz: str = None,
        confidence: float = None,
    ):
        # The non-empty category name.
        self.clazz = clazz
        # A finite numerical value. The source document does not specify a value range.
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clazz is not None:
            result['Clazz'] = self.clazz

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clazz') is not None:
            self.clazz = m.get('Clazz')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        return self


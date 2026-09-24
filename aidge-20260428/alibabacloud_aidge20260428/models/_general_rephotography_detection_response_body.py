# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class GeneralRephotographyDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GeneralRephotographyDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The recapture detection result.
        self.data = data
        # The response message or failure description.
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
            temp_model = main_models.GeneralRephotographyDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GeneralRephotographyDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.GeneralRephotographyDetectionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The business result. This value is an empty object if the request fails.
        self.result = result
        # The usage information. The value is `{"ProcessingCount":1}` on success, or an empty object on failure.
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
            temp_model = main_models.GeneralRephotographyDetectionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class GeneralRephotographyDetectionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        grounding: main_models.GeneralRephotographyDetectionResponseBodyDataResultGrounding = None,
        is_fake: bool = None,
        type: str = None,
    ):
        # The supplementary element localization result.
        self.grounding = grounding
        # Indicates whether the image is a recaptured photo.
        self.is_fake = is_fake
        # The detection type. The value is fixed as general.
        self.type = type

    def validate(self):
        if self.grounding:
            self.grounding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grounding is not None:
            result['Grounding'] = self.grounding.to_map()

        if self.is_fake is not None:
            result['IsFake'] = self.is_fake

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grounding') is not None:
            temp_model = main_models.GeneralRephotographyDetectionResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        if m.get('IsFake') is not None:
            self.is_fake = m.get('IsFake')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GeneralRephotographyDetectionResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.GeneralRephotographyDetectionResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage of the localization. Valid values:
        # - complete: All relevant visible targets are fully covered.
        # - partial: Only some targets are valid or recognizable.
        self.coverage = coverage
        # The array of targets. A maximum of 12 items are returned. This value can be empty if no relevant targets exist.
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
                temp_model = main_models.GeneralRephotographyDetectionResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class GeneralRephotographyDetectionResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[float] = None,
        label: str = None,
        text: str = None,
    ):
        # The bounding box coordinates.
        self.bbox_2d = bbox_2d
        # The target category. For valid values, see the table below.
        self.label = label
        # The confirmed short name or text of up to 24 characters. This value is an empty string if the text is unreadable.
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


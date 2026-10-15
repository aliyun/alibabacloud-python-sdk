# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MilkPowderCartonCodeRephotographyDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The recapture detection result.
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
            temp_model = main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MilkPowderCartonCodeRephotographyDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The details of the recapture detection result.
        self.result = result
        # The usage information. The value is `{"ProcessingCount":1}` if the call is successful, or an empty object if the call fails.
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
            temp_model = main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        grounding: main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGrounding = None,
        is_fake: bool = None,
        is_suspect: bool = None,
        photo_status: int = None,
        score: float = None,
        type: str = None,
    ):
        # The supplementary element grounding results.
        self.grounding = grounding
        # Indicates whether the image is recaptured.
        self.is_fake = is_fake
        # Indicates whether the image is suspected to be recaptured.
        self.is_suspect = is_suspect
        # The recapture status. Valid values:
        # - `0`: Non-recapture.
        # - `1`: Recapture.
        # - `2`: Suspected recapture.
        self.photo_status = photo_status
        # The confidence score for recapture detection.
        self.score = score
        # The detection type. The value is fixed to `boxCode`.
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

        if self.is_suspect is not None:
            result['IsSuspect'] = self.is_suspect

        if self.photo_status is not None:
            result['PhotoStatus'] = self.photo_status

        if self.score is not None:
            result['Score'] = self.score

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grounding') is not None:
            temp_model = main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        if m.get('IsFake') is not None:
            self.is_fake = m.get('IsFake')

        if m.get('IsSuspect') is not None:
            self.is_suspect = m.get('IsSuspect')

        if m.get('PhotoStatus') is not None:
            self.photo_status = m.get('PhotoStatus')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage of the grounding. Valid values:
        # - `complete`: The relevant visible targets are complete.
        # - `partial`: Only some targets are valid or recognizable.
        self.coverage = coverage
        # The array of targets, which contains up to 12 items. This array can be empty if no relevant targets are found.
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
                temp_model = main_models.MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class MilkPowderCartonCodeRephotographyDetectionResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[float] = None,
        label: str = None,
        text: str = None,
    ):
        # The coordinates of the bounding box in the `[top-left x, top-left y, bottom-right x, bottom-right y]` format. The value range is 0 to 1000. The left value must be less than the right value, and the top value must be less than the bottom value.
        self.bbox_2d = bbox_2d
        # The category of the target. For enumerated values, see the following table.
        self.label = label
        # The confirmed short name or text, which contains up to 24 characters. This field is an empty string if the text is unclear.
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


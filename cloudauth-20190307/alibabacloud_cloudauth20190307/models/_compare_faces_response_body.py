# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class CompareFacesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CompareFacesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # HTTP status code.
        self.code = code
        # Result of the face comparison.
        self.data = data
        # Error code.
        self.message = message
        # ID of the current request.
        self.request_id = request_id
        # Indicates whether the response was successful.
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
            temp_model = main_models.CompareFacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CompareFacesResponseBodyData(DaraModel):
    def __init__(
        self,
        confidence_thresholds: str = None,
        similarity_score: float = None,
    ):
        # Confidence thresholds for face comparison. The returned content is a JSON Object, with the specific structure being `"key":"value"`.
        # 
        # - `key` represents the false acceptance rate, which is the probability of misidentifying someone else as the specified person.
        # - `value` is the corresponding threshold.
        # 
        # 
        # > Regarding the confidence thresholds (confidenceThresholds) in the example:
        # - `"0.0001": "90.07"` indicates that the threshold is 90.07 when the false acceptance rate is 0.01%.
        # - `"0.001": "80.01"` indicates that the threshold is 80.01 when the false acceptance rate is 0.1%.
        # - `"0.01": "70.02"` indicates that the threshold is 70.02 when the false acceptance rate is 1%.
        # 
        # Confidence thresholds are dynamically provided based on different images and algorithms, so do not persist these thresholds.
        self.confidence_thresholds = confidence_thresholds
        # The degree of similarity between the faces in the two images. The value range is [0, 100], with higher values indicating greater similarity.
        self.similarity_score = similarity_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds

        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')

        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')

        return self


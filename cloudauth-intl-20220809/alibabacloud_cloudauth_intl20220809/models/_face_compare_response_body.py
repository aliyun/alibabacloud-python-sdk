# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceCompareResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceCompareResponseBodyResult = None,
    ):
        # The [response code](https://www.alibabacloud.com/help/en/ekyc/latest/facecompare?spm=a3c0i.23458820.2359477120.28.21167d3fzUmXQC#c43fd16d07mae).
        self.code = code
        # The detailed description of the response code.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Result object
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.FaceCompareResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceCompareResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_face_info: main_models.FaceCompareResponseBodyResultExtFaceInfo = None,
        face_comparison_score: float = None,
        passed: str = None,
        transaction_id: str = None,
    ):
        self.ext_face_info = ext_face_info
        # The face comparison score. The value ranges from 0 to 100.
        self.face_comparison_score = face_comparison_score
        # The final authentication result. Valid values:
        # 
        # - **Y**: The authentication is passed.
        # 
        # - **N**: The authentication failed.
        self.passed = passed
        # The transaction ID.
        self.transaction_id = transaction_id

    def validate(self):
        if self.ext_face_info:
            self.ext_face_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info.to_map()

        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            temp_model = main_models.FaceCompareResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m.get('ExtFaceInfo'))

        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

class FaceCompareResponseBodyResultExtFaceInfo(DaraModel):
    def __init__(
        self,
        face_quality_score: float = None,
        illumination_score: float = None,
        ka_occlusion_score: float = None,
        occlusion_score: float = None,
        sharpness_score: float = None,
    ):
        self.face_quality_score = face_quality_score
        self.illumination_score = illumination_score
        self.ka_occlusion_score = ka_occlusion_score
        self.occlusion_score = occlusion_score
        self.sharpness_score = sharpness_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score

        if self.illumination_score is not None:
            result['IlluminationScore'] = self.illumination_score

        if self.ka_occlusion_score is not None:
            result['KaOcclusionScore'] = self.ka_occlusion_score

        if self.occlusion_score is not None:
            result['OcclusionScore'] = self.occlusion_score

        if self.sharpness_score is not None:
            result['SharpnessScore'] = self.sharpness_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')

        if m.get('IlluminationScore') is not None:
            self.illumination_score = m.get('IlluminationScore')

        if m.get('KaOcclusionScore') is not None:
            self.ka_occlusion_score = m.get('KaOcclusionScore')

        if m.get('OcclusionScore') is not None:
            self.occlusion_score = m.get('OcclusionScore')

        if m.get('SharpnessScore') is not None:
            self.sharpness_score = m.get('SharpnessScore')

        return self


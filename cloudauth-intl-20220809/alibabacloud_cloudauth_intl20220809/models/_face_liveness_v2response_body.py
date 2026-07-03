# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceLivenessV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceLivenessV2ResponseBodyResult = None,
    ):
        # The return code.
        self.code = code
        # The return message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The returned result.
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
            temp_model = main_models.FaceLivenessV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceLivenessV2ResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_face_info: main_models.FaceLivenessV2ResponseBodyResultExtFaceInfo = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # The face result information.
        self.ext_face_info = ext_face_info
        # Indicates whether the authentication is passed. Valid values:
        # 
        # - Y: passed.
        # - N: not passed.
        self.passed = passed
        # The sub-result code.
        self.sub_code = sub_code
        # The unique ID of the authentication request.
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

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            temp_model = main_models.FaceLivenessV2ResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m.get('ExtFaceInfo'))

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

class FaceLivenessV2ResponseBodyResultExtFaceInfo(DaraModel):
    def __init__(
        self,
        face_age: int = None,
        face_attack: str = None,
        face_attribute_info: str = None,
        face_gender: str = None,
        face_quality_score: float = None,
        illumination_score: float = None,
        ka_occlusion_score: float = None,
        occlusion_result: str = None,
        occlusion_score: float = None,
        sharpness_score: float = None,
    ):
        # The predicted reference age of the face. The prediction may fail and return no value.
        self.face_age = face_age
        # The liveness detection result. Valid values: Y (attack detected) and N (Normal).
        self.face_attack = face_attack
        self.face_attribute_info = face_attribute_info
        # The predicted gender of the face image. The prediction may fail and return no value. Valid values:
        # 
        # - M: male.
        # - F: female.
        self.face_gender = face_gender
        # The quality score of the liveness face. Valid values: 0 to 100. A higher value indicates better quality.
        self.face_quality_score = face_quality_score
        # The algorithm score for illumination as a quality sub-dimension. Valid values: 0 to 100. A higher value indicates better quality.
        self.illumination_score = illumination_score
        # The algorithm score for key area occlusion as a quality sub-dimension. Valid values: 0 to 100. A higher value indicates better quality.
        self.ka_occlusion_score = ka_occlusion_score
        # Indicates whether facial occlusion is detected. A value of Y indicates occlusion is detected. A value of N indicates no occlusion is detected.
        self.occlusion_result = occlusion_result
        # The algorithm score for occlusion as a quality sub-dimension. Valid values: 0 to 100. A higher value indicates better quality.
        self.occlusion_score = occlusion_score
        # The algorithm score for image sharpness as a quality sub-dimension. Valid values: 0 to 100. A higher value indicates better quality.
        self.sharpness_score = sharpness_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_age is not None:
            result['FaceAge'] = self.face_age

        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack

        if self.face_attribute_info is not None:
            result['FaceAttributeInfo'] = self.face_attribute_info

        if self.face_gender is not None:
            result['FaceGender'] = self.face_gender

        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score

        if self.illumination_score is not None:
            result['IlluminationScore'] = self.illumination_score

        if self.ka_occlusion_score is not None:
            result['KaOcclusionScore'] = self.ka_occlusion_score

        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result

        if self.occlusion_score is not None:
            result['OcclusionScore'] = self.occlusion_score

        if self.sharpness_score is not None:
            result['SharpnessScore'] = self.sharpness_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAge') is not None:
            self.face_age = m.get('FaceAge')

        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')

        if m.get('FaceAttributeInfo') is not None:
            self.face_attribute_info = m.get('FaceAttributeInfo')

        if m.get('FaceGender') is not None:
            self.face_gender = m.get('FaceGender')

        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')

        if m.get('IlluminationScore') is not None:
            self.illumination_score = m.get('IlluminationScore')

        if m.get('KaOcclusionScore') is not None:
            self.ka_occlusion_score = m.get('KaOcclusionScore')

        if m.get('OcclusionResult') is not None:
            self.occlusion_result = m.get('OcclusionResult')

        if m.get('OcclusionScore') is not None:
            self.occlusion_score = m.get('OcclusionScore')

        if m.get('SharpnessScore') is not None:
            self.sharpness_score = m.get('SharpnessScore')

        return self


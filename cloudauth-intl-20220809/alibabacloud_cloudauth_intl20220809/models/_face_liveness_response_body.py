# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceLivenessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceLivenessResponseBodyResult = None,
    ):
        # [The response code.](https://www.alibabacloud.com/help/en/ekyc/latest/cadqvlft48igbpdc?spm=a2c63.p38356.0.i54#3d0ed52f967g6)
        self.code = code
        # A detailed description of the response code.
        self.message = message
        # The request ID.
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
            temp_model = main_models.FaceLivenessResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceLivenessResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_face_info: main_models.FaceLivenessResponseBodyResultExtFaceInfo = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # The results of the passive liveness detection. The value is in the JSON format. For more information, see [ExtFaceInfo](https://www.alibabacloud.com/help/en/ekyc/latest/cadqvlft48igbpdc?spm=a2c63.p38356.0.i54#5ff42f7274agz).
        self.ext_face_info = ext_face_info
        # The authentication result. Valid values:
        # 
        # - Y: The authentication is passed.
        # 
        # - N: The authentication is not passed.
        self.passed = passed
        # The code that corresponds to the verification result. For more information, see [ResultObject.SubCode error codes](https://www.alibabacloud.com/help/en/ekyc/latest/cadqvlft48igbpdc?spm=a2c63.p38356.0.i54#5ff3e16174tl2).
        self.sub_code = sub_code
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
            temp_model = main_models.FaceLivenessResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m.get('ExtFaceInfo'))

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

class FaceLivenessResponseBodyResultExtFaceInfo(DaraModel):
    def __init__(
        self,
        face_age: int = None,
        face_attack: str = None,
        face_gender: str = None,
        face_quality_score: float = None,
        occlusion_result: str = None,
    ):
        # The predicted age of the person in the image. The prediction may fail, resulting in an empty value.
        self.face_age = face_age
        # Indicates whether a presentation attack was detected on the captured face. Y means an attack was detected. N means no attack was detected.
        self.face_attack = face_attack
        # The predicted gender of the person in the image. The prediction may fail, resulting in an empty value.
        # 
        # - **M**: Male
        # 
        # - **F**: Female
        self.face_gender = face_gender
        # Optional. The quality score of the live face. The value ranges from 0 to 100.
        self.face_quality_score = face_quality_score
        # Optional. Indicates whether the face is occluded. Y means the face is occluded. N means the face is not occluded.
        self.occlusion_result = occlusion_result

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

        if self.face_gender is not None:
            result['FaceGender'] = self.face_gender

        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score

        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAge') is not None:
            self.face_age = m.get('FaceAge')

        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')

        if m.get('FaceGender') is not None:
            self.face_gender = m.get('FaceGender')

        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')

        if m.get('OcclusionResult') is not None:
            self.occlusion_result = m.get('OcclusionResult')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceDuplicationCheckIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceDuplicationCheckIntlResponseBodyResult = None,
    ):
        # Return code.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Return result.
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
            temp_model = main_models.FaceDuplicationCheckIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceDuplicationCheckIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        duplicate_face: str = None,
        face_age: str = None,
        face_attack: str = None,
        face_attack_score: str = None,
        face_comparison_score: str = None,
        face_gender: str = None,
        face_passed: str = None,
        face_registration_id: str = None,
        face_registration_result: int = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # Returns the face library face ID and UserID when a duplicate face is detected.
        self.duplicate_face = duplicate_face
        # The estimated age of the face, which may not be returned if the prediction fails.
        self.face_age = face_age
        # Indicates whether the captured face involves a liveness attack, Y for an attack, N for no attack.
        # Returned when silent liveness detection is enabled.
        self.face_attack = face_attack
        # The probability of a liveness attack detected by silent liveness detection. The value range is 0 to 100.
        # Returned when silent liveness detection is enabled.
        self.face_attack_score = face_attack_score
        # When the verification mode is 1 or 2, returns the 1:1 verification comparison score
        # Comparison score range 0～100.
        self.face_comparison_score = face_comparison_score
        # The predicted gender of the face in the image, which may not be returned if the prediction fails.
        # - M: Male
        # - F: Female
        self.face_gender = face_gender
        # Final authentication result, values:
        # - Y: Passed
        # - N: Not passed
        self.face_passed = face_passed
        # Returns the corresponding FACEID only when the customer sets auto-registration and the face registration is successful.
        self.face_registration_id = face_registration_id
        # Face registration result 
        # - 0- Failed 
        # - 1- Succeeded
        self.face_registration_result = face_registration_result
        # Description of the authentication result. For more information, see ResultObject.SubCode error code description.
        self.sub_code = sub_code
        # Unique identifier of the authentication request.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duplicate_face is not None:
            result['DuplicateFace'] = self.duplicate_face

        if self.face_age is not None:
            result['FaceAge'] = self.face_age

        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack

        if self.face_attack_score is not None:
            result['FaceAttackScore'] = self.face_attack_score

        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score

        if self.face_gender is not None:
            result['FaceGender'] = self.face_gender

        if self.face_passed is not None:
            result['FacePassed'] = self.face_passed

        if self.face_registration_id is not None:
            result['FaceRegistrationId'] = self.face_registration_id

        if self.face_registration_result is not None:
            result['FaceRegistrationResult'] = self.face_registration_result

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DuplicateFace') is not None:
            self.duplicate_face = m.get('DuplicateFace')

        if m.get('FaceAge') is not None:
            self.face_age = m.get('FaceAge')

        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')

        if m.get('FaceAttackScore') is not None:
            self.face_attack_score = m.get('FaceAttackScore')

        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')

        if m.get('FaceGender') is not None:
            self.face_gender = m.get('FaceGender')

        if m.get('FacePassed') is not None:
            self.face_passed = m.get('FacePassed')

        if m.get('FaceRegistrationId') is not None:
            self.face_registration_id = m.get('FaceRegistrationId')

        if m.get('FaceRegistrationResult') is not None:
            self.face_registration_result = m.get('FaceRegistrationResult')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self


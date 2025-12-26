# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceCrossCompareIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceCrossCompareIntlResponseBodyResult = None,
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
            temp_model = main_models.FaceCrossCompareIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceCrossCompareIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        face_comparison_score_a2b: float = None,
        face_comparison_score_b2c: float = None,
        face_comparison_score_c2a: float = None,
        face_passed: str = None,
        transaction_id: str = None,
    ):
        # A to B comparison score, range 0～100.
        self.face_comparison_score_a2b = face_comparison_score_a2b
        # B to C comparison score, range 0～100.
        self.face_comparison_score_b2c = face_comparison_score_b2c
        # C to A comparison score, range 0～100.
        self.face_comparison_score_c2a = face_comparison_score_c2a
        # Final verification result, values:
        # - Y: Pass
        # - N: Fail
        self.face_passed = face_passed
        # Unique identifier for the authentication request.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_comparison_score_a2b is not None:
            result['FaceComparisonScoreA2B'] = self.face_comparison_score_a2b

        if self.face_comparison_score_b2c is not None:
            result['FaceComparisonScoreB2C'] = self.face_comparison_score_b2c

        if self.face_comparison_score_c2a is not None:
            result['FaceComparisonScoreC2A'] = self.face_comparison_score_c2a

        if self.face_passed is not None:
            result['FacePassed'] = self.face_passed

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceComparisonScoreA2B') is not None:
            self.face_comparison_score_a2b = m.get('FaceComparisonScoreA2B')

        if m.get('FaceComparisonScoreB2C') is not None:
            self.face_comparison_score_b2c = m.get('FaceComparisonScoreB2C')

        if m.get('FaceComparisonScoreC2A') is not None:
            self.face_comparison_score_c2a = m.get('FaceComparisonScoreC2A')

        if m.get('FacePassed') is not None:
            self.face_passed = m.get('FacePassed')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self


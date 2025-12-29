# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class AIGCFaceVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.AIGCFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.AIGCFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self



class AIGCFaceVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        result: str = None,
        score: str = None,
    ):
        # Unique real-person authentication identifier.
        self.certify_id = certify_id
        # Authentication result. Values:
        # 
        # ● Y: AIGC-generated face.
        # 
        # ● N: Not detected
        self.result = result
        # Detection score
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.result is not None:
            result['Result'] = self.result

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self


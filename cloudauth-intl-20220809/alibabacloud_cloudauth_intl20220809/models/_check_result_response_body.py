# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class CheckResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CheckResultResponseBodyResult = None,
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
            temp_model = main_models.CheckResultResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CheckResultResponseBodyResult(DaraModel):
    def __init__(
        self,
        ekyc_result: str = None,
        ext_basic_info: str = None,
        ext_face_info: str = None,
        ext_id_info: str = None,
        ext_info: str = None,
        ext_risk_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        # Authentication result.
        self.ekyc_result = ekyc_result
        # Extended basic information.
        self.ext_basic_info = ext_basic_info
        # Face information.
        self.ext_face_info = ext_face_info
        # ID information.
        self.ext_id_info = ext_id_info
        # Extended information
        self.ext_info = ext_info
        # Risk information.
        self.ext_risk_info = ext_risk_info
        # Whether the authentication is passed.
        # 
        # - Y: Passed
        # - N: Not passed
        self.passed = passed
        # Sub-result code.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ekyc_result is not None:
            result['EkycResult'] = self.ekyc_result

        if self.ext_basic_info is not None:
            result['ExtBasicInfo'] = self.ext_basic_info

        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info

        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.ext_risk_info is not None:
            result['ExtRiskInfo'] = self.ext_risk_info

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EkycResult') is not None:
            self.ekyc_result = m.get('EkycResult')

        if m.get('ExtBasicInfo') is not None:
            self.ext_basic_info = m.get('ExtBasicInfo')

        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')

        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('ExtRiskInfo') is not None:
            self.ext_risk_info = m.get('ExtRiskInfo')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self


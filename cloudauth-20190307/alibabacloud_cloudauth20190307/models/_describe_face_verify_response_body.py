# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeFaceVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, other values indicate failure.
        self.code = code
        # Error message
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information
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
            temp_model = main_models.DescribeFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeFaceVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        device_risk: str = None,
        device_token: str = None,
        identity_info: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
        success: str = None,
        user_info: str = None,
    ):
        # Device risk label.
        self.device_risk = device_risk
        # Device token.
        self.device_token = device_token
        # Information about the authenticated subject, usually empty in general authentication scenarios.
        self.identity_info = identity_info
        # Attachment information of the authenticated subject, mainly image materials. JSON format, see example below.
        self.material_info = material_info
        # Whether it passed, T for pass, F for fail.
        self.passed = passed
        # Description of the authentication result. For details, see the SubCode explanation below.
        self.sub_code = sub_code
        # Whether the response was successful.
        self.success = success
        # Records the identity information and corresponding encoding entered by the user under the rare character mode. The returned data is a JSON formatted string, which will be an empty string if there are no rare characters in the name.
        # 
        # - name: Refers to the name entered by the user.
        # 
        # - verifyName: Refers to the final name encoding after verification. For example, if a rare character is verified through transcoding: “Mr. Wang”, the actual verified name is “Wang Xiansheng”.
        # 
        # - number: Refers to the identification number entered by the user.
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_risk is not None:
            result['DeviceRisk'] = self.device_risk

        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info

        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.success is not None:
            result['Success'] = self.success

        if self.user_info is not None:
            result['UserInfo'] = self.user_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceRisk') is not None:
            self.device_risk = m.get('DeviceRisk')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')

        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class EcologyOpennessAuthenticateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EcologyOpennessAuthenticateResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Response Result
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

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
            temp_model = main_models.EcologyOpennessAuthenticateResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EcologyOpennessAuthenticateResponseBodyResult(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
        user_open_id: str = None,
    ):
        # entity key
        self.encode_key = encode_key
        # entity Type
        self.encode_type = encode_type
        # scenario code
        self.scene_code = scene_code
        # Third-party user identifier
        self.third_user_identifier = third_user_identifier
        # Third-party user type
        self.third_user_type = third_user_type
        # Tmall Genie user openId
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier

        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type

        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')

        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')

        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        return self


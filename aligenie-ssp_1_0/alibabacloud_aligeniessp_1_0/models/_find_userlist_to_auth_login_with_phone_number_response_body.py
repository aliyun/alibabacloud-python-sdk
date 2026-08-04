# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class FindUserlistToAuthLoginWithPhoneNumberResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data_obj: main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # When the code is 5140003, it indicates that the invocation failed because no account list eligible for authorization login was found for the given phone number. The frontend can prompt the user to confirm generating a Jingle account via the phone number or suggest registering a Taobao account using the phone number first. In subsequent flows, the frontend must return the sessionId from DataObj to the server.
        self.data_obj = data_obj
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Response Result
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.data_obj:
            self.data_obj.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_obj is not None:
            result['DataObj'] = self.data_obj.to_map()

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

        if m.get('DataObj') is not None:
            temp_model = main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj()
            self.data_obj = temp_model.from_map(m.get('DataObj'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult(DaraModel):
    def __init__(
        self,
        user_list_to_auth_login: List[main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin] = None,
    ):
        # List of accounts eligible for authorization login
        self.user_list_to_auth_login = user_list_to_auth_login

    def validate(self):
        if self.user_list_to_auth_login:
            for v1 in self.user_list_to_auth_login:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserListToAuthLogin'] = []
        if self.user_list_to_auth_login is not None:
            for k1 in self.user_list_to_auth_login:
                result['UserListToAuthLogin'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list_to_auth_login = []
        if m.get('UserListToAuthLogin') is not None:
            for k1 in m.get('UserListToAuthLogin'):
                temp_model = main_models.FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin()
                self.user_list_to_auth_login.append(temp_model.from_map(k1))

        return self

class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        encrypted_user_identifier: str = None,
        finding_type: str = None,
        nickname: str = None,
        user_type: str = None,
    ):
        # Profile picture
        self.avatar = avatar
        # Encrypted User Identifier
        self.encrypted_user_identifier = encrypted_user_identifier
        # User Search Type  
        # 
        # For Taobao users, the value is fixed as:  
        # PHONE_NUMBER_BINDING_WITH_TAOBAO: The phoneNumber is queried as the phone number bound to a Taobao account.  
        # 
        # For Tmall Genie users, the value can be:  
        # PHONE_NUMBER_BINDING_WITH_ALIGENIE: The phoneNumber is queried as the phone number bound to a Tmall Genie device;  
        # PHONE_NUMBER_BINDING_WITH_TAOBAO: The phoneNumber is queried as the phone number bound to a Taobao account.
        self.finding_type = finding_type
        # Nickname
        self.nickname = nickname
        # User Type  
        # TAOBAO: Taobao user  
        # ALIGENIE: Tmall Genie user
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.encrypted_user_identifier is not None:
            result['EncryptedUserIdentifier'] = self.encrypted_user_identifier

        if self.finding_type is not None:
            result['FindingType'] = self.finding_type

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('EncryptedUserIdentifier') is not None:
            self.encrypted_user_identifier = m.get('EncryptedUserIdentifier')

        if m.get('FindingType') is not None:
            self.finding_type = m.get('FindingType')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

class FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj(DaraModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # Session ID
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self


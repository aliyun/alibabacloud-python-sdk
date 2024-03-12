# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class GetPhoneNumberIdentificationResultRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_id: str = None,
        session_payload: str = None,
    ):
        # The authorization code.
        self.auth_code = auth_code
        # The external ID.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number of the subscriber. The phone number to be verified must be in the Mobile Station International Subscriber Directory Number (MSISDN) format.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The session ID.
        self.session_id = session_id
        # The session payload.
        self.session_payload = session_payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_payload is not None:
            result['SessionPayload'] = self.session_payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionPayload') is not None:
            self.session_payload = m.get('SessionPayload')
        return self


class GetPhoneNumberIdentificationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        is_identified: str = None,
    ):
        # Indicates whether the phone number passed the verification.
        self.is_identified = is_identified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_identified is not None:
            result['IsIdentified'] = self.is_identified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsIdentified') is not None:
            self.is_identified = m.get('IsIdentified')
        return self


class GetPhoneNumberIdentificationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhoneNumberIdentificationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The return code. Valid values:
        # 
        # *   OK: The request is successful.
        # *   NoIdentificationResult: No verification result is available or the verification failed.
        # *   SessionNotValid: The session is invalid or expired.
        # *   MobileNumberIllegal: The format of the phone number is invalid.
        self.code = code
        # The returned data.
        self.data = data
        # The description of the return code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberIdentificationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberIdentificationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneNumberIdentificationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneNumberIdentificationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberIdentificationUrlRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        ip: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        remember_phone_number: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code.
        self.auth_code = auth_code
        # The IP address of the subscriber\"s phone.
        self.ip = ip
        # The external ID.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number of the subscriber. The phone number is in the Mobile Station International Subscriber Directory Number (MSISDN) format.
        self.phone_number = phone_number
        # Specifies whether to remember the phone number.
        self.remember_phone_number = remember_phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.remember_phone_number is not None:
            result['RememberPhoneNumber'] = self.remember_phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RememberPhoneNumber') is not None:
            self.remember_phone_number = m.get('RememberPhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPhoneNumberIdentificationUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        identification_url: str = None,
        session_id: str = None,
    ):
        # The verification URL.
        self.identification_url = identification_url
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification_url is not None:
            result['IdentificationUrl'] = self.identification_url
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentificationUrl') is not None:
            self.identification_url = m.get('IdentificationUrl')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetPhoneNumberIdentificationUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhoneNumberIdentificationUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The return code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **IdentificationNotAvailable**: The verification system does not support the phone number that corresponds to the IP address.
        # *   **MobileNumberIllegal**: The format of the phone number is invalid.
        self.code = code
        # The returned data.
        self.data = data
        # The description of the return code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberIdentificationUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberIdentificationUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneNumberIdentificationUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneNumberIdentificationUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



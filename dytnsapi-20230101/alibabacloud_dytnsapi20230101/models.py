# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class DescribeNumberHLRRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.owner_id = owner_id
        self.phone_number = phone_number
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeNumberHLRResponseBodyDataCall(TeaModel):
    def __init__(
        self,
        cleansed_code: str = None,
        max_length: int = None,
        min_length: int = None,
    ):
        # call
        self.cleansed_code = cleansed_code
        self.max_length = max_length
        self.min_length = min_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cleansed_code is not None:
            result['CleansedCode'] = self.cleansed_code
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleansedCode') is not None:
            self.cleansed_code = m.get('CleansedCode')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        return self


class DescribeNumberHLRResponseBodyDataLive(TeaModel):
    def __init__(
        self,
        device_status: str = None,
        roaming: str = None,
        roaming_country: str = None,
        subscriber_status: str = None,
    ):
        self.device_status = device_status
        self.roaming = roaming
        self.roaming_country = roaming_country
        self.subscriber_status = subscriber_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.roaming is not None:
            result['Roaming'] = self.roaming
        if self.roaming_country is not None:
            result['RoamingCountry'] = self.roaming_country
        if self.subscriber_status is not None:
            result['SubscriberStatus'] = self.subscriber_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Roaming') is not None:
            self.roaming = m.get('Roaming')
        if m.get('RoamingCountry') is not None:
            self.roaming_country = m.get('RoamingCountry')
        if m.get('SubscriberStatus') is not None:
            self.subscriber_status = m.get('SubscriberStatus')
        return self


class DescribeNumberHLRResponseBodyDataSms(TeaModel):
    def __init__(
        self,
        cleansed_code: int = None,
        max_length: int = None,
        min_length: int = None,
    ):
        # sms
        self.cleansed_code = cleansed_code
        self.max_length = max_length
        self.min_length = min_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cleansed_code is not None:
            result['CleansedCode'] = self.cleansed_code
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleansedCode') is not None:
            self.cleansed_code = m.get('CleansedCode')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        return self


class DescribeNumberHLRResponseBodyData(TeaModel):
    def __init__(
        self,
        blocked: str = None,
        call: DescribeNumberHLRResponseBodyDataCall = None,
        carrier: str = None,
        city: str = None,
        country_iso_3: str = None,
        live: DescribeNumberHLRResponseBodyDataLive = None,
        phone_type: str = None,
        sms: DescribeNumberHLRResponseBodyDataSms = None,
    ):
        self.blocked = blocked
        self.call = call
        self.carrier = carrier
        self.city = city
        self.country_iso_3 = country_iso_3
        self.live = live
        self.phone_type = phone_type
        self.sms = sms

    def validate(self):
        if self.call:
            self.call.validate()
        if self.live:
            self.live.validate()
        if self.sms:
            self.sms.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blocked is not None:
            result['Blocked'] = self.blocked
        if self.call is not None:
            result['Call'] = self.call.to_map()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.city is not None:
            result['City'] = self.city
        if self.country_iso_3 is not None:
            result['CountryIso3'] = self.country_iso_3
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type
        if self.sms is not None:
            result['Sms'] = self.sms.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blocked') is not None:
            self.blocked = m.get('Blocked')
        if m.get('Call') is not None:
            temp_model = DescribeNumberHLRResponseBodyDataCall()
            self.call = temp_model.from_map(m['Call'])
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CountryIso3') is not None:
            self.country_iso_3 = m.get('CountryIso3')
        if m.get('Live') is not None:
            temp_model = DescribeNumberHLRResponseBodyDataLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')
        if m.get('Sms') is not None:
            temp_model = DescribeNumberHLRResponseBodyDataSms()
            self.sms = temp_model.from_map(m['Sms'])
        return self


class DescribeNumberHLRResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: DescribeNumberHLRResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNumberHLRResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNumberHLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNumberHLRResponseBody = None,
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
            temp_model = DescribeNumberHLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNumberMccMncRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.owner_id = owner_id
        self.phone_number = phone_number
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeNumberMccMncResponseBodyData(TeaModel):
    def __init__(
        self,
        country_iso_3: str = None,
        mcc: str = None,
        mnc: str = None,
        ported: bool = None,
    ):
        self.country_iso_3 = country_iso_3
        self.mcc = mcc
        self.mnc = mnc
        self.ported = ported

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_iso_3 is not None:
            result['CountryIso3'] = self.country_iso_3
        if self.mcc is not None:
            result['Mcc'] = self.mcc
        if self.mnc is not None:
            result['Mnc'] = self.mnc
        if self.ported is not None:
            result['Ported'] = self.ported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryIso3') is not None:
            self.country_iso_3 = m.get('CountryIso3')
        if m.get('Mcc') is not None:
            self.mcc = m.get('Mcc')
        if m.get('Mnc') is not None:
            self.mnc = m.get('Mnc')
        if m.get('Ported') is not None:
            self.ported = m.get('Ported')
        return self


class DescribeNumberMccMncResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: DescribeNumberMccMncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNumberMccMncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNumberMccMncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNumberMccMncResponseBody = None,
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
            temp_model = DescribeNumberMccMncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The external ID.
        # 
        # This parameter is required.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number of the subscriber. The phone number to be verified must be in the Mobile Station International Subscriber Directory Number (MSISDN) format.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The session payload.
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The IP address of the subscriber\\"s phone.
        self.ip = ip
        # The external ID.
        # 
        # This parameter is required.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number of the subscriber. The phone number is in the Mobile Station International Subscriber Directory Number (MSISDN) format.
        # 
        # This parameter is required.
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



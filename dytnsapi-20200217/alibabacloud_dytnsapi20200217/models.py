# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class DescribePhoneNumberStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class DescribePhoneNumberStatusResponseBodyPhoneStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        serial_id: str = None,
        carrier: str = None,
    ):
        self.status = status
        self.serial_id = serial_id
        self.carrier = carrier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.serial_id is not None:
            result['SerialId'] = self.serial_id
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SerialId') is not None:
            self.serial_id = m.get('SerialId')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        return self


class DescribePhoneNumberStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        phone_status: DescribePhoneNumberStatusResponseBodyPhoneStatus = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.phone_status = phone_status

    def validate(self):
        if self.phone_status:
            self.phone_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.phone_status is not None:
            result['PhoneStatus'] = self.phone_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhoneStatus') is not None:
            temp_model = DescribePhoneNumberStatusResponseBodyPhoneStatus()
            self.phone_status = temp_model.from_map(m['PhoneStatus'])
        return self


class DescribePhoneNumberStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePhoneNumberStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePhoneNumberStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute(TeaModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        is_number_portability: bool = None,
        number_segment: int = None,
        city: str = None,
        province: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.is_number_portability = is_number_portability
        self.number_segment = number_segment
        self.city = city
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.is_number_portability is not None:
            result['IsNumberPortability'] = self.is_number_portability
        if self.number_segment is not None:
            result['NumberSegment'] = self.number_segment
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('IsNumberPortability') is not None:
            self.is_number_portability = m.get('IsNumberPortability')
        if m.get('NumberSegment') is not None:
            self.number_segment = m.get('NumberSegment')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribePhoneNumberAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        phone_number_attribute: DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.phone_number_attribute = phone_number_attribute

    def validate(self):
        if self.phone_number_attribute:
            self.phone_number_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.phone_number_attribute is not None:
            result['PhoneNumberAttribute'] = self.phone_number_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhoneNumberAttribute') is not None:
            temp_model = DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute()
            self.phone_number_attribute = temp_model.from_map(m['PhoneNumberAttribute'])
        return self


class DescribePhoneNumberAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePhoneNumberAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePhoneNumberAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberResaleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number: str = None,
        since: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number = phone_number
        self.since = since

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.since is not None:
            result['Since'] = self.since
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Since') is not None:
            self.since = m.get('Since')
        return self


class DescribePhoneNumberResaleResponseBodyTwiceTelVerify(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        verify_result: int = None,
    ):
        self.carrier = carrier
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class DescribePhoneNumberResaleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        twice_tel_verify: DescribePhoneNumberResaleResponseBodyTwiceTelVerify = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.twice_tel_verify = twice_tel_verify

    def validate(self):
        if self.twice_tel_verify:
            self.twice_tel_verify.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.twice_tel_verify is not None:
            result['TwiceTelVerify'] = self.twice_tel_verify.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TwiceTelVerify') is not None:
            temp_model = DescribePhoneNumberResaleResponseBodyTwiceTelVerify()
            self.twice_tel_verify = temp_model.from_map(m['TwiceTelVerify'])
        return self


class DescribePhoneNumberResaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePhoneNumberResaleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePhoneNumberResaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



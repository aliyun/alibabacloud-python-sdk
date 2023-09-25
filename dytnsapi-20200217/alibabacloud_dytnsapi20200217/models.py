# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CompanyFourElementsVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        legal_person_cert_name: str = None,
        legal_person_cert_no: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.ep_cert_name = ep_cert_name
        self.ep_cert_no = ep_cert_no
        self.legal_person_cert_name = legal_person_cert_name
        self.legal_person_cert_no = legal_person_cert_no
        self.owner_id = owner_id
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
        if self.ep_cert_name is not None:
            result['EpCertName'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['EpCertNo'] = self.ep_cert_no
        if self.legal_person_cert_name is not None:
            result['LegalPersonCertName'] = self.legal_person_cert_name
        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EpCertName') is not None:
            self.ep_cert_name = m.get('EpCertName')
        if m.get('EpCertNo') is not None:
            self.ep_cert_no = m.get('EpCertNo')
        if m.get('LegalPersonCertName') is not None:
            self.legal_person_cert_name = m.get('LegalPersonCertName')
        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CompanyFourElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: Dict[str, Any] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        self.detail_info = detail_info
        self.reason_code = reason_code
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class CompanyFourElementsVerificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CompanyFourElementsVerificationResponseBodyData = None,
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
            temp_model = CompanyFourElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompanyFourElementsVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompanyFourElementsVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CompanyFourElementsVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompanyThreeElementsVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        legal_person_cert_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.ep_cert_name = ep_cert_name
        self.ep_cert_no = ep_cert_no
        self.legal_person_cert_name = legal_person_cert_name
        self.owner_id = owner_id
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
        if self.ep_cert_name is not None:
            result['EpCertName'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['EpCertNo'] = self.ep_cert_no
        if self.legal_person_cert_name is not None:
            result['LegalPersonCertName'] = self.legal_person_cert_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EpCertName') is not None:
            self.ep_cert_name = m.get('EpCertName')
        if m.get('EpCertNo') is not None:
            self.ep_cert_no = m.get('EpCertNo')
        if m.get('LegalPersonCertName') is not None:
            self.legal_person_cert_name = m.get('LegalPersonCertName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CompanyThreeElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: Dict[str, Any] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        self.detail_info = detail_info
        self.reason_code = reason_code
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class CompanyThreeElementsVerificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CompanyThreeElementsVerificationResponseBodyData = None,
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
            temp_model = CompanyThreeElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompanyThreeElementsVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompanyThreeElementsVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CompanyThreeElementsVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompanyTwoElementsVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.ep_cert_name = ep_cert_name
        self.ep_cert_no = ep_cert_no
        self.owner_id = owner_id
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
        if self.ep_cert_name is not None:
            result['EpCertName'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['EpCertNo'] = self.ep_cert_no
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EpCertName') is not None:
            self.ep_cert_name = m.get('EpCertName')
        if m.get('EpCertNo') is not None:
            self.ep_cert_no = m.get('EpCertNo')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CompanyTwoElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: Dict[str, Any] = None,
        reason_code: str = None,
        verify_result: str = None,
    ):
        self.detail_info = detail_info
        self.reason_code = reason_code
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class CompanyTwoElementsVerificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CompanyTwoElementsVerificationResponseBodyData = None,
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
            temp_model = CompanyTwoElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompanyTwoElementsVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompanyTwoElementsVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CompanyTwoElementsVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEmptyNumberRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeEmptyNumberResponseBodyData(TeaModel):
    def __init__(
        self,
        number: str = None,
        status: str = None,
    ):
        self.number = number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEmptyNumberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeEmptyNumberResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribeEmptyNumberResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEmptyNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEmptyNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeEmptyNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberAnalysisRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        number_type: int = None,
        owner_id: int = None,
        rate: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.number_type = number_type
        self.owner_id = owner_id
        self.rate = rate
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.number_type is not None:
            result['NumberType'] = self.number_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('NumberType') is not None:
            self.number_type = m.get('NumberType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePhoneNumberAnalysisResponseBodyDataList(TeaModel):
    def __init__(
        self,
        code: str = None,
        number: str = None,
    ):
        self.code = code
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DescribePhoneNumberAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[DescribePhoneNumberAnalysisResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribePhoneNumberAnalysisResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribePhoneNumberAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePhoneNumberAnalysisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribePhoneNumberAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneNumberAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneNumberAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneNumberAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberAnalysisAIRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        model_config: str = None,
        owner_id: int = None,
        rate: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.model_config = model_config
        self.owner_id = owner_id
        self.rate = rate
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('ModelConfig') is not None:
            self.model_config = m.get('ModelConfig')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePhoneNumberAnalysisAIResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        number: str = None,
    ):
        self.code = code
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DescribePhoneNumberAnalysisAIResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePhoneNumberAnalysisAIResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribePhoneNumberAnalysisAIResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneNumberAnalysisAIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneNumberAnalysisAIResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneNumberAnalysisAIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
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
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute(TeaModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        is_number_portability: bool = None,
        number_segment: int = None,
        province: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.city = city
        self.is_number_portability = is_number_portability
        self.number_segment = number_segment
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
        if self.city is not None:
            result['City'] = self.city
        if self.is_number_portability is not None:
            result['IsNumberPortability'] = self.is_number_portability
        if self.number_segment is not None:
            result['NumberSegment'] = self.number_segment
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsNumberPortability') is not None:
            self.is_number_portability = m.get('IsNumberPortability')
        if m.get('NumberSegment') is not None:
            self.number_segment = m.get('NumberSegment')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribePhoneNumberAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        phone_number_attribute: DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.phone_number_attribute = phone_number_attribute
        self.request_id = request_id

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
        if self.phone_number_attribute is not None:
            result['PhoneNumberAttribute'] = self.phone_number_attribute.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhoneNumberAttribute') is not None:
            temp_model = DescribePhoneNumberAttributeResponseBodyPhoneNumberAttribute()
            self.phone_number_attribute = temp_model.from_map(m['PhoneNumberAttribute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneNumberAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneNumberAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneNumberAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberOnlineTimeRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.carrier = carrier
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePhoneNumberOnlineTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier_code: str = None,
        verify_result: str = None,
    ):
        self.carrier_code = carrier_code
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier_code is not None:
            result['CarrierCode'] = self.carrier_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CarrierCode') is not None:
            self.carrier_code = m.get('CarrierCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class DescribePhoneNumberOnlineTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePhoneNumberOnlineTimeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribePhoneNumberOnlineTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneNumberOnlineTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneNumberOnlineTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneNumberOnlineTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneNumberOperatorAttributeRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePhoneNumberOperatorAttributeResponseBodyData(TeaModel):
    def __init__(
        self,
        basic_carrier: str = None,
        carrier: str = None,
        city: str = None,
        is_number_portability: bool = None,
        number_segment: int = None,
        province: str = None,
    ):
        self.basic_carrier = basic_carrier
        self.carrier = carrier
        self.city = city
        self.is_number_portability = is_number_portability
        self.number_segment = number_segment
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
        if self.city is not None:
            result['City'] = self.city
        if self.is_number_portability is not None:
            result['IsNumberPortability'] = self.is_number_portability
        if self.number_segment is not None:
            result['NumberSegment'] = self.number_segment
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsNumberPortability') is not None:
            self.is_number_portability = m.get('IsNumberPortability')
        if m.get('NumberSegment') is not None:
            self.number_segment = m.get('NumberSegment')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribePhoneNumberOperatorAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePhoneNumberOperatorAttributeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribePhoneNumberOperatorAttributeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneNumberOperatorAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneNumberOperatorAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneNumberOperatorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneTwiceTelVerifyRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePhoneTwiceTelVerifyResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        verify_result: str = None,
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


class DescribePhoneTwiceTelVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribePhoneTwiceTelVerifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = DescribePhoneTwiceTelVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePhoneTwiceTelVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePhoneTwiceTelVerifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribePhoneTwiceTelVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvalidPhoneNumberFilterRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class InvalidPhoneNumberFilterResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        encrypted_number: str = None,
        expire_time: str = None,
        original_number: str = None,
    ):
        self.code = code
        self.encrypted_number = encrypted_number
        self.expire_time = expire_time
        self.original_number = original_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.encrypted_number is not None:
            result['EncryptedNumber'] = self.encrypted_number
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.original_number is not None:
            result['OriginalNumber'] = self.original_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EncryptedNumber') is not None:
            self.encrypted_number = m.get('EncryptedNumber')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OriginalNumber') is not None:
            self.original_number = m.get('OriginalNumber')
        return self


class InvalidPhoneNumberFilterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[InvalidPhoneNumberFilterResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = InvalidPhoneNumberFilterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InvalidPhoneNumberFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvalidPhoneNumberFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = InvalidPhoneNumberFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberConvertServiceRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberConvertServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        conver_result: bool = None,
        number: str = None,
        number_md_5: str = None,
        number_sha_256: str = None,
    ):
        self.conver_result = conver_result
        self.number = number
        self.number_md_5 = number_md_5
        self.number_sha_256 = number_sha_256

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conver_result is not None:
            result['ConverResult'] = self.conver_result
        if self.number is not None:
            result['Number'] = self.number
        if self.number_md_5 is not None:
            result['NumberMd5'] = self.number_md_5
        if self.number_sha_256 is not None:
            result['NumberSha256'] = self.number_sha_256
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConverResult') is not None:
            self.conver_result = m.get('ConverResult')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberMd5') is not None:
            self.number_md_5 = m.get('NumberMd5')
        if m.get('NumberSha256') is not None:
            self.number_sha_256 = m.get('NumberSha256')
        return self


class PhoneNumberConvertServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[PhoneNumberConvertServiceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PhoneNumberConvertServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberConvertServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberConvertServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberConvertServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberEncryptRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberEncryptResponseBodyData(TeaModel):
    def __init__(
        self,
        encrypted_number: str = None,
        expire_time: str = None,
        original_number: str = None,
    ):
        self.encrypted_number = encrypted_number
        self.expire_time = expire_time
        self.original_number = original_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_number is not None:
            result['EncryptedNumber'] = self.encrypted_number
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.original_number is not None:
            result['OriginalNumber'] = self.original_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedNumber') is not None:
            self.encrypted_number = m.get('EncryptedNumber')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OriginalNumber') is not None:
            self.original_number = m.get('OriginalNumber')
        return self


class PhoneNumberEncryptResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[PhoneNumberEncryptResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PhoneNumberEncryptResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberEncryptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberEncryptResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForAccountRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        self.carrier = carrier
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PhoneNumberStatusForAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForAccountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForPublicRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForPublicResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        self.carrier = carrier
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PhoneNumberStatusForPublicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForPublicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForPublicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForPublicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForPublicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForPublicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForRealRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForRealResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        self.carrier = carrier
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PhoneNumberStatusForRealResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForRealResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForRealResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForRealResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForRealResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForRealResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForSmsRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForSmsResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        self.carrier = carrier
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PhoneNumberStatusForSmsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForSmsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForSmsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForSmsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForVirtualRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForVirtualResponseBodyData(TeaModel):
    def __init__(
        self,
        is_privacy_number: bool = None,
    ):
        self.is_privacy_number = is_privacy_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_privacy_number is not None:
            result['IsPrivacyNumber'] = self.is_privacy_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPrivacyNumber') is not None:
            self.is_privacy_number = m.get('IsPrivacyNumber')
        return self


class PhoneNumberStatusForVirtualResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForVirtualResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForVirtualResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForVirtualResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForVirtualResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForVirtualResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PhoneNumberStatusForVoiceRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PhoneNumberStatusForVoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        self.carrier = carrier
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PhoneNumberStatusForVoiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PhoneNumberStatusForVoiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = PhoneNumberStatusForVoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PhoneNumberStatusForVoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PhoneNumberStatusForVoiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PhoneNumberStatusForVoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvailableAuthCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 标签id
        self.tag_id = tag_id

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
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class QueryAvailableAuthCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvailableAuthCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAvailableAuthCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryAvailableAuthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagApplyRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 标签id
        self.tag_id = tag_id

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
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class QueryTagApplyRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        apply_material_desc: str = None,
        auto_audit: int = None,
        charging_standard_link: str = None,
        encrypted_query: int = None,
        need_apply_material: int = None,
        sla_link: str = None,
    ):
        # 申请材料要求
        self.apply_material_desc = apply_material_desc
        # 是否自动审批
        self.auto_audit = auto_audit
        # 计费标准说明链接
        self.charging_standard_link = charging_standard_link
        # 是否支持加密查询
        self.encrypted_query = encrypted_query
        # 是否需要提供申请材料
        self.need_apply_material = need_apply_material
        # 服务协议链接
        self.sla_link = sla_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_material_desc is not None:
            result['ApplyMaterialDesc'] = self.apply_material_desc
        if self.auto_audit is not None:
            result['AutoAudit'] = self.auto_audit
        if self.charging_standard_link is not None:
            result['ChargingStandardLink'] = self.charging_standard_link
        if self.encrypted_query is not None:
            result['EncryptedQuery'] = self.encrypted_query
        if self.need_apply_material is not None:
            result['NeedApplyMaterial'] = self.need_apply_material
        if self.sla_link is not None:
            result['SlaLink'] = self.sla_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyMaterialDesc') is not None:
            self.apply_material_desc = m.get('ApplyMaterialDesc')
        if m.get('AutoAudit') is not None:
            self.auto_audit = m.get('AutoAudit')
        if m.get('ChargingStandardLink') is not None:
            self.charging_standard_link = m.get('ChargingStandardLink')
        if m.get('EncryptedQuery') is not None:
            self.encrypted_query = m.get('EncryptedQuery')
        if m.get('NeedApplyMaterial') is not None:
            self.need_apply_material = m.get('NeedApplyMaterial')
        if m.get('SlaLink') is not None:
            self.sla_link = m.get('SlaLink')
        return self


class QueryTagApplyRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTagApplyRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryTagApplyRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTagApplyRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagApplyRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryTagApplyRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagInfoBySelectionRequest(TeaModel):
    def __init__(
        self,
        industry_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_id: int = None,
        tag_id: int = None,
    ):
        # 行业id
        self.industry_id = industry_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 场景id
        self.scene_id = scene_id
        # 标签id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class QueryTagInfoBySelectionResponseBodyDataParamListValueDict(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
    ):
        # 英文名
        self.code = code
        # 中文名
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class QueryTagInfoBySelectionResponseBodyDataParamList(TeaModel):
    def __init__(
        self,
        code: str = None,
        hint: str = None,
        must: bool = None,
        name: str = None,
        type: str = None,
        value_dict: List[QueryTagInfoBySelectionResponseBodyDataParamListValueDict] = None,
    ):
        # 参数英文名
        self.code = code
        # 输入提示
        self.hint = hint
        # 是否必填
        self.must = must
        # 参数中文名
        self.name = name
        # 类型EnumUIWidgetTypes对应的code
        self.type = type
        # 枚举值定义，code:desc
        self.value_dict = value_dict

    def validate(self):
        if self.value_dict:
            for k in self.value_dict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.hint is not None:
            result['Hint'] = self.hint
        if self.must is not None:
            result['Must'] = self.must
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        result['ValueDict'] = []
        if self.value_dict is not None:
            for k in self.value_dict:
                result['ValueDict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Hint') is not None:
            self.hint = m.get('Hint')
        if m.get('Must') is not None:
            self.must = m.get('Must')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.value_dict = []
        if m.get('ValueDict') is not None:
            for k in m.get('ValueDict'):
                temp_model = QueryTagInfoBySelectionResponseBodyDataParamListValueDict()
                self.value_dict.append(temp_model.from_map(k))
        return self


class QueryTagInfoBySelectionResponseBodyData(TeaModel):
    def __init__(
        self,
        auth_code_list: List[str] = None,
        demo_address: str = None,
        doc_address: str = None,
        enum_definition_address: str = None,
        flow_name: str = None,
        industry_id: int = None,
        industry_name: str = None,
        param_list: List[QueryTagInfoBySelectionResponseBodyDataParamList] = None,
        scene_id: int = None,
        scene_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        # 可用的授权码列表
        self.auth_code_list = auth_code_list
        # API demo链接
        self.demo_address = demo_address
        # API文档链接
        self.doc_address = doc_address
        # 枚举值定义链接
        self.enum_definition_address = enum_definition_address
        # 流程名称
        self.flow_name = flow_name
        # 行业id
        self.industry_id = industry_id
        # 行业名称
        self.industry_name = industry_name
        # 标签参数列表
        self.param_list = param_list
        # 场景id
        self.scene_id = scene_id
        # 场景名称
        self.scene_name = scene_name
        # 标签id
        self.tag_id = tag_id
        # 标签名称
        self.tag_name = tag_name

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code_list is not None:
            result['AuthCodeList'] = self.auth_code_list
        if self.demo_address is not None:
            result['DemoAddress'] = self.demo_address
        if self.doc_address is not None:
            result['DocAddress'] = self.doc_address
        if self.enum_definition_address is not None:
            result['EnumDefinitionAddress'] = self.enum_definition_address
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCodeList') is not None:
            self.auth_code_list = m.get('AuthCodeList')
        if m.get('DemoAddress') is not None:
            self.demo_address = m.get('DemoAddress')
        if m.get('DocAddress') is not None:
            self.doc_address = m.get('DocAddress')
        if m.get('EnumDefinitionAddress') is not None:
            self.enum_definition_address = m.get('EnumDefinitionAddress')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = QueryTagInfoBySelectionResponseBodyDataParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryTagInfoBySelectionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryTagInfoBySelectionResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTagInfoBySelectionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTagInfoBySelectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagInfoBySelectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryTagInfoBySelectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagListPageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTagListPageResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        code: str = None,
        doc_address: str = None,
        id: int = None,
        industry_id: int = None,
        industry_name: str = None,
        introduction: str = None,
        is_open: int = None,
        name: str = None,
        sale_status_str: str = None,
        scene_id: int = None,
        scene_name: str = None,
    ):
        # 前端调用的api名称
        self.api_name = api_name
        # code
        self.code = code
        # API文档链接
        self.doc_address = doc_address
        # 标签 id
        self.id = id
        # 行业id
        self.industry_id = industry_id
        # 行业名称
        self.industry_name = industry_name
        # 标签介绍
        self.introduction = introduction
        # 是否已经申请开通
        self.is_open = is_open
        # 标签名称
        self.name = name
        # 0 隐藏 1 公开
        self.sale_status_str = sale_status_str
        # 场景id
        self.scene_id = scene_id
        # 场景名称
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.code is not None:
            result['Code'] = self.code
        if self.doc_address is not None:
            result['DocAddress'] = self.doc_address
        if self.id is not None:
            result['Id'] = self.id
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id
        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.is_open is not None:
            result['IsOpen'] = self.is_open
        if self.name is not None:
            result['Name'] = self.name
        if self.sale_status_str is not None:
            result['SaleStatusStr'] = self.sale_status_str
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocAddress') is not None:
            self.doc_address = m.get('DocAddress')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')
        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SaleStatusStr') is not None:
            self.sale_status_str = m.get('SaleStatusStr')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class QueryTagListPageResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        records: List[QueryTagListPageResponseBodyDataRecords] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.records = records
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = QueryTagListPageResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class QueryTagListPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryTagListPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryTagListPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTagListPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagListPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryTagListPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUsageStatisticsByTagIdRequest(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag_id: int = None,
    ):
        # 开始时间
        self.begin_time = begin_time
        # 结束时间
        self.end_time = end_time
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 结束时间
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class QueryUsageStatisticsByTagIdResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization_code: str = None,
        fail_total: int = None,
        gmt_date_str: str = None,
        id: int = None,
        industry_name: str = None,
        partner_id: int = None,
        scene_name: str = None,
        success_total: int = None,
        tag_id: int = None,
        tag_name: str = None,
        total: int = None,
    ):
        # 授权码
        self.authorization_code = authorization_code
        # 查询失败号码数
        self.fail_total = fail_total
        # 创建时间
        self.gmt_date_str = gmt_date_str
        # 授权码使用记录 id
        self.id = id
        # 行业名称
        self.industry_name = industry_name
        # 客户 pid
        self.partner_id = partner_id
        # 场景名称
        self.scene_name = scene_name
        # 查询成功号码数
        self.success_total = success_total
        # 标签名称
        self.tag_id = tag_id
        # 标签名称
        self.tag_name = tag_name
        # 查询总号码数
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code
        if self.fail_total is not None:
            result['FailTotal'] = self.fail_total
        if self.gmt_date_str is not None:
            result['GmtDateStr'] = self.gmt_date_str
        if self.id is not None:
            result['Id'] = self.id
        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.success_total is not None:
            result['SuccessTotal'] = self.success_total
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')
        if m.get('FailTotal') is not None:
            self.fail_total = m.get('FailTotal')
        if m.get('GmtDateStr') is not None:
            self.gmt_date_str = m.get('GmtDateStr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SuccessTotal') is not None:
            self.success_total = m.get('SuccessTotal')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryUsageStatisticsByTagIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryUsageStatisticsByTagIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryUsageStatisticsByTagIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUsageStatisticsByTagIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUsageStatisticsByTagIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryUsageStatisticsByTagIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ThreeElementsVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        cert_code: str = None,
        input_number: str = None,
        mask: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.cert_code = cert_code
        self.input_number = input_number
        self.mask = mask
        self.name = name
        self.owner_id = owner_id
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
        if self.cert_code is not None:
            result['CertCode'] = self.cert_code
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('CertCode') is not None:
            self.cert_code = m.get('CertCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ThreeElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        basic_carrier: str = None,
        is_consistent: int = None,
    ):
        self.basic_carrier = basic_carrier
        self.is_consistent = is_consistent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier
        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')
        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')
        return self


class ThreeElementsVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ThreeElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = ThreeElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ThreeElementsVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ThreeElementsVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ThreeElementsVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TwoElementsVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.auth_code = auth_code
        self.input_number = input_number
        self.mask = mask
        self.name = name
        self.owner_id = owner_id
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
        if self.input_number is not None:
            result['InputNumber'] = self.input_number
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class TwoElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        basic_carrier: str = None,
        is_consistent: int = None,
    ):
        self.basic_carrier = basic_carrier
        self.is_consistent = is_consistent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier
        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')
        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')
        return self


class TwoElementsVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TwoElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
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
            temp_model = TwoElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TwoElementsVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TwoElementsVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = TwoElementsVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



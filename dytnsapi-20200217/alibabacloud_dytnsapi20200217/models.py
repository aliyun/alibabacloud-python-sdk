# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        # The authorization code.
        # 
        # >  On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/overview?spm=a2c4g.608385.0.0.79847f8b3awqUC), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The enterprise name.
        self.ep_cert_name = ep_cert_name
        # The business license number.
        self.ep_cert_no = ep_cert_no
        # The name of the legal representative.
        # 
        # >  If an enterprise has multiple legal representatives, separate them with commas (,).
        self.legal_person_cert_name = legal_person_cert_name
        # The ID card number of the legal representative.
        # 
        # >  If an enterprise has multiple legal representatives, separate the ID card numbers with commas (,).
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


class CompanyFourElementsVerificationResponseBodyDataDetailInfo(TeaModel):
    def __init__(
        self,
        enterprise_status: str = None,
        open_time: str = None,
    ):
        # The business status of the enterprise.
        self.enterprise_status = enterprise_status
        # The business term of the enterprise.
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enterprise_status is not None:
            result['EnterpriseStatus'] = self.enterprise_status
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseStatus') is not None:
            self.enterprise_status = m.get('EnterpriseStatus')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class CompanyFourElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: CompanyFourElementsVerificationResponseBodyDataDetailInfo = None,
        inconsistent_data: List[str] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        # The information about the enterprise.
        self.detail_info = detail_info
        # The fields to be verified.
        self.inconsistent_data = inconsistent_data
        # The code of the verification result. Valid values:
        # 
        # *   0: The four elements belong to the same enterprise.
        # *   1: The four elements belong to the same enterprise, but the business status of the enterprise is abnormal.
        # *   2: The legal representative information cannot match the enterprise information.
        # *   3: The four elements do not belong to the same enterprise.
        # *   4: No information about the enterprise is found.
        # *   5: No information about the legal representative is found.
        self.reason_code = reason_code
        # The verification result. Valid values:
        # 
        # *   true: The four elements belong to the same enterprise and the business status of the enterprise is Active.
        # *   false: The four elements do not belong to the same enterprise.
        self.verify_result = verify_result

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()
        if self.inconsistent_data is not None:
            result['InconsistentData'] = self.inconsistent_data
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = CompanyFourElementsVerificationResponseBodyDataDetailInfo()
            self.detail_info = temp_model.from_map(m['DetailInfo'])
        if m.get('InconsistentData') is not None:
            self.inconsistent_data = m.get('InconsistentData')
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/overview?spm=a2c4g.608385.0.0.79847f8b3awqUC), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The enterprise name.
        self.ep_cert_name = ep_cert_name
        # The business license number.
        self.ep_cert_no = ep_cert_no
        # The name of the legal representative.
        # 
        # >  If an enterprise has multiple legal representatives, separate them with commas (,).
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


class CompanyThreeElementsVerificationResponseBodyDataDetailInfo(TeaModel):
    def __init__(
        self,
        enterprise_status: str = None,
        open_time: str = None,
    ):
        # The business status of the enterprise.
        self.enterprise_status = enterprise_status
        # The business term of the enterprise.
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enterprise_status is not None:
            result['EnterpriseStatus'] = self.enterprise_status
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseStatus') is not None:
            self.enterprise_status = m.get('EnterpriseStatus')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class CompanyThreeElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: CompanyThreeElementsVerificationResponseBodyDataDetailInfo = None,
        inconsistent_data: List[str] = None,
        reason_code: int = None,
        verify_result: str = None,
    ):
        # The information about the enterprise.
        self.detail_info = detail_info
        # The fields to be verified.
        self.inconsistent_data = inconsistent_data
        # The code of the verification result. Valid values:
        # 
        # *   0: The three elements belong to the same enterprise.
        # *   1: The three elements belong to the same enterprise, and the business status of the enterprise is abnormal.
        # *   2: The legal representative information cannot match the enterprise information.
        # *   3: The three elements do not belong to the same enterprise.
        # *   4: No information about the enterprise is found.
        # *   5: No information about the legal representative is found.
        self.reason_code = reason_code
        # The verification result. Valid values:
        # 
        # *   true: The three elements belong to the same enterprise and the business status of the enterprise is Active.
        # *   false: The three elements do not belong to the same enterprise.
        self.verify_result = verify_result

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()
        if self.inconsistent_data is not None:
            result['InconsistentData'] = self.inconsistent_data
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = CompanyThreeElementsVerificationResponseBodyDataDetailInfo()
            self.detail_info = temp_model.from_map(m['DetailInfo'])
        if m.get('InconsistentData') is not None:
            self.inconsistent_data = m.get('InconsistentData')
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/overview?spm=a2c4g.608385.0.0.79847f8b3awqUC), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The enterprise name.
        self.ep_cert_name = ep_cert_name
        # The business license number.
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


class CompanyTwoElementsVerificationResponseBodyDataDetailInfo(TeaModel):
    def __init__(
        self,
        enterprise_status: str = None,
        open_time: str = None,
    ):
        # The business status of the enterprise.
        self.enterprise_status = enterprise_status
        # The business term of the enterprise.
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enterprise_status is not None:
            result['EnterpriseStatus'] = self.enterprise_status
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseStatus') is not None:
            self.enterprise_status = m.get('EnterpriseStatus')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class CompanyTwoElementsVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        detail_info: CompanyTwoElementsVerificationResponseBodyDataDetailInfo = None,
        inconsistent_data: List[str] = None,
        reason_code: str = None,
        verify_result: str = None,
    ):
        # The information about the enterprise.
        self.detail_info = detail_info
        # The fields to be verified.
        self.inconsistent_data = inconsistent_data
        # The code of the verification result. Valid values:
        # 
        # *   0: The two elements belong to the same enterprise.
        # *   1: The two elements belong to the same enterprise, but the business status of the enterprise is abnormal.
        # *   3: The two elements do not belong to the same enterprise.
        # *   4: No information about the enterprise is found.
        self.reason_code = reason_code
        # The verification result. Valid values:
        # 
        # *   true: The two elements belong to the same enterprise and the business status of the enterprise is Active.
        # *   false: The two elements do not belong to the same enterprise.
        self.verify_result = verify_result

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()
        if self.inconsistent_data is not None:
            result['InconsistentData'] = self.inconsistent_data
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = CompanyTwoElementsVerificationResponseBodyDataDetailInfo()
            self.detail_info = temp_model.from_map(m['DetailInfo'])
        if m.get('InconsistentData') is not None:
            self.inconsistent_data = m.get('InconsistentData')
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # >  You can query only one phone number a time.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # The specified phone number.
        self.number = number
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **EMPTY**: The queried phone number is a nonexistent number.
        # *   **NORMAL**: The queried phone number is valid.
        # *   **SUSPECT_EMPTY**: The queried phone number is suspected to be a nonexistent number.
        # *   **UNKNOWN**: The queried phone number is unknown.
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
        # The HTTP status code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **InvalidPhoneNumber.Check**: The phone number is invalid.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the ****[**Labels**](https://dytns.console.aliyun.com/analysis/square) page, find the label that you want to use, click Activate Now, enter the required information, and then submit your application. After your application is approved, you can obtain an authorization code.
        self.auth_code = auth_code
        # The phone number to be queried.
        self.input_number = input_number
        # The model parameter configuration. This field is required by some labels.
        self.model_config = model_config
        self.owner_id = owner_id
        # The score threshold for the phone number. Valid values: **0 to 100**.
        # 
        # >  The system provided by Alibaba Cloud determines whether to accept the specified score threshold. When the system does not accept the specified score threshold, the value of this field is invalid.
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
        # The returned code.
        # 
        # *   YES: The specified phone number is valid.
        # *   NO: The specified phone number is invalid.
        # *   UNKNOWN: The specified phone number is unknown
        self.code = code
        # The specified phone number.
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
        # The response code. Valid values:
        # 
        # *   OK: The request is successful.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        # The phone number that you want to query.
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
        # The basic carrier. Valid values:
        # 
        # *   **China Mobile**\
        # *   **China Unicom**\
        # *   **China Telecom**\
        self.basic_carrier = basic_carrier
        # The actual carrier, including the virtual network operator (VNO). If the phone number involves mobile number portability, the value of this parameter is the carrier after mobile number portability.
        self.carrier = carrier
        # The city where the phone number is registered.
        self.city = city
        # Indicates whether the phone number involves mobile number portability. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_number_portability = is_number_portability
        # The number segment to which the phone number belongs.
        self.number_segment = number_segment
        # The province where the phone number is registered.
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **InvalidParameter**: The specified phone number is invalid or the parameter format is invalid.
        # *   **PhoneNumberNotfound**: No attribute information can be found for the specified phone number.
        # *   **isp.UNKNOWN**: An unknown exception occurred.
        self.code = code
        # The returned message.
        self.message = message
        # The attribute information about the phone number.
        self.phone_number_attribute = phone_number_attribute
        # The request ID.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The carrier. Valid values:
        # 
        # *   **MOBILE**: China Mobile
        # *   **UNICOM**: China Unicom
        # *   **TELECOM**: China Telecom
        # 
        # >  Alibaba Cloud automatically determines the carrier based on the carrier who assigns the phone number. Therefore, the value of this field does not affect the query result.
        self.carrier = carrier
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # The carrier code. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # *   **CBN**: China Broadnet
        self.carrier_code = carrier_code
        # The enumerated value of the usage period of a phone number. Valid values:
        # 
        # *   **-1**: No usage period information is available for the phone number.
        # *   **0**: The phone number status is abnormal. For example, the phone number is a nonexistent number.
        # *   **1** :\[0-3) months.
        # *   **2** :\[3-6] months.
        # *   **3** :(6-12] months.
        # *   **4** :(12-24] months.
        # *   **5** :(24,+) months.
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **PortabilityNumberNotSupported**: The phone number that is involved in mobile number portability is not supported.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        # 
        # >  You are charged if the value of Code is OK and the value of VerifyResult is not -1. For more information, see [Pricing](~~154751~~).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**: The phone number is MD5-encrypted.
        # *   **SHA256**: The phone number is SHA256-encrypted.
        # 
        # > Letters in the string must be uppercase.
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
        # The basic carrier. Valid values:
        # 
        # *   **China Mobile**\
        # *   **China Unicom**\
        # *   **China Telecom**\
        # *   **China Broadnet**\
        self.basic_carrier = basic_carrier
        # The actual carrier, including the virtual network operator (VNO). If the phone number involves mobile number portability, the value of this parameter is the carrier after mobile number portability.
        self.carrier = carrier
        # The city where the phone number is registered.
        self.city = city
        # Indicates whether the phone number involves mobile number portability. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_number_portability = is_number_portability
        # The number segment to which the phone number belongs.
        self.number_segment = number_segment
        # The province where the phone number is registered.
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **InvalidParameter**: The specified phone number is invalid or the parameter format is invalid.
        # *   **PhoneNumberNotfound**: No attribute information can be found for the specified phone number.
        # *   **isp.UNKNOWN**: An unknown exception occurred.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
        self.mask = mask
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The registration time. Specify the time in the yyyy-MM-dd HH:mm:ss format. This time is the service registration time of the mobile phone user. If the service registration time is later than the time when the phone number is assigned by a carrier, it indicates that the phone number is not a reassigned number. Otherwise, the phone number is a reassigned number.
        # 
        # > 
        # 
        # *   If a carrier allocates a single number multiple times, the system will determine whether the phone number is a reassigned number based on the time when the carrier last allocated the phone number.
        # 
        # *   The service registration time must be later than 00:00:00 on January 1, 1970.
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
        # The carrier. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  The returned result indicates the carrier who assigns the phone number. If the phone number involves mobile number portability, the carrier after mobile number portability is returned.
        self.carrier = carrier
        # The result of the request. Valid values:
        # 
        # *   **0**: It is unable to judge whether the phone number is a reassigned number.
        # *   **1**: The phone number is a reassigned number.
        # *   **2**: The phone number is not a reassigned number.
        # *   **3**: The phone number has been canceled.
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **PortabilityNumberNotSupported**: The phone number that is involved in mobile number portability is not supported.
        # *   **RequestNumberNotSupported**: You are not allowed to query phone numbers assigned by China Broadnet (that is, phone numbers start with 192) and phone numbers assigned by virtual network operators (VNOs).
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        # 
        # >  You are charged for phone number verifications if the value of Code is OK and the value of VerifyResult is not 0. For more information, see [Pricing](~~154751~~).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot and locate issues.
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


class GetUAIDApplyTokenSignRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        client_type: str = None,
        format: str = None,
        out_id: str = None,
        owner_id: int = None,
        param_key: str = None,
        param_str: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        time: str = None,
    ):
        self.auth_code = auth_code
        self.carrier = carrier
        self.client_type = client_type
        self.format = format
        self.out_id = out_id
        self.owner_id = owner_id
        self.param_key = param_key
        self.param_str = param_str
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.time = time

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
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.format is not None:
            result['Format'] = self.format
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.param_key is not None:
            result['ParamKey'] = self.param_key
        if self.param_str is not None:
            result['ParamStr'] = self.param_str
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')
        if m.get('ParamStr') is not None:
            self.param_str = m.get('ParamStr')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetUAIDApplyTokenSignResponseBodyData(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        out_id: str = None,
        sign: str = None,
    ):
        self.carrier = carrier
        self.out_id = out_id
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class GetUAIDApplyTokenSignResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetUAIDApplyTokenSignResponseBodyData = None,
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
            temp_model = GetUAIDApplyTokenSignResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUAIDApplyTokenSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUAIDApplyTokenSignResponseBody = None,
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
            temp_model = GetUAIDApplyTokenSignResponseBody()
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        self.input_number = input_number
        # The encryption method of the phone number.
        # 
        # >  Only the NORMAL encryption method is supported.
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
        # The returned filter results.
        # 
        # *   **YES**: the valid phone number. The mappings are returned.
        # *   **NO**: the invalid phone number. No mappings are returned.
        self.code = code
        # The encrypted phone number.
        self.encrypted_number = encrypted_number
        # The time when the phone number expires.
        self.expire_time = expire_time
        # The original phone number.
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **MobileNumberIllegal**: The phone number is invalid.
        # *   **EncyrptTypeIllegal**: The encryption type is invalid.
        # *   **MobileNumberTypeNotMatch**: The phone number does not match the encryption type.
        # *   **CarrierIllegal**: The carrier type is invalid.
        # *   **AuthCodeNotExist**: The authorization code does not exist.
        # *   **PortabilityNumberNotSupported**: Mobile number portability is not supported.
        # *   **Unknown**: An unknown exception occurred.
        # *   **AuthCodeAndApiNotMatch**: A system exception occurred.
        # *   **AuthCodeAndApiNotMatch**: The authorization code does not match the API operation.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # Details about the returned entries.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # >  You can query only one phone number at a time.
        self.input_number = input_number
        # The encryption method of the phone number. Set the value to **NORMAL**.
        # 
        # >  Only the NORMAL encryption method is supported.
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
        # The encrypted phone number.
        self.encrypted_number = encrypted_number
        # The time when the phone number expires.
        self.expire_time = expire_time
        # The original phone number.
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
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](~~109196~~).
        self.code = code
        # Details about the returned entries.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # The basic carrier who assings the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number is valid.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The queried phone number cannot be connected.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **DEFECT**: The queried phone number is invalid.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization ID.
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, the value of this field is an 11-digit phone number.
        # *   If the value of Mask is MD5, the value of this field is a 32-bit encrypted string.
        # *   If the value of Mask is SHA256, the value of this field is a 64-bit encrypted string.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # The basic carrier who assigns the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned.
        # 
        # Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number can be reached.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The phone is powered off.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **SUSPECTED_POWER_OFF**: The phone is suspected to be powered off.
        # *   **BUSY**: The queried phone number is busy.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        # 
        # >  For a list of error codes, see [Service error codes](https://next.api.aliyun.com/document/Dytnsapi/2020-02-17/errorCode).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization ID.
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, the value of this field is an 11-digit phone number.
        # *   If the value of Mask is MD5, the value of this field is a 32-bit encrypted string.
        # *   If the value of Mask is SHA256, the value of this field is a 64-bit encrypted string.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # The basic carrier who assigns the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number can be reached.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The phone is powered off.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **BUSY**: The queried phone number is busy.
        # *   **SUSPECTED_POWER_OFF**: The phone is suspected to be powered off.
        # *   **DEFECT**: The queried phone number is invalid.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: plaintext
        # *   **MD5**\
        # *   **SHA256**\
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
        # The basic carrier who assigns the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number can be reached.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The phone is powered off.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **DEFECT**: The queried phone number is invalid.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY, SUSPECTED_POWER_OFF, and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization ID.
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, the value of this field is an 11-digit phone number.
        # *   If the value of Mask is MD5, the value of this field is a 32-bit encrypted string.
        # *   If the value of Mask is SHA256, the value of this field is a 64-bit encrypted string.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
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
        # Indicate whether the phone number is a virtual number assigned by the carrier. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be queried.
        # 
        # *   If the value of Mask is NORMAL, specify an 11-digit phone number in plaintext.
        # *   If the value of Mask is MD5, specify a 32-bit string that is encrypted by using MD5.
        # *   If the value of Mask is SHA256, specify a 64-bit string that is encrypted by using SHA256.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method. Valid values:
        # 
        # *   **NORMAL**: plaintext
        # *   **MD5**\
        # *   **SHA256**\
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
        # The basic carrier who assigns the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number can be reached.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The phone is powered off.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **SUSPECTED_POWER_OFF**: The phone is suspected to be powered off.
        # *   **DEFECT**: The queried phone number is invalid.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY, SUSPECTED_POWER_OFF, and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
        # The tag ID.
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
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The tag ID.
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
        # The requirements for application materials.
        self.apply_material_desc = apply_material_desc
        # Indicates whether the application is automatically approved.
        self.auto_audit = auto_audit
        # The URL for the billing documentation.
        self.charging_standard_link = charging_standard_link
        # indicates whether encrypted queries are supported.
        self.encrypted_query = encrypted_query
        # Indicates whether application materials are required.
        self.need_apply_material = need_apply_material
        # The URL for the service agreement.
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
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The industry ID.
        self.industry_id = industry_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scene ID.
        self.scene_id = scene_id
        # The tag ID.
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
        # The English name.
        self.code = code
        # The Chinese name.
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
        # The English name of the parameter.
        self.code = code
        # The input hint.
        self.hint = hint
        # Indicates whether the parameter is required.
        self.must = must
        # The Chinese name of the parameter.
        self.name = name
        # The type. The code that corresponds to EnumUIWidgetTypes.
        self.type = type
        # The definitions of the enumerated values such as Code or Desc.
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
        complexity_type: str = None,
        demo_address: str = None,
        doc_address: str = None,
        enum_definition_address: str = None,
        flow_name: str = None,
        industry_id: int = None,
        industry_name: str = None,
        param_list: List[QueryTagInfoBySelectionResponseBodyDataParamList] = None,
        rich_text_description: str = None,
        scene_id: int = None,
        scene_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        # The list of available authorization codes.
        self.auth_code_list = auth_code_list
        self.complexity_type = complexity_type
        # The URL for the API demo.
        self.demo_address = demo_address
        # The URL for the API documentation.
        self.doc_address = doc_address
        # The URL for the definitions of the enumerated values.
        self.enum_definition_address = enum_definition_address
        # The flow name.
        self.flow_name = flow_name
        # The industry ID.
        self.industry_id = industry_id
        # The industry name.
        self.industry_name = industry_name
        # The list of tag parameters.
        self.param_list = param_list
        self.rich_text_description = rich_text_description
        # The scene ID.
        self.scene_id = scene_id
        # The scene name.
        self.scene_name = scene_name
        # The tag ID.
        self.tag_id = tag_id
        # The tag name.
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
        if self.complexity_type is not None:
            result['ComplexityType'] = self.complexity_type
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
        if self.rich_text_description is not None:
            result['RichTextDescription'] = self.rich_text_description
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
        if m.get('ComplexityType') is not None:
            self.complexity_type = m.get('ComplexityType')
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
        if m.get('RichTextDescription') is not None:
            self.rich_text_description = m.get('RichTextDescription')
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
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The page number. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page.
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
        # The API operation that is called by the frontend.
        self.api_name = api_name
        # Code
        self.code = code
        # The URL for the API documentation.
        self.doc_address = doc_address
        # The tag ID.
        self.id = id
        # The industry ID.
        self.industry_id = industry_id
        # The industry name.
        self.industry_name = industry_name
        # The tag description.
        self.introduction = introduction
        # Indicates whether the number is activated.
        self.is_open = is_open
        # The tag name.
        self.name = name
        # *   0: The number is hidden.
        # *   1: The number is public.
        self.sale_status_str = sale_status_str
        # The scene ID.
        self.scene_id = scene_id
        # The scene name.
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
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The retruned data.
        self.records = records
        # The total number of returned entries.
        self.total_count = total_count
        # The total number of returned pages.
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
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The beginning of the time range to query.
        self.begin_time = begin_time
        # The end of the time range to query.
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag ID.
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
        # The authorization code.
        self.authorization_code = authorization_code
        # The numbers for which the query failed.
        self.fail_total = fail_total
        # The creation time.
        self.gmt_date_str = gmt_date_str
        # The ID of the authorization code usage record.
        self.id = id
        # The industry name.
        self.industry_name = industry_name
        # The customer product ID (PID).
        self.partner_id = partner_id
        # The scene name.
        self.scene_name = scene_name
        # The numbers for which the query succeeded.
        self.success_total = success_total
        # The tag name.
        self.tag_id = tag_id
        # The tag name.
        self.tag_name = tag_name
        # The total quantity of numbers that are involved in the query.
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
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
        # 
        # *   true
        # *   false
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The ID card number to be verified.
        # 
        # *   If the value of Mask is NORMAL, specify a value in plaintext for this field.
        # *   If the value of Mask is MD5, specify a MD5-encrypted value for this field.
        # *   If the value of Mask is SHA256, specify a SHA256-encrypted value for this field.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.cert_code = cert_code
        # The phone number to be verified.
        # 
        # *   If the value of Mask is NORMAL, specify a value in plaintext for this field.
        # *   If the value of Mask is MD5, specify a MD5-encrypted value for this field.
        # *   If the value of Mask is SHA256, specify a SHA256-encrypted value for this field.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method. Valid values:
        # 
        # *   **NORMAL**: The phone number is not encrypted.
        # *   **MD5**\
        # *   **SHA256**\
        self.mask = mask
        # The name to be verified.
        # 
        # *   If the value of Mask is NORMAL, specify a value in plaintext for this field.
        # *   If the value of Mask is MD5, specify a MD5-encrypted value for this field.
        # *   If the value of Mask is SHA256, specify a SHA256-encrypted value for this field.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
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
        # The basic carrier. Valid values:
        # 
        # *   **China Mobile**\
        # *   **China Unicom**\
        # *   **China Telecom**\
        self.basic_carrier = basic_carrier
        # Indicates whether the specified name, phone number, and ID card number belong to the same user. Valid values:
        # 
        # * **1**: The specified name, phone number, and ID card number belong to the same user.
        # * **0**: The specified name, phone number, and ID card number do not belong to the same user.
        # * **2**: The specified name, phone number, and ID card number cannot be found.
        # 
        # **Note** The phone number registration data of a user is usually updated one or three days after registration. The registration data can be queried only after the update. The following table shows the verification results under different phone number states.
        # 
        # |Carrier/Phone number state|Out-of-service|Nonexistent|Canceled|
        # |---|---|---|---|
        # |China Mobile|Verifications can be carried out normally.|The specified name, phone number, and ID card number cannot be found.|The specified name, phone number, and ID card number cannot be found.|
        # |China Unicom|Verifications can be carried out normally.|The specified name, phone number, and ID card number do not belong to the same user.|The specified name, phone number, and ID card number do not belong to the same user.|
        # |China Telecom|Verifications can be carried out normally.|The specified name, phone number, and ID card number cannot be found.|The specified name, phone number, and ID card number cannot be found.|
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
        # The response code.
        # 
        # *   **OK**: The request is successful.
        # *   For more information, see Error codes in this documentation.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        # The authorization code.
        # 
        # >  On the **My Applications** page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), you can obtain the authorization code (also known as authorization ID).
        self.auth_code = auth_code
        # The phone number to be verified.
        # 
        # *   If the value of Mask is NORMAL, specify a value in plaintext for this field.
        # *   If the value of Mask is MD5, specify a MD5-encrypted value for this field.
        # *   If the value of Mask is SHA256, specify a SHA256-encrypted value for this field.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
        self.input_number = input_number
        # The encryption method. Valid values:
        # 
        # *   **NORMAL**: plaintext
        # *   **MD5**\
        # *   **SHA256**\
        self.mask = mask
        # The name to be verified.
        # 
        # *   If the value of Mask is NORMAL, specify a value in plaintext for this field.
        # *   If the value of Mask is MD5, specify a MD5-encrypted value for this field.
        # *   If the value of Mask is SHA256, specify a SHA256-encrypted value for this field.
        # 
        # >  Letters in the encrypted strings are not case-sensitive.
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
        # The basic carriers. Valid values:
        # 
        # *   **China Mobile**\
        # *   **China Unicom**\
        # *   **China Telecom**\
        # 
        # >  You are not allowed to verify numbers assigned by China Broadnet.
        self.basic_carrier = basic_carrier
        # Indicates whether the specified name and phone number belong to the same user. Valid values:
        # 
        # * **1**: The specified name and phone number belong to the same user.
        # 
        # * **0**: The specified name and phone number do not belong to the same user.
        # 
        # * **2**: The specified name and phone number cannot be found.
        # 
        # The phone number registration data of a user is usually updated one or three days after registration. The registration data can be queried only after the update. The following table shows the verification results under different phone number states.
        # 
        # |Carrier/Phone number state|Out-of-service|Nonexistent|Canceled|
        # |---|---|---|---|
        # |China Mobile|Verifications can be carried out normally.|The specified name and phone number cannot be found.|The specified name and phone number cannot be found.|
        # |China Unicom|Verifications can be carried out normally.|The specified name and phone number do not belong to the same user.|The specified name and phone number do not belong to the same user.|
        # |China Telecom|Verifications can be carried out normally.|The specified name and phone number cannot be found.|The specified name and phone number cannot be found.|
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
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   For more information, see Error codes in this documentation.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number or name at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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


class UAIDVerificationRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        ip: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token: str = None,
        user_grant_id: str = None,
    ):
        self.auth_code = auth_code
        self.carrier = carrier
        self.ip = ip
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.token = token
        self.user_grant_id = user_grant_id

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
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.token is not None:
            result['Token'] = self.token
        if self.user_grant_id is not None:
            result['UserGrantId'] = self.user_grant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserGrantId') is not None:
            self.user_grant_id = m.get('UserGrantId')
        return self


class UAIDVerificationResponseBodyData(TeaModel):
    def __init__(
        self,
        uaid: str = None,
    ):
        self.uaid = uaid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uaid is not None:
            result['Uaid'] = self.uaid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uaid') is not None:
            self.uaid = m.get('Uaid')
        return self


class UAIDVerificationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: UAIDVerificationResponseBodyData = None,
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
            temp_model = UAIDVerificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UAIDVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UAIDVerificationResponseBody = None,
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
            temp_model = UAIDVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



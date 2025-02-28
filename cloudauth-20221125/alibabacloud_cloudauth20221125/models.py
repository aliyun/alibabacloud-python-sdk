# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class EntElementVerifyRequest(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        info_verify_type: str = None,
        legal_person_cert_no: str = None,
        legal_person_name: str = None,
        license_no: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        self.ent_name = ent_name
        self.info_verify_type = info_verify_type
        self.legal_person_cert_no = legal_person_cert_no
        self.legal_person_name = legal_person_name
        self.license_no = license_no
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.scene_code = scene_code
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.info_verify_type is not None:
            result['InfoVerifyType'] = self.info_verify_type
        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.license_no is not None:
            result['LicenseNo'] = self.license_no
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InfoVerifyType') is not None:
            self.info_verify_type = m.get('InfoVerifyType')
        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')
        return self


class EntElementVerifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        open_time: str = None,
        reason_code: str = None,
        reason_detail: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.open_time = open_time
        self.reason_code = reason_code
        self.reason_detail = reason_detail
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.reason_detail is not None:
            result['ReasonDetail'] = self.reason_detail
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('ReasonDetail') is not None:
            self.reason_detail = m.get('ReasonDetail')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EntElementVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EntElementVerifyResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            temp_model = EntElementVerifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EntElementVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntElementVerifyResponseBody = None,
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
            temp_model = EntElementVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntElementVerifyV2Request(TeaModel):
    def __init__(
        self,
        ent_name: str = None,
        info_verify_type: str = None,
        legal_person_cert_no: str = None,
        legal_person_name: str = None,
        license_no: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        # This parameter is required.
        self.ent_name = ent_name
        # This parameter is required.
        self.info_verify_type = info_verify_type
        self.legal_person_cert_no = legal_person_cert_no
        self.legal_person_name = legal_person_name
        # This parameter is required.
        self.license_no = license_no
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # This parameter is required.
        self.merchant_user_id = merchant_user_id
        # This parameter is required.
        self.scene_code = scene_code
        # This parameter is required.
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.info_verify_type is not None:
            result['InfoVerifyType'] = self.info_verify_type
        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.license_no is not None:
            result['LicenseNo'] = self.license_no
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InfoVerifyType') is not None:
            self.info_verify_type = m.get('InfoVerifyType')
        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')
        return self


class EntElementVerifyV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        open_time: str = None,
        reason_detail: str = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.open_time = open_time
        self.reason_detail = reason_detail
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.reason_detail is not None:
            result['ReasonDetail'] = self.reason_detail
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('ReasonDetail') is not None:
            self.reason_detail = m.get('ReasonDetail')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EntElementVerifyV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EntElementVerifyV2ResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            temp_model = EntElementVerifyV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EntElementVerifyV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntElementVerifyV2ResponseBody = None,
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
            temp_model = EntElementVerifyV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntRiskQueryRequest(TeaModel):
    def __init__(
        self,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        param_type: str = None,
        param_value: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.param_type = param_type
        self.param_value = param_value
        self.scene_code = scene_code
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')
        return self


class EntRiskQueryResponseBodyResultRiskList(TeaModel):
    def __init__(
        self,
        credit_code: str = None,
        ent_name: str = None,
        listed_date: str = None,
        listed_reason: str = None,
        operation_org: str = None,
        reg_no: str = None,
        removed_date: str = None,
        removed_org: str = None,
        removed_reason: str = None,
    ):
        self.credit_code = credit_code
        self.ent_name = ent_name
        self.listed_date = listed_date
        self.listed_reason = listed_reason
        self.operation_org = operation_org
        self.reg_no = reg_no
        self.removed_date = removed_date
        self.removed_org = removed_org
        self.removed_reason = removed_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_code is not None:
            result['CreditCode'] = self.credit_code
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.listed_date is not None:
            result['ListedDate'] = self.listed_date
        if self.listed_reason is not None:
            result['ListedReason'] = self.listed_reason
        if self.operation_org is not None:
            result['OperationOrg'] = self.operation_org
        if self.reg_no is not None:
            result['RegNo'] = self.reg_no
        if self.removed_date is not None:
            result['RemovedDate'] = self.removed_date
        if self.removed_org is not None:
            result['RemovedOrg'] = self.removed_org
        if self.removed_reason is not None:
            result['RemovedReason'] = self.removed_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditCode') is not None:
            self.credit_code = m.get('CreditCode')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('ListedDate') is not None:
            self.listed_date = m.get('ListedDate')
        if m.get('ListedReason') is not None:
            self.listed_reason = m.get('ListedReason')
        if m.get('OperationOrg') is not None:
            self.operation_org = m.get('OperationOrg')
        if m.get('RegNo') is not None:
            self.reg_no = m.get('RegNo')
        if m.get('RemovedDate') is not None:
            self.removed_date = m.get('RemovedDate')
        if m.get('RemovedOrg') is not None:
            self.removed_org = m.get('RemovedOrg')
        if m.get('RemovedReason') is not None:
            self.removed_reason = m.get('RemovedReason')
        return self


class EntRiskQueryResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        risk_list: List[EntRiskQueryResponseBodyResultRiskList] = None,
        status: str = None,
    ):
        self.biz_code = biz_code
        self.risk_list = risk_list
        self.status = status

    def validate(self):
        if self.risk_list:
            for k in self.risk_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        result['RiskList'] = []
        if self.risk_list is not None:
            for k in self.risk_list:
                result['RiskList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        self.risk_list = []
        if m.get('RiskList') is not None:
            for k in m.get('RiskList'):
                temp_model = EntRiskQueryResponseBodyResultRiskList()
                self.risk_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EntRiskQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EntRiskQueryResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            temp_model = EntRiskQueryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EntRiskQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntRiskQueryResponseBody = None,
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
            temp_model = EntRiskQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntVerifyRequest(TeaModel):
    def __init__(
        self,
        account_no: str = None,
        ent_name: str = None,
        info_verify_type: str = None,
        legal_person_cert_no: str = None,
        legal_person_mobile: str = None,
        legal_person_name: str = None,
        license_no: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        risk_model_version: str = None,
        risk_verify_type: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        self.account_no = account_no
        self.ent_name = ent_name
        self.info_verify_type = info_verify_type
        self.legal_person_cert_no = legal_person_cert_no
        self.legal_person_mobile = legal_person_mobile
        self.legal_person_name = legal_person_name
        self.license_no = license_no
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.risk_model_version = risk_model_version
        self.risk_verify_type = risk_verify_type
        self.scene_code = scene_code
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.ent_name is not None:
            result['EntName'] = self.ent_name
        if self.info_verify_type is not None:
            result['InfoVerifyType'] = self.info_verify_type
        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no
        if self.legal_person_mobile is not None:
            result['LegalPersonMobile'] = self.legal_person_mobile
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.license_no is not None:
            result['LicenseNo'] = self.license_no
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.risk_model_version is not None:
            result['RiskModelVersion'] = self.risk_model_version
        if self.risk_verify_type is not None:
            result['RiskVerifyType'] = self.risk_verify_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')
        if m.get('InfoVerifyType') is not None:
            self.info_verify_type = m.get('InfoVerifyType')
        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')
        if m.get('LegalPersonMobile') is not None:
            self.legal_person_mobile = m.get('LegalPersonMobile')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('RiskModelVersion') is not None:
            self.risk_model_version = m.get('RiskModelVersion')
        if m.get('RiskVerifyType') is not None:
            self.risk_verify_type = m.get('RiskVerifyType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')
        return self


class EntVerifyResponseBodyResultRiskVerifyResultModelResults(TeaModel):
    def __init__(
        self,
        model_name: str = None,
        result: str = None,
    ):
        self.model_name = model_name
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class EntVerifyResponseBodyResultRiskVerifyResult(TeaModel):
    def __init__(
        self,
        found: bool = None,
        model_results: List[EntVerifyResponseBodyResultRiskVerifyResultModelResults] = None,
    ):
        self.found = found
        self.model_results = model_results

    def validate(self):
        if self.model_results:
            for k in self.model_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.found is not None:
            result['Found'] = self.found
        result['ModelResults'] = []
        if self.model_results is not None:
            for k in self.model_results:
                result['ModelResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Found') is not None:
            self.found = m.get('Found')
        self.model_results = []
        if m.get('ModelResults') is not None:
            for k in m.get('ModelResults'):
                temp_model = EntVerifyResponseBodyResultRiskVerifyResultModelResults()
                self.model_results.append(temp_model.from_map(k))
        return self


class EntVerifyResponseBodyResult(TeaModel):
    def __init__(
        self,
        risk_verify_result: EntVerifyResponseBodyResultRiskVerifyResult = None,
    ):
        self.risk_verify_result = risk_verify_result

    def validate(self):
        if self.risk_verify_result:
            self.risk_verify_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_verify_result is not None:
            result['RiskVerifyResult'] = self.risk_verify_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskVerifyResult') is not None:
            temp_model = EntVerifyResponseBodyResultRiskVerifyResult()
            self.risk_verify_result = temp_model.from_map(m['RiskVerifyResult'])
        return self


class EntVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: EntVerifyResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
            temp_model = EntVerifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EntVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntVerifyResponseBody = None,
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
            temp_model = EntVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



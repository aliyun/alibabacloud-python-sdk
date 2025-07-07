# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class EnterpriseAccountChangeLoginPasswordRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        encrypt_password: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.encrypt_password = encrypt_password
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.encrypt_password is not None:
            result['EncryptPassword'] = self.encrypt_password
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EncryptPassword') is not None:
            self.encrypt_password = m.get('EncryptPassword')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnterpriseAccountChangeLoginPasswordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        pass_: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.pass_ = pass_
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
        if self.message is not None:
            result['Message'] = self.message
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountChangeLoginPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountChangeLoginPasswordResponseBody = None,
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
            temp_model = EnterpriseAccountChangeLoginPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountChangeSecurityEmailRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        security_email: str = None,
        verify_code: str = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.security_email = security_email
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_email is not None:
            result['SecurityEmail'] = self.security_email
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityEmail') is not None:
            self.security_email = m.get('SecurityEmail')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class EnterpriseAccountChangeSecurityEmailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountChangeSecurityEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountChangeSecurityEmailResponseBody = None,
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
            temp_model = EnterpriseAccountChangeSecurityEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountChangeSecurityMobileRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        encrypt_ticket: str = None,
        new_mobile: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        verification_code: str = None,
    ):
        self.app_name = app_name
        self.encrypt_ticket = encrypt_ticket
        # This parameter is required.
        self.new_mobile = new_mobile
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.new_mobile is not None:
            result['NewMobile'] = self.new_mobile
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('NewMobile') is not None:
            self.new_mobile = m.get('NewMobile')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class EnterpriseAccountChangeSecurityMobileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountChangeSecurityMobileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountChangeSecurityMobileResponseBody = None,
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
            temp_model = EnterpriseAccountChangeSecurityMobileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountQueryAccountGrantedRolesRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        is_open_api: bool = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        show_complete_info: bool = None,
    ):
        self.app_name = app_name
        self.is_open_api = is_open_api
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.pk = pk
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.is_open_api is not None:
            result['IsOpenApi'] = self.is_open_api
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('IsOpenApi') is not None:
            self.is_open_api = m.get('IsOpenApi')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        return self


class EnterpriseAccountQueryAccountGrantedRolesResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_role_code: str = None,
        biz_role_name: str = None,
    ):
        self.biz_role_code = biz_role_code
        self.biz_role_name = biz_role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')
        return self


class EnterpriseAccountQueryAccountGrantedRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[EnterpriseAccountQueryAccountGrantedRolesResponseBodyData] = None,
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
                temp_model = EnterpriseAccountQueryAccountGrantedRolesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountQueryAccountGrantedRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountQueryAccountGrantedRolesResponseBody = None,
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
            temp_model = EnterpriseAccountQueryAccountGrantedRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountQueryAccountsInfoRequest(TeaModel):
    def __init__(
        self,
        encrypt_ticket: str = None,
        max_results: int = None,
        next_token: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pks_json: str = None,
        request_id: str = None,
        show_complete_info: bool = None,
    ):
        self.encrypt_ticket = encrypt_ticket
        self.max_results = max_results
        self.next_token = next_token
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pks_json = pks_json
        # This parameter is required.
        self.request_id = request_id
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pks_json is not None:
            result['PksJson'] = self.pks_json
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('PksJson') is not None:
            self.pks_json = m.get('PksJson')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        return self


class EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList(TeaModel):
    def __init__(
        self,
        alias: str = None,
        belong_to_master_account: bool = None,
        email: str = None,
        enterprise_ec_id: str = None,
        enterprise_entity_id: str = None,
        enterprise_license_no: str = None,
        enterprise_name: str = None,
        enterprise_nb_id: str = None,
        freeze_login: bool = None,
        login_id: str = None,
        manage_invite_time_stamp: str = None,
        pk: str = None,
        security_mobile: str = None,
    ):
        self.alias = alias
        self.belong_to_master_account = belong_to_master_account
        self.email = email
        self.enterprise_ec_id = enterprise_ec_id
        self.enterprise_entity_id = enterprise_entity_id
        self.enterprise_license_no = enterprise_license_no
        self.enterprise_name = enterprise_name
        self.enterprise_nb_id = enterprise_nb_id
        self.freeze_login = freeze_login
        self.login_id = login_id
        self.manage_invite_time_stamp = manage_invite_time_stamp
        self.pk = pk
        self.security_mobile = security_mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.belong_to_master_account is not None:
            result['BelongToMasterAccount'] = self.belong_to_master_account
        if self.email is not None:
            result['Email'] = self.email
        if self.enterprise_ec_id is not None:
            result['EnterpriseEcId'] = self.enterprise_ec_id
        if self.enterprise_entity_id is not None:
            result['EnterpriseEntityId'] = self.enterprise_entity_id
        if self.enterprise_license_no is not None:
            result['EnterpriseLicenseNo'] = self.enterprise_license_no
        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name
        if self.enterprise_nb_id is not None:
            result['EnterpriseNbId'] = self.enterprise_nb_id
        if self.freeze_login is not None:
            result['FreezeLogin'] = self.freeze_login
        if self.login_id is not None:
            result['LoginId'] = self.login_id
        if self.manage_invite_time_stamp is not None:
            result['ManageInviteTimeStamp'] = self.manage_invite_time_stamp
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.security_mobile is not None:
            result['SecurityMobile'] = self.security_mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('BelongToMasterAccount') is not None:
            self.belong_to_master_account = m.get('BelongToMasterAccount')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnterpriseEcId') is not None:
            self.enterprise_ec_id = m.get('EnterpriseEcId')
        if m.get('EnterpriseEntityId') is not None:
            self.enterprise_entity_id = m.get('EnterpriseEntityId')
        if m.get('EnterpriseLicenseNo') is not None:
            self.enterprise_license_no = m.get('EnterpriseLicenseNo')
        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')
        if m.get('EnterpriseNbId') is not None:
            self.enterprise_nb_id = m.get('EnterpriseNbId')
        if m.get('FreezeLogin') is not None:
            self.freeze_login = m.get('FreezeLogin')
        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')
        if m.get('ManageInviteTimeStamp') is not None:
            self.manage_invite_time_stamp = m.get('ManageInviteTimeStamp')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('SecurityMobile') is not None:
            self.security_mobile = m.get('SecurityMobile')
        return self


class EnterpriseAccountQueryAccountsInfoResponseBody(TeaModel):
    def __init__(
        self,
        account_info_dto_list: List[EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList] = None,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_info_dto_list = account_info_dto_list
        self.code = code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_info_dto_list:
            for k in self.account_info_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountInfoDtoList'] = []
        if self.account_info_dto_list is not None:
            for k in self.account_info_dto_list:
                result['AccountInfoDtoList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_info_dto_list = []
        if m.get('AccountInfoDtoList') is not None:
            for k in m.get('AccountInfoDtoList'):
                temp_model = EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList()
                self.account_info_dto_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountQueryAccountsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountQueryAccountsInfoResponseBody = None,
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
            temp_model = EnterpriseAccountQueryAccountsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountQueryLoginSettingsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        is_open_api: bool = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        show_complete_info: bool = None,
    ):
        self.app_name = app_name
        self.is_open_api = is_open_api
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.pk = pk
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.is_open_api is not None:
            result['IsOpenApi'] = self.is_open_api
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('IsOpenApi') is not None:
            self.is_open_api = m.get('IsOpenApi')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        return self


class EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto(TeaModel):
    def __init__(
        self,
        ip_mask_enabled_status: str = None,
        ip_masks: List[str] = None,
    ):
        self.ip_mask_enabled_status = ip_mask_enabled_status
        self.ip_masks = ip_masks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_mask_enabled_status is not None:
            result['IpMaskEnabledStatus'] = self.ip_mask_enabled_status
        if self.ip_masks is not None:
            result['IpMasks'] = self.ip_masks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpMaskEnabledStatus') is not None:
            self.ip_mask_enabled_status = m.get('IpMaskEnabledStatus')
        if m.get('IpMasks') is not None:
            self.ip_masks = m.get('IpMasks')
        return self


class EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto(TeaModel):
    def __init__(
        self,
        protect_level: str = None,
        risk_control_enabled: bool = None,
        verify_detail: str = None,
        verify_type: str = None,
    ):
        self.protect_level = protect_level
        self.risk_control_enabled = risk_control_enabled
        self.verify_detail = verify_detail
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_level is not None:
            result['ProtectLevel'] = self.protect_level
        if self.risk_control_enabled is not None:
            result['RiskControlEnabled'] = self.risk_control_enabled
        if self.verify_detail is not None:
            result['VerifyDetail'] = self.verify_detail
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectLevel') is not None:
            self.protect_level = m.get('ProtectLevel')
        if m.get('RiskControlEnabled') is not None:
            self.risk_control_enabled = m.get('RiskControlEnabled')
        if m.get('VerifyDetail') is not None:
            self.verify_detail = m.get('VerifyDetail')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class EnterpriseAccountQueryLoginSettingsResponseBodyData(TeaModel):
    def __init__(
        self,
        ip_mask_dto: EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto = None,
        mfa_bind_status: str = None,
        risk_control_dto: EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto = None,
        security_mobile_login_status: str = None,
        session_expire_time: int = None,
    ):
        self.ip_mask_dto = ip_mask_dto
        self.mfa_bind_status = mfa_bind_status
        self.risk_control_dto = risk_control_dto
        self.security_mobile_login_status = security_mobile_login_status
        self.session_expire_time = session_expire_time

    def validate(self):
        if self.ip_mask_dto:
            self.ip_mask_dto.validate()
        if self.risk_control_dto:
            self.risk_control_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_mask_dto is not None:
            result['IpMaskDto'] = self.ip_mask_dto.to_map()
        if self.mfa_bind_status is not None:
            result['MfaBindStatus'] = self.mfa_bind_status
        if self.risk_control_dto is not None:
            result['RiskControlDto'] = self.risk_control_dto.to_map()
        if self.security_mobile_login_status is not None:
            result['SecurityMobileLoginStatus'] = self.security_mobile_login_status
        if self.session_expire_time is not None:
            result['SessionExpireTime'] = self.session_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpMaskDto') is not None:
            temp_model = EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto()
            self.ip_mask_dto = temp_model.from_map(m['IpMaskDto'])
        if m.get('MfaBindStatus') is not None:
            self.mfa_bind_status = m.get('MfaBindStatus')
        if m.get('RiskControlDto') is not None:
            temp_model = EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto()
            self.risk_control_dto = temp_model.from_map(m['RiskControlDto'])
        if m.get('SecurityMobileLoginStatus') is not None:
            self.security_mobile_login_status = m.get('SecurityMobileLoginStatus')
        if m.get('SessionExpireTime') is not None:
            self.session_expire_time = m.get('SessionExpireTime')
        return self


class EnterpriseAccountQueryLoginSettingsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnterpriseAccountQueryLoginSettingsResponseBodyData = None,
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
            temp_model = EnterpriseAccountQueryLoginSettingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountQueryLoginSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountQueryLoginSettingsResponseBody = None,
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
            temp_model = EnterpriseAccountQueryLoginSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountRemoveMfaRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnterpriseAccountRemoveMfaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountRemoveMfaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountRemoveMfaResponseBody = None,
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
            temp_model = EnterpriseAccountRemoveMfaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountSeparateEaRequest(TeaModel):
    def __init__(
        self,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
    ):
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class EnterpriseAccountSeparateEaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountSeparateEaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountSeparateEaResponseBody = None,
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
            temp_model = EnterpriseAccountSeparateEaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateAccountAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        app_name: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
    ):
        self.alias = alias
        self.app_name = app_name
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnterpriseAccountUpdateAccountAliasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountUpdateAccountAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateAccountAliasResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateAccountAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateAccountBizRoleGrantRequest(TeaModel):
    def __init__(
        self,
        biz_role_code_list_json: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
    ):
        self.biz_role_code_list_json = biz_role_code_list_json
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_code_list_json is not None:
            result['BizRoleCodeListJson'] = self.biz_role_code_list_json
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCodeListJson') is not None:
            self.biz_role_code_list_json = m.get('BizRoleCodeListJson')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class EnterpriseAccountUpdateAccountBizRoleGrantResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountUpdateAccountBizRoleGrantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateAccountBizRoleGrantResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateAccountBizRoleGrantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateIpMaskRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        ip_masks_json: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.ip_masks_json = ip_masks_json
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ip_masks_json is not None:
            result['IpMasksJson'] = self.ip_masks_json
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('IpMasksJson') is not None:
            self.ip_masks_json = m.get('IpMasksJson')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnterpriseAccountUpdateIpMaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountUpdateIpMaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateIpMaskResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateIpMaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateOperateRiskControlRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        product_level: str = None,
        request_id: str = None,
        validate_type: str = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.product_level = product_level
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.validate_type = validate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.product_level is not None:
            result['ProductLevel'] = self.product_level
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProductLevel') is not None:
            self.product_level = m.get('ProductLevel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')
        return self


class EnterpriseAccountUpdateOperateRiskControlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountUpdateOperateRiskControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateOperateRiskControlResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateOperateRiskControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateSecurityMobileLoginStatusRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnterpriseAccountUpdateSecurityMobileLoginStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        pass_: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.pass_ = pass_
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
        if self.message is not None:
            result['Message'] = self.message
        if self.pass_ is not None:
            result['Pass'] = self.pass_
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseAccountUpdateSecurityMobileLoginStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateSecurityMobileLoginStatusResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateSecurityMobileLoginStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseAccountUpdateSessionExpireTimeRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        session_expire_time: int = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.session_expire_time = session_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_expire_time is not None:
            result['SessionExpireTime'] = self.session_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionExpireTime') is not None:
            self.session_expire_time = m.get('SessionExpireTime')
        return self


class EnterpriseAccountUpdateSessionExpireTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseAccountUpdateSessionExpireTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseAccountUpdateSessionExpireTimeResponseBody = None,
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
            temp_model = EnterpriseAccountUpdateSessionExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseOrgQueryLoadTreeRequest(TeaModel):
    def __init__(
        self,
        encrypt_ticket: str = None,
        load_org_only: bool = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        request_id: str = None,
    ):
        self.encrypt_ticket = encrypt_ticket
        self.load_org_only = load_org_only
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.load_org_only is not None:
            result['LoadOrgOnly'] = self.load_org_only
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('LoadOrgOnly') is not None:
            self.load_org_only = m.get('LoadOrgOnly')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnterpriseOrgQueryLoadTreeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tree_dto: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tree_dto = tree_dto

    def validate(self):
        pass

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
        if self.success is not None:
            result['Success'] = self.success
        if self.tree_dto is not None:
            result['TreeDto'] = self.tree_dto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TreeDto') is not None:
            self.tree_dto = m.get('TreeDto')
        return self


class EnterpriseOrgQueryLoadTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseOrgQueryLoadTreeResponseBody = None,
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
            temp_model = EnterpriseOrgQueryLoadTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRegisterAccountRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        encrypt_password: str = None,
        encrypt_ticket: str = None,
        login_email: str = None,
        organization_id: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        request_id: str = None,
        show_complete_info: bool = None,
        site_nick: str = None,
    ):
        self.alias = alias
        self.encrypt_password = encrypt_password
        self.encrypt_ticket = encrypt_ticket
        self.login_email = login_email
        self.organization_id = organization_id
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.request_id = request_id
        self.show_complete_info = show_complete_info
        self.site_nick = site_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.encrypt_password is not None:
            result['EncryptPassword'] = self.encrypt_password
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        if self.site_nick is not None:
            result['SiteNick'] = self.site_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('EncryptPassword') is not None:
            self.encrypt_password = m.get('EncryptPassword')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        if m.get('SiteNick') is not None:
            self.site_nick = m.get('SiteNick')
        return self


class EnterpriseRegisterAccountResponseBodyAccountInfo(TeaModel):
    def __init__(
        self,
        enterprise_license_no: str = None,
        enterprise_name: str = None,
        login_id: str = None,
        pk: str = None,
    ):
        self.enterprise_license_no = enterprise_license_no
        self.enterprise_name = enterprise_name
        self.login_id = login_id
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enterprise_license_no is not None:
            result['EnterpriseLicenseNo'] = self.enterprise_license_no
        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name
        if self.login_id is not None:
            result['LoginId'] = self.login_id
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseLicenseNo') is not None:
            self.enterprise_license_no = m.get('EnterpriseLicenseNo')
        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')
        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class EnterpriseRegisterAccountResponseBody(TeaModel):
    def __init__(
        self,
        account_info: EnterpriseRegisterAccountResponseBodyAccountInfo = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_info = account_info
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_info:
            self.account_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info is not None:
            result['AccountInfo'] = self.account_info.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountInfo') is not None:
            temp_model = EnterpriseRegisterAccountResponseBodyAccountInfo()
            self.account_info = temp_model.from_map(m['AccountInfo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseRegisterAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRegisterAccountResponseBody = None,
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
            temp_model = EnterpriseRegisterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleCreateBizRoleRequest(TeaModel):
    def __init__(
        self,
        biz_permission_code_list_json: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        resource_type: str = None,
    ):
        self.biz_permission_code_list_json = biz_permission_code_list_json
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_permission_code_list_json is not None:
            result['BizPermissionCodeListJson'] = self.biz_permission_code_list_json
        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc
        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCodeListJson') is not None:
            self.biz_permission_code_list_json = m.get('BizPermissionCodeListJson')
        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')
        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class EnterpriseRoleCreateBizRoleResponseBody(TeaModel):
    def __init__(
        self,
        biz_role_code: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_role_code = biz_role_code
        self.code = code
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
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseRoleCreateBizRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleCreateBizRoleResponseBody = None,
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
            temp_model = EnterpriseRoleCreateBizRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleDeleteBizRoleRequest(TeaModel):
    def __init__(
        self,
        biz_role_code: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        self.biz_role_code = biz_role_code
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        return self


class EnterpriseRoleDeleteBizRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseRoleDeleteBizRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleDeleteBizRoleResponseBody = None,
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
            temp_model = EnterpriseRoleDeleteBizRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleQueryAccountForRoleGrantByPageRequest(TeaModel):
    def __init__(
        self,
        biz_role_code: str = None,
        encrypt_ticket: str = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page_no: int = None,
        page_size: int = None,
        query: str = None,
        show_complete_info: bool = None,
    ):
        self.biz_role_code = biz_role_code
        self.encrypt_ticket = encrypt_ticket
        self.max_results = max_results
        self.next_token = next_token
        self.org_id = org_id
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page_no = page_no
        self.page_size = page_size
        self.query = query
        self.show_complete_info = show_complete_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        return self


class EnterpriseRoleQueryAccountForRoleGrantByPageResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        alias: str = None,
        aliyun_id: str = None,
        granted: bool = None,
        pk: str = None,
    ):
        self.alias = alias
        self.aliyun_id = aliyun_id
        self.granted = granted
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.granted is not None:
            result['Granted'] = self.granted
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Granted') is not None:
            self.granted = m.get('Granted')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class EnterpriseRoleQueryAccountForRoleGrantByPageResponseBody(TeaModel):
    def __init__(
        self,
        accounts: List[EnterpriseRoleQueryAccountForRoleGrantByPageResponseBodyAccounts] = None,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.accounts = accounts
        self.code = code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = EnterpriseRoleQueryAccountForRoleGrantByPageResponseBodyAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class EnterpriseRoleQueryAccountForRoleGrantByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleQueryAccountForRoleGrantByPageResponseBody = None,
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
            temp_model = EnterpriseRoleQueryAccountForRoleGrantByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleQueryBizRoleByPageRequest(TeaModel):
    def __init__(
        self,
        encrypt_ticket: str = None,
        max_results: int = None,
        next_token: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page_no: int = None,
        page_size: int = None,
        query: str = None,
        resource_type: str = None,
        src_type: str = None,
    ):
        self.encrypt_ticket = encrypt_ticket
        self.max_results = max_results
        self.next_token = next_token
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page_no = page_no
        self.page_size = page_size
        self.query = query
        self.resource_type = resource_type
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        return self


class EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles(TeaModel):
    def __init__(
        self,
        biz_permission_count: int = None,
        biz_permission_name_list: List[str] = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        granted_pk_count: int = None,
        resource_type: str = None,
        src_type: str = None,
    ):
        self.biz_permission_count = biz_permission_count
        self.biz_permission_name_list = biz_permission_name_list
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.granted_pk_count = granted_pk_count
        self.resource_type = resource_type
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_permission_count is not None:
            result['BizPermissionCount'] = self.biz_permission_count
        if self.biz_permission_name_list is not None:
            result['BizPermissionNameList'] = self.biz_permission_name_list
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc
        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name
        if self.granted_pk_count is not None:
            result['GrantedPkCount'] = self.granted_pk_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCount') is not None:
            self.biz_permission_count = m.get('BizPermissionCount')
        if m.get('BizPermissionNameList') is not None:
            self.biz_permission_name_list = m.get('BizPermissionNameList')
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')
        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')
        if m.get('GrantedPkCount') is not None:
            self.granted_pk_count = m.get('GrantedPkCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        return self


class EnterpriseRoleQueryBizRoleByPageResponseBody(TeaModel):
    def __init__(
        self,
        biz_roles: List[EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles] = None,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.biz_roles = biz_roles
        self.code = code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.biz_roles:
            for k in self.biz_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizRoles'] = []
        if self.biz_roles is not None:
            for k in self.biz_roles:
                result['BizRoles'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_roles = []
        if m.get('BizRoles') is not None:
            for k in m.get('BizRoles'):
                temp_model = EnterpriseRoleQueryBizRoleByPageResponseBodyBizRoles()
                self.biz_roles.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class EnterpriseRoleQueryBizRoleByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleQueryBizRoleByPageResponseBody = None,
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
            temp_model = EnterpriseRoleQueryBizRoleByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleQueryBizRoleDetailRequest(TeaModel):
    def __init__(
        self,
        biz_role_code: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        self.biz_role_code = biz_role_code
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        return self


class EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions(TeaModel):
    def __init__(
        self,
        biz_permission_code: str = None,
        biz_permission_desc: str = None,
        biz_permission_name: str = None,
    ):
        self.biz_permission_code = biz_permission_code
        self.biz_permission_desc = biz_permission_desc
        self.biz_permission_name = biz_permission_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_permission_code is not None:
            result['BizPermissionCode'] = self.biz_permission_code
        if self.biz_permission_desc is not None:
            result['BizPermissionDesc'] = self.biz_permission_desc
        if self.biz_permission_name is not None:
            result['BizPermissionName'] = self.biz_permission_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCode') is not None:
            self.biz_permission_code = m.get('BizPermissionCode')
        if m.get('BizPermissionDesc') is not None:
            self.biz_permission_desc = m.get('BizPermissionDesc')
        if m.get('BizPermissionName') is not None:
            self.biz_permission_name = m.get('BizPermissionName')
        return self


class EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail(TeaModel):
    def __init__(
        self,
        biz_permissions: List[EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions] = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        resource_type: str = None,
        src_type: str = None,
    ):
        self.biz_permissions = biz_permissions
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.resource_type = resource_type
        self.src_type = src_type

    def validate(self):
        if self.biz_permissions:
            for k in self.biz_permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizPermissions'] = []
        if self.biz_permissions is not None:
            for k in self.biz_permissions:
                result['BizPermissions'].append(k.to_map() if k else None)
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc
        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_permissions = []
        if m.get('BizPermissions') is not None:
            for k in m.get('BizPermissions'):
                temp_model = EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetailBizPermissions()
                self.biz_permissions.append(temp_model.from_map(k))
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')
        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        return self


class EnterpriseRoleQueryBizRoleDetailResponseBody(TeaModel):
    def __init__(
        self,
        biz_role_detail: EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_role_detail = biz_role_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.biz_role_detail:
            self.biz_role_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_role_detail is not None:
            result['BizRoleDetail'] = self.biz_role_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleDetail') is not None:
            temp_model = EnterpriseRoleQueryBizRoleDetailResponseBodyBizRoleDetail()
            self.biz_role_detail = temp_model.from_map(m['BizRoleDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseRoleQueryBizRoleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleQueryBizRoleDetailResponseBody = None,
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
            temp_model = EnterpriseRoleQueryBizRoleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseRoleUpdateBizRoleRequest(TeaModel):
    def __init__(
        self,
        biz_permission_code_list_json: str = None,
        biz_role_code: str = None,
        biz_role_desc: str = None,
        biz_role_name: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        self.biz_permission_code_list_json = biz_permission_code_list_json
        self.biz_role_code = biz_role_code
        self.biz_role_desc = biz_role_desc
        self.biz_role_name = biz_role_name
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_permission_code_list_json is not None:
            result['BizPermissionCodeListJson'] = self.biz_permission_code_list_json
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code
        if self.biz_role_desc is not None:
            result['BizRoleDesc'] = self.biz_role_desc
        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizPermissionCodeListJson') is not None:
            self.biz_permission_code_list_json = m.get('BizPermissionCodeListJson')
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')
        if m.get('BizRoleDesc') is not None:
            self.biz_role_desc = m.get('BizRoleDesc')
        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        return self


class EnterpriseRoleUpdateBizRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseRoleUpdateBizRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseRoleUpdateBizRoleResponseBody = None,
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
            temp_model = EnterpriseRoleUpdateBizRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseTodoDealAccountTodoRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        remark: str = None,
        status: str = None,
        todo_id: str = None,
    ):
        self.app_name = app_name
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.remark = remark
        self.status = status
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.todo_id is not None:
            result['TodoId'] = self.todo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')
        return self


class EnterpriseTodoDealAccountTodoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class EnterpriseTodoDealAccountTodoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseTodoDealAccountTodoResponseBody = None,
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
            temp_model = EnterpriseTodoDealAccountTodoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseTodoQueryAccountTodoListRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        max_results: int = None,
        next_token: str = None,
        operate_pk: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page: int = None,
        page_size: int = None,
        show_complete_info: bool = None,
        status: str = None,
        todo_type: str = None,
    ):
        self.app_name = app_name
        self.max_results = max_results
        self.next_token = next_token
        self.operate_pk = operate_pk
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page = page
        self.page_size = page_size
        self.show_complete_info = show_complete_info
        self.status = status
        self.todo_type = todo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operate_pk is not None:
            result['OperatePk'] = self.operate_pk
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        if self.status is not None:
            result['Status'] = self.status
        if self.todo_type is not None:
            result['TodoType'] = self.todo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperatePk') is not None:
            self.operate_pk = m.get('OperatePk')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe(TeaModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for k in self.manager_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count
        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count
        result['ManagerList'] = []
        if self.manager_list is not None:
            for k in self.manager_list:
                result['ManagerList'].append(k.to_map() if k else None)
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')
        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')
        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k in m.get('ManagerList'):
                temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLeManagerList()
                self.manager_list.append(temp_model.from_map(k))
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        audit_time: int = None,
        ec_id: str = None,
        le_id: str = None,
        nb_id: str = None,
        pk: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.audit_time = audit_time
        self.ec_id = ec_id
        self.le_id = le_id
        self.nb_id = nb_id
        self.pk = pk
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe(TeaModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for k in self.manager_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count
        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count
        result['ManagerList'] = []
        if self.manager_list is not None:
            for k in self.manager_list:
                result['ManagerList'].append(k.to_map() if k else None)
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')
        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')
        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k in m.get('ManagerList'):
                temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLeManagerList()
                self.manager_list.append(temp_model.from_map(k))
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        applicant_aliyun_id: str = None,
        applicant_pk: str = None,
        apply_remark: str = None,
        apply_time: int = None,
        auditor_aliyun_id: str = None,
        auditor_pk: str = None,
        auditor_status: str = None,
        canceled_time: int = None,
        closed: bool = None,
        curr_auditor: bool = None,
        from_le: EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe = None,
        pk: str = None,
        process_list: List[EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList] = None,
        status: str = None,
        timeout_time: int = None,
        to_le: EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe = None,
        to_le_audit: bool = None,
        todo_id: str = None,
        todo_type: str = None,
        todo_view: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.applicant_aliyun_id = applicant_aliyun_id
        self.applicant_pk = applicant_pk
        self.apply_remark = apply_remark
        self.apply_time = apply_time
        self.auditor_aliyun_id = auditor_aliyun_id
        self.auditor_pk = auditor_pk
        self.auditor_status = auditor_status
        self.canceled_time = canceled_time
        self.closed = closed
        self.curr_auditor = curr_auditor
        self.from_le = from_le
        self.pk = pk
        self.process_list = process_list
        self.status = status
        self.timeout_time = timeout_time
        self.to_le = to_le
        self.to_le_audit = to_le_audit
        self.todo_id = todo_id
        self.todo_type = todo_type
        self.todo_view = todo_view

    def validate(self):
        if self.from_le:
            self.from_le.validate()
        if self.process_list:
            for k in self.process_list:
                if k:
                    k.validate()
        if self.to_le:
            self.to_le.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.applicant_aliyun_id is not None:
            result['ApplicantAliyunId'] = self.applicant_aliyun_id
        if self.applicant_pk is not None:
            result['ApplicantPk'] = self.applicant_pk
        if self.apply_remark is not None:
            result['ApplyRemark'] = self.apply_remark
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.auditor_aliyun_id is not None:
            result['AuditorAliyunId'] = self.auditor_aliyun_id
        if self.auditor_pk is not None:
            result['AuditorPk'] = self.auditor_pk
        if self.auditor_status is not None:
            result['AuditorStatus'] = self.auditor_status
        if self.canceled_time is not None:
            result['CanceledTime'] = self.canceled_time
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.curr_auditor is not None:
            result['CurrAuditor'] = self.curr_auditor
        if self.from_le is not None:
            result['FromLe'] = self.from_le.to_map()
        if self.pk is not None:
            result['Pk'] = self.pk
        result['ProcessList'] = []
        if self.process_list is not None:
            for k in self.process_list:
                result['ProcessList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time
        if self.to_le is not None:
            result['ToLe'] = self.to_le.to_map()
        if self.to_le_audit is not None:
            result['ToLeAudit'] = self.to_le_audit
        if self.todo_id is not None:
            result['TodoId'] = self.todo_id
        if self.todo_type is not None:
            result['TodoType'] = self.todo_type
        if self.todo_view is not None:
            result['TodoView'] = self.todo_view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('ApplicantAliyunId') is not None:
            self.applicant_aliyun_id = m.get('ApplicantAliyunId')
        if m.get('ApplicantPk') is not None:
            self.applicant_pk = m.get('ApplicantPk')
        if m.get('ApplyRemark') is not None:
            self.apply_remark = m.get('ApplyRemark')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('AuditorAliyunId') is not None:
            self.auditor_aliyun_id = m.get('AuditorAliyunId')
        if m.get('AuditorPk') is not None:
            self.auditor_pk = m.get('AuditorPk')
        if m.get('AuditorStatus') is not None:
            self.auditor_status = m.get('AuditorStatus')
        if m.get('CanceledTime') is not None:
            self.canceled_time = m.get('CanceledTime')
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('CurrAuditor') is not None:
            self.curr_auditor = m.get('CurrAuditor')
        if m.get('FromLe') is not None:
            temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListFromLe()
            self.from_le = temp_model.from_map(m['FromLe'])
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        self.process_list = []
        if m.get('ProcessList') is not None:
            for k in m.get('ProcessList'):
                temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListProcessList()
                self.process_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')
        if m.get('ToLe') is not None:
            temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoListToLe()
            self.to_le = temp_model.from_map(m['ToLe'])
        if m.get('ToLeAudit') is not None:
            self.to_le_audit = m.get('ToLeAudit')
        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')
        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')
        if m.get('TodoView') is not None:
            self.todo_view = m.get('TodoView')
        return self


class EnterpriseTodoQueryAccountTodoListResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        todo_list: List[EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList] = None,
    ):
        self.count = count
        self.todo_list = todo_list

    def validate(self):
        if self.todo_list:
            for k in self.todo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['TodoList'] = []
        if self.todo_list is not None:
            for k in self.todo_list:
                result['TodoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.todo_list = []
        if m.get('TodoList') is not None:
            for k in m.get('TodoList'):
                temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyDataTodoList()
                self.todo_list.append(temp_model.from_map(k))
        return self


class EnterpriseTodoQueryAccountTodoListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnterpriseTodoQueryAccountTodoListResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
            temp_model = EnterpriseTodoQueryAccountTodoListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseTodoQueryAccountTodoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseTodoQueryAccountTodoListResponseBody = None,
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
            temp_model = EnterpriseTodoQueryAccountTodoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        max_results: int = None,
        next_token: str = None,
        operate_pk: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        page: int = None,
        page_size: int = None,
        show_complete_info: bool = None,
        status: str = None,
        todo_type: str = None,
    ):
        self.app_name = app_name
        self.max_results = max_results
        self.next_token = next_token
        self.operate_pk = operate_pk
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.page = page
        self.page_size = page_size
        self.show_complete_info = show_complete_info
        self.status = status
        self.todo_type = todo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operate_pk is not None:
            result['OperatePk'] = self.operate_pk
        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id
        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id
        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.show_complete_info is not None:
            result['ShowCompleteInfo'] = self.show_complete_info
        if self.status is not None:
            result['Status'] = self.status
        if self.todo_type is not None:
            result['TodoType'] = self.todo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperatePk') is not None:
            self.operate_pk = m.get('OperatePk')
        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')
        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')
        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShowCompleteInfo') is not None:
            self.show_complete_info = m.get('ShowCompleteInfo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLeManagerList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLe(TeaModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for k in self.manager_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count
        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count
        result['ManagerList'] = []
        if self.manager_list is not None:
            for k in self.manager_list:
                result['ManagerList'].append(k.to_map() if k else None)
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')
        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')
        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k in m.get('ManagerList'):
                temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLeManagerList()
                self.manager_list.append(temp_model.from_map(k))
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListProcessList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        audit_time: int = None,
        ec_id: str = None,
        le_id: str = None,
        nb_id: str = None,
        pk: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.audit_time = audit_time
        self.ec_id = ec_id
        self.le_id = le_id
        self.nb_id = nb_id
        self.pk = pk
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLeManagerList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        pk: str = None,
        pk_encoded: str = None,
        role: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.pk = pk
        self.pk_encoded = pk_encoded
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.pk_encoded is not None:
            result['PkEncoded'] = self.pk_encoded
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('PkEncoded') is not None:
            self.pk_encoded = m.get('PkEncoded')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLe(TeaModel):
    def __init__(
        self,
        ec_id: str = None,
        le_id: str = None,
        license_number: str = None,
        manageable_account_count: int = None,
        managed_account_count: int = None,
        manager_list: List[EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLeManagerList] = None,
        nb_id: str = None,
        subject_name: str = None,
        subject_type: str = None,
    ):
        self.ec_id = ec_id
        self.le_id = le_id
        self.license_number = license_number
        self.manageable_account_count = manageable_account_count
        self.managed_account_count = managed_account_count
        self.manager_list = manager_list
        self.nb_id = nb_id
        self.subject_name = subject_name
        self.subject_type = subject_type

    def validate(self):
        if self.manager_list:
            for k in self.manager_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number
        if self.manageable_account_count is not None:
            result['ManageableAccountCount'] = self.manageable_account_count
        if self.managed_account_count is not None:
            result['ManagedAccountCount'] = self.managed_account_count
        result['ManagerList'] = []
        if self.manager_list is not None:
            for k in self.manager_list:
                result['ManagerList'].append(k.to_map() if k else None)
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.subject_name is not None:
            result['SubjectName'] = self.subject_name
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')
        if m.get('ManageableAccountCount') is not None:
            self.manageable_account_count = m.get('ManageableAccountCount')
        if m.get('ManagedAccountCount') is not None:
            self.managed_account_count = m.get('ManagedAccountCount')
        self.manager_list = []
        if m.get('ManagerList') is not None:
            for k in m.get('ManagerList'):
                temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLeManagerList()
                self.manager_list.append(temp_model.from_map(k))
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('SubjectName') is not None:
            self.subject_name = m.get('SubjectName')
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoList(TeaModel):
    def __init__(
        self,
        aliyun_id: str = None,
        applicant_aliyun_id: str = None,
        applicant_pk: str = None,
        apply_remark: str = None,
        apply_time: int = None,
        auditor_aliyun_id: str = None,
        auditor_pk: str = None,
        auditor_status: str = None,
        canceled_time: int = None,
        closed: bool = None,
        curr_auditor: bool = None,
        from_le: EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLe = None,
        pk: str = None,
        process_list: List[EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListProcessList] = None,
        status: str = None,
        timeout_time: int = None,
        to_le: EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLe = None,
        to_le_audit: bool = None,
        todo_id: str = None,
        todo_type: str = None,
        todo_view: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.applicant_aliyun_id = applicant_aliyun_id
        self.applicant_pk = applicant_pk
        self.apply_remark = apply_remark
        self.apply_time = apply_time
        self.auditor_aliyun_id = auditor_aliyun_id
        self.auditor_pk = auditor_pk
        self.auditor_status = auditor_status
        self.canceled_time = canceled_time
        self.closed = closed
        self.curr_auditor = curr_auditor
        self.from_le = from_le
        self.pk = pk
        self.process_list = process_list
        self.status = status
        self.timeout_time = timeout_time
        self.to_le = to_le
        self.to_le_audit = to_le_audit
        self.todo_id = todo_id
        self.todo_type = todo_type
        self.todo_view = todo_view

    def validate(self):
        if self.from_le:
            self.from_le.validate()
        if self.process_list:
            for k in self.process_list:
                if k:
                    k.validate()
        if self.to_le:
            self.to_le.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.applicant_aliyun_id is not None:
            result['ApplicantAliyunId'] = self.applicant_aliyun_id
        if self.applicant_pk is not None:
            result['ApplicantPk'] = self.applicant_pk
        if self.apply_remark is not None:
            result['ApplyRemark'] = self.apply_remark
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.auditor_aliyun_id is not None:
            result['AuditorAliyunId'] = self.auditor_aliyun_id
        if self.auditor_pk is not None:
            result['AuditorPk'] = self.auditor_pk
        if self.auditor_status is not None:
            result['AuditorStatus'] = self.auditor_status
        if self.canceled_time is not None:
            result['CanceledTime'] = self.canceled_time
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.curr_auditor is not None:
            result['CurrAuditor'] = self.curr_auditor
        if self.from_le is not None:
            result['FromLe'] = self.from_le.to_map()
        if self.pk is not None:
            result['Pk'] = self.pk
        result['ProcessList'] = []
        if self.process_list is not None:
            for k in self.process_list:
                result['ProcessList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time
        if self.to_le is not None:
            result['ToLe'] = self.to_le.to_map()
        if self.to_le_audit is not None:
            result['ToLeAudit'] = self.to_le_audit
        if self.todo_id is not None:
            result['TodoId'] = self.todo_id
        if self.todo_type is not None:
            result['TodoType'] = self.todo_type
        if self.todo_view is not None:
            result['TodoView'] = self.todo_view
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('ApplicantAliyunId') is not None:
            self.applicant_aliyun_id = m.get('ApplicantAliyunId')
        if m.get('ApplicantPk') is not None:
            self.applicant_pk = m.get('ApplicantPk')
        if m.get('ApplyRemark') is not None:
            self.apply_remark = m.get('ApplyRemark')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('AuditorAliyunId') is not None:
            self.auditor_aliyun_id = m.get('AuditorAliyunId')
        if m.get('AuditorPk') is not None:
            self.auditor_pk = m.get('AuditorPk')
        if m.get('AuditorStatus') is not None:
            self.auditor_status = m.get('AuditorStatus')
        if m.get('CanceledTime') is not None:
            self.canceled_time = m.get('CanceledTime')
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('CurrAuditor') is not None:
            self.curr_auditor = m.get('CurrAuditor')
        if m.get('FromLe') is not None:
            temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListFromLe()
            self.from_le = temp_model.from_map(m['FromLe'])
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        self.process_list = []
        if m.get('ProcessList') is not None:
            for k in m.get('ProcessList'):
                temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListProcessList()
                self.process_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')
        if m.get('ToLe') is not None:
            temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoListToLe()
            self.to_le = temp_model.from_map(m['ToLe'])
        if m.get('ToLeAudit') is not None:
            self.to_le_audit = m.get('ToLeAudit')
        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')
        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')
        if m.get('TodoView') is not None:
            self.todo_view = m.get('TodoView')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        todo_list: List[EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoList] = None,
    ):
        self.count = count
        self.todo_list = todo_list

    def validate(self):
        if self.todo_list:
            for k in self.todo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['TodoList'] = []
        if self.todo_list is not None:
            for k in self.todo_list:
                result['TodoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.todo_list = []
        if m.get('TodoList') is not None:
            for k in m.get('TodoList'):
                temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyDataTodoList()
                self.todo_list.append(temp_model.from_map(k))
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
            temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseTodoQueryAccountTodoListByApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseTodoQueryAccountTodoListByApplicantResponseBody = None,
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
            temp_model = EnterpriseTodoQueryAccountTodoListByApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterpriseUninvitedAdminInviteJoinEnterpriseRequest(TeaModel):
    def __init__(
        self,
        ec_id: str = None,
        encrypt_ticket: str = None,
        invitee_pk: str = None,
        le_id: str = None,
        nb_id: str = None,
        remark: str = None,
    ):
        self.ec_id = ec_id
        self.encrypt_ticket = encrypt_ticket
        self.invitee_pk = invitee_pk
        self.le_id = le_id
        self.nb_id = nb_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket
        if self.invitee_pk is not None:
            result['InviteePk'] = self.invitee_pk
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')
        if m.get('InviteePk') is not None:
            self.invitee_pk = m.get('InviteePk')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData(TeaModel):
    def __init__(
        self,
        applicant_aliyun_id: str = None,
        applicant_pk: str = None,
        apply_remark: str = None,
        apply_time: int = None,
        auditor_aliyun_id: str = None,
        auditor_pk: str = None,
        ec_id: str = None,
        le_id: str = None,
        le_license_no: str = None,
        le_name: str = None,
        message: str = None,
        nb_id: str = None,
        operated_aliyun_id: str = None,
        operated_pk: str = None,
        success: str = None,
        timeout_time: int = None,
        todo_id: str = None,
        todo_type: str = None,
    ):
        self.applicant_aliyun_id = applicant_aliyun_id
        self.applicant_pk = applicant_pk
        self.apply_remark = apply_remark
        self.apply_time = apply_time
        self.auditor_aliyun_id = auditor_aliyun_id
        self.auditor_pk = auditor_pk
        self.ec_id = ec_id
        self.le_id = le_id
        self.le_license_no = le_license_no
        self.le_name = le_name
        self.message = message
        self.nb_id = nb_id
        self.operated_aliyun_id = operated_aliyun_id
        self.operated_pk = operated_pk
        self.success = success
        self.timeout_time = timeout_time
        self.todo_id = todo_id
        self.todo_type = todo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_aliyun_id is not None:
            result['ApplicantAliyunId'] = self.applicant_aliyun_id
        if self.applicant_pk is not None:
            result['ApplicantPk'] = self.applicant_pk
        if self.apply_remark is not None:
            result['ApplyRemark'] = self.apply_remark
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.auditor_aliyun_id is not None:
            result['AuditorAliyunId'] = self.auditor_aliyun_id
        if self.auditor_pk is not None:
            result['AuditorPk'] = self.auditor_pk
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        if self.le_id is not None:
            result['LeId'] = self.le_id
        if self.le_license_no is not None:
            result['LeLicenseNo'] = self.le_license_no
        if self.le_name is not None:
            result['LeName'] = self.le_name
        if self.message is not None:
            result['Message'] = self.message
        if self.nb_id is not None:
            result['NbId'] = self.nb_id
        if self.operated_aliyun_id is not None:
            result['OperatedAliyunId'] = self.operated_aliyun_id
        if self.operated_pk is not None:
            result['OperatedPk'] = self.operated_pk
        if self.success is not None:
            result['Success'] = self.success
        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time
        if self.todo_id is not None:
            result['TodoId'] = self.todo_id
        if self.todo_type is not None:
            result['TodoType'] = self.todo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantAliyunId') is not None:
            self.applicant_aliyun_id = m.get('ApplicantAliyunId')
        if m.get('ApplicantPk') is not None:
            self.applicant_pk = m.get('ApplicantPk')
        if m.get('ApplyRemark') is not None:
            self.apply_remark = m.get('ApplyRemark')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('AuditorAliyunId') is not None:
            self.auditor_aliyun_id = m.get('AuditorAliyunId')
        if m.get('AuditorPk') is not None:
            self.auditor_pk = m.get('AuditorPk')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        if m.get('LeId') is not None:
            self.le_id = m.get('LeId')
        if m.get('LeLicenseNo') is not None:
            self.le_license_no = m.get('LeLicenseNo')
        if m.get('LeName') is not None:
            self.le_name = m.get('LeName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NbId') is not None:
            self.nb_id = m.get('NbId')
        if m.get('OperatedAliyunId') is not None:
            self.operated_aliyun_id = m.get('OperatedAliyunId')
        if m.get('OperatedPk') is not None:
            self.operated_pk = m.get('OperatedPk')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')
        if m.get('TodoId') is not None:
            self.todo_id = m.get('TodoId')
        if m.get('TodoType') is not None:
            self.todo_type = m.get('TodoType')
        return self


class EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData] = None,
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
                temp_model = EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnterpriseUninvitedAdminInviteJoinEnterpriseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBody = None,
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
            temp_model = EnterpriseUninvitedAdminInviteJoinEnterpriseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



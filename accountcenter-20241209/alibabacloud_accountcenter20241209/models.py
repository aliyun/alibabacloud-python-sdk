# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


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



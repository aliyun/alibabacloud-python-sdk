# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_appstream_center20210220 import models as main_models
from darabonba.model import DaraModel

class GetLoginTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        account_type: str = None,
        ad_domain: str = None,
        email: str = None,
        end_user_id: str = None,
        idp_id: str = None,
        industry: str = None,
        keep_alive_token: str = None,
        label: str = None,
        login_token: str = None,
        mfa_type_list: List[main_models.GetLoginTokenResponseBodyMfaTypeList] = None,
        next_stage: str = None,
        nick_name: str = None,
        office_sites: List[str] = None,
        password_strategy: main_models.GetLoginTokenResponseBodyPasswordStrategy = None,
        phone: str = None,
        props: Dict[str, str] = None,
        qr_code_png: str = None,
        reason: str = None,
        request_id: str = None,
        risk_verify_info: main_models.GetLoginTokenResponseBodyRiskVerifyInfo = None,
        secret: str = None,
        session_id: str = None,
        tenant_alias: str = None,
        tenant_id: int = None,
        tenant_infos: List[main_models.GetLoginTokenResponseBodyTenantInfos] = None,
        vpc_region_id: str = None,
        window_display_mode: str = None,
        wy_id: str = None,
    ):
        self.access_type = access_type
        self.account_type = account_type
        self.ad_domain = ad_domain
        self.email = email
        self.end_user_id = end_user_id
        self.idp_id = idp_id
        self.industry = industry
        self.keep_alive_token = keep_alive_token
        self.label = label
        self.login_token = login_token
        self.mfa_type_list = mfa_type_list
        self.next_stage = next_stage
        self.nick_name = nick_name
        self.office_sites = office_sites
        self.password_strategy = password_strategy
        self.phone = phone
        self.props = props
        self.qr_code_png = qr_code_png
        self.reason = reason
        self.request_id = request_id
        self.risk_verify_info = risk_verify_info
        self.secret = secret
        self.session_id = session_id
        self.tenant_alias = tenant_alias
        self.tenant_id = tenant_id
        self.tenant_infos = tenant_infos
        self.vpc_region_id = vpc_region_id
        self.window_display_mode = window_display_mode
        self.wy_id = wy_id

    def validate(self):
        if self.mfa_type_list:
            for v1 in self.mfa_type_list:
                 if v1:
                    v1.validate()
        if self.password_strategy:
            self.password_strategy.validate()
        if self.risk_verify_info:
            self.risk_verify_info.validate()
        if self.tenant_infos:
            for v1 in self.tenant_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.keep_alive_token is not None:
            result['KeepAliveToken'] = self.keep_alive_token

        if self.label is not None:
            result['Label'] = self.label

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        result['MfaTypeList'] = []
        if self.mfa_type_list is not None:
            for k1 in self.mfa_type_list:
                result['MfaTypeList'].append(k1.to_map() if k1 else None)

        if self.next_stage is not None:
            result['NextStage'] = self.next_stage

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.office_sites is not None:
            result['OfficeSites'] = self.office_sites

        if self.password_strategy is not None:
            result['PasswordStrategy'] = self.password_strategy.to_map()

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.props is not None:
            result['Props'] = self.props

        if self.qr_code_png is not None:
            result['QrCodePng'] = self.qr_code_png

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_verify_info is not None:
            result['RiskVerifyInfo'] = self.risk_verify_info.to_map()

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        result['TenantInfos'] = []
        if self.tenant_infos is not None:
            for k1 in self.tenant_infos:
                result['TenantInfos'].append(k1.to_map() if k1 else None)

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        if self.window_display_mode is not None:
            result['WindowDisplayMode'] = self.window_display_mode

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('KeepAliveToken') is not None:
            self.keep_alive_token = m.get('KeepAliveToken')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        self.mfa_type_list = []
        if m.get('MfaTypeList') is not None:
            for k1 in m.get('MfaTypeList'):
                temp_model = main_models.GetLoginTokenResponseBodyMfaTypeList()
                self.mfa_type_list.append(temp_model.from_map(k1))

        if m.get('NextStage') is not None:
            self.next_stage = m.get('NextStage')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OfficeSites') is not None:
            self.office_sites = m.get('OfficeSites')

        if m.get('PasswordStrategy') is not None:
            temp_model = main_models.GetLoginTokenResponseBodyPasswordStrategy()
            self.password_strategy = temp_model.from_map(m.get('PasswordStrategy'))

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('Props') is not None:
            self.props = m.get('Props')

        if m.get('QrCodePng') is not None:
            self.qr_code_png = m.get('QrCodePng')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskVerifyInfo') is not None:
            temp_model = main_models.GetLoginTokenResponseBodyRiskVerifyInfo()
            self.risk_verify_info = temp_model.from_map(m.get('RiskVerifyInfo'))

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        self.tenant_infos = []
        if m.get('TenantInfos') is not None:
            for k1 in m.get('TenantInfos'):
                temp_model = main_models.GetLoginTokenResponseBodyTenantInfos()
                self.tenant_infos.append(temp_model.from_map(k1))

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        if m.get('WindowDisplayMode') is not None:
            self.window_display_mode = m.get('WindowDisplayMode')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class GetLoginTokenResponseBodyTenantInfos(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        tenant_alias: str = None,
    ):
        self.access_type = access_type
        self.tenant_alias = tenant_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')

        return self

class GetLoginTokenResponseBodyRiskVerifyInfo(DaraModel):
    def __init__(
        self,
        email: str = None,
        last_lock_duration: int = None,
        locked: bool = None,
        phone: str = None,
    ):
        self.email = email
        self.last_lock_duration = last_lock_duration
        self.locked = locked
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.last_lock_duration is not None:
            result['LastLockDuration'] = self.last_lock_duration

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('LastLockDuration') is not None:
            self.last_lock_duration = m.get('LastLockDuration')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

class GetLoginTokenResponseBodyPasswordStrategy(DaraModel):
    def __init__(
        self,
        tenant_alternative_chars: List[str] = None,
        tenant_password_length: int = None,
    ):
        self.tenant_alternative_chars = tenant_alternative_chars
        self.tenant_password_length = tenant_password_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_alternative_chars is not None:
            result['TenantAlternativeChars'] = self.tenant_alternative_chars

        if self.tenant_password_length is not None:
            result['TenantPasswordLength'] = self.tenant_password_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantAlternativeChars') is not None:
            self.tenant_alternative_chars = m.get('TenantAlternativeChars')

        if m.get('TenantPasswordLength') is not None:
            self.tenant_password_length = m.get('TenantPasswordLength')

        return self

class GetLoginTokenResponseBodyMfaTypeList(DaraModel):
    def __init__(
        self,
        name: str = None,
        stage: str = None,
    ):
        self.name = name
        self.stage = stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.stage is not None:
            result['Stage'] = self.stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        return self


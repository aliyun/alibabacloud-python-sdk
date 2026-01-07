# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseAccountQueryAccountsInfoResponseBody(DaraModel):
    def __init__(
        self,
        account_info_dto_list: List[main_models.EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList] = None,
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
            for v1 in self.account_info_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountInfoDtoList'] = []
        if self.account_info_dto_list is not None:
            for k1 in self.account_info_dto_list:
                result['AccountInfoDtoList'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('AccountInfoDtoList'):
                temp_model = main_models.EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList()
                self.account_info_dto_list.append(temp_model.from_map(k1))

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

class EnterpriseAccountQueryAccountsInfoResponseBodyAccountInfoDtoList(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


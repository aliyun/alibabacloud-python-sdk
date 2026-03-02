# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetAccountSecurityPracticeReportResponseBody(DaraModel):
    def __init__(
        self,
        account_security_practice_info: main_models.GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo = None,
        request_id: str = None,
    ):
        self.account_security_practice_info = account_security_practice_info
        self.request_id = request_id

    def validate(self):
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_security_practice_info is not None:
            result['AccountSecurityPracticeInfo'] = self.account_security_practice_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPracticeInfo') is not None:
            temp_model = main_models.GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(m.get('AccountSecurityPracticeInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo(DaraModel):
    def __init__(
        self,
        account_security_practice_user_info: main_models.GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo = None,
        score: int = None,
    ):
        self.account_security_practice_user_info = account_security_practice_user_info
        self.score = score

    def validate(self):
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = main_models.GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(m.get('AccountSecurityPracticeUserInfo'))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(DaraModel):
    def __init__(
        self,
        bind_mfa: bool = None,
        old_ak_num: int = None,
        root_with_access_key: int = None,
        sub_user: int = None,
        sub_user_bind_mfa: int = None,
        sub_user_pwd_level: str = None,
        sub_user_with_old_access_key: int = None,
        sub_user_with_unused_access_key: int = None,
        unused_ak_num: int = None,
    ):
        self.bind_mfa = bind_mfa
        self.old_ak_num = old_ak_num
        self.root_with_access_key = root_with_access_key
        self.sub_user = sub_user
        self.sub_user_bind_mfa = sub_user_bind_mfa
        self.sub_user_pwd_level = sub_user_pwd_level
        self.sub_user_with_old_access_key = sub_user_with_old_access_key
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key
        self.unused_ak_num = unused_ak_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa

        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num

        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key

        if self.sub_user is not None:
            result['SubUser'] = self.sub_user

        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa

        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level

        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key

        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key

        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindMfa') is not None:
            self.bind_mfa = m.get('BindMfa')

        if m.get('OldAkNum') is not None:
            self.old_ak_num = m.get('OldAkNum')

        if m.get('RootWithAccessKey') is not None:
            self.root_with_access_key = m.get('RootWithAccessKey')

        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')

        if m.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = m.get('SubUserBindMfa')

        if m.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = m.get('SubUserPwdLevel')

        if m.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = m.get('SubUserWithOldAccessKey')

        if m.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = m.get('SubUserWithUnusedAccessKey')

        if m.get('UnusedAkNum') is not None:
            self.unused_ak_num = m.get('UnusedAkNum')

        return self


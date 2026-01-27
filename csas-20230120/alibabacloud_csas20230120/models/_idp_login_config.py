# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpLoginConfig(DaraModel):
    def __init__(
        self,
        mobile_login_type: str = None,
        mobile_mfa_types: str = None,
        pc_login_type: str = None,
        pc_mfa_types: str = None,
        totp_corp_verify_aes_key: str = None,
        totp_corp_verify_token: str = None,
        totp_corp_verify_url: str = None,
    ):
        self.mobile_login_type = mobile_login_type
        self.mobile_mfa_types = mobile_mfa_types
        self.pc_login_type = pc_login_type
        self.pc_mfa_types = pc_mfa_types
        self.totp_corp_verify_aes_key = totp_corp_verify_aes_key
        self.totp_corp_verify_token = totp_corp_verify_token
        self.totp_corp_verify_url = totp_corp_verify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_login_type is not None:
            result['MobileLoginType'] = self.mobile_login_type

        if self.mobile_mfa_types is not None:
            result['MobileMfaTypes'] = self.mobile_mfa_types

        if self.pc_login_type is not None:
            result['PcLoginType'] = self.pc_login_type

        if self.pc_mfa_types is not None:
            result['PcMfaTypes'] = self.pc_mfa_types

        if self.totp_corp_verify_aes_key is not None:
            result['TotpCorpVerifyAesKey'] = self.totp_corp_verify_aes_key

        if self.totp_corp_verify_token is not None:
            result['TotpCorpVerifyToken'] = self.totp_corp_verify_token

        if self.totp_corp_verify_url is not None:
            result['TotpCorpVerifyUrl'] = self.totp_corp_verify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileLoginType') is not None:
            self.mobile_login_type = m.get('MobileLoginType')

        if m.get('MobileMfaTypes') is not None:
            self.mobile_mfa_types = m.get('MobileMfaTypes')

        if m.get('PcLoginType') is not None:
            self.pc_login_type = m.get('PcLoginType')

        if m.get('PcMfaTypes') is not None:
            self.pc_mfa_types = m.get('PcMfaTypes')

        if m.get('TotpCorpVerifyAesKey') is not None:
            self.totp_corp_verify_aes_key = m.get('TotpCorpVerifyAesKey')

        if m.get('TotpCorpVerifyToken') is not None:
            self.totp_corp_verify_token = m.get('TotpCorpVerifyToken')

        if m.get('TotpCorpVerifyUrl') is not None:
            self.totp_corp_verify_url = m.get('TotpCorpVerifyUrl')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgAccountRequest(DaraModel):
    def __init__(
        self,
        login_email: str = None,
        mpk: str = None,
        nation_code: str = None,
        own: str = None,
        real_parent_pk: str = None,
        security_mobile: str = None,
        show_nick_name: str = None,
        site_nick: str = None,
        src_account_info: str = None,
    ):
        self.login_email = login_email
        # This parameter is required.
        self.mpk = mpk
        self.nation_code = nation_code
        self.own = own
        self.real_parent_pk = real_parent_pk
        self.security_mobile = security_mobile
        self.show_nick_name = show_nick_name
        self.site_nick = site_nick
        self.src_account_info = src_account_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.nation_code is not None:
            result['NationCode'] = self.nation_code

        if self.own is not None:
            result['Own'] = self.own

        if self.real_parent_pk is not None:
            result['RealParentPk'] = self.real_parent_pk

        if self.security_mobile is not None:
            result['SecurityMobile'] = self.security_mobile

        if self.show_nick_name is not None:
            result['ShowNickName'] = self.show_nick_name

        if self.site_nick is not None:
            result['SiteNick'] = self.site_nick

        if self.src_account_info is not None:
            result['srcAccountInfo'] = self.src_account_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('NationCode') is not None:
            self.nation_code = m.get('NationCode')

        if m.get('Own') is not None:
            self.own = m.get('Own')

        if m.get('RealParentPk') is not None:
            self.real_parent_pk = m.get('RealParentPk')

        if m.get('SecurityMobile') is not None:
            self.security_mobile = m.get('SecurityMobile')

        if m.get('ShowNickName') is not None:
            self.show_nick_name = m.get('ShowNickName')

        if m.get('SiteNick') is not None:
            self.site_nick = m.get('SiteNick')

        if m.get('srcAccountInfo') is not None:
            self.src_account_info = m.get('srcAccountInfo')

        return self


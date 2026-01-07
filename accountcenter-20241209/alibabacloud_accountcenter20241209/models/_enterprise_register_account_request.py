# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseRegisterAccountRequest(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseUninvitedAdminInviteJoinEnterpriseRequest(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


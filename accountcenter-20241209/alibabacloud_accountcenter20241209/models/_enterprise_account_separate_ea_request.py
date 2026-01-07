# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseAccountSeparateEaRequest(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


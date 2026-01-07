# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseOrgQueryLoadTreeRequest(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


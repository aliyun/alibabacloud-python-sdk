# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseRoleQueryBizRoleDetailRequest(DaraModel):
    def __init__(
        self,
        biz_role_code: str = None,
        encrypt_ticket: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
    ):
        self.biz_role_code = biz_role_code
        self.encrypt_ticket = encrypt_ticket
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        return self


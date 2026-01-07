# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseAccountChangeSecurityMobileRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        encrypt_ticket: str = None,
        new_mobile: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        pk: str = None,
        request_id: str = None,
        verification_code: str = None,
    ):
        self.app_name = app_name
        self.encrypt_ticket = encrypt_ticket
        # This parameter is required.
        self.new_mobile = new_mobile
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.request_id = request_id
        # This parameter is required.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.encrypt_ticket is not None:
            result['EncryptTicket'] = self.encrypt_ticket

        if self.new_mobile is not None:
            result['NewMobile'] = self.new_mobile

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('EncryptTicket') is not None:
            self.encrypt_ticket = m.get('EncryptTicket')

        if m.get('NewMobile') is not None:
            self.new_mobile = m.get('NewMobile')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self


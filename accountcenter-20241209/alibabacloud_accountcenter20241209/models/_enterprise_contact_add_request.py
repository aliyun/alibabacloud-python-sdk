# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnterpriseContactAddRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        async_email_verify: bool = None,
        async_mobile_verify: bool = None,
        contact_email: str = None,
        contact_mobile: str = None,
        contact_name: str = None,
        contact_position: str = None,
        email_code: str = None,
        mobile_code: str = None,
        oriented_ec_id: str = None,
        oriented_le_id: str = None,
        oriented_nb_id: str = None,
        shared_contact: bool = None,
    ):
        self.app_name = app_name
        self.async_email_verify = async_email_verify
        self.async_mobile_verify = async_mobile_verify
        self.contact_email = contact_email
        self.contact_mobile = contact_mobile
        self.contact_name = contact_name
        self.contact_position = contact_position
        self.email_code = email_code
        self.mobile_code = mobile_code
        self.oriented_ec_id = oriented_ec_id
        self.oriented_le_id = oriented_le_id
        self.oriented_nb_id = oriented_nb_id
        self.shared_contact = shared_contact

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.async_email_verify is not None:
            result['AsyncEmailVerify'] = self.async_email_verify

        if self.async_mobile_verify is not None:
            result['AsyncMobileVerify'] = self.async_mobile_verify

        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.contact_position is not None:
            result['ContactPosition'] = self.contact_position

        if self.email_code is not None:
            result['EmailCode'] = self.email_code

        if self.mobile_code is not None:
            result['MobileCode'] = self.mobile_code

        if self.oriented_ec_id is not None:
            result['OrientedEcId'] = self.oriented_ec_id

        if self.oriented_le_id is not None:
            result['OrientedLeId'] = self.oriented_le_id

        if self.oriented_nb_id is not None:
            result['OrientedNbId'] = self.oriented_nb_id

        if self.shared_contact is not None:
            result['SharedContact'] = self.shared_contact

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AsyncEmailVerify') is not None:
            self.async_email_verify = m.get('AsyncEmailVerify')

        if m.get('AsyncMobileVerify') is not None:
            self.async_mobile_verify = m.get('AsyncMobileVerify')

        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('ContactPosition') is not None:
            self.contact_position = m.get('ContactPosition')

        if m.get('EmailCode') is not None:
            self.email_code = m.get('EmailCode')

        if m.get('MobileCode') is not None:
            self.mobile_code = m.get('MobileCode')

        if m.get('OrientedEcId') is not None:
            self.oriented_ec_id = m.get('OrientedEcId')

        if m.get('OrientedLeId') is not None:
            self.oriented_le_id = m.get('OrientedLeId')

        if m.get('OrientedNbId') is not None:
            self.oriented_nb_id = m.get('OrientedNbId')

        if m.get('SharedContact') is not None:
            self.shared_contact = m.get('SharedContact')

        return self


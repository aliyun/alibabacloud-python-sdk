# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContactsRequest(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_id: int = None,
        contact_name: str = None,
        contact_phone: str = None,
        mail_status: int = None,
        open_status_warning: bool = None,
        opent_attribution_warning: bool = None,
        owner_id: int = None,
        phone_status: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.contact_email = contact_email
        # This parameter is required.
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.mail_status = mail_status
        self.open_status_warning = open_status_warning
        self.opent_attribution_warning = opent_attribution_warning
        self.owner_id = owner_id
        self.phone_status = phone_status
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone

        if self.mail_status is not None:
            result['MailStatus'] = self.mail_status

        if self.open_status_warning is not None:
            result['OpenStatusWarning'] = self.open_status_warning

        if self.opent_attribution_warning is not None:
            result['OpentAttributionWarning'] = self.opent_attribution_warning

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_status is not None:
            result['PhoneStatus'] = self.phone_status

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')

        if m.get('MailStatus') is not None:
            self.mail_status = m.get('MailStatus')

        if m.get('OpenStatusWarning') is not None:
            self.open_status_warning = m.get('OpenStatusWarning')

        if m.get('OpentAttributionWarning') is not None:
            self.opent_attribution_warning = m.get('OpentAttributionWarning')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneStatus') is not None:
            self.phone_status = m.get('PhoneStatus')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self


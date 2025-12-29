# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class ListContactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListContactsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListContactsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListContactsResponseBodyData(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_id: int = None,
        contact_name: str = None,
        contact_phone: str = None,
        mail_status: int = None,
        main: int = None,
        open_status_warning: bool = None,
        opent_attribution_warning: bool = None,
        phone_status: int = None,
    ):
        self.contact_email = contact_email
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.mail_status = mail_status
        self.main = main
        self.open_status_warning = open_status_warning
        self.opent_attribution_warning = opent_attribution_warning
        self.phone_status = phone_status

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

        if self.main is not None:
            result['Main'] = self.main

        if self.open_status_warning is not None:
            result['OpenStatusWarning'] = self.open_status_warning

        if self.opent_attribution_warning is not None:
            result['OpentAttributionWarning'] = self.opent_attribution_warning

        if self.phone_status is not None:
            result['PhoneStatus'] = self.phone_status

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

        if m.get('Main') is not None:
            self.main = m.get('Main')

        if m.get('OpenStatusWarning') is not None:
            self.open_status_warning = m.get('OpenStatusWarning')

        if m.get('OpentAttributionWarning') is not None:
            self.opent_attribution_warning = m.get('OpentAttributionWarning')

        if m.get('PhoneStatus') is not None:
            self.phone_status = m.get('PhoneStatus')

        return self


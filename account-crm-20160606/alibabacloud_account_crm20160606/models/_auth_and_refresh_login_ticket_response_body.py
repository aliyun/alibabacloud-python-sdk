# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class AuthAndRefreshLoginTicketResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AuthAndRefreshLoginTicketResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AuthAndRefreshLoginTicketResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AuthAndRefreshLoginTicketResponseBodyData(DaraModel):
    def __init__(
        self,
        new_login_ticket: str = None,
    ):
        self.new_login_ticket = new_login_ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_login_ticket is not None:
            result['NewLoginTicket'] = self.new_login_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewLoginTicket') is not None:
            self.new_login_ticket = m.get('NewLoginTicket')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class AuthLoginTicketResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        login_ticket_dto: main_models.AuthLoginTicketResponseBodyLoginTicketDto = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.login_ticket_dto = login_ticket_dto
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.login_ticket_dto:
            self.login_ticket_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.login_ticket_dto is not None:
            result['LoginTicketDto'] = self.login_ticket_dto.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LoginTicketDto') is not None:
            temp_model = main_models.AuthLoginTicketResponseBodyLoginTicketDto()
            self.login_ticket_dto = temp_model.from_map(m.get('LoginTicketDto'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AuthLoginTicketResponseBodyLoginTicketDto(DaraModel):
    def __init__(
        self,
        login_ticket: str = None,
    ):
        self.login_ticket = login_ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginTicket') is not None:
            self.login_ticket = m.get('LoginTicket')

        return self


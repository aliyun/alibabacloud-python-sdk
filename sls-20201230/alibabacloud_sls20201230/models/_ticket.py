# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Ticket(DaraModel):
    def __init__(
        self,
        caller_uid: int = None,
        create_date: str = None,
        expiration_time: int = None,
        expire_date: str = None,
        extra: str = None,
        name: str = None,
        number: int = None,
        sharing_to: str = None,
        ticket: str = None,
        ticket_id: str = None,
        used_number: int = None,
        valid: bool = None,
    ):
        self.caller_uid = caller_uid
        self.create_date = create_date
        self.expiration_time = expiration_time
        self.expire_date = expire_date
        self.extra = extra
        self.name = name
        self.number = number
        self.sharing_to = sharing_to
        self.ticket = ticket
        self.ticket_id = ticket_id
        self.used_number = used_number
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid

        if self.create_date is not None:
            result['createDate'] = self.create_date

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.expire_date is not None:
            result['expireDate'] = self.expire_date

        if self.extra is not None:
            result['extra'] = self.extra

        if self.name is not None:
            result['name'] = self.name

        if self.number is not None:
            result['number'] = self.number

        if self.sharing_to is not None:
            result['sharingTo'] = self.sharing_to

        if self.ticket is not None:
            result['ticket'] = self.ticket

        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id

        if self.used_number is not None:
            result['usedNumber'] = self.used_number

        if self.valid is not None:
            result['valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')

        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('sharingTo') is not None:
            self.sharing_to = m.get('sharingTo')

        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')

        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')

        if m.get('usedNumber') is not None:
            self.used_number = m.get('usedNumber')

        if m.get('valid') is not None:
            self.valid = m.get('valid')

        return self


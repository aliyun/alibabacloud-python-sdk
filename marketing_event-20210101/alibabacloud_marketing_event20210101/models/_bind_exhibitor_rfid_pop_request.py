# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindExhibitorRfidPopRequest(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        device_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        guest_ticket_record_id: int = None,
        id: int = None,
        rfid: str = None,
        ticket_code: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.device_id = device_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guest_ticket_record_id = guest_ticket_record_id
        self.id = id
        # This parameter is required.
        self.rfid = rfid
        # This parameter is required.
        self.ticket_code = ticket_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.guest_ticket_record_id is not None:
            result['GuestTicketRecordId'] = self.guest_ticket_record_id

        if self.id is not None:
            result['Id'] = self.id

        if self.rfid is not None:
            result['Rfid'] = self.rfid

        if self.ticket_code is not None:
            result['TicketCode'] = self.ticket_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GuestTicketRecordId') is not None:
            self.guest_ticket_record_id = m.get('GuestTicketRecordId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Rfid') is not None:
            self.rfid = m.get('Rfid')

        if m.get('TicketCode') is not None:
            self.ticket_code = m.get('TicketCode')

        return self


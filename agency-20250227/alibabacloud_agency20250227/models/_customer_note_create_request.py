# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomerNoteCreateRequest(DaraModel):
    def __init__(
        self,
        contact_information: str = None,
        contact_name: str = None,
        customer_name: str = None,
        customer_uid: str = None,
        note_content: str = None,
        touch_date: int = None,
    ):
        self.contact_information = contact_information
        self.contact_name = contact_name
        self.customer_name = customer_name
        self.customer_uid = customer_uid
        self.note_content = note_content
        self.touch_date = touch_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_information is not None:
            result['ContactInformation'] = self.contact_information

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.note_content is not None:
            result['NoteContent'] = self.note_content

        if self.touch_date is not None:
            result['TouchDate'] = self.touch_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactInformation') is not None:
            self.contact_information = m.get('ContactInformation')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('NoteContent') is not None:
            self.note_content = m.get('NoteContent')

        if m.get('TouchDate') is not None:
            self.touch_date = m.get('TouchDate')

        return self


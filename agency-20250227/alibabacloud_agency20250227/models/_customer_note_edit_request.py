# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomerNoteEditRequest(DaraModel):
    def __init__(
        self,
        contact_information: str = None,
        contact_name: str = None,
        note_content: str = None,
        note_id: int = None,
        touch_date: int = None,
    ):
        self.contact_information = contact_information
        self.contact_name = contact_name
        self.note_content = note_content
        self.note_id = note_id
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

        if self.note_content is not None:
            result['NoteContent'] = self.note_content

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.touch_date is not None:
            result['TouchDate'] = self.touch_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactInformation') is not None:
            self.contact_information = m.get('ContactInformation')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('NoteContent') is not None:
            self.note_content = m.get('NoteContent')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('TouchDate') is not None:
            self.touch_date = m.get('TouchDate')

        return self


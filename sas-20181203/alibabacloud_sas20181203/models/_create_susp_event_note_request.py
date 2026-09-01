# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSuspEventNoteRequest(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        note: str = None,
        resource_directory_account_id: int = None,
    ):
        # The ID of the security alert event to which you want to add a note. Call [DescribeSuspEvents](https://help.aliyun.com/document_detail/251497.html) to obtain the ID of the alert event.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The note to add.
        # 
        # This parameter is required.
        self.note = note
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.note is not None:
            result['Note'] = self.note

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self


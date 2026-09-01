# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSuspEventNodeRequest(DaraModel):
    def __init__(
        self,
        note_id: int = None,
        resource_directory_account_id: int = None,
    ):
        # The ID of the description.
        # 
        # > You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to obtain the ID of the description by using the EventNotes field.
        # 
        # This parameter is required.
        self.note_id = note_id
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self


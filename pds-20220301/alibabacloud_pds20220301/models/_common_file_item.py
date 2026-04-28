# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CommonFileItem(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        self.drive_id = drive_id
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self


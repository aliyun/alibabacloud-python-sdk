# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddStoryFile(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        # Error codes when adding a single file.
        self.error_code = error_code
        # Error message when adding a single file.
        self.error_message = error_message
        # The file ID.
        self.file_id = file_id
        # File version.
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self


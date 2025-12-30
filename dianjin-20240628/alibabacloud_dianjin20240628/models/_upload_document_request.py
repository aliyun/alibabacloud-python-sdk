# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadDocumentRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        file_name: str = None,
        file_url: str = None,
        library_id: str = None,
    ):
        self.data = data
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        return self


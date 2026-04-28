# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompleteFileRequest(DaraModel):
    def __init__(
        self,
        crc_64hash: str = None,
        drive_id: str = None,
        file_id: str = None,
        upload_id: str = None,
    ):
        self.crc_64hash = crc_64hash
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The upload ID.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.upload_id is not None:
            result['upload_id'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')

        return self


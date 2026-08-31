# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MiguSourceUploadDTO(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        file_type: str = None,
        source_id: str = None,
        upload_url: str = None,
    ):
        # The expiration time of the upload URL in RFC 3339 format.
        self.expires_at = expires_at
        # The type of the source file (uppercase). Valid values: VIDEO, IMAGE, AUDIO, and TEXT.
        self.file_type = file_type
        # The unique identifier of the source file, used for subsequent generation tasks and downloads.
        self.source_id = source_id
        # The OSS pre-signed upload URL. Use the PUT method to upload the file.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')

        return self


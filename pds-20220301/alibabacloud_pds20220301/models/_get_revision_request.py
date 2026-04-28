# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRevisionRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        revision_id: str = None,
        url_expire_sec: int = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # Specifies the returned fields.
        # 
        # By default, this parameter is left empty. If you set this parameter to \\*, all fields are returned. If you leave this parameter empty, the creator of the file is not returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id
        # The validity period of the file download or preview. Valid values: 10 to 86400.
        # 
        # Default value: 900. Unit: seconds.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        return self


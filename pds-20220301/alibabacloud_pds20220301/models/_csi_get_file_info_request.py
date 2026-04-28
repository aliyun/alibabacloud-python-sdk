# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CsiGetFileInfoRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        url_expire_sec: int = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id
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

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ArchiveFilesRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_ids: List[str] = None,
        name: str = None,
        share_id: str = None,
    ):
        self.drive_id = drive_id
        # This parameter is required.
        self.file_ids = file_ids
        # This parameter is required.
        self.name = name
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_ids is not None:
            result['file_ids'] = self.file_ids

        if self.name is not None:
            result['name'] = self.name

        if self.share_id is not None:
            result['share_id'] = self.share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_ids') is not None:
            self.file_ids = m.get('file_ids')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        return self


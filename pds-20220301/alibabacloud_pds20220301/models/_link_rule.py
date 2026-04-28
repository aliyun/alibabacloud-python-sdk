# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LinkRule(DaraModel):
    def __init__(
        self,
        link_type: str = None,
        src_drive_id: str = None,
        src_drive_name: str = None,
        src_file_id: str = None,
        src_file_name: str = None,
        src_valid: bool = None,
    ):
        self.link_type = link_type
        self.src_drive_id = src_drive_id
        self.src_drive_name = src_drive_name
        self.src_file_id = src_file_id
        self.src_file_name = src_file_name
        self.src_valid = src_valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link_type is not None:
            result['link_type'] = self.link_type

        if self.src_drive_id is not None:
            result['src_drive_id'] = self.src_drive_id

        if self.src_drive_name is not None:
            result['src_drive_name'] = self.src_drive_name

        if self.src_file_id is not None:
            result['src_file_id'] = self.src_file_id

        if self.src_file_name is not None:
            result['src_file_name'] = self.src_file_name

        if self.src_valid is not None:
            result['src_valid'] = self.src_valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link_type') is not None:
            self.link_type = m.get('link_type')

        if m.get('src_drive_id') is not None:
            self.src_drive_id = m.get('src_drive_id')

        if m.get('src_drive_name') is not None:
            self.src_drive_name = m.get('src_drive_name')

        if m.get('src_file_id') is not None:
            self.src_file_id = m.get('src_file_id')

        if m.get('src_file_name') is not None:
            self.src_file_name = m.get('src_file_name')

        if m.get('src_valid') is not None:
            self.src_valid = m.get('src_valid')

        return self


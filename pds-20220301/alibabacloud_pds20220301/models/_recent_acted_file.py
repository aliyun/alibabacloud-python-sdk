# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RecentActedFile(DaraModel):
    def __init__(
        self,
        action_list: List[str] = None,
        category: str = None,
        deleted: bool = None,
        drive_id: str = None,
        drive_is_handover: bool = None,
        drive_name: str = None,
        drive_owner_id: str = None,
        drive_owner_type: str = None,
        file_id: str = None,
        file_name: str = None,
        size: int = None,
        thumbnail: str = None,
        trashed: bool = None,
    ):
        self.action_list = action_list
        self.category = category
        self.deleted = deleted
        self.drive_id = drive_id
        self.drive_is_handover = drive_is_handover
        self.drive_name = drive_name
        self.drive_owner_id = drive_owner_id
        self.drive_owner_type = drive_owner_type
        self.file_id = file_id
        self.file_name = file_name
        self.size = size
        self.thumbnail = thumbnail
        self.trashed = trashed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['action_list'] = self.action_list

        if self.category is not None:
            result['category'] = self.category

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.drive_is_handover is not None:
            result['drive_is_handover'] = self.drive_is_handover

        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.drive_owner_id is not None:
            result['drive_owner_id'] = self.drive_owner_id

        if self.drive_owner_type is not None:
            result['drive_owner_type'] = self.drive_owner_type

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.size is not None:
            result['size'] = self.size

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.trashed is not None:
            result['trashed'] = self.trashed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('drive_is_handover') is not None:
            self.drive_is_handover = m.get('drive_is_handover')

        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('drive_owner_id') is not None:
            self.drive_owner_id = m.get('drive_owner_id')

        if m.get('drive_owner_type') is not None:
            self.drive_owner_type = m.get('drive_owner_type')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('trashed') is not None:
            self.trashed = m.get('trashed')

        return self


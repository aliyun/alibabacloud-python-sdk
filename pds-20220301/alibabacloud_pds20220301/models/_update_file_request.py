# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileRequest(DaraModel):
    def __init__(
        self,
        check_name_mode: str = None,
        description: str = None,
        drive_id: str = None,
        file_id: str = None,
        hidden: bool = None,
        labels: List[str] = None,
        local_modified_at: str = None,
        name: str = None,
        starred: bool = None,
    ):
        # The processing method that is used if the file that you want to modify has the same name as an existing file on the cloud. Valid values:
        # 
        # ignore: allows you to modify the file by using the same name as an existing file on the cloud.
        # 
        # auto_rename: automatically renames the file that has the same name on the cloud. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not modify the file that you want to modify but returns the information about the file that has the same name on the cloud.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The description of the file. The description can be up to 1,024 characters in length.
        self.description = description
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to hide the file.
        self.hidden = hidden
        # The tags of the file. You can specify up to 100 tags.
        self.labels = labels
        # The local time when the file was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_modified_at = local_modified_at
        # The name of the file. The name can be up to 1,024 bytes in length based on the UTF-8 encoding rule.
        self.name = name
        # Specifies whether to add the file to favorites.
        self.starred = starred

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode

        if self.description is not None:
            result['description'] = self.description

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.hidden is not None:
            result['hidden'] = self.hidden

        if self.labels is not None:
            result['labels'] = self.labels

        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.starred is not None:
            result['starred'] = self.starred

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('starred') is not None:
            self.starred = m.get('starred')

        return self


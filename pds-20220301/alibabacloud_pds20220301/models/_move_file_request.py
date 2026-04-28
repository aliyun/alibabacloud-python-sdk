# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveFileRequest(DaraModel):
    def __init__(
        self,
        check_name_mode: str = None,
        drive_id: str = None,
        file_id: str = None,
        to_parent_file_id: str = None,
    ):
        # The processing method that is used if the file that you want to move has the same name as an existing file in the destination directory. Valid values:
        # 
        # ignore: allows you to move the file by using the same name as an existing file in the destination directory.
        # 
        # auto_rename: automatically renames the file that has the same name exists in the destination directory. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not move the file that you want to move but returns the information about the file that has the same name in the destination directory.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the destination parent directory to which you want to move a file or folder. If you want to move a file or folder to the root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.to_parent_file_id = to_parent_file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')

        return self


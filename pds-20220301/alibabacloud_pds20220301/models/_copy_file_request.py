# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyFileRequest(DaraModel):
    def __init__(
        self,
        auto_rename: bool = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
        to_drive_id: str = None,
        to_parent_file_id: str = None,
    ):
        # Specifies whether to automatically rename the file if the file name already exists in the destination folder. Default value: false.
        self.auto_rename = auto_rename
        # The drive ID.
        self.drive_id = drive_id
        # The file ID or folder ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The ID of the drive to which you want to copy the file or folder. Default value: the value of drive_id.
        self.to_drive_id = to_drive_id
        # The ID of the destination parent folder. If you want to copy the file or folder to a root directory, set this parameter to root.
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
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id

        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('to_drive_id') is not None:
            self.to_drive_id = m.get('to_drive_id')

        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')

        return self


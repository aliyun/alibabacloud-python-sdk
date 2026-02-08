# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppMaterialFile(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        content_type: str = None,
        create_time: str = None,
        deleted_time: str = None,
        directory_id: str = None,
        file_id: str = None,
        file_url: str = None,
        height: int = None,
        name: str = None,
        status: str = None,
        storage_size: str = None,
        suffix: str = None,
        type: str = None,
        width: int = None,
    ):
        self.biz_id = biz_id
        self.content_type = content_type
        self.create_time = create_time
        self.deleted_time = deleted_time
        self.directory_id = directory_id
        self.file_id = file_id
        self.file_url = file_url
        self.height = height
        self.name = name
        self.status = status
        self.storage_size = storage_size
        self.suffix = suffix
        self.type = type
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.height is not None:
            result['Height'] = self.height

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self


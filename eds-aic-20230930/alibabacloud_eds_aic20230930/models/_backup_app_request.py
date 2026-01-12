# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BackupAppRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        source_app_list: List[str] = None,
        upload_endpoint: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        self.backup_file_name = backup_file_name
        # This parameter is required.
        self.backup_file_path = backup_file_path
        self.description = description
        # This parameter is required.
        self.source_app_list = source_app_list
        # This parameter is required.
        self.upload_endpoint = upload_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list

        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name

        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path

        if self.description is not None:
            result['Description'] = self.description

        if self.source_app_list is not None:
            result['SourceAppList'] = self.source_app_list

        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')

        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')

        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SourceAppList') is not None:
            self.source_app_list = m.get('SourceAppList')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        return self


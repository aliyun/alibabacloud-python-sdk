# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RecoverAppRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_file_id: str = None,
        backup_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # This parameter is required.
        self.backup_file_id = backup_file_id
        # This parameter is required.
        self.backup_file_path = backup_file_path
        self.upload_endpoint = upload_endpoint
        # This parameter is required.
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list

        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id

        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path

        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')

        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')

        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self


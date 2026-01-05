# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RecoveryFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to back up the whole instance.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The OSS path to which the backup file is uploaded.
        # 
        # >  When calling the describeBuckets operation to retrieve a bucket name, you must also call the ossObjectList operation to obtain the object key. Combine these to form the full path: oss://${bucketName}/${key}.
        self.backup_file_path = backup_file_path
        # The endpoint of the OSS bucket that stores the backup file.
        # 
        # > : When calling the DescribeBuckets operation to query buckets, retrieve the IntranetEndpoint value if the cloud phone and the OSS bucket are in the same region. If they are in different regions, retrieve the ExtranetEndpoint value instead.
        self.upload_endpoint = upload_endpoint
        # The type of the backup.
        # 
        # Valid values:
        # 
        # *   OSS: backup files are stored in OSS buckets.
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

        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all

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

        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')

        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')

        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self


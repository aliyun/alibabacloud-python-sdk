# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BackupFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_all: bool = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        exclude_app_list: List[str] = None,
        exclude_source_file_path_list: List[str] = None,
        source_app_list: List[str] = None,
        source_file_path_list: List[str] = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The list of instance IDs.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to back up the entire instance.
        self.backup_all = backup_all
        # The name of the backup file.
        self.backup_file_name = backup_file_name
        # The upload address of the backup file.
        # > If you upload the backup file to an OSS bucket, call the describeBuckets operation to obtain the bucketName, and select ossObjectList to obtain the key. The key is the folder path in the OSS bucket. Concatenate them into `oss://${bucketName}/${key}`.
        # 
        # This parameter is required.
        self.backup_file_path = backup_file_path
        # The description of the backup file.
        self.description = description
        # The list of application package names excluded from full instance backup. Matched applications only skip APK collection, and user data is backed up as usual. If this parameter is not specified, no applications are excluded.
        self.exclude_app_list = exclude_app_list
        # The list of file paths in the Android container to exclude from the backup.
        self.exclude_source_file_path_list = exclude_source_file_path_list
        # The list of package names of the applications to back up.
        self.source_app_list = source_app_list
        # The list of file paths to back up.
        self.source_file_path_list = source_file_path_list
        # The domain name of the backup address.
        # 
        # > If you upload the backup file to an OSS bucket, call the describeBuckets operation to obtain the bucket. If the Cloud Phone instance and the bucket are in the same region, obtain the intranetEndpoint field. If they are in different regions, obtain the extranetEndpoint field.
        self.upload_endpoint = upload_endpoint
        # The backup type.
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

        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name

        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path

        if self.description is not None:
            result['Description'] = self.description

        if self.exclude_app_list is not None:
            result['ExcludeAppList'] = self.exclude_app_list

        if self.exclude_source_file_path_list is not None:
            result['ExcludeSourceFilePathList'] = self.exclude_source_file_path_list

        if self.source_app_list is not None:
            result['SourceAppList'] = self.source_app_list

        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list

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

        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')

        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExcludeAppList') is not None:
            self.exclude_app_list = m.get('ExcludeAppList')

        if m.get('ExcludeSourceFilePathList') is not None:
            self.exclude_source_file_path_list = m.get('ExcludeSourceFilePathList')

        if m.get('SourceAppList') is not None:
            self.source_app_list = m.get('SourceAppList')

        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self


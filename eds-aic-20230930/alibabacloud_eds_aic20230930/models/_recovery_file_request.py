# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class RecoveryFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_path: str = None,
        custom_scripts: List[main_models.RecoveryFileRequestCustomScripts] = None,
        exclude_app_list: List[str] = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The list of instance IDs.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether it is a full-device backup.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The OSS address to which the backup file is uploaded.
        # <notice>Call the describeBuckets operation to obtain the bucketName, and select ossObjectList to obtain the key. The key is the path of the backup file. Concatenate them into "oss://${bucketName}/${key}".</notice>
        self.backup_file_path = backup_file_path
        self.custom_scripts = custom_scripts
        # The list of excluded app package names for full-device restore. Matched apps are not uninstalled, and their APKs are not installed (compatible with legacy backups that contain APKs). Only user data is replaced. The empty shell must be installed by the customer using pm install. If this parameter is not specified, no apps are excluded.
        self.exclude_app_list = exclude_app_list
        # The domain name of the backup address.
        # <notice>Call the DescribeBuckets operation to obtain the bucket. If the cloud phone and the bucket are in the same region, obtain the IntranetEndpoint field. If they are in different regions, obtain the ExtranetEndpoint field.</notice>
        self.upload_endpoint = upload_endpoint
        # The backup type.
        self.upload_type = upload_type

    def validate(self):
        if self.custom_scripts:
            for v1 in self.custom_scripts:
                 if v1:
                    v1.validate()

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

        result['CustomScripts'] = []
        if self.custom_scripts is not None:
            for k1 in self.custom_scripts:
                result['CustomScripts'].append(k1.to_map() if k1 else None)

        if self.exclude_app_list is not None:
            result['ExcludeAppList'] = self.exclude_app_list

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

        self.custom_scripts = []
        if m.get('CustomScripts') is not None:
            for k1 in m.get('CustomScripts'):
                temp_model = main_models.RecoveryFileRequestCustomScripts()
                self.custom_scripts.append(temp_model.from_map(k1))

        if m.get('ExcludeAppList') is not None:
            self.exclude_app_list = m.get('ExcludeAppList')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self

class RecoveryFileRequestCustomScripts(DaraModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object_key: str = None,
        oss_region: str = None,
        test_instance_ids: List[str] = None,
    ):
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_object_key = oss_object_key
        self.oss_region = oss_region
        self.test_instance_ids = test_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object_key is not None:
            result['OssObjectKey'] = self.oss_object_key

        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region

        if self.test_instance_ids is not None:
            result['TestInstanceIds'] = self.test_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObjectKey') is not None:
            self.oss_object_key = m.get('OssObjectKey')

        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')

        if m.get('TestInstanceIds') is not None:
            self.test_instance_ids = m.get('TestInstanceIds')

        return self


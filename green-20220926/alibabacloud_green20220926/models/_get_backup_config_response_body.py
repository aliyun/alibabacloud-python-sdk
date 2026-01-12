# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBackupConfigResponseBody(DaraModel):
    def __init__(
        self,
        backup_mode: int = None,
        bucket: str = None,
        enable: bool = None,
        enable_backup: bool = None,
        enable_backup_voice: bool = None,
        expire_seconds: int = None,
        gmt_modified: str = None,
        path: str = None,
        path_voice: str = None,
        region: str = None,
        request_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        uid: str = None,
    ):
        # Backup scope.
        self.backup_mode = backup_mode
        # File server OSS Bucket.
        self.bucket = bucket
        # Whether it is enabled. Values:
        # - **true**: Enabled
        # - **false**: Disabled
        self.enable = enable
        # Whether to enable backup.
        self.enable_backup = enable_backup
        # Whether to enable audio backup.
        self.enable_backup_voice = enable_backup_voice
        # Expiration time in seconds.
        self.expire_seconds = expire_seconds
        # Modification time.
        self.gmt_modified = gmt_modified
        # Path.
        self.path = path
        # Audio backup path.
        self.path_voice = path_voice
        # Region ID.
        self.region = region
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # UID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enable_backup is not None:
            result['EnableBackup'] = self.enable_backup

        if self.enable_backup_voice is not None:
            result['EnableBackupVoice'] = self.enable_backup_voice

        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.path is not None:
            result['Path'] = self.path

        if self.path_voice is not None:
            result['PathVoice'] = self.path_voice

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnableBackup') is not None:
            self.enable_backup = m.get('EnableBackup')

        if m.get('EnableBackupVoice') is not None:
            self.enable_backup_voice = m.get('EnableBackupVoice')

        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PathVoice') is not None:
            self.path_voice = m.get('PathVoice')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySmbAclRequest(DaraModel):
    def __init__(
        self,
        enable_anonymous_access: bool = None,
        encrypt_data: bool = None,
        file_system_id: str = None,
        home_dir_path: str = None,
        keytab: str = None,
        keytab_md_5: str = None,
        reject_unencrypted_access: bool = None,
        super_admin_sid: str = None,
    ):
        # Specifies whether to allow anonymous access. 
        # 
        # - true: Anonymous access is allowed.
        # 
        # - false (default): Anonymous access is not allowed.
        self.enable_anonymous_access = enable_anonymous_access
        # Specifies whether to enable encryption in transit.
        # 
        # - true: Encryption in transit is enabled.
        # 
        # - false (default): Encryption in transit is not enabled.
        self.encrypt_data = encrypt_data
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The home folder path for each user. The file path format is as follows:
        # 
        # - Use a forward slash (/) or backslash (\\) as the separator.
        # 
        # - Each segment cannot contain `<>":|?*`.
        # 
        # - The length of each segment ranges from 0 to 255.
        # 
        # - The total length ranges from 0 to 32767.
        # 
        # For example, if the user folder is `/home`, the file system performs automatic creation of the `/home/A` folder when user A performs logon. If `/home/A` already exists, this step is skipped.
        # 
        # > User A must have the permission to create folders. Otherwise, the `/home/A` folder cannot be created.
        self.home_dir_path = home_dir_path
        # The Base64-encoded string of the keytab file content.
        self.keytab = keytab
        # The MD5-encrypted string of the keytab file content.
        self.keytab_md_5 = keytab_md_5
        # Specifies whether to reject unencrypted clients.
        # 
        # - true: Unencrypted clients are rejected.
        # 
        # - false (default): Unencrypted clients are not rejected.
        self.reject_unencrypted_access = reject_unencrypted_access
        # The ID of the superuser. The ID must follow these rules:
        # 
        # - Must start with `S`, and no other letters are allowed after the initial S.
        # 
        # - Must contain at least three hyphens (-) as separators.
        # 
        # For example, `S-1-5-22` or `S-1-5-22-23`.
        self.super_admin_sid = super_admin_sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_anonymous_access is not None:
            result['EnableAnonymousAccess'] = self.enable_anonymous_access

        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path

        if self.keytab is not None:
            result['Keytab'] = self.keytab

        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5

        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access

        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')

        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')

        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')

        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')

        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')

        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')

        return self


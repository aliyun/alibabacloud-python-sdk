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
        # Specifies whether to allow anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false (default): The file system denies anonymous access.
        self.enable_anonymous_access = enable_anonymous_access
        # Specifies whether to enable encryption in transit. Valid values:
        # 
        # *   true: enables encryption in transit.
        # *   false (default): disables encryption in transit.
        self.encrypt_data = encrypt_data
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The home directory of each user. Each user-specific home directory must meet the following requirements:
        # 
        # *   Each segment starts with a forward slash (/) or a backward slash (\\\\).
        # *   Each segment does not contain the following special characters: `<>":|?*`.
        # *   Each segment is 0 to 255 characters in length.
        # *   The total length is 0 to 32,767 characters.
        # 
        # For example, if you create a user named A and the home directory is `/home`, the file system automatically creates a directory named `/home/A` when User A logs on to the file system. If the `/home/A` directory already exists, the file system does not create the directory.
        # 
        # > User A must have the permissions to create folders in the \\home directory. Otherwise, the file system cannot create the `/home/A` directory when User A logs on to the file system.
        self.home_dir_path = home_dir_path
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5
        # Specifies whether to deny access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false (default): The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access
        # The ID of a super admin. The ID must meet the following requirements:
        # 
        # *   The ID starts with `S` and does not contain letters except S.
        # *   The ID contains at least three hyphens (-) as delimiters.
        # 
        # Examples: `S-1-5-22` and `S-1-5-22-23`.
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


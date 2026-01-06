# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeSmbAclResponseBody(DaraModel):
    def __init__(
        self,
        acl: main_models.DescribeSmbAclResponseBodyAcl = None,
        request_id: str = None,
    ):
        # The information about the ACL feature.
        self.acl = acl
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = main_models.DescribeSmbAclResponseBodyAcl()
            self.acl = temp_model.from_map(m.get('Acl'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSmbAclResponseBodyAcl(DaraModel):
    def __init__(
        self,
        enable_anonymous_access: bool = None,
        enabled: bool = None,
        encrypt_data: bool = None,
        home_dir_path: str = None,
        reject_unencrypted_access: bool = None,
        super_admin_sid: str = None,
    ):
        # Indicates whether the file system allows anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false: The file system does not allow anonymous access.
        self.enable_anonymous_access = enable_anonymous_access
        # Indicates whether the ACL feature is enabled. Valid values:
        # 
        # *   true: The ACL feature is enabled.
        # *   false: The ACL feature is disabled.
        self.enabled = enabled
        # Indicates whether encryption in transit is enabled. Valid values:
        # 
        # *   true: Encryption in transit is enabled.
        # *   false: Encryption in transit is disabled.
        self.encrypt_data = encrypt_data
        # The home directory of each user.
        self.home_dir_path = home_dir_path
        # Indicates whether the file system denies access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false: The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access
        # The ID of a super admin.
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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data

        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path

        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access

        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')

        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')

        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')

        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')

        return self


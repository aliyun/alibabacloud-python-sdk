# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceTDERequest(DaraModel):
    def __init__(
        self,
        certificate: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        encryption_key: str = None,
        is_rotate: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        pass_word: str = None,
        private_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        tdestatus: str = None,
    ):
        # The file that contains the certificate.\\
        # Format:
        # 
        # *   Public endpoint: `oss-<The ID of the region>.aliyuncs.com:<The name of the bucket>:<The name of the certificate file>` (The file name contains the extension.)
        # *   Internal endpoint: `oss-<The ID of the region>-internal.aliyuncs.com:<The name of the bucket>:<The name of the certificate file>` (The file name contains the extension.)
        # 
        # > *   This parameter is available when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server.
        # > *   You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent region list.
        self.certificate = certificate
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database for which you want to enable TDE. You can specify up to 50 database names in a single request. If you specify multiple database names, separate the database names with commas (,).
        # 
        # > This parameter is available and must be specified only when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server.
        self.dbname = dbname
        # The ID of the custom key.
        # 
        # > This parameter is available when the instance runs MySQL or PostgreSQL.
        self.encryption_key = encryption_key
        # Specifies whether to replace the key. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  This parameter is available for only ApsaraDB RDS for PostgreSQL instances.
        self.is_rotate = is_rotate
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the certificate.
        # 
        # > This parameter is available when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server.
        self.pass_word = pass_word
        # The file that contains the private key of the certificate.\\
        # Format:
        # 
        # *   Public endpoint: `oss-<The ID of the region>.aliyuncs.com:<The name of the bucket>:<The name of the file that contains the private key>` (The file name contains the extension.)
        # *   Internal endpoint: `oss-<The ID of the region>-internal.aliyuncs.com:<The name of the bucket>:<The name of the file that contains the private key>` (The file name contains the extension.)
        # 
        # > *   This parameter is available when the instance runs SQL Server 2019 SE or an Enterprise Edition of SQL Server.
        # > *   You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent region list.
        self.private_key = private_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role. A RAM role is a virtual identity that you can create within your Alibaba Cloud account. For more information, see [RAM role overview](https://help.aliyun.com/document_detail/93689.html).
        # 
        # > This parameter is available when the instance runs MySQL or PostgreSQL.
        self.role_arn = role_arn
        # The status of TDE. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        # 
        # This parameter is required.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.is_rotate is not None:
            result['IsRotate'] = self.is_rotate

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pass_word is not None:
            result['PassWord'] = self.pass_word

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('IsRotate') is not None:
            self.is_rotate = m.get('IsRotate')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self


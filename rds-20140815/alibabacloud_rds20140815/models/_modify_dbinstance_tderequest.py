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
        # The certificate file.
        # 
        # Format:
        # - Public endpoint: `oss-<RegionId>.aliyuncs.com:<BucketName>:<CertificateFileName (with file extension)>`
        # - Internal network endpoint: `oss-<RegionId>-internal.aliyuncs.com:<BucketName>:<CertificateFileName (with file extension)>`
        # 
        # > - This parameter is active only for SQL Server 2019 Standard Edition, 2022 Standard Edition, 2025 Standard Edition, and SQL Server Enterprise instance instances.
        # > - You can call [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) to query active region IDs.
        self.certificate = certificate
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database for which you want to enable TDE. You can specify multiple database names separated by commas (,). You can specify up to 50 database names.
        # > This parameter is active and required only for SQL Server 2019 Standard Edition, 2022 Standard Edition, 2025 Standard Edition, and SQL Server Enterprise instance instances.
        self.dbname = dbname
        # The custom key ID.
        # > This parameter is available only for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances.
        self.encryption_key = encryption_key
        # Specifies whether to rotate the key. Valid values:
        # - **true**: Rotate the key.
        # - **false** (default): Do not rotate the key.
        # 
        # > This parameter is available only for ApsaraDB RDS for PostgreSQL instances.
        self.is_rotate = is_rotate
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The certificate password.
        # > This parameter is active only for SQL Server 2019 Standard Edition, 2022 Standard Edition, 2025 Standard Edition, and SQL Server Enterprise instance instances.
        self.pass_word = pass_word
        # The private key file.
        # 
        # Format:
        # - Public endpoint: `oss-<RegionId>.aliyuncs.com:<BucketName>:<PrivateKeyFileName (with file extension)>`
        # - Internal network endpoint: `oss-<RegionId>-internal.aliyuncs.com:<BucketName>:<PrivateKeyFileName (with file extension)>`
        # 
        # > - This parameter is active only for SQL Server 2019 Standard Edition, 2022 Standard Edition, 2025 Standard Edition, and SQL Server Enterprise instance instances.
        # > - You can call [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) to query active region IDs.
        self.private_key = private_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The global resource descriptor of the RAM role. The resource descriptor is used to specify a RAM role. For details, see [RAM role overview](https://help.aliyun.com/document_detail/93689.html).
        # > This parameter is available only for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances.
        self.role_arn = role_arn
        # The TDE status. Valid values:
        # - **Enabled** 
        # - **Disabled**
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


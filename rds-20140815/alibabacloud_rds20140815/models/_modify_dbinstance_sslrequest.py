# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSSLRequest(DaraModel):
    def __init__(
        self,
        acl: str = None,
        catype: str = None,
        certificate: str = None,
        client_cacert: str = None,
        client_caenabled: int = None,
        client_cert_revocation_list: str = None,
        client_crl_enabled: int = None,
        connection_string: str = None,
        dbinstance_id: str = None,
        force_encryption: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pass_word: str = None,
        replication_acl: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sslenabled: int = None,
        server_cert: str = None,
        server_key: str = None,
        tls_version: str = None,
    ):
        # The authentication method for an ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **cert**
        # - **prefer**
        # - **verify-ca**
        # - **verify-full** (supported for ApsaraDB RDS for PostgreSQL 12 and later)
        # 
        # > This parameter can be configured only when ClientCAEnabled is set to **1**.
        self.acl = acl
        # The type of certificate for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances with cloud disks. Valid values:
        # - **aliyun** (default): Alibaba Cloud certificate.
        # - **custom**: Custom certificate.
        # > This parameter is required when SSLEnabled is set to **1**.
        self.catype = catype
        # The custom certificate content for an ApsaraDB RDS for SQL Server instance. Only the `pfx` certificate format is supported.
        # - Public endpoint: `oss-<RegionId>.aliyuncs.com:<BucketName>:<CertificateFileName (certificate file extension)>`
        # - Internal endpoint: `oss-<RegionId>-internal.aliyuncs.com:<BucketName>:<CertificateFileName (certificate file extension)>`
        self.certificate = certificate
        # The client certificate authorization authority public key for an ApsaraDB RDS for PostgreSQL instance with cloud disks.
        # 
        # > This parameter is required when ClientCAEnabled is set to **1**.
        self.client_cacert = client_cacert
        # Specifies whether to enable the client certification authority (CA) public key for an ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **1**: Enable.
        # - **0**: Disable.
        self.client_caenabled = client_caenabled
        # The client certificate revocation certificate file for an ApsaraDB RDS for PostgreSQL instance with cloud disks.
        # 
        # > This parameter is required when ClientCrlEnabled is set to **1**.
        self.client_cert_revocation_list = client_cert_revocation_list
        # Specifies whether to enable the client certificate revocation list (CRL) for an ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **1**: Enable.
        # - **0**: Disable.
        # 
        # > This parameter can be configured only when ClientCAEnabled is set to **1**.
        self.client_crl_enabled = client_crl_enabled
        # The internal or public endpoint for which you want to create or update the server certificate.
        # 
        # This parameter is required.
        self.connection_string = connection_string
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The [SSL forced encryption switch](https://help.aliyun.com/document_detail/95715.html) for ApsaraDB RDS for MySQL and ApsaraDB RDS for SQL Server instances. Valid values:
        # 
        # - **1**: Enabled.
        # - **0**: Disabled.
        self.force_encryption = force_encryption
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the custom certificate for an ApsaraDB RDS for SQL Server instance.
        self.pass_word = pass_word
        # The authentication method for replication permissions on an ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **cert**
        # - **prefer**
        # - **verify-ca**
        # - **verify-full** (supported for ApsaraDB RDS for PostgreSQL 12 and later)
        # > This parameter can be configured only when ClientCAEnabled is set to **1**.
        self.replication_acl = replication_acl
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable or disable SSL. Valid values:
        # * **1**: Enable.
        # * **0**: Disable.
        self.sslenabled = sslenabled
        # The custom certificate content of the server for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances with cloud disks.
        # 
        # > This parameter is required when CAType is set to **custom**.
        self.server_cert = server_cert
        # The private key of the server certificate for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances with cloud disks.
        # 
        # > This parameter is required when CAType is set to **custom**.
        self.server_key = server_key
        # The [minimum TLS version](https://help.aliyun.com/document_detail/95715.html) for an ApsaraDB RDS for SQL Server instance. Connection requests from clients with a TLS version lower than the specified version are rejected. Valid values: 1.0, 1.1, and 1.2.
        # 
        # For example, if you set this parameter to 1.1, the server accepts only connection requests from clients that use TLS 1.1 or TLS 1.2. Connection requests from clients that use TLS 1.0 are rejected.
        self.tls_version = tls_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['ACL'] = self.acl

        if self.catype is not None:
            result['CAType'] = self.catype

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.client_cacert is not None:
            result['ClientCACert'] = self.client_cacert

        if self.client_caenabled is not None:
            result['ClientCAEnabled'] = self.client_caenabled

        if self.client_cert_revocation_list is not None:
            result['ClientCertRevocationList'] = self.client_cert_revocation_list

        if self.client_crl_enabled is not None:
            result['ClientCrlEnabled'] = self.client_crl_enabled

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.force_encryption is not None:
            result['ForceEncryption'] = self.force_encryption

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pass_word is not None:
            result['PassWord'] = self.pass_word

        if self.replication_acl is not None:
            result['ReplicationACL'] = self.replication_acl

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert

        if self.server_key is not None:
            result['ServerKey'] = self.server_key

        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACL') is not None:
            self.acl = m.get('ACL')

        if m.get('CAType') is not None:
            self.catype = m.get('CAType')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('ClientCACert') is not None:
            self.client_cacert = m.get('ClientCACert')

        if m.get('ClientCAEnabled') is not None:
            self.client_caenabled = m.get('ClientCAEnabled')

        if m.get('ClientCertRevocationList') is not None:
            self.client_cert_revocation_list = m.get('ClientCertRevocationList')

        if m.get('ClientCrlEnabled') is not None:
            self.client_crl_enabled = m.get('ClientCrlEnabled')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ForceEncryption') is not None:
            self.force_encryption = m.get('ForceEncryption')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')

        if m.get('ReplicationACL') is not None:
            self.replication_acl = m.get('ReplicationACL')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')

        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')

        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')

        return self


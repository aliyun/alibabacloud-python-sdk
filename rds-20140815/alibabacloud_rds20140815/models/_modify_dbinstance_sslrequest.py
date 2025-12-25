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
        # The method that is used to verify the identities of clients. This parameter is supported only when the instance runs PostgreSQL with cloud disks. In addition, this parameter is available only when the public key of the CA that issues client certificates is enabled. Valid values:
        # 
        # *   **cert**
        # *   **prefer**
        # *   **verify-ca**
        # *   **verify-full** (supported only when the instance runs PostgreSQL 12 or later)
        self.acl = acl
        # The type of the server certificate. This parameter is supported only when the instance runs MySQL or PostgreSQL with cloud disks. If you set SSLEnabled to **1**, the default value of this parameter is **aliyun**. Valid values:
        # 
        # *   **aliyun**: a cloud certificate
        # *   **custom**: a custom certificate
        self.catype = catype
        # The custom certificate. The custom certificate is in the `PFX` format.
        # 
        # *   Public endpoint: `oss-<The ID of the region>.aliyuncs.com:<The name of the bucket>:<The name of the certificate file (The file name contains the extension.)>`
        # *   Internal endpoint: `oss-<The ID of the region>-internal.aliyuncs.com:<The name of the bucket>:<The name of the certificate file (The file name contains the extension.)>`
        self.certificate = certificate
        # The public key of the CA that issues client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks. This parameter must be specified when ClientCAEbabled is set to **1**.
        self.client_cacert = client_cacert
        # Specifies whether to enable the public key of the CA that issues client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks. Valid values:
        # 
        # *   **1**: enables the public key.
        # *   **0**: disables the public key.
        self.client_caenabled = client_caenabled
        # The CRL that contains revoked client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks. This parameter must be specified when ClientCrlEnabled is set to **1**.
        self.client_cert_revocation_list = client_cert_revocation_list
        # Specifies whether to enable a certificate revocation list (CRL) that contains revoked client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks. In addition, this parameter is available only when the public key of the CA that issues client certificates is enabled. Valid values:
        # 
        # *   **1**: enables the CRL.
        # *   **0**: disables the CRL.
        self.client_crl_enabled = client_crl_enabled
        # The internal or public endpoint for which the server certificate needs to be created or updated.
        # 
        # This parameter is required.
        self.connection_string = connection_string
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable the forceful SSL encryption feature. This parameter is supported only for ApsaraDB RDS for SQL Server instances. For more information, see [Configure the SSL encryption feature](https://help.aliyun.com/document_detail/95715.html). Valid values:
        # 
        # *   **1**: enables the feature.
        # *   **0**: disables the feature.
        self.force_encryption = force_encryption
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the certificate.
        self.pass_word = pass_word
        # The method that is used to verify the replication permission. This parameter is supported only when the instance runs PostgreSQL with cloud disks. In addition, this parameter is available only when the public key of the CA that issues client certificates is enabled. Valid values:
        # 
        # *   **cert**
        # *   **prefer**
        # *   **verify-ca**
        # *   **verify-full** (supported only when the instance runs PostgreSQL 12 or later)
        self.replication_acl = replication_acl
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable or disable the SSL encryption feature. Valid values:
        # 
        # *   **1**: enables the feature.
        # *   **0**: disables the feature.
        self.sslenabled = sslenabled
        # The content of the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disks. This parameter must be specified when CAType is set to **custom**.
        self.server_cert = server_cert
        # The private key of the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disks. This parameter must be specified when CAType is set to **custom**.
        self.server_key = server_key
        # The minimum Transport Layer Security (TLS) version. Valid values: 1.0, 1.1, and 1.2. This parameter is supported only for ApsaraDB RDS for SQL Server instances. For more information, see [Configure the SSL encryption feature](https://help.aliyun.com/document_detail/95715.html).
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


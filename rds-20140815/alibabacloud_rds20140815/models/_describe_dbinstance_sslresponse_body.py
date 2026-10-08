# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        acl: str = None,
        catype: str = None,
        client_cacert: str = None,
        client_cacert_expire_time: str = None,
        client_cert_revocation_list: str = None,
        connection_string: str = None,
        force_encryption: str = None,
        last_modify_status: str = None,
        modify_status_reason: str = None,
        replication_acl: str = None,
        request_id: str = None,
        require_update: str = None,
        require_update_item: str = None,
        require_update_reason: str = None,
        sslcreate_time: str = None,
        sslenabled: str = None,
        sslexpire_time: str = None,
        server_caurl: str = None,
        server_cert: str = None,
        server_key: str = None,
        tls_version: str = None,
    ):
        # The authentication method of the ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **cert**
        # - **prefer**
        # - **verify-ca**
        # - **verify-full** (supported by ApsaraDB RDS for PostgreSQL 12 and later)
        self.acl = acl
        # The server certificate type of the ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **aliyun**: The cloud certificate is used.
        # - **custom**: A custom certificate is used.
        self.catype = catype
        # The public key of the client certificate authority (CA) for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.client_cacert = client_cacert
        # The expiration time of the public key of the client certificate authorization authority (CA) for the ApsaraDB RDS for PostgreSQL instance with cloud disks. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # This parameter is not supported. You can ignore this parameter.
        self.client_cacert_expire_time = client_cacert_expire_time
        # The client certificate revocation certificate file of the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.client_cert_revocation_list = client_cert_revocation_list
        # The endpoint that is protected by SSL.
        self.connection_string = connection_string
        # Indicates whether the [forced Secure Sockets Layer (SSL) encryption feature](https://help.aliyun.com/document_detail/95715.html) is enabled for the ApsaraDB RDS for SQL Server instance. Valid values:
        # 
        # - **1**: Enabled.
        # - **0**: Disabled.
        self.force_encryption = force_encryption
        # The current SSL link configuration status of the ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # 
        # - **success**: Successful.
        # - **setting**: Being configured.
        # - **failed**: Failed.
        self.last_modify_status = last_modify_status
        # The reason for the current SSL link configuration status of the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.modify_status_reason = modify_status_reason
        # The authentication method for replication permissions of the ApsaraDB RDS for PostgreSQL instance with cloud disks. Valid values:
        # - **cert**
        # - **prefer**
        # - **verify-ca**
        # - **verify-full** (supported by ApsaraDB RDS for PostgreSQL 12 and later)
        self.replication_acl = replication_acl
        # The request ID.
        self.request_id = request_id
        # Indicates whether the SSL certificate needs to be updated. Valid values:
        # 
        # > The SSL certificate is valid for one year. If the certificate is not renewed after it expires, client programs that use encrypted connections cannot connect to the instance.
        # <details>
        # <summary>MySQL and SQL Server</summary>
        # 
        # - **No**: No update is required.
        # - **Yes**: An update is required.
        # </details>
        # 
        # <details>
        # <summary>PostgreSQL</summary>
        # 
        # - **0**: No update is required.
        # - **1**: An update is required.
        # 
        # </details>
        self.require_update = require_update
        # The list of server certificates that need to be updated for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.require_update_item = require_update_item
        # The reason why the certificates need to be updated for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.require_update_reason = require_update_reason
        # The creation time of the server certificate for the ApsaraDB RDS for PostgreSQL instance with cloud disks. This parameter is valid only when CAType is set to aliyun.
        self.sslcreate_time = sslcreate_time
        # The SSL encryption status. Valid values:
        # <details>
        # <summary>MySQL and SQL Server</summary>
        # 
        # - **Yes**: Enabled.
        # - **No**: Disabled.
        # </details>
        # 
        # <details>
        # <summary>PostgreSQL</summary>
        # 
        # - **on**: Enabled.
        # - **off**: Disabled.
        # 
        # </details>
        self.sslenabled = sslenabled
        # The expiration time of the SSL certificate. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.sslexpire_time = sslexpire_time
        # The URL of the CA certificate that is used to issue the server certificate for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.server_caurl = server_caurl
        # The content of the server certificate for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.server_cert = server_cert
        # The private key of the server certificate for the ApsaraDB RDS for PostgreSQL instance with cloud disks.
        self.server_key = server_key
        # The specified [minimum TLS version](https://help.aliyun.com/document_detail/95715.html) for the ApsaraDB RDS for SQL Server instance. Valid values: 1.0, 1.1, and 1.2.
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

        if self.client_cacert is not None:
            result['ClientCACert'] = self.client_cacert

        if self.client_cacert_expire_time is not None:
            result['ClientCACertExpireTime'] = self.client_cacert_expire_time

        if self.client_cert_revocation_list is not None:
            result['ClientCertRevocationList'] = self.client_cert_revocation_list

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.force_encryption is not None:
            result['ForceEncryption'] = self.force_encryption

        if self.last_modify_status is not None:
            result['LastModifyStatus'] = self.last_modify_status

        if self.modify_status_reason is not None:
            result['ModifyStatusReason'] = self.modify_status_reason

        if self.replication_acl is not None:
            result['ReplicationACL'] = self.replication_acl

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.require_update is not None:
            result['RequireUpdate'] = self.require_update

        if self.require_update_item is not None:
            result['RequireUpdateItem'] = self.require_update_item

        if self.require_update_reason is not None:
            result['RequireUpdateReason'] = self.require_update_reason

        if self.sslcreate_time is not None:
            result['SSLCreateTime'] = self.sslcreate_time

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.sslexpire_time is not None:
            result['SSLExpireTime'] = self.sslexpire_time

        if self.server_caurl is not None:
            result['ServerCAUrl'] = self.server_caurl

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

        if m.get('ClientCACert') is not None:
            self.client_cacert = m.get('ClientCACert')

        if m.get('ClientCACertExpireTime') is not None:
            self.client_cacert_expire_time = m.get('ClientCACertExpireTime')

        if m.get('ClientCertRevocationList') is not None:
            self.client_cert_revocation_list = m.get('ClientCertRevocationList')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ForceEncryption') is not None:
            self.force_encryption = m.get('ForceEncryption')

        if m.get('LastModifyStatus') is not None:
            self.last_modify_status = m.get('LastModifyStatus')

        if m.get('ModifyStatusReason') is not None:
            self.modify_status_reason = m.get('ModifyStatusReason')

        if m.get('ReplicationACL') is not None:
            self.replication_acl = m.get('ReplicationACL')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequireUpdate') is not None:
            self.require_update = m.get('RequireUpdate')

        if m.get('RequireUpdateItem') is not None:
            self.require_update_item = m.get('RequireUpdateItem')

        if m.get('RequireUpdateReason') is not None:
            self.require_update_reason = m.get('RequireUpdateReason')

        if m.get('SSLCreateTime') is not None:
            self.sslcreate_time = m.get('SSLCreateTime')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('SSLExpireTime') is not None:
            self.sslexpire_time = m.get('SSLExpireTime')

        if m.get('ServerCAUrl') is not None:
            self.server_caurl = m.get('ServerCAUrl')

        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')

        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')

        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')

        return self


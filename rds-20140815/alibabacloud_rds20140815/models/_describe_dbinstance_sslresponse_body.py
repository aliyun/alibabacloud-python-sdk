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
        # The method that is used to verify the instance. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        # 
        # *   **cert**
        # *   **prefer**
        # *   **verify-ca**
        # *   **verify-full** (supported only when the instance runs PostgreSQL 12 or later)
        self.acl = acl
        # The type of the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disks. Valid values:
        # 
        # *   **aliyun**: a cloud certificate
        # *   **custom**: a custom certificate
        self.catype = catype
        # The public key of the CA that issues client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.client_cacert = client_cacert
        # The time when the public key of the CA that issues client certificates expires. This parameter is supported only when the instance runs PostgreSQL with cloud disks. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format and must be in UTC.
        # 
        # This parameter is not supported.
        self.client_cacert_expire_time = client_cacert_expire_time
        # The certificate revocation list (CRL) that contains revoked client certificates. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.client_cert_revocation_list = client_cert_revocation_list
        # The endpoint that is protected by SSL encryption.
        self.connection_string = connection_string
        # Indicates whether the [forceful SSL encryption](https://help.aliyun.com/document_detail/95715.html) feature is enabled. This parameter is supported only for RDS for SQL Server instances.
        # 
        # *   **1**: The feature is enabled.
        # *   **0**: The feature is disabled.
        self.force_encryption = force_encryption
        # The status of the SSL link. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        # 
        # *   **success**: The SSL link is successfully configured.
        # *   **setting**: The SSL link is being configured.
        # *   **failed**: The SSL link failed to be configured.
        self.last_modify_status = last_modify_status
        # The reason why the SSL link stays in the current state. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.modify_status_reason = modify_status_reason
        # The method that is used to verify the replication permission. This parameter is supported only when the instance runs PostgreSQL with cloud disks. Valid values:
        # 
        # *   **cert**
        # *   **prefer**
        # *   **verify-ca**
        # *   **verify-full** (supported only when the instance runs PostgreSQL 12 or later)
        self.replication_acl = replication_acl
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the SSL certificate needs to be updated. Valid values:
        # 
        # >  An SSL certificate remains valid for one year. Before the used SSL certificate expires, you must update the validity period of the SSL certificate. If you do not update the validity period of the SSL certificate, your application or client that uses encrypted network connections cannot connect to your RDS instance.
        # 
        # **RDS instances that run MySQL and SQL Server**
        # 
        # *   **No**: The SSL certificate does not need to be updated.
        # *   **Yes**: The SSL certificate needs to be updated.
        # 
        # **RDS instances that run PostgreSQL**
        # 
        # *   **0**: The SSL certificate does not need to be updated.
        # *   **1**: The SSL certificate needs to be updated.
        self.require_update = require_update
        # The server certificate that needs to be updated. This parameter is supported only when the instance runs PostgreSQL with cloud disk.
        self.require_update_item = require_update_item
        # The reason why the server certificate needs to be updated. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.require_update_reason = require_update_reason
        # The time when the server certificate was created. This parameter is supported only when the instance runs PostgreSQL with cloud disks. In addition, this parameter is valid only when the CAType parameter value is aliyun.
        self.sslcreate_time = sslcreate_time
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # **RDS instances that run MySQL and SQL Server**
        # 
        # *   **Yes**: SSL encryption is enabled.
        # *   **No**: SSL encryption is disabled.
        # 
        # **RDS instances that run PostgreSQL**
        # 
        # *   **on**: SSL encryption is enabled.
        # *   **off**: SSL encryption is disabled.
        self.sslenabled = sslenabled
        # The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format and must be in UTC.
        self.sslexpire_time = sslexpire_time
        # The URL of the certificate that is used to issue the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disk.
        self.server_caurl = server_caurl
        # The content of the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.server_cert = server_cert
        # The private key of the server certificate. This parameter is supported only when the instance runs PostgreSQL with cloud disks.
        self.server_key = server_key
        # The [minimum Transport Layer Security (TLS) version](https://help.aliyun.com/document_detail/95715.html). Valid values: 1.0, 1.1, and 1.2. This parameter is supported only for ApsaraDB RDS for SQL Server instances.
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


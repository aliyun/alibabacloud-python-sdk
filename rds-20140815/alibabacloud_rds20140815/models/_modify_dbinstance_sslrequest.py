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
        self.acl = acl
        self.catype = catype
        self.certificate = certificate
        self.client_cacert = client_cacert
        self.client_caenabled = client_caenabled
        self.client_cert_revocation_list = client_cert_revocation_list
        self.client_crl_enabled = client_crl_enabled
        # This parameter is required.
        self.connection_string = connection_string
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.force_encryption = force_encryption
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pass_word = pass_word
        self.replication_acl = replication_acl
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sslenabled = sslenabled
        self.server_cert = server_cert
        self.server_key = server_key
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


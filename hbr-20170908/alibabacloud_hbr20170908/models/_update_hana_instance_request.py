# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHanaInstanceRequest(DaraModel):
    def __init__(
        self,
        alert_setting: str = None,
        cluster_id: str = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        password: str = None,
        resource_group_id: str = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        # 
        # This parameter is required.
        self.instance_number = instance_number
        # The password that is used to connect with the SAP HANA database.
        self.password = password
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL). Valid values:
        # 
        # *   true: The SAP HANA database is connected over SSL.
        # *   false: The SAP HANA database is not connected over SSL.
        # 
        # This parameter is required.
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Specifies whether to verify the SSL certificate of the SAP HANA database. Valid values:
        # 
        # *   true: The SSL certificate of the SAP HANA database is verified.
        # *   false: The SSL certificate of the SAP HANA database is not verified.
        # 
        # This parameter is required.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_setting is not None:
            result['AlertSetting'] = self.alert_setting

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.hana_name is not None:
            result['HanaName'] = self.hana_name

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number

        if self.password is not None:
            result['Password'] = self.password

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.validate_certificate is not None:
            result['ValidateCertificate'] = self.validate_certificate

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('HanaName') is not None:
            self.hana_name = m.get('HanaName')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self


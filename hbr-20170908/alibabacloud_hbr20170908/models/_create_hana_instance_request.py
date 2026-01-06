# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHanaInstanceRequest(DaraModel):
    def __init__(
        self,
        alert_setting: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        ecs_instance_id: str = None,
        hana_name: str = None,
        host: str = None,
        instance_number: int = None,
        password: str = None,
        resource_group_id: str = None,
        sid: str = None,
        use_ssl: bool = None,
        user_name: str = None,
        validate_certificate: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The backup type. Valid values:
        # 
        # - **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # - **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of the ECS instances that host the SAP HANA instance to be registered. Cloud Backup installs backup clients on the specified ECS instances.
        self.ecs_instance_id = ecs_instance_id
        # The name of the SAP HANA instance.
        self.hana_name = hana_name
        # The private or internal IP address of the host where the primary node of the SAP HANA instance resides.
        self.host = host
        # The instance number of the SAP HANA system.
        self.instance_number = instance_number
        # The password that is used to connect with the SAP HANA database.
        self.password = password
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security identifier (SID) of the SAP HANA database. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?spm=a2c4g.11186623.0.0.55c34b4ftZeXNK).
        self.sid = sid
        # Specifies whether to connect with the SAP HANA database over Secure Sockets Layer (SSL).
        self.use_ssl = use_ssl
        # The username of the SYSTEMDB database.
        self.user_name = user_name
        # Specifies whether to verify the SSL certificate of the SAP HANA database.
        self.validate_certificate = validate_certificate
        # The ID of the backup vault.
        # 
        # This parameter is required.
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

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

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

        if self.sid is not None:
            result['Sid'] = self.sid

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

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

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

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ValidateCertificate') is not None:
            self.validate_certificate = m.get('ValidateCertificate')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self


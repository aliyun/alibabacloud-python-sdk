# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientsRequest(DaraModel):
    def __init__(
        self,
        alert_setting: str = None,
        client_info: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        resource_group_id: str = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the HBR client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The installation information of the HBR clients.
        self.client_info = client_info
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The backup type. Valid values:
        # 
        # - **SELF_ACCOUNT**: Data is backed up within the same Alibaba Cloud account.
        # - **CROSS_ACCOUNT**: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to transmit data over HTTPS. Valid values:
        # 
        # *   true: transmits data over HTTPS.
        # *   false: transmits data over HTTP.
        self.use_https = use_https
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

        if self.client_info is not None:
            result['ClientInfo'] = self.client_info

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.use_https is not None:
            result['UseHttps'] = self.use_https

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')

        if m.get('ClientInfo') is not None:
            self.client_info = m.get('ClientInfo')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self


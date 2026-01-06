# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClientSettingsRequest(DaraModel):
    def __init__(
        self,
        alert_on_partial_complete: bool = None,
        client_id: str = None,
        data_network_type: str = None,
        data_proxy_setting: str = None,
        max_cpu_core: int = None,
        max_memory: int = None,
        max_worker: int = None,
        proxy_host: str = None,
        proxy_password: str = None,
        proxy_port: int = None,
        proxy_user: str = None,
        resource_group_id: str = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # Specifies whether to generate alert for partially completed jobs. This parameter is valid only for on-premises file backup and ECS file backup.
        self.alert_on_partial_complete = alert_on_partial_complete
        # The ID of the HBR client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The type of the endpoint on the data plane. Valid values:
        # 
        # *   **PUBLIC**: Internet
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CLASSIC**: classic network
        self.data_network_type = data_network_type
        # The proxy configuration on the data plane. Valid values:
        # 
        # *   **DISABLE**: The proxy is not used.
        # *   **USE_CONTROL_PROXY** (default): The configuration is the same as that on the control plane.
        # *   **CUSTOM**: The configuration is customized (HTTP).
        self.data_proxy_setting = data_proxy_setting
        # The number of CPU cores used by a single backup job. The value 0 indicates that the number is unlimited.
        self.max_cpu_core = max_cpu_core
        # The maximum memory that can be used by the client. Unit: bytes. Only V2.13.0 and later are supported.
        self.max_memory = max_memory
        # The number of concurrent backup jobs. The value 0 indicates that the number is unlimited.
        self.max_worker = max_worker
        # The custom host IP address of the proxy server on the data plane.
        self.proxy_host = proxy_host
        # The custom password of the proxy server on the data plane.
        self.proxy_password = proxy_password
        # The custom host port of the proxy server on the data plane.
        self.proxy_port = proxy_port
        # The custom username of the proxy server on the data plane.
        self.proxy_user = proxy_user
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to transmit the data on the data plane over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https
        # The ID of the backup vault. This parameter is required for the old HBR client.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.data_network_type is not None:
            result['DataNetworkType'] = self.data_network_type

        if self.data_proxy_setting is not None:
            result['DataProxySetting'] = self.data_proxy_setting

        if self.max_cpu_core is not None:
            result['MaxCpuCore'] = self.max_cpu_core

        if self.max_memory is not None:
            result['MaxMemory'] = self.max_memory

        if self.max_worker is not None:
            result['MaxWorker'] = self.max_worker

        if self.proxy_host is not None:
            result['ProxyHost'] = self.proxy_host

        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password

        if self.proxy_port is not None:
            result['ProxyPort'] = self.proxy_port

        if self.proxy_user is not None:
            result['ProxyUser'] = self.proxy_user

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.use_https is not None:
            result['UseHttps'] = self.use_https

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DataNetworkType') is not None:
            self.data_network_type = m.get('DataNetworkType')

        if m.get('DataProxySetting') is not None:
            self.data_proxy_setting = m.get('DataProxySetting')

        if m.get('MaxCpuCore') is not None:
            self.max_cpu_core = m.get('MaxCpuCore')

        if m.get('MaxMemory') is not None:
            self.max_memory = m.get('MaxMemory')

        if m.get('MaxWorker') is not None:
            self.max_worker = m.get('MaxWorker')

        if m.get('ProxyHost') is not None:
            self.proxy_host = m.get('ProxyHost')

        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')

        if m.get('ProxyPort') is not None:
            self.proxy_port = m.get('ProxyPort')

        if m.get('ProxyUser') is not None:
            self.proxy_user = m.get('ProxyUser')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self


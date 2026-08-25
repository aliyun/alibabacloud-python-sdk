# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: List[main_models.DescribeBackupClientsResponseBodyClients] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of backup clients.
        self.clients = clients
        # The response code. 200 indicates success.
        self.code = code
        # The returned message. The value "successful" is returned for successful requests. An error message is returned for failed requests.
        self.message = message
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Minimum value: 1. Maximum value: 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The total number of backup clients that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            for v1 in self.clients:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clients'] = []
        if self.clients is not None:
            for k1 in self.clients:
                result['Clients'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.DescribeBackupClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupClientsResponseBodyClients(DaraModel):
    def __init__(
        self,
        appliance: bool = None,
        arch_type: str = None,
        backup_status: str = None,
        client_id: str = None,
        client_type: str = None,
        client_version: str = None,
        created_time: int = None,
        hostname: str = None,
        instance_id: str = None,
        instance_name: str = None,
        last_heart_beat_time: int = None,
        max_client_version: str = None,
        os_type: str = None,
        private_ip_v4: str = None,
        settings: main_models.DescribeBackupClientsResponseBodyClientsSettings = None,
        status: str = None,
        tags: List[main_models.DescribeBackupClientsResponseBodyClientsTags] = None,
        updated_time: int = None,
        zone_id: str = None,
    ):
        # Indicates whether the client is a hardware monitoring appliance client.
        # 
        # - true: The client is a hardware monitoring appliance client.
        # - false: The client is not a hardware monitoring appliance client.
        self.appliance = appliance
        # This parameter is valid only when **ClientType** is set to **ECS_CLIENT**. The system architecture of the backup client. Valid values:
        # * **amd64**
        # * **386**
        self.arch_type = arch_type
        # The protection status of the backup client. Valid values:
        # * **UNPROTECTED**: The server is not protected.
        # * **PROTECTED**: The server is protected.
        self.backup_status = backup_status
        # The ID of the backup client.
        self.client_id = client_id
        # The type of the backup client. The value **ECS_CLIENT** indicates an ECS File Backup client.
        self.client_type = client_type
        # The version number of the backup client.
        self.client_version = client_version
        # The time when the backup client was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The hostname of the backup client.
        self.hostname = hostname
        # The instance ID.
        # 
        # - If the client type is ECS File Backup client, this parameter indicates the ECS instance ID.
        # - If the client type is local file backup client, this parameter indicates the hardware fingerprint generated based on system information.
        self.instance_id = instance_id
        # This parameter is valid only when **ClientType** is set to **ECS_CLIENT**. The name of the ECS instance.
        self.instance_name = instance_name
        # The time of the last heartbeat of the backup client. This value is a UNIX timestamp. Unit: seconds.
        self.last_heart_beat_time = last_heart_beat_time
        # The latest version number of the backup client.
        self.max_client_version = max_client_version
        # This parameter is valid only when **ClientType** is set to **ECS_CLIENT**. The operating system type of the client. Valid values:
        # * **windows**
        # * **linux**
        self.os_type = os_type
        # This parameter is valid only when **ClientType** is set to **ECS_CLIENT**. The internal IP address of the ECS instance.
        self.private_ip_v4 = private_ip_v4
        # The configuration information of the backup client.
        self.settings = settings
        # The status of the backup client. Valid values:
        # * **REGISTERED**: The client is registered.
        # * **ACTIVATED**: The client is activated.
        # * **DEACTIVATED**: The client activation has expired.
        # * **INSTALLING**: The client is being installed.
        # * **INSTALL_FAILED**: The client installation failed.
        # * **NOT_INSTALLED**: The client is not installed.
        # * **UPGRADING**: The client is being upgraded.
        # * **UPGRADE_FAILED**: The client upgrade failed.
        # * **UNINSTALLING**: The client is being uninstalled.
        # * **UNINSTALL_FAILED**: The client uninstallation failed.
        # * **STOPPED**: The client service is stopped.
        # * **UNKNOWN**: The client is disconnected.
        self.status = status
        # The tag information.
        self.tags = tags
        # The time when the backup client was last updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # This parameter is valid only when **ClientType** is set to **ECS_CLIENT**. The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.settings:
            self.settings.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appliance is not None:
            result['Appliance'] = self.appliance

        if self.arch_type is not None:
            result['ArchType'] = self.arch_type

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time

        if self.max_client_version is not None:
            result['MaxClientVersion'] = self.max_client_version

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.private_ip_v4 is not None:
            result['PrivateIpV4'] = self.private_ip_v4

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Appliance') is not None:
            self.appliance = m.get('Appliance')

        if m.get('ArchType') is not None:
            self.arch_type = m.get('ArchType')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')

        if m.get('MaxClientVersion') is not None:
            self.max_client_version = m.get('MaxClientVersion')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PrivateIpV4') is not None:
            self.private_ip_v4 = m.get('PrivateIpV4')

        if m.get('Settings') is not None:
            temp_model = main_models.DescribeBackupClientsResponseBodyClientsSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeBackupClientsResponseBodyClientsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeBackupClientsResponseBodyClientsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the backup vault. Valid values of N: 1 to 20.
        # 
        # - The tag key cannot start with `aliyun` or `acs:`. 
        # - The tag key cannot contain `http://` or `https://`.
        # - The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20.
        # 
        # - The tag value cannot start with `aliyun` or `acs:`. 
        # - The tag value cannot contain `http://` or `https://`.
        # - The tag value cannot be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeBackupClientsResponseBodyClientsSettings(DaraModel):
    def __init__(
        self,
        alert_on_partial_complete: bool = None,
        data_network_type: str = None,
        data_proxy_setting: str = None,
        max_cpu_core: str = None,
        max_memory: int = None,
        max_worker: str = None,
        proxy_host: str = None,
        proxy_password: str = None,
        proxy_port: int = None,
        proxy_user: str = None,
        use_https: str = None,
    ):
        # Specifies whether to send alerts for partially completed jobs. This setting applies only to File Backup and ECS File Backup Essential Edition.
        self.alert_on_partial_complete = alert_on_partial_complete
        # The type of the data plane endpoint. Valid values:
        # 
        # - **PUBLIC**: public network.
        # - **VPC**: VPC network.
        # - **CLASSIC**: classic network.
        self.data_network_type = data_network_type
        # The data plane proxy setting. Valid values:
        # 
        # - **DISABLE**: No proxy is used.
        # - **USE_CONTROL_PROXY** (default): The same configuration as the control plane is used.
        # - **CUSTOM**: A custom configuration is used (HTTP protocol).
        self.data_proxy_setting = data_proxy_setting
        # The number of CPU cores used by a single backup job. A value of 0 indicates no limit.
        self.max_cpu_core = max_cpu_core
        # The maximum memory that the client can use. Unit: bytes. Only versions 2.13.0 and later are supported.
        self.max_memory = max_memory
        # The number of concurrent workers for a single backup job. A value of 0 indicates no limit.
        self.max_worker = max_worker
        # The IP address of the custom data plane proxy server.
        self.proxy_host = proxy_host
        # The password of the custom data plane proxy server.
        self.proxy_password = proxy_password
        # The port of the custom data plane proxy server.
        self.proxy_port = proxy_port
        # The username of the custom data plane proxy server.
        self.proxy_user = proxy_user
        # Indicates whether HTTPS is used to transmit data plane data.
        # 
        # - true: HTTPS is used for transmission.
        # - false: HTTP is used for transmission.
        self.use_https = use_https

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_on_partial_complete is not None:
            result['AlertOnPartialComplete'] = self.alert_on_partial_complete

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

        if self.use_https is not None:
            result['UseHttps'] = self.use_https

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertOnPartialComplete') is not None:
            self.alert_on_partial_complete = m.get('AlertOnPartialComplete')

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

        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')

        return self


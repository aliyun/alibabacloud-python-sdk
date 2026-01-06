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
        # The queried backup clients.
        self.clients = clients
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned HBR clients that meet the specified conditions.
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
        # Indicates whether the client is installed on an all-in-one PC that integrates hardware and monitoring program. Valid values:
        # 
        # *   true: The client is installed on an all-in-one PC that integrates hardware and monitoring program.
        # *   false: The client is not installed on an all-in-one PC that integrates hardware and monitoring program.
        self.appliance = appliance
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the system architecture where the backup client resides. Valid values:
        # 
        # *   **amd64**
        # *   **386**
        self.arch_type = arch_type
        # The protection status of the backup client. Valid values:
        # 
        # *   **UNPROTECTED**: The backup client is not protected.
        # *   **PROTECTED**: The backup client is protected.
        self.backup_status = backup_status
        # The ID of the backup client.
        self.client_id = client_id
        # The type of the backup client. Valid value: **ECS_CLIENT**, which indicates a client for ECS file backup.
        self.client_type = client_type
        # The version number of the backup client.
        self.client_version = client_version
        # The time when the backup client was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The hostname of the backup client.
        self.hostname = hostname
        # The instance ID.
        # 
        # *   If the client is used to back up ECS files, this parameter indicates the ID of an ECS instance.
        # *   If the client is used to back up on-premises files, this parameter indicates the hardware fingerprint that is generated based on the system information.
        self.instance_id = instance_id
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the name of the ECS instance.
        self.instance_name = instance_name
        # The last heartbeat time of the backup client. The value is a UNIX timestamp. Unit: seconds.
        self.last_heart_beat_time = last_heart_beat_time
        # The latest version number of the backup client.
        self.max_client_version = max_client_version
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the operating system type of the backup client. Valid values:
        # 
        # *   **windows**
        # *   **linux**
        self.os_type = os_type
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the internal IP address of the ECS instance.
        self.private_ip_v4 = private_ip_v4
        # The configuration information of the backup client.
        self.settings = settings
        # The status of the backup client. Valid values:
        # 
        # *   **REGISTERED**: The backup client is registered.
        # *   **ACTIVATED**: The backup client is activated.
        # *   **DEACTIVATED**: The backup client fails to be activated.
        # *   **INSTALLING**: The backup client is being installed.
        # *   **INSTALL_FAILED**: The backup client fails to be installed.
        # *   **NOT_INSTALLED**: The backup client is not installed.
        # *   **UPGRADING**: The backup client is being upgraded.
        # *   **UPGRADE_FAILED**: The backup client fails to be upgraded.
        # *   **UNINSTALLING**: The backup client is being uninstalled.
        # *   **UNINSTALL_FAILED**: The backup client fails to be uninstalled.
        # *   **STOPPED**: The backup client is out of service.
        # *   **UNKNOWN**: The backup client is disconnected.
        self.status = status
        # The tag information.
        self.tags = tags
        # The time when the backup client was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # This parameter is valid only if the **ClientType** parameter is set to **ECS_CLIENT**. This parameter indicates the zone of the backup client.
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
        # The tag key of the backup vault. Valid values of N: 1 to 20
        # 
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The tag value of the backup vault. Valid values of N: 1 to 20
        # 
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        # *   The tag value cannot be an empty string.
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
        # Indicates whether alerts are generated for partially completed jobs. This parameter is valid only for on-premises file backup and ECS file backup.
        self.alert_on_partial_complete = alert_on_partial_complete
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
        # Indicates whether data on the data plane is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
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


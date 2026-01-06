# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: main_models.DescribeClientsResponseBodyClients = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The Cloud Backup clients.
        self.clients = clients
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()

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
        if m.get('Clients') is not None:
            temp_model = main_models.DescribeClientsResponseBodyClients()
            self.clients = temp_model.from_map(m.get('Clients'))

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

class DescribeClientsResponseBodyClients(DaraModel):
    def __init__(
        self,
        client: List[main_models.DescribeClientsResponseBodyClientsClient] = None,
    ):
        self.client = client

    def validate(self):
        if self.client:
            for v1 in self.client:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Client'] = []
        if self.client is not None:
            for k1 in self.client:
                result['Client'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k1 in m.get('Client'):
                temp_model = main_models.DescribeClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k1))

        return self

class DescribeClientsResponseBodyClientsClient(DaraModel):
    def __init__(
        self,
        alert_setting: str = None,
        client_id: str = None,
        client_name: str = None,
        client_type: str = None,
        client_version: str = None,
        cluster_id: str = None,
        created_time: int = None,
        heart_beat_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        max_version: str = None,
        network_type: str = None,
        status: str = None,
        status_message: str = None,
        updated_time: int = None,
        use_https: bool = None,
        vault_id: str = None,
    ):
        # The alert settings. Valid value: INHERITED, which indicates that the Cloud Backup client sends alert notifications by using the same method configured for the backup vault.
        self.alert_setting = alert_setting
        # The ID of the Cloud Backup client.
        self.client_id = client_id
        # The client name.
        self.client_name = client_name
        # The type of the Cloud Backup client. Valid value: **ECS_AGENT**, which indicates an SAP HANA backup client.
        self.client_type = client_type
        # The version number of the Cloud Backup client.
        self.client_version = client_version
        # The ID of the SAP HANA instance.
        self.cluster_id = cluster_id
        # The time when the Cloud Backup client was created.
        self.created_time = created_time
        # The latest heartbeat time of the Cloud Backup client. This value is a UNIX timestamp. Unit: seconds.
        self.heart_beat_time = heart_beat_time
        # The instance ID.
        self.instance_id = instance_id
        # The name of the ECS instance.
        self.instance_name = instance_name
        # The maximum version number of the Cloud Backup client.
        self.max_version = max_version
        # The network type. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: the virtual private cloud (VPC)
        self.network_type = network_type
        # The status of the Cloud Backup client. Valid values:
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
        # The status information.
        self.status_message = status_message
        # The time when the Cloud Backup client was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # Indicates whether data is transmitted over HTTPS. Valid values:
        # 
        # *   true: Data is transmitted over HTTPS.
        # *   false: Data is transmitted over HTTP.
        self.use_https = use_https
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

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_name is not None:
            result['ClientName'] = self.client_name

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.heart_beat_time is not None:
            result['HeartBeatTime'] = self.heart_beat_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.use_https is not None:
            result['UseHttps'] = self.use_https

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertSetting') is not None:
            self.alert_setting = m.get('AlertSetting')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('HeartBeatTime') is not None:
            self.heart_beat_time = m.get('HeartBeatTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UseHttps') is not None:
            self.use_https = m.get('UseHttps')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self


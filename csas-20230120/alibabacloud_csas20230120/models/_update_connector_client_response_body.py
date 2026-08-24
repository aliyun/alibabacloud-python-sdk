# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateConnectorClientResponseBody(DaraModel):
    def __init__(
        self,
        connector_client: main_models.UpdateConnectorClientResponseBodyConnectorClient = None,
        request_id: str = None,
    ):
        # ConnectorClient。
        self.connector_client = connector_client
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.connector_client:
            self.connector_client.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_client is not None:
            result['ConnectorClient'] = self.connector_client.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorClient') is not None:
            temp_model = main_models.UpdateConnectorClientResponseBodyConnectorClient()
            self.connector_client = temp_model.from_map(m.get('ConnectorClient'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateConnectorClientResponseBodyConnectorClient(DaraModel):
    def __init__(
        self,
        cpusize: str = None,
        connection_status: str = None,
        connector_id: str = None,
        create_time: str = None,
        dev_tag: str = None,
        hosname: str = None,
        kernel_version: str = None,
        memory_size: str = None,
        operation_status: str = None,
        private_ip: str = None,
        process_run_time: int = None,
        public_ip: str = None,
        release_notes: List[str] = None,
        status: str = None,
        upgrade_status: str = None,
        version: str = None,
        version_to_rollback: str = None,
    ):
        # The number of CPUs of the ConnectorClient.
        self.cpusize = cpusize
        # The connection status of the ConnectorClient. Valid values:
        # - **Connected**: connected.
        # - **Disconnected**: disconnected.
        self.connection_status = connection_status
        # ConnectorID。
        self.connector_id = connector_id
        # The time when the connector was created.
        self.create_time = create_time
        # The unique identifier of the ConnectorClient device.
        self.dev_tag = dev_tag
        # The hostname.
        self.hosname = hosname
        # The kernel version of the ConnectorClient.
        self.kernel_version = kernel_version
        # The memory size of the ConnectorClient. Unit: MB.
        self.memory_size = memory_size
        # The O&M status. Valid values:
        # - **Running**: O&M in progress.
        # - **Failed**: O&M failed.
        # - (empty string): not in O&M status.
        self.operation_status = operation_status
        # The private IP address of the ConnectorClient.
        self.private_ip = private_ip
        # The program runtime. Unit: seconds.
        self.process_run_time = process_run_time
        # The public IP address of the ConnectorClient.
        self.public_ip = public_ip
        # The version number.
        self.release_notes = release_notes
        # The enabled status of the ConnectorClient, which can be used to force the client offline. Valid values:
        # - **Enabled**: enabled.
        # - **Disabled**: disabled.
        self.status = status
        # The version status of the connector. Valid values:
        # 
        # - **Latest**: the current version is the latest version.
        # - **NewVersionAvailable**: a newer version is available for upgrade.
        self.upgrade_status = upgrade_status
        # The blockchain version.
        self.version = version
        # The version to roll back to.
        self.version_to_rollback = version_to_rollback

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpusize is not None:
            result['CPUSize'] = self.cpusize

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.hosname is not None:
            result['Hosname'] = self.hosname

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.process_run_time is not None:
            result['ProcessRunTime'] = self.process_run_time

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.release_notes is not None:
            result['ReleaseNotes'] = self.release_notes

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.version is not None:
            result['Version'] = self.version

        if self.version_to_rollback is not None:
            result['VersionToRollback'] = self.version_to_rollback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUSize') is not None:
            self.cpusize = m.get('CPUSize')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('Hosname') is not None:
            self.hosname = m.get('Hosname')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('ProcessRunTime') is not None:
            self.process_run_time = m.get('ProcessRunTime')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('ReleaseNotes') is not None:
            self.release_notes = m.get('ReleaseNotes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionToRollback') is not None:
            self.version_to_rollback = m.get('VersionToRollback')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: List[main_models.DescribeBackupClientsResponseBodyClients] = None,
        request_id: str = None,
    ):
        # An array that consists of the information about the anti-ransomware agent.
        self.clients = clients
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.DescribeBackupClientsResponseBodyClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupClientsResponseBodyClients(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_status: str = None,
        client_version: str = None,
        instance_id: str = None,
        uuid: str = None,
    ):
        # The ID of the anti-ransomware agent.
        self.client_id = client_id
        # The status of the anti-ransomware agent.
        # 
        # Valid values:
        # 
        # *   **INSTALLING**: The agent is being installed.
        # *   **ONLINE**: The agent is online.
        # *   **UNINSTALLING**: The agent is being uninstalled.
        # *   **NOT_INSTALLED**: The agent is not installed.
        # *   **ACTIVATED**: The agent is enabled.
        # *   **CLIENT_CONNECTION_ERROR**: A connection error occurs on the agent.
        self.client_status = client_status
        # The version of the anti-ransomware agent.
        self.client_version = client_version
        # The ID of the ECS instance on which the anti-ransomware agent is installed.
        self.instance_id = instance_id
        # The UUID of the Elastic Compute Service (ECS) instance on which the anti-ransomware agent is installed.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


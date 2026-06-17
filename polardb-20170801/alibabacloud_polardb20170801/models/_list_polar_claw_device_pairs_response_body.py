# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ListPolarClawDevicePairsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        paired: List[main_models.ListPolarClawDevicePairsResponseBodyPaired] = None,
        pending: List[main_models.ListPolarClawDevicePairsResponseBodyPending] = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The status code of the response.
        self.code = code
        # The response message.
        self.message = message
        # A list of paired devices.
        self.paired = paired
        # A list of pending pairing requests.
        self.pending = pending
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.paired:
            for v1 in self.paired:
                 if v1:
                    v1.validate()
        if self.pending:
            for v1 in self.pending:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Paired'] = []
        if self.paired is not None:
            for k1 in self.paired:
                result['Paired'].append(k1.to_map() if k1 else None)

        result['Pending'] = []
        if self.pending is not None:
            for k1 in self.pending:
                result['Pending'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.paired = []
        if m.get('Paired') is not None:
            for k1 in m.get('Paired'):
                temp_model = main_models.ListPolarClawDevicePairsResponseBodyPaired()
                self.paired.append(temp_model.from_map(k1))

        self.pending = []
        if m.get('Pending') is not None:
            for k1 in m.get('Pending'):
                temp_model = main_models.ListPolarClawDevicePairsResponseBodyPending()
                self.pending.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPolarClawDevicePairsResponseBodyPending(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_mode: str = None,
        device_family: str = None,
        device_id: str = None,
        display_name: str = None,
        is_repair: bool = None,
        pair_request_id: str = None,
        platform: str = None,
        public_key: str = None,
        remote_ip: str = None,
        role: str = None,
        roles: List[str] = None,
        scopes: List[str] = None,
        silent: bool = None,
        ts: int = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client mode.
        self.client_mode = client_mode
        # The device family.
        self.device_family = device_family
        # The unique device ID.
        self.device_id = device_id
        # The display name of the device.
        self.display_name = display_name
        # Whether the request is to repair an existing pairing.
        self.is_repair = is_repair
        # The pairing request ID.
        self.pair_request_id = pair_request_id
        # The operating system.
        self.platform = platform
        # The Ed25519 public key.
        self.public_key = public_key
        # The requester\\"s remote IP address.
        self.remote_ip = remote_ip
        # The device role.
        self.role = role
        # The list of roles.
        self.roles = roles
        # The list of permission scopes.
        self.scopes = scopes
        # Whether this is a silent pairing.
        self.silent = silent
        # The timestamp of the pairing request, in Unix milliseconds.
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_mode is not None:
            result['ClientMode'] = self.client_mode

        if self.device_family is not None:
            result['DeviceFamily'] = self.device_family

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_repair is not None:
            result['IsRepair'] = self.is_repair

        if self.pair_request_id is not None:
            result['PairRequestId'] = self.pair_request_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.remote_ip is not None:
            result['RemoteIp'] = self.remote_ip

        if self.role is not None:
            result['Role'] = self.role

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        if self.silent is not None:
            result['Silent'] = self.silent

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientMode') is not None:
            self.client_mode = m.get('ClientMode')

        if m.get('DeviceFamily') is not None:
            self.device_family = m.get('DeviceFamily')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsRepair') is not None:
            self.is_repair = m.get('IsRepair')

        if m.get('PairRequestId') is not None:
            self.pair_request_id = m.get('PairRequestId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('RemoteIp') is not None:
            self.remote_ip = m.get('RemoteIp')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        if m.get('Silent') is not None:
            self.silent = m.get('Silent')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class ListPolarClawDevicePairsResponseBodyPaired(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_mode: str = None,
        created_at_ms: int = None,
        device_family: str = None,
        device_id: str = None,
        display_name: str = None,
        last_seen_at_ms: int = None,
        platform: str = None,
        role: str = None,
        scopes: List[str] = None,
    ):
        # The client ID.
        self.client_id = client_id
        # The client mode.
        self.client_mode = client_mode
        # The time when the device pairing was created, in Unix milliseconds.
        self.created_at_ms = created_at_ms
        # The device family.
        self.device_family = device_family
        # The unique device ID.
        self.device_id = device_id
        # The display name of the device.
        self.display_name = display_name
        # The time when the device was last active, in Unix milliseconds.
        self.last_seen_at_ms = last_seen_at_ms
        # The operating system.
        self.platform = platform
        # The device role.
        self.role = role
        # The list of permission scopes.
        self.scopes = scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_mode is not None:
            result['ClientMode'] = self.client_mode

        if self.created_at_ms is not None:
            result['CreatedAtMs'] = self.created_at_ms

        if self.device_family is not None:
            result['DeviceFamily'] = self.device_family

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.last_seen_at_ms is not None:
            result['LastSeenAtMs'] = self.last_seen_at_ms

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.role is not None:
            result['Role'] = self.role

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientMode') is not None:
            self.client_mode = m.get('ClientMode')

        if m.get('CreatedAtMs') is not None:
            self.created_at_ms = m.get('CreatedAtMs')

        if m.get('DeviceFamily') is not None:
            self.device_family = m.get('DeviceFamily')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('LastSeenAtMs') is not None:
            self.last_seen_at_ms = m.get('LastSeenAtMs')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        return self


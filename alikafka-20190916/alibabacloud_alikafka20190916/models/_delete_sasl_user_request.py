# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSaslUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mechanism: str = None,
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Encryption method. Valid values:
        # 
        # - SCRAM-SHA-512 (selected by default)
        # 
        # - SCRAM-SHA-256
        # 
        # > This parameter is only supported for Serverless instances.
        self.mechanism = mechanism
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Type. Valid values:
        # 
        # - **plain**: A simple username and password verification mechanism. MSMQ optimizes the PLAIN mechanism to support adding SASL users dynamically without restarting the instance.
        # 
        # - **scram**: A username and password verification mechanism with higher security than PLAIN. MSMQ uses SCRAM-SHA-256.
        # 
        # - **LDAP**: Only applicable for deleting Confluent instance users.
        # 
        # Default value: **plain**.
        self.type = type
        # Username.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mechanism is not None:
            result['Mechanism'] = self.mechanism

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mechanism') is not None:
            self.mechanism = m.get('Mechanism')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self


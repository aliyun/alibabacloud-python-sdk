# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSaslUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mechanism: str = None,
        password: str = None,
        region_id: str = None,
        type: str = None,
        username: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The encryption method. Valid values:
        # 
        # - SCRAM-SHA-512 (default)
        # 
        # - SCRAM-SHA-256
        # 
        # > This parameter is supported only for Serverless instances.
        self.mechanism = mechanism
        # The password.
        # 
        # This parameter is required.
        self.password = password
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The SASL mechanism. Valid values:
        # 
        # - plain: a simple username and password authentication mechanism. Message Queue for Apache Kafka optimizes the PLAIN mechanism to support the dynamic creation of SASL users without the need to restart the instance.
        # 
        # - scram: a username and password authentication mechanism that provides higher security than the PLAIN mechanism. Message Queue for Apache Kafka uses Salted Challenge Response Authentication Mechanism (SCRAM)-SHA-256.
        # 
        # - LDAP: This value is applicable only when you create users for Confluent instances.
        # 
        # Default value: plain.
        self.type = type
        # The username.
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

        if self.password is not None:
            result['Password'] = self.password

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

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self


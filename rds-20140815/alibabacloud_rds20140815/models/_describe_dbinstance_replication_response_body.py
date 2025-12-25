# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceReplicationResponseBody(DaraModel):
    def __init__(
        self,
        external_replication: str = None,
        replication_delay: str = None,
        replication_error_message: str = None,
        replication_ip: str = None,
        replication_port: str = None,
        replication_source: str = None,
        replication_state: str = None,
        request_id: str = None,
    ):
        # Indicates whether the native replication mods is enabled. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.external_replication = external_replication
        # The replication latency. Unit: seconds.
        self.replication_delay = replication_delay
        # The replication error message.
        self.replication_error_message = replication_error_message
        self.replication_ip = replication_ip
        self.replication_port = replication_port
        # The source of the native replication.
        self.replication_source = replication_source
        # The current replication status. Valid values:
        # 
        # *   **Running**
        # *   **Connecting**
        # *   **Stopped**
        # *   **Error**
        self.replication_state = replication_state
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_replication is not None:
            result['ExternalReplication'] = self.external_replication

        if self.replication_delay is not None:
            result['ReplicationDelay'] = self.replication_delay

        if self.replication_error_message is not None:
            result['ReplicationErrorMessage'] = self.replication_error_message

        if self.replication_ip is not None:
            result['ReplicationIp'] = self.replication_ip

        if self.replication_port is not None:
            result['ReplicationPort'] = self.replication_port

        if self.replication_source is not None:
            result['ReplicationSource'] = self.replication_source

        if self.replication_state is not None:
            result['ReplicationState'] = self.replication_state

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalReplication') is not None:
            self.external_replication = m.get('ExternalReplication')

        if m.get('ReplicationDelay') is not None:
            self.replication_delay = m.get('ReplicationDelay')

        if m.get('ReplicationErrorMessage') is not None:
            self.replication_error_message = m.get('ReplicationErrorMessage')

        if m.get('ReplicationIp') is not None:
            self.replication_ip = m.get('ReplicationIp')

        if m.get('ReplicationPort') is not None:
            self.replication_port = m.get('ReplicationPort')

        if m.get('ReplicationSource') is not None:
            self.replication_source = m.get('ReplicationSource')

        if m.get('ReplicationState') is not None:
            self.replication_state = m.get('ReplicationState')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


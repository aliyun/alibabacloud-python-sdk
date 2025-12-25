# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActivateMigrationTargetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        request_id: str = None,
        source_ip_address: str = None,
        source_port: int = None,
        task_id: int = None,
    ):
        # The name of the destination instance.
        self.dbinstance_name = dbinstance_name
        # The ID of the request.
        self.request_id = request_id
        # The private IP address that is used to connect to the self-managed PostgreSQL instance.
        self.source_ip_address = source_ip_address
        # The port number that is used to connect to the self-managed PostgreSQL instance.
        self.source_port = source_port
        # The ID of the identification task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        export_type: int = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.export_type = export_type
        # This parameter is required.
        self.instance_id = instance_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportDefinitionAsynchronousRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        import_type: int = None,
        instance_id: str = None,
        instance_name: str = None,
        oss_url: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.import_type = import_type
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.oss_url = oss_url
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

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self


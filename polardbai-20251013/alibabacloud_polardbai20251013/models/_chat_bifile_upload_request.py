# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIFileUploadRequest(DaraModel):
    def __init__(
        self,
        auth_message: str = None,
        auth_type: str = None,
        file_name: str = None,
        instance_name: str = None,
    ):
        self.auth_message = auth_message
        self.auth_type = auth_type
        self.file_name = file_name
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_message is not None:
            result['AuthMessage'] = self.auth_message

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMessage') is not None:
            self.auth_message = m.get('AuthMessage')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self


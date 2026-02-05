# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuspendCallWithFileRequest(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.file_path = file_path
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


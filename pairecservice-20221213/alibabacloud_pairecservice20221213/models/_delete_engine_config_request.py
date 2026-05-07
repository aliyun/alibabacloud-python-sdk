# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEngineConfigRequest(DaraModel):
    def __init__(
        self,
        delete_all: bool = None,
        instance_id: str = None,
    ):
        self.delete_all = delete_all
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


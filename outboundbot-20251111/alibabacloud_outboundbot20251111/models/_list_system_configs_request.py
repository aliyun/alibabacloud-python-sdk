# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSystemConfigsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The system configuration name.\\
        # callableTime: the outbound job window.\\
        # calleeDailyAttemptLimit: the maximum number of daily calls to a single callee number.
        self.name = name
        # The configuration type ID.\\
        # If ObjectType is set to INSTANCE, this parameter specifies the instance ID.\\
        # If ObjectType is set to TENANT, this parameter specifies the tenant ID.
        self.object_id = object_id
        # The configuration type.\\
        # INSTANCE: instance-level.\\
        # TENANT: tenant-level.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self


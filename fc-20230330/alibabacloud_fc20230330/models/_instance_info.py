# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceInfo(DaraModel):
    def __init__(
        self,
        created_time_ms: int = None,
        destroyed_time_ms: int = None,
        instance_id: str = None,
        qualifier: str = None,
        resource_type: str = None,
        status: str = None,
        version_id: str = None,
    ):
        self.created_time_ms = created_time_ms
        self.destroyed_time_ms = destroyed_time_ms
        self.instance_id = instance_id
        self.qualifier = qualifier
        self.resource_type = resource_type
        self.status = status
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time_ms is not None:
            result['createdTimeMs'] = self.created_time_ms

        if self.destroyed_time_ms is not None:
            result['destroyedTimeMs'] = self.destroyed_time_ms

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTimeMs') is not None:
            self.created_time_ms = m.get('createdTimeMs')

        if m.get('destroyedTimeMs') is not None:
            self.destroyed_time_ms = m.get('destroyedTimeMs')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self


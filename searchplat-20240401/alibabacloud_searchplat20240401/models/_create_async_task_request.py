# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAsyncTaskRequest(DaraModel):
    def __init__(
        self,
        data_id: int = None,
        id: str = None,
        name: str = None,
        service_id: str = None,
        service_type: str = None,
        dry_run: bool = None,
    ):
        # The playground data ID.
        self.data_id = data_id
        # The asynchronous task ID.
        self.id = id
        # The task name.
        self.name = name
        # The service ID.
        self.service_id = service_id
        # The service type.
        self.service_type = service_type
        # Specifies whether to perform a dry run request.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAsyncTasksRequest(DaraModel):
    def __init__(
        self,
        data_id: int = None,
        dry_run: bool = None,
        service_type: str = None,
    ):
        # The trial data ID.
        self.data_id = data_id
        # Specifies whether to validate the request parameters without performing the actual operation. Default value: false.
        # 
        # Valid values:
        # 
        # - **true**
        # 
        # - **false**.
        self.dry_run = dry_run
        # The service type.
        # 
        # - document-analyze.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self


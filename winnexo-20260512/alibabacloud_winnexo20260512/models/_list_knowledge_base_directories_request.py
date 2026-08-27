# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBaseDirectoriesRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tenant_id: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The field by which the results are sorted. Valid values:
        # 
        # - event_time: event creation time
        # - event_execute_start_time: event execution time
        # - event_execute_finish_time: event completion time
        self.sort_field = sort_field
        # The sort order. This parameter takes effect only when sortBy is specified. Valid values: ASC, DESC (case-insensitive).
        self.sort_order = sort_order
        # The tenant ID. This is a common parameter. You can pass it explicitly by using --tenant-id in winnexo-cli.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


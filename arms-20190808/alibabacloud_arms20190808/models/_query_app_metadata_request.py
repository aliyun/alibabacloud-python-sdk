# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAppMetadataRequest(DaraModel):
    def __init__(
        self,
        end_time_ms: int = None,
        meta_ids: str = None,
        meta_type: str = None,
        pid: str = None,
        region_id: str = None,
        start_time_ms: int = None,
    ):
        self.end_time_ms = end_time_ms
        # The metadata IDs. Use a comma (,) to separate multiple IDs.
        # 
        # You can obtain the exception ID on the **exception analysis** page of the target application in the ARMS console.
        # 
        # This parameter is required.
        self.meta_ids = meta_ids
        # The type of the metadata. Valid values:
        # 
        # - sql: Retrieves the SQL statement by sqlId.
        # 
        # - exception: Retrieves the exception stack by exceptionId.
        # 
        # This parameter is required.
        self.meta_type = meta_type
        # The application ID. To obtain the ID, call the **ListTraceApps** operation.
        # 
        # This parameter is required.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.start_time_ms = start_time_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_ms is not None:
            result['EndTimeMs'] = self.end_time_ms

        if self.meta_ids is not None:
            result['MetaIds'] = self.meta_ids

        if self.meta_type is not None:
            result['MetaType'] = self.meta_type

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time_ms is not None:
            result['StartTimeMs'] = self.start_time_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeMs') is not None:
            self.end_time_ms = m.get('EndTimeMs')

        if m.get('MetaIds') is not None:
            self.meta_ids = m.get('MetaIds')

        if m.get('MetaType') is not None:
            self.meta_type = m.get('MetaType')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTimeMs') is not None:
            self.start_time_ms = m.get('StartTimeMs')

        return self


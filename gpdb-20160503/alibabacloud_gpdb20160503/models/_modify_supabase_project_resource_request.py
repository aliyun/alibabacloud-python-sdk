# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySupabaseProjectResourceRequest(DaraModel):
    def __init__(
        self,
        modify_type: str = None,
        project_id: str = None,
        project_spec: str = None,
        region_id: str = None,
        storage_size: int = None,
    ):
        # The modification type.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        # The Supabase project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The new project specifications.
        self.project_spec = project_spec
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id
        # The storage size, in GB.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_spec is not None:
            result['ProjectSpec'] = self.project_spec

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectSpec') is not None:
            self.project_spec = m.get('ProjectSpec')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self


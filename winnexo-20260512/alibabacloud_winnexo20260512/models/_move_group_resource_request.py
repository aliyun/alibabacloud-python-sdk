# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveGroupResourceRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
        tenant_id: str = None,
    ):
        # The collaboration space ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The real ID of the physical directory in the space where the resource currently resides. The root sentinel is not supported.
        # 
        # This parameter is required.
        self.source_directory_id = source_directory_id
        # The physical GROUP resource ID to be moved. Referenced resources are read-only.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The real ID of the target physical directory in the same space. This value must be different from the source directory ID.
        # 
        # This parameter is required.
        self.target_directory_id = target_directory_id
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.source_directory_id is not None:
            result['sourceDirectoryId'] = self.source_directory_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self


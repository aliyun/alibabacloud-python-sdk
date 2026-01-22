# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBNodePerformanceRequest(DaraModel):
    def __init__(
        self,
        character_type: str = None,
        dbinstance_name: str = None,
        dbnode_ids: str = None,
        dbnode_role: str = None,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.character_type = character_type
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.dbnode_ids = dbnode_ids
        self.dbnode_role = dbnode_role
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids

        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')

        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSubscriptionMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sid: str = None,
        sub_migration_job_ids_shrink: str = None,
        topics_shrink: str = None,
    ):
        # The ID of the distributed change tracking instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the region in which the change tracking instance resides.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the consumer group.
        # 
        # This parameter is required.
        self.sid = sid
        # The IDs of all subtasks in the distributed change tracking task. Separate multiple subtask IDs with commas (,).
        # 
        # >  You must specify at least one of the SubMigrationJobIds and **Topics** parameters. We recommend that you specify the SubMigrationJobIds parameter.
        self.sub_migration_job_ids_shrink = sub_migration_job_ids_shrink
        # The topics of all subtasks in the distributed change tracking task. Separate multiple topics with commas (,).
        # 
        # >  You must specify at least one of the **SubMigrationJobIds** and Topics parameters. We recommend that you specify the **SubMigrationJobIds** parameter.
        self.topics_shrink = topics_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.sub_migration_job_ids_shrink is not None:
            result['SubMigrationJobIds'] = self.sub_migration_job_ids_shrink

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('SubMigrationJobIds') is not None:
            self.sub_migration_job_ids_shrink = m.get('SubMigrationJobIds')

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        return self


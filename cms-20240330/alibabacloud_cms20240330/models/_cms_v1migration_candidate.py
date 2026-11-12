# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CmsV1MigrationCandidate(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        migration_status: str = None,
        observe_group_id: str = None,
        origin_group_id: str = None,
        rejection_reason: str = None,
        selectable: bool = None,
        source_read_only: bool = None,
        source_type: str = None,
        target_group_name: str = None,
    ):
        # The name of the source application group.
        self.group_name = group_name
        # The current migration or takeover status of the source group. Valid values: NOT_MIGRATED: Not migrated. PROCESSING: In progress. MIGRATED: Migrated. If a historical task lacks proof of source read-only status, NEEDS_REVIEW is returned through rejectionReason.
        self.migration_status = migration_status
        # The ID of the target observation group.
        self.observe_group_id = observe_group_id
        # The ID of the source CloudMonitor 1.0 application group.
        self.origin_group_id = origin_group_id
        # The reason why the group cannot be selected.
        self.rejection_reason = rejection_reason
        # Specifies whether the group can be selected for migration.
        self.selectable = selectable
        # Specifies whether the source 1.0 group is persistently read-only.
        self.source_read_only = source_read_only
        # The type of the source application group. Valid values: custom: Custom group. tag: Tag-based group. regMgr: Resource group-based group.
        self.source_type = source_type
        # The name of the target observation group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.observe_group_id is not None:
            result['observeGroupId'] = self.observe_group_id

        if self.origin_group_id is not None:
            result['originGroupId'] = self.origin_group_id

        if self.rejection_reason is not None:
            result['rejectionReason'] = self.rejection_reason

        if self.selectable is not None:
            result['selectable'] = self.selectable

        if self.source_read_only is not None:
            result['sourceReadOnly'] = self.source_read_only

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.target_group_name is not None:
            result['targetGroupName'] = self.target_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('observeGroupId') is not None:
            self.observe_group_id = m.get('observeGroupId')

        if m.get('originGroupId') is not None:
            self.origin_group_id = m.get('originGroupId')

        if m.get('rejectionReason') is not None:
            self.rejection_reason = m.get('rejectionReason')

        if m.get('selectable') is not None:
            self.selectable = m.get('selectable')

        if m.get('sourceReadOnly') is not None:
            self.source_read_only = m.get('sourceReadOnly')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('targetGroupName') is not None:
            self.target_group_name = m.get('targetGroupName')

        return self


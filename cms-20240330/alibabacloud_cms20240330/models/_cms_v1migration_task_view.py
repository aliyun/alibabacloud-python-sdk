# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CmsV1MigrationTaskView(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        can_recover: bool = None,
        error_message: str = None,
        group_name: str = None,
        observe_group_id: str = None,
        origin_group_id: str = None,
        source_read_only: bool = None,
        status: str = None,
        takeover_stage: str = None,
        target_group_name: str = None,
        task_id: int = None,
    ):
        # The migration batch ID.
        self.batch_id = batch_id
        # Indicates whether to provide a recovery prompt for existing frozen tasks. This field does not grant authorization. Each recovery re-verifies the original bindings. Tasks with the SUCCESS status are not retried.
        self.can_recover = can_recover
        # The task failure description.
        self.error_message = error_message
        # The source application group name.
        self.group_name = group_name
        # The target observation group ID.
        self.observe_group_id = observe_group_id
        # The source CloudMonitor 1.0 application group ID.
        self.origin_group_id = origin_group_id
        # Indicates whether the source 1.0 group is persistently set to read-only.
        self.source_read_only = source_read_only
        # The migration task status. Valid values: PENDING, RUNNING, SUCCESS, SKIPPED, and FAILED.
        self.status = status
        # The takeover stage. Valid values: PENDING, SOURCE_LOCKED, TARGET_CREATED, READ_ONLY, and NEEDS_REVIEW.
        self.takeover_stage = takeover_stage
        # The target observation group name.
        self.target_group_name = target_group_name
        # The migration task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.can_recover is not None:
            result['canRecover'] = self.can_recover

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.observe_group_id is not None:
            result['observeGroupId'] = self.observe_group_id

        if self.origin_group_id is not None:
            result['originGroupId'] = self.origin_group_id

        if self.source_read_only is not None:
            result['sourceReadOnly'] = self.source_read_only

        if self.status is not None:
            result['status'] = self.status

        if self.takeover_stage is not None:
            result['takeoverStage'] = self.takeover_stage

        if self.target_group_name is not None:
            result['targetGroupName'] = self.target_group_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('canRecover') is not None:
            self.can_recover = m.get('canRecover')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('observeGroupId') is not None:
            self.observe_group_id = m.get('observeGroupId')

        if m.get('originGroupId') is not None:
            self.origin_group_id = m.get('originGroupId')

        if m.get('sourceReadOnly') is not None:
            self.source_read_only = m.get('sourceReadOnly')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('takeoverStage') is not None:
            self.takeover_stage = m.get('takeoverStage')

        if m.get('targetGroupName') is not None:
            self.target_group_name = m.get('targetGroupName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self


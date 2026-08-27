# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class QuerySyncResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_at: str = None,
        corp_id: str = None,
        dept_stats: main_models.QuerySyncResultResponseBodyDeptStats = None,
        duration_seconds: int = None,
        error_message: str = None,
        member_stats: main_models.QuerySyncResultResponseBodyMemberStats = None,
        message: str = None,
        platform_type: str = None,
        request_id: str = None,
        started_at: str = None,
        status: str = None,
        submitted_at: str = None,
        summary: str = None,
        task_id: int = None,
    ):
        # The response status code.
        self.code = code
        # The time when the task was completed (ISO 8601 format).
        self.completed_at = completed_at
        # The enterprise identifier.
        self.corp_id = corp_id
        # The department synchronization statistics. This field has a value when the task is completed.
        self.dept_stats = dept_stats
        # The execution duration, in seconds.
        self.duration_seconds = duration_seconds
        # The error message.
        self.error_message = error_message
        # The member synchronization statistics. This field has a value when syncMembers is set to true and the task is completed.
        self.member_stats = member_stats
        # The description of the status code.
        self.message = message
        # The platform type.
        self.platform_type = platform_type
        # The request trace ID.
        self.request_id = request_id
        # The time when the task started (ISO 8601 format).
        self.started_at = started_at
        # The task status. Valid values: PENDING, RUNNING, COMPLETED, FAILED, TIMEOUT, and CANCELED.
        self.status = status
        # The time when the task was submitted (ISO 8601 format).
        self.submitted_at = submitted_at
        # The intelligent meeting summary content.
        self.summary = summary
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.dept_stats:
            self.dept_stats.validate()
        if self.member_stats:
            self.member_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.dept_stats is not None:
            result['deptStats'] = self.dept_stats.to_map()

        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.member_stats is not None:
            result['memberStats'] = self.member_stats.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.platform_type is not None:
            result['platformType'] = self.platform_type

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.submitted_at is not None:
            result['submittedAt'] = self.submitted_at

        if self.summary is not None:
            result['summary'] = self.summary

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('deptStats') is not None:
            temp_model = main_models.QuerySyncResultResponseBodyDeptStats()
            self.dept_stats = temp_model.from_map(m.get('deptStats'))

        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('memberStats') is not None:
            temp_model = main_models.QuerySyncResultResponseBodyMemberStats()
            self.member_stats = temp_model.from_map(m.get('memberStats'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submittedAt') is not None:
            self.submitted_at = m.get('submittedAt')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class QuerySyncResultResponseBodyMemberStats(DaraModel):
    def __init__(
        self,
        failed: int = None,
        relationship_added: int = None,
        relationship_removed: int = None,
        total_external: int = None,
        unchanged: int = None,
    ):
        # The number of failed members.
        self.failed = failed
        # The number of added member relationships.
        self.relationship_added = relationship_added
        # The number of removed member relationships.
        self.relationship_removed = relationship_removed
        # The total number of external members.
        self.total_external = total_external
        # The number of unchanged member relationships.
        self.unchanged = unchanged

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['failed'] = self.failed

        if self.relationship_added is not None:
            result['relationshipAdded'] = self.relationship_added

        if self.relationship_removed is not None:
            result['relationshipRemoved'] = self.relationship_removed

        if self.total_external is not None:
            result['totalExternal'] = self.total_external

        if self.unchanged is not None:
            result['unchanged'] = self.unchanged

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('relationshipAdded') is not None:
            self.relationship_added = m.get('relationshipAdded')

        if m.get('relationshipRemoved') is not None:
            self.relationship_removed = m.get('relationshipRemoved')

        if m.get('totalExternal') is not None:
            self.total_external = m.get('totalExternal')

        if m.get('unchanged') is not None:
            self.unchanged = m.get('unchanged')

        return self

class QuerySyncResultResponseBodyDeptStats(DaraModel):
    def __init__(
        self,
        created: int = None,
        deleted: int = None,
        moved: int = None,
        renamed: int = None,
        skipped: int = None,
        total_external: int = None,
    ):
        # The total number of external departments.
        self.created = created
        # The number of user groups marked for deletion.
        self.deleted = deleted
        # The number of moved user groups.
        self.moved = moved
        # The number of renamed user groups.
        self.renamed = renamed
        # The number of skipped user groups.
        self.skipped = skipped
        # The total number of external departments.
        self.total_external = total_external

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.moved is not None:
            result['moved'] = self.moved

        if self.renamed is not None:
            result['renamed'] = self.renamed

        if self.skipped is not None:
            result['skipped'] = self.skipped

        if self.total_external is not None:
            result['totalExternal'] = self.total_external

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('moved') is not None:
            self.moved = m.get('moved')

        if m.get('renamed') is not None:
            self.renamed = m.get('renamed')

        if m.get('skipped') is not None:
            self.skipped = m.get('skipped')

        if m.get('totalExternal') is not None:
            self.total_external = m.get('totalExternal')

        return self


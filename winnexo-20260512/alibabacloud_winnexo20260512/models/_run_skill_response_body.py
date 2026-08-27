# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSkillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_at: str = None,
        message: str = None,
        request_id: str = None,
        run_id: str = None,
        skill_code: str = None,
        skill_name: str = None,
        status: str = None,
    ):
        # The response status code.
        self.code = code
        # The task creation time in ISO 8601 UTC format.
        self.created_at = created_at
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The asynchronous task ID, used for querying with getSkillRun.
        self.run_id = run_id
        # The skill code that was actually executed.
        self.skill_code = skill_code
        # The skill name.
        self.skill_name = skill_name
        # The task status. Returns Running immediately upon submission.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


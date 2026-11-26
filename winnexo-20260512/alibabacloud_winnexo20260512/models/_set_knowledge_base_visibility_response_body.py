# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetKnowledgeBaseVisibilityResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        target_id: str = None,
        target_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
        visibility_mode: str = None,
    ):
        # The status code.
        self.code = code
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The target ID, which varies based on the target type.
        # - If the type is period, specify the period ID.
        # - If the type is objective, specify the objective ID.
        # - If the type is kr, specify the keyResult ID.
        self.target_id = target_id
        # The type of the current permission. Valid values:
        # - period: period type
        # - objective: objective type
        # - kr: keyResult type
        self.target_type = target_type
        # The collection of user groups.
        self.user_group_ids = user_group_ids
        # The collection of users.
        self.user_ids = user_ids
        # The visibility scope mode.
        self.visibility_mode = visibility_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        if self.visibility_mode is not None:
            result['visibilityMode'] = self.visibility_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        if m.get('visibilityMode') is not None:
            self.visibility_mode = m.get('visibilityMode')

        return self


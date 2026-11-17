# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryKnowledgeBaseBuildTaskInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        knowledge_base_id: str = None,
        task_instance_id: str = None,
    ):
        # The idempotency key for the retry operation. Keep the original value when you resend the same request, and use a new token when you initiate another retry.
        self.client_token = client_token
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the instance to be retried.
        # 
        # This parameter is required.
        self.task_instance_id = task_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self


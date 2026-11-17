# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeBaseBuildTaskInstanceRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        task_instance_id: str = None,
    ):
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The execution ID.
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
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self


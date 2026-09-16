# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeRecallRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        path: str = None,
        question: str = None,
        tags: str = None,
        topk: int = None,
        user: str = None,
    ):
        # The ID of the ADB MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The file path prefix. Only files that match the specified path prefix are recalled.
        self.path = path
        # The question for knowledge base recall.
        # 
        # This parameter is required.
        self.question = question
        # The list of tags in JSON format.
        self.tags = tags
        # The top K associated files to recall.
        self.topk = topk
        # The username. Only files that the specified user has permission to access are recalled.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.path is not None:
            result['Path'] = self.path

        if self.question is not None:
            result['Question'] = self.question

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.topk is not None:
            result['Topk'] = self.topk

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Topk') is not None:
            self.topk = m.get('Topk')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self


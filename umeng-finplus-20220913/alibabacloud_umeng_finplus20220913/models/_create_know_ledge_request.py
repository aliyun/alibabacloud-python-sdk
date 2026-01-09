# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class CreateKnowLedgeRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateKnowLedgeRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateKnowLedgeRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class CreateKnowLedgeRequestBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        internal_knowledge_id: str = None,
        knowledge_name: str = None,
    ):
        self.app_id = app_id
        self.internal_knowledge_id = internal_knowledge_id
        self.knowledge_name = knowledge_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.internal_knowledge_id is not None:
            result['internalKnowledgeId'] = self.internal_knowledge_id

        if self.knowledge_name is not None:
            result['knowledgeName'] = self.knowledge_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('internalKnowledgeId') is not None:
            self.internal_knowledge_id = m.get('internalKnowledgeId')

        if m.get('knowledgeName') is not None:
            self.knowledge_name = m.get('knowledgeName')

        return self


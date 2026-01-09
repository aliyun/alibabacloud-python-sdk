# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeDataRequest(DaraModel):
    def __init__(
        self,
        body: main_models.GetKnowledgeDataRequestBody = None,
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
            temp_model = main_models.GetKnowledgeDataRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class GetKnowledgeDataRequestBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        knowledge_id_list: List[str] = None,
    ):
        self.app_id = app_id
        self.knowledge_id_list = knowledge_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.knowledge_id_list is not None:
            result['knowledgeIdList'] = self.knowledge_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('knowledgeIdList') is not None:
            self.knowledge_id_list = m.get('knowledgeIdList')

        return self


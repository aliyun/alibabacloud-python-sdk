# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetKnowledgeDataResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetKnowledgeDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKnowledgeDataResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        internal_knowledge_id: str = None,
        knowledge_name: str = None,
        message: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.internal_knowledge_id = internal_knowledge_id
        self.knowledge_name = knowledge_name
        self.message = message
        self.status = status

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

        if self.message is not None:
            result['message'] = self.message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('internalKnowledgeId') is not None:
            self.internal_knowledge_id = m.get('internalKnowledgeId')

        if m.get('knowledgeName') is not None:
            self.knowledge_name = m.get('knowledgeName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


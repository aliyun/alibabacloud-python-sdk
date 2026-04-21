# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class MedicalKnowResult(DaraModel):
    def __init__(
        self,
        messages: List[main_models.MedicalKnowledgeInfo] = None,
        query_context: main_models.MultimodalQueryContext = None,
        request_id: str = None,
        search_information: main_models.UnifiedSearchInformation = None,
    ):
        self.messages = messages
        self.query_context = query_context
        self.request_id = request_id
        self.search_information = search_information

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.query_context:
            self.query_context.validate()
        if self.search_information:
            self.search_information.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.MedicalKnowledgeInfo()
                self.messages.append(temp_model.from_map(k1))

        if m.get('queryContext') is not None:
            temp_model = main_models.MultimodalQueryContext()
            self.query_context = temp_model.from_map(m.get('queryContext'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('searchInformation') is not None:
            temp_model = main_models.UnifiedSearchInformation()
            self.search_information = temp_model.from_map(m.get('searchInformation'))

        return self


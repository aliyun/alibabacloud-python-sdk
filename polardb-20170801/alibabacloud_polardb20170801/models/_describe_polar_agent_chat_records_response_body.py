# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarAgentChatRecordsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribePolarAgentChatRecordsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribePolarAgentChatRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePolarAgentChatRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        answer: str = None,
        feedback_type: str = None,
        query: str = None,
        query_id: str = None,
        session_id: str = None,
    ):
        self.answer = answer
        self.feedback_type = feedback_type
        self.query = query
        # Query ID。
        self.query_id = query_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.feedback_type is not None:
            result['FeedbackType'] = self.feedback_type

        if self.query is not None:
            result['Query'] = self.query

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('FeedbackType') is not None:
            self.feedback_type = m.get('FeedbackType')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self


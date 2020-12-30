# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class QueryDatabotRequest(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        query: str = None,
        session_id: str = None,
    ):
        self.access_id = access_id
        self.query = query
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.query is not None:
            result['Query'] = self.query
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class QueryDatabotResponseBody(TeaModel):
    def __init__(
        self,
        cost_time: int = None,
        request_id: str = None,
        data: Dict[str, Any] = None,
    ):
        self.cost_time = cost_time
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryDatabotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDatabotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDatabotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



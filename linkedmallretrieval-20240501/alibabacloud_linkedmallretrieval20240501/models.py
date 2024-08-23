# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AISearchQuery(TeaModel):
    def __init__(
        self,
        card: str = None,
        query: str = None,
    ):
        self.card = card
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card is not None:
            result['card'] = self.card
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card') is not None:
            self.card = m.get('card')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class EventHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_id: str = None,
        request_id: str = None,
        response_time: int = None,
    ):
        self.event = event
        self.event_id = event_id
        self.request_id = request_id
        self.response_time = response_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class AISearchResult(TeaModel):
    def __init__(
        self,
        header: EventHeader = None,
        payload: str = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = EventHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AISearchRequest(TeaModel):
    def __init__(
        self,
        card: str = None,
        query: str = None,
    ):
        self.card = card
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card is not None:
            result['card'] = self.card
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card') is not None:
            self.card = m.get('card')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class AISearchResponseBodyHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_id: str = None,
        request_id: str = None,
        response_time: str = None,
    ):
        self.event = event
        self.event_id = event_id
        self.request_id = request_id
        self.response_time = response_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class AISearchResponseBody(TeaModel):
    def __init__(
        self,
        header: AISearchResponseBodyHeader = None,
        payload: str = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = AISearchResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AISearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AISearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AISearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AISearchV2Request(TeaModel):
    def __init__(
        self,
        query: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class AISearchV2ResponseBodyHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_id: str = None,
        response_time: int = None,
    ):
        self.event = event
        self.event_id = event_id
        self.response_time = response_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class AISearchV2ResponseBody(TeaModel):
    def __init__(
        self,
        header: AISearchV2ResponseBodyHeader = None,
        payload: str = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = AISearchV2ResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AISearchV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AISearchV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AISearchV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



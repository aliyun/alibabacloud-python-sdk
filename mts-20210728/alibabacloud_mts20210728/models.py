# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class QueryCopyrightRequest(TeaModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        job_id: str = None,
        level: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.job_id = job_id
        self.level = level
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        callback: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        input: str = None,
        job_id: str = None,
        level: int = None,
        message: str = None,
        message_id: int = None,
        output: str = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        self.callback = callback
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.input = input
        self.job_id = job_id
        self.level = level
        self.message = message
        self.message_id = message_id
        self.output = output
        self.result = result
        self.status = status
        self.user_data = user_data
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.output is not None:
            result['Output'] = self.output
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryCopyrightResponseBodyData] = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCopyrightResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCopyrightExtractRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryCopyrightExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class QueryCopyrightExtractResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryCopyrightExtractResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryCopyrightExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryCopyrightExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCopyrightExtractResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryCopyrightExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceAbRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
    ):
        self.job_id = job_id
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class QueryTraceAbResponseBodyData(TeaModel):
    def __init__(
        self,
        callback: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        input: str = None,
        job_id: str = None,
        level: int = None,
        media_id: str = None,
        output: str = None,
        result: str = None,
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        self.callback = callback
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.input = input
        self.job_id = job_id
        self.level = level
        self.media_id = media_id
        self.output = output
        self.result = result
        self.status = status
        self.user_data = user_data
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTraceAbResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryTraceAbResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTraceAbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceAbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTraceAbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryTraceAbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceExtractRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryTraceExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        trace: str = None,
    ):
        self.trace = trace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace is not None:
            result['Trace'] = self.trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        return self


class QueryTraceExtractResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryTraceExtractResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTraceExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTraceExtractResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryTraceExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceMuRequest(TeaModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        job_id: str = None,
        level: int = None,
        message_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.job_id = job_id
        self.level = level
        self.message_id = message_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTraceMuResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        job_id: str = None,
        media_id: str = None,
        output: str = None,
        status: str = None,
        trace: str = None,
        trace_id: int = None,
        user_data: str = None,
        user_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.job_id = job_id
        self.media_id = media_id
        self.output = output
        self.status = status
        self.trace = trace
        self.trace_id = trace_id
        self.user_data = user_data
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.trace is not None:
            result['Trace'] = self.trace
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTraceMuResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryTraceMuResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTraceMuResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceMuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTraceMuResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryTraceMuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCopyrightExtractRequest(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        input: str = None,
        params: str = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.input = input
        self.params = params
        self.url = url
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.input is not None:
            result['Input'] = self.input
        if self.params is not None:
            result['Params'] = self.params
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitCopyrightExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitCopyrightExtractResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitCopyrightExtractResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitCopyrightExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitCopyrightExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitCopyrightExtractResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitCopyrightExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCopyrightJobRequest(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        description: str = None,
        input: str = None,
        level: int = None,
        message: str = None,
        output: str = None,
        params: str = None,
        start_time: int = None,
        total_time: int = None,
        url: str = None,
        user_data: str = None,
        visible_message: str = None,
    ):
        self.call_back = call_back
        self.description = description
        self.input = input
        self.level = level
        self.message = message
        self.output = output
        self.params = params
        self.start_time = start_time
        self.total_time = total_time
        self.url = url
        self.user_data = user_data
        self.visible_message = visible_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.description is not None:
            result['Description'] = self.description
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.params is not None:
            result['Params'] = self.params
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.visible_message is not None:
            result['VisibleMessage'] = self.visible_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VisibleMessage') is not None:
            self.visible_message = m.get('VisibleMessage')
        return self


class SubmitCopyrightJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitCopyrightJobResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitCopyrightJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitCopyrightJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitCopyrightJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitCopyrightJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitCopyrightJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImageCopyrightRequest(TeaModel):
    def __init__(
        self,
        level: int = None,
        message: str = None,
        output: str = None,
        params: str = None,
    ):
        self.level = level
        self.message = message
        self.output = output
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class SubmitImageCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitImageCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitImageCopyrightResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitImageCopyrightResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitImageCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitImageCopyrightResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitImageCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTraceAbRequest(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        cipher_base_64ed: str = None,
        input: str = None,
        level: int = None,
        output: str = None,
        start_time: int = None,
        total_time: int = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.cipher_base_64ed = cipher_base_64ed
        self.input = input
        self.level = level
        self.output = output
        self.start_time = start_time
        self.total_time = total_time
        self.url = url
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.cipher_base_64ed is not None:
            result['CipherBase64ed'] = self.cipher_base_64ed
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('CipherBase64ed') is not None:
            self.cipher_base_64ed = m.get('CipherBase64ed')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitTraceAbResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
    ):
        self.job_id = job_id
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SubmitTraceAbResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitTraceAbResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTraceAbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTraceAbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTraceAbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitTraceAbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTraceExtractRequest(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        input: str = None,
        params: str = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.input = input
        self.params = params
        self.url = url
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.input is not None:
            result['Input'] = self.input
        if self.params is not None:
            result['Params'] = self.params
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitTraceExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitTraceExtractResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitTraceExtractResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTraceExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTraceExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTraceExtractResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitTraceExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTracemuRequest(TeaModel):
    def __init__(
        self,
        key_uri: str = None,
        media_id: str = None,
        output: str = None,
        params: str = None,
        trace: str = None,
    ):
        self.key_uri = key_uri
        self.media_id = media_id
        self.output = output
        self.params = params
        self.trace = trace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.params is not None:
            result['Params'] = self.params
        if self.trace is not None:
            result['Trace'] = self.trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyUri') is not None:
            self.key_uri = m.get('KeyUri')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        return self


class SubmitTracemuResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
    ):
        self.code = code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitTracemuResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitTracemuResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTracemuResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTracemuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTracemuResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitTracemuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



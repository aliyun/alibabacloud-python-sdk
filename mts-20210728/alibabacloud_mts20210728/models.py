# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        # 创建时间起始
        self.create_time_end = create_time_end
        # 创建时间截止
        self.create_time_start = create_time_start
        # 任务id
        self.job_id = job_id
        # 水印强度
        self.level = level
        # 水印信息id
        self.message_id = message_id
        # 页偏移
        self.page_number = page_number
        # 每页数量
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
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 任务id
        self.job_id = job_id
        # 媒体id
        self.media_id = media_id
        # 输出oss地址
        self.output = output
        # 任务状态
        self.status = status
        # 溯源水印信息
        self.trace = trace
        # 溯源水印信息id
        self.trace_id = trace_id
        # 用户自定义数据
        self.user_data = user_data
        # uid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['Gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['Gmt_modified'] = self.gmt_modified
        if self.job_id is not None:
            result['Job_id'] = self.job_id
        if self.media_id is not None:
            result['Media_id'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.trace is not None:
            result['Trace'] = self.trace
        if self.trace_id is not None:
            result['Trace_id'] = self.trace_id
        if self.user_data is not None:
            result['User_data'] = self.user_data
        if self.user_id is not None:
            result['User_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gmt_create') is not None:
            self.gmt_create = m.get('Gmt_create')
        if m.get('Gmt_modified') is not None:
            self.gmt_modified = m.get('Gmt_modified')
        if m.get('Job_id') is not None:
            self.job_id = m.get('Job_id')
        if m.get('Media_id') is not None:
            self.media_id = m.get('Media_id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        if m.get('Trace_id') is not None:
            self.trace_id = m.get('Trace_id')
        if m.get('User_data') is not None:
            self.user_data = m.get('User_data')
        if m.get('User_id') is not None:
            self.user_id = m.get('User_id')
        return self


class QueryTraceMuResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryTraceMuResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # 返回数据结构
        self.data = data
        # 返回信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceMuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTraceMuResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTraceMuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImageCopyrightRequest(TeaModel):
    def __init__(
        self,
        input: str = None,
        level: int = None,
        message: str = None,
        output: str = None,
    ):
        # 需要加水印的图片oss地址
        self.input = input
        # 水印强度
        self.level = level
        # 水印信息
        self.message = message
        # 水印图片输出oss地址
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class SubmitImageCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 任务id
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
        # 返回数据
        self.data = data
        # 返回信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitImageCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitImageCopyrightResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitImageCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryImageCopyrightRequest(TeaModel):
    def __init__(
        self,
        create_time_end: int = None,
        create_time_start: int = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 创建时间起始
        self.create_time_end = create_time_end
        # 创建时间截止
        self.create_time_start = create_time_start
        # 任务ID
        self.job_id = job_id
        # 页偏移
        self.page_number = page_number
        # 每页数量
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryImageCopyrightResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        input: str = None,
        job_id: str = None,
        level: int = None,
        message: str = None,
        message_id: int = None,
        output: str = None,
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 水印图片输入oss地址
        self.input = input
        # 任务id
        self.job_id = job_id
        # 水印强度
        self.level = level
        # 水印信息
        self.message = message
        # 水印信息id
        self.message_id = message_id
        # 加完水印后的输出oss地址
        self.output = output
        # 任务状态
        self.status = status
        # 用户自定义数据
        self.user_data = user_data
        # uid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['Gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['Gmt_modified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['Job_id'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['Message_id'] = self.message_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['User_data'] = self.user_data
        if self.user_id is not None:
            result['User_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gmt_create') is not None:
            self.gmt_create = m.get('Gmt_create')
        if m.get('Gmt_modified') is not None:
            self.gmt_modified = m.get('Gmt_modified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Job_id') is not None:
            self.job_id = m.get('Job_id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Message_id') is not None:
            self.message_id = m.get('Message_id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User_data') is not None:
            self.user_data = m.get('User_data')
        if m.get('User_id') is not None:
            self.user_id = m.get('User_id')
        return self


class QueryImageCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryImageCopyrightResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # 返回数据
        self.data = data
        # 返回信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryImageCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryImageCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryImageCopyrightResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryImageCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        # 创建时间截止
        self.create_time_end = create_time_end
        # 创建时间起始
        self.create_time_start = create_time_start
        # 任务id
        self.job_id = job_id
        # 水印强度
        self.level = level
        # 翻页下标
        self.page_number = page_number
        # 每页数量
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
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # 回调url
        self.callback = callback
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 水印视频输入
        self.input = input
        # 任务id
        self.job_id = job_id
        # 水印强度
        self.level = level
        # 水印信息
        self.message = message
        # 水印信息id
        self.message_id = message_id
        # 水印视频输出
        self.output = output
        # 状态
        self.status = status
        # 用户数据
        self.user_data = user_data
        # 用户ID
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
            result['Gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['Gmt_modified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['Job_id'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['Message_id'] = self.message_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['User_data'] = self.user_data
        if self.user_id is not None:
            result['User_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Gmt_create') is not None:
            self.gmt_create = m.get('Gmt_create')
        if m.get('Gmt_modified') is not None:
            self.gmt_modified = m.get('Gmt_modified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Job_id') is not None:
            self.job_id = m.get('Job_id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Message_id') is not None:
            self.message_id = m.get('Message_id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User_data') is not None:
            self.user_data = m.get('User_data')
        if m.get('User_id') is not None:
            self.user_id = m.get('User_id')
        return self


class QueryCopyrightResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[QueryCopyrightResponseBodyData] = None,
        status_code: int = None,
    ):
        self.request_id = request_id
        self.data = data
        # 状态码
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryCopyrightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCopyrightResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTracemuRequest(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        output: str = None,
        trace: str = None,
    ):
        # ab流处理后的媒体id
        self.media_id = media_id
        # m3u8文件输出oss地址
        self.output = output
        # 溯源水印信息
        self.trace = trace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.trace is not None:
            result['Trace'] = self.trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        return self


class SubmitTracemuResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 任务id
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


class SubmitTracemuResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitTracemuResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # 返回数据
        self.data = data
        # 返回信息
        self.message = message
        # 请求Id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTracemuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitTracemuResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitTracemuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceAbRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
    ):
        # 任务id
        self.job_id = job_id
        # 媒体id
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
        status: str = None,
        user_data: str = None,
        user_id: int = None,
    ):
        # 任务结果回调
        self.callback = callback
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 输入oss地址
        self.input = input
        # 任务id
        self.job_id = job_id
        # 水印强度
        self.level = level
        # 媒体id
        self.media_id = media_id
        # 输出地址
        self.output = output
        # 任务状态
        self.status = status
        # 用户数据
        self.user_data = user_data
        # uid
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
            result['Gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['Gmt_modified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['Job_id'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.media_id is not None:
            result['Media_id'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['User_data'] = self.user_data
        if self.user_id is not None:
            result['User_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Gmt_create') is not None:
            self.gmt_create = m.get('Gmt_create')
        if m.get('Gmt_modified') is not None:
            self.gmt_modified = m.get('Gmt_modified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Job_id') is not None:
            self.job_id = m.get('Job_id')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Media_id') is not None:
            self.media_id = m.get('Media_id')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('User_data') is not None:
            self.user_data = m.get('User_data')
        if m.get('User_id') is not None:
            self.user_id = m.get('User_id')
        return self


class QueryTraceAbResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryTraceAbResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # 返回结构
        self.data = data
        # 返回信息
        self.message = message
        # 请求id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceAbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTraceAbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTraceAbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTraceAbRequest(TeaModel):
    def __init__(
        self,
        call_back: str = None,
        input: str = None,
        level: int = None,
        output: str = None,
        user_data: str = None,
    ):
        # 任务结果回调
        self.call_back = call_back
        # 溯源水印ab流处理视频输入
        self.input = input
        # 水印强度
        self.level = level
        # 溯源水印ab流处理输出
        self.output = output
        # 用户自定义数据，最大长度1024个字节
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
        if self.level is not None:
            result['Level'] = self.level
        if self.output is not None:
            result['Output'] = self.output
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitTraceAbResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
    ):
        # 任务ID
        self.job_id = job_id
        # 媒体id
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
        # 返回数据
        self.data = data
        # 返回信息
        self.message = message
        # 请求Id
        self.request_id = request_id
        # 状态码
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
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTraceAbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitTraceAbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitTraceAbResponseBody()
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
        user_data: str = None,
    ):
        # 任务结果回调url
        self.call_back = call_back
        # 水印信息描述
        self.description = description
        # 输入的视频，oss三元组
        self.input = input
        # 水印强度，取值1，2，3
        self.level = level
        # 水印信息
        self.message = message
        # 输出的视频，oss三元组
        self.output = output
        # 用户自定义数据
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
        if self.user_data is not None:
            result['UserData'] = self.user_data
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
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitCopyrightJobResponseBodyData(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 任务id
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
        request_id: str = None,
        message: str = None,
        data: SubmitCopyrightJobResponseBodyData = None,
        status_code: int = None,
    ):
        # 请求Id
        self.request_id = request_id
        # 返回信息
        self.message = message
        # 返回数据
        self.data = data
        # 状态码
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = SubmitCopyrightJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitCopyrightJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitCopyrightJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitCopyrightJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



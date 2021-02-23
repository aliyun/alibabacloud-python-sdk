# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddAudioAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        watermark_id: str = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.watermark_id = watermark_id
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddAudioAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddAudioAsyncResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        request_id: str = None,
        data: List[AddAudioAsyncResponseBodyData] = None,
    ):
        self.msg = msg
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddAudioAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddAudioAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAudioAsyncResponseBody = None,
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
            temp_model = AddAudioAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        watermark_id: str = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.watermark_id = watermark_id
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddImageAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddImageAsyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[AddImageAsyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddImageAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddImageAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageAsyncResponseBody = None,
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
            temp_model = AddImageAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageSyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        watermark_id: str = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.watermark_id = watermark_id
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddImageSyncResponseBodyData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        data_id: str = None,
    ):
        self.result_url = result_url
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['dataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        return self


class AddImageSyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[AddImageSyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddImageSyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddImageSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddImageSyncResponseBody = None,
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
            temp_model = AddImageSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVideoAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        watermark_id: str = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.watermark_id = watermark_id
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class AddVideoAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class AddVideoAsyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[AddVideoAsyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddVideoAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class AddVideoAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVideoAsyncResponseBody = None,
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
            temp_model = AddVideoAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioAddRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAudioAddResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_url: str = None,
        result_url: str = None,
        data_id: str = None,
        gmt_modified: int = None,
        media_type: str = None,
        msg: str = None,
        task_uid: str = None,
        app_id: int = None,
        gmt_create: int = None,
        opt_type: str = None,
        finished_time: int = None,
        id: int = None,
    ):
        self.status = status
        self.source_url = source_url
        self.result_url = result_url
        self.data_id = data_id
        self.gmt_modified = gmt_modified
        self.media_type = media_type
        self.msg = msg
        self.task_uid = task_uid
        self.app_id = app_id
        self.gmt_create = gmt_create
        self.opt_type = opt_type
        self.finished_time = finished_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAudioAddResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAudioAddResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAudioAddResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAudioAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAudioAddResponseBody = None,
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
            temp_model = GetAudioAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: str = None,
        url_list: str = None,
        water_mark_type: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.url_list = url_list
        self.water_mark_type = water_mark_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        if self.water_mark_type is not None:
            result['WaterMarkType'] = self.water_mark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        if m.get('WaterMarkType') is not None:
            self.water_mark_type = m.get('WaterMarkType')
        return self


class GetAudioAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetAudioAsyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetAudioAsyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAudioAsyncResponseBody = None,
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
            temp_model = GetAudioAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioExtractRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAudioExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_url: str = None,
        result_url: str = None,
        data_id: str = None,
        gmt_modified: int = None,
        media_type: str = None,
        msg: str = None,
        task_uid: str = None,
        app_id: int = None,
        gmt_create: int = None,
        opt_type: str = None,
        finished_time: int = None,
        id: int = None,
    ):
        self.status = status
        self.source_url = source_url
        self.result_url = result_url
        self.data_id = data_id
        self.gmt_modified = gmt_modified
        self.media_type = media_type
        self.msg = msg
        self.task_uid = task_uid
        self.app_id = app_id
        self.gmt_create = gmt_create
        self.opt_type = opt_type
        self.finished_time = finished_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAudioExtractResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAudioExtractResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAudioExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAudioExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAudioExtractResponseBody = None,
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
            temp_model = GetAudioExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAudioTraceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: str = None,
        file_uid: str = None,
        user_info_list: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.file_uid = file_uid
        self.user_info_list = user_info_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.file_uid is not None:
            result['FileUid'] = self.file_uid
        if self.user_info_list is not None:
            result['userInfoList'] = self.user_info_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('FileUid') is not None:
            self.file_uid = m.get('FileUid')
        if m.get('userInfoList') is not None:
            self.user_info_list = m.get('userInfoList')
        return self


class GetAudioTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        user_info: str = None,
    ):
        self.result_url = result_url
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        return self


class GetAudioTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetAudioTraceResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAudioTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetAudioTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAudioTraceResponseBody = None,
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
            temp_model = GetAudioTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: int = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class GetImageAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetImageAsyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetImageAsyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetImageAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetImageAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageAsyncResponseBody = None,
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
            temp_model = GetImageAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageSyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: str = None,
        url_list: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        return self


class GetImageSyncResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        watermark_id: str = None,
        meta_file_url: str = None,
    ):
        self.data_id = data_id
        self.watermark_id = watermark_id
        self.meta_file_url = meta_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_id is not None:
            result['dataId'] = self.data_id
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.meta_file_url is not None:
            result['MetaFileUrl'] = self.meta_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('MetaFileUrl') is not None:
            self.meta_file_url = m.get('MetaFileUrl')
        return self


class GetImageSyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetImageSyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetImageSyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetImageSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageSyncResponseBody = None,
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
            temp_model = GetImageSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAddRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoAddResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_url: str = None,
        result_url: str = None,
        data_id: str = None,
        gmt_modified: int = None,
        media_type: str = None,
        msg: str = None,
        task_uid: str = None,
        app_id: int = None,
        gmt_create: int = None,
        opt_type: str = None,
        finished_time: int = None,
        id: int = None,
    ):
        self.status = status
        self.source_url = source_url
        self.result_url = result_url
        self.data_id = data_id
        self.gmt_modified = gmt_modified
        self.media_type = media_type
        self.msg = msg
        self.task_uid = task_uid
        self.app_id = app_id
        self.gmt_create = gmt_create
        self.opt_type = opt_type
        self.finished_time = finished_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetVideoAddResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetVideoAddResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetVideoAddResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetVideoAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoAddResponseBody = None,
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
            temp_model = GetVideoAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAsyncRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: str = None,
        url_list: str = None,
        water_mark_type: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.url_list = url_list
        self.water_mark_type = water_mark_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.url_list is not None:
            result['urlList'] = self.url_list
        if self.water_mark_type is not None:
            result['WaterMarkType'] = self.water_mark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('urlList') is not None:
            self.url_list = m.get('urlList')
        if m.get('WaterMarkType') is not None:
            self.water_mark_type = m.get('WaterMarkType')
        return self


class GetVideoAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        task_uid: str = None,
        data_id: str = None,
    ):
        self.task_uid = task_uid
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class GetVideoAsyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetVideoAsyncResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoAsyncResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoAsyncResponseBody = None,
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
            temp_model = GetVideoAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoExtractRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoExtractResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_url: str = None,
        result_url: str = None,
        data_id: str = None,
        gmt_modified: int = None,
        media_type: str = None,
        msg: str = None,
        task_uid: str = None,
        app_id: int = None,
        gmt_create: int = None,
        opt_type: str = None,
        finished_time: int = None,
        id: int = None,
    ):
        self.status = status
        self.source_url = source_url
        self.result_url = result_url
        self.data_id = data_id
        self.gmt_modified = gmt_modified
        self.media_type = media_type
        self.msg = msg
        self.task_uid = task_uid
        self.app_id = app_id
        self.gmt_create = gmt_create
        self.opt_type = opt_type
        self.finished_time = finished_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.opt_type is not None:
            result['OptType'] = self.opt_type
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetVideoExtractResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetVideoExtractResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetVideoExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetVideoExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoExtractResponseBody = None,
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
            temp_model = GetVideoExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTraceRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        app_name: str = None,
        file_uid: str = None,
        user_info_list: str = None,
    ):
        self.source_ip = source_ip
        self.app_name = app_name
        self.file_uid = file_uid
        self.user_info_list = user_info_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.file_uid is not None:
            result['FileUid'] = self.file_uid
        if self.user_info_list is not None:
            result['userInfoList'] = self.user_info_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('FileUid') is not None:
            self.file_uid = m.get('FileUid')
        if m.get('userInfoList') is not None:
            self.user_info_list = m.get('userInfoList')
        return self


class GetVideoTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        result_url: str = None,
        user_info: str = None,
    ):
        self.result_url = result_url
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result_url is not None:
            result['ResultUrl'] = self.result_url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        return self


class GetVideoTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetVideoTraceResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVideoTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetVideoTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoTraceResponseBody = None,
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
            temp_model = GetVideoTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



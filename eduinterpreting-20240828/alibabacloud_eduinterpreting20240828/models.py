# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class RecognizeAudioRequest(TeaModel):
    def __init__(
        self,
        audio_file_url: str = None,
        callback_url: str = None,
        enable_call_back: bool = None,
        outer_biz_id: str = None,
    ):
        # This parameter is required.
        self.audio_file_url = audio_file_url
        self.callback_url = callback_url
        # This parameter is required.
        self.enable_call_back = enable_call_back
        # This parameter is required.
        self.outer_biz_id = outer_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_file_url is not None:
            result['AudioFileUrl'] = self.audio_file_url
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.enable_call_back is not None:
            result['EnableCallBack'] = self.enable_call_back
        if self.outer_biz_id is not None:
            result['OuterBizId'] = self.outer_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFileUrl') is not None:
            self.audio_file_url = m.get('AudioFileUrl')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('EnableCallBack') is not None:
            self.enable_call_back = m.get('EnableCallBack')
        if m.get('OuterBizId') is not None:
            self.outer_biz_id = m.get('OuterBizId')
        return self


class RecognizeAudioResponseBodyItemList(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        text: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RecognizeAudioResponseBody(TeaModel):
    def __init__(
        self,
        item_list: List[RecognizeAudioResponseBodyItemList] = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.item_list = item_list
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = RecognizeAudioResponseBodyItemList()
                self.item_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecognizeAudioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecognizeAudioResponseBody = None,
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
            temp_model = RecognizeAudioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitEvaluationTaskRequest(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        callback_url: str = None,
        material_text: str = None,
        outer_biz_id: str = None,
        suggested_answer: str = None,
        text: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.audio_url = audio_url
        # This parameter is required.
        self.callback_url = callback_url
        # This parameter is required.
        self.material_text = material_text
        # This parameter is required.
        self.outer_biz_id = outer_biz_id
        # This parameter is required.
        self.suggested_answer = suggested_answer
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.material_text is not None:
            result['MaterialText'] = self.material_text
        if self.outer_biz_id is not None:
            result['OuterBizId'] = self.outer_biz_id
        if self.suggested_answer is not None:
            result['SuggestedAnswer'] = self.suggested_answer
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('MaterialText') is not None:
            self.material_text = m.get('MaterialText')
        if m.get('OuterBizId') is not None:
            self.outer_biz_id = m.get('OuterBizId')
        if m.get('SuggestedAnswer') is not None:
            self.suggested_answer = m.get('SuggestedAnswer')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SubmitEvaluationTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitEvaluationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitEvaluationTaskResponseBody = None,
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
            temp_model = SubmitEvaluationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



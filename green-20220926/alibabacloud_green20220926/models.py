# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddAnswerSampleRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
        sample_object: str = None,
        samples: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id
        self.sample_object = sample_object
        self.samples = samples

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sample_object is not None:
            result['SampleObject'] = self.sample_object
        if self.samples is not None:
            result['Samples'] = self.samples
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SampleObject') is not None:
            self.sample_object = m.get('SampleObject')
        if m.get('Samples') is not None:
            self.samples = m.get('Samples')
        return self


class AddAnswerSampleResponseBodyResult(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_samples: List[str] = None,
        invalid_count: int = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_samples: List[str] = None,
        success_count: int = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_samples = illegal_length_samples
        self.invalid_count = invalid_count
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_samples = repeat_samples
        self.success_count = success_count
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_samples is not None:
            result['IllegalLengthSamples'] = self.illegal_length_samples
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_samples is not None:
            result['RepeatSamples'] = self.repeat_samples
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthSamples') is not None:
            self.illegal_length_samples = m.get('IllegalLengthSamples')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatSamples') is not None:
            self.repeat_samples = m.get('RepeatSamples')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AddAnswerSampleResponseBody(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        request_id: str = None,
        result: AddAnswerSampleResponseBodyResult = None,
        task_id: str = None,
    ):
        self.lib_id = lib_id
        self.request_id = request_id
        self.result = result
        self.task_id = task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddAnswerSampleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddAnswerSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddAnswerSampleResponseBody = None,
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
            temp_model = AddAnswerSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImageLibRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.lib_name = lib_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddImageLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageLibResponseBody = None,
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
            temp_model = AddImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddImages2LibRequest(TeaModel):
    def __init__(
        self,
        img_url: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.img_url = img_url
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddImages2LibResponseBodyData(TeaModel):
    def __init__(
        self,
        img_id: str = None,
    ):
        self.img_id = img_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_id is not None:
            result['ImgId'] = self.img_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgId') is not None:
            self.img_id = m.get('ImgId')
        return self


class AddImages2LibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AddImages2LibResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = AddImages2LibResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImages2LibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImages2LibResponseBody = None,
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
            temp_model = AddImages2LibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddKeywordLibRequest(TeaModel):
    def __init__(
        self,
        keywords: str = None,
        keywords_object: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        self.keywords = keywords
        self.keywords_object = keywords_object
        self.lib_name = lib_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddKeywordLibResponseBodyDataKeywordsResult(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_keywords: List[str] = None,
        invalid_count: int = None,
        invalid_keywords: List[str] = None,
        lib_id: str = None,
        repeat_count: int = None,
        repeat_keywords: List[str] = None,
        success_count: int = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_keywords = illegal_length_keywords
        self.invalid_count = invalid_count
        self.invalid_keywords = invalid_keywords
        self.lib_id = lib_id
        self.repeat_count = repeat_count
        self.repeat_keywords = repeat_keywords
        self.success_count = success_count
        self.tips = tips
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_keywords is not None:
            result['IllegalLengthKeywords'] = self.illegal_length_keywords
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.invalid_keywords is not None:
            result['InvalidKeywords'] = self.invalid_keywords
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_keywords is not None:
            result['RepeatKeywords'] = self.repeat_keywords
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthKeywords') is not None:
            self.illegal_length_keywords = m.get('IllegalLengthKeywords')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('InvalidKeywords') is not None:
            self.invalid_keywords = m.get('InvalidKeywords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatKeywords') is not None:
            self.repeat_keywords = m.get('RepeatKeywords')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AddKeywordLibResponseBodyData(TeaModel):
    def __init__(
        self,
        keywords_result: AddKeywordLibResponseBodyDataKeywordsResult = None,
        lib_id: str = None,
        task_id: str = None,
    ):
        self.keywords_result = keywords_result
        self.lib_id = lib_id
        self.task_id = task_id

    def validate(self):
        if self.keywords_result:
            self.keywords_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords_result is not None:
            result['KeywordsResult'] = self.keywords_result.to_map()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordsResult') is not None:
            temp_model = AddKeywordLibResponseBodyDataKeywordsResult()
            self.keywords_result = temp_model.from_map(m['KeywordsResult'])
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AddKeywordLibResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = AddKeywordLibResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddKeywordLibResponseBody = None,
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
            temp_model = AddKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddKeywordsRequest(TeaModel):
    def __init__(
        self,
        keywords: str = None,
        keywords_object: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.keywords = keywords
        self.keywords_object = keywords_object
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddKeywordsResponseBodyDataKeywordsResult(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_keywords: List[str] = None,
        invalid_count: int = None,
        invalid_keywords: List[str] = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_keywords: List[str] = None,
        success_count: int = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_keywords = illegal_length_keywords
        self.invalid_count = invalid_count
        self.invalid_keywords = invalid_keywords
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_keywords = repeat_keywords
        self.success_count = success_count
        self.tips = tips
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_keywords is not None:
            result['IllegalLengthKeywords'] = self.illegal_length_keywords
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.invalid_keywords is not None:
            result['InvalidKeywords'] = self.invalid_keywords
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_keywords is not None:
            result['RepeatKeywords'] = self.repeat_keywords
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthKeywords') is not None:
            self.illegal_length_keywords = m.get('IllegalLengthKeywords')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('InvalidKeywords') is not None:
            self.invalid_keywords = m.get('InvalidKeywords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatKeywords') is not None:
            self.repeat_keywords = m.get('RepeatKeywords')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AddKeywordsResponseBodyData(TeaModel):
    def __init__(
        self,
        keywords_result: AddKeywordsResponseBodyDataKeywordsResult = None,
        lib_id: str = None,
        task_id: str = None,
    ):
        self.keywords_result = keywords_result
        self.lib_id = lib_id
        self.task_id = task_id

    def validate(self):
        if self.keywords_result:
            self.keywords_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords_result is not None:
            result['KeywordsResult'] = self.keywords_result.to_map()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordsResult') is not None:
            temp_model = AddKeywordsResponseBodyDataKeywordsResult()
            self.keywords_result = temp_model.from_map(m['KeywordsResult'])
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: AddKeywordsResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = AddKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddKeywordsResponseBody = None,
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
            temp_model = AddKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddKeywordsToLibRequest(TeaModel):
    def __init__(
        self,
        keywords: str = None,
        keywords_object: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.keywords = keywords
        self.keywords_object = keywords_object
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddKeywordsToLibResponseBodyDataKeywordsResult(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_keywords: List[str] = None,
        invalid_count: int = None,
        invalid_keywords: List[str] = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_keywords: List[str] = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_keywords = illegal_length_keywords
        self.invalid_count = invalid_count
        self.invalid_keywords = invalid_keywords
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_keywords = repeat_keywords
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_keywords is not None:
            result['IllegalLengthKeywords'] = self.illegal_length_keywords
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.invalid_keywords is not None:
            result['InvalidKeywords'] = self.invalid_keywords
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_keywords is not None:
            result['RepeatKeywords'] = self.repeat_keywords
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthKeywords') is not None:
            self.illegal_length_keywords = m.get('IllegalLengthKeywords')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('InvalidKeywords') is not None:
            self.invalid_keywords = m.get('InvalidKeywords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatKeywords') is not None:
            self.repeat_keywords = m.get('RepeatKeywords')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AddKeywordsToLibResponseBodyData(TeaModel):
    def __init__(
        self,
        keywords_result: AddKeywordsToLibResponseBodyDataKeywordsResult = None,
        lib_id: str = None,
        task_id: str = None,
    ):
        self.keywords_result = keywords_result
        self.lib_id = lib_id
        self.task_id = task_id

    def validate(self):
        if self.keywords_result:
            self.keywords_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords_result is not None:
            result['KeywordsResult'] = self.keywords_result.to_map()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordsResult') is not None:
            temp_model = AddKeywordsToLibResponseBodyDataKeywordsResult()
            self.keywords_result = temp_model.from_map(m['KeywordsResult'])
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddKeywordsToLibResponseBody(TeaModel):
    def __init__(
        self,
        data: AddKeywordsToLibResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddKeywordsToLibResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddKeywordsToLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddKeywordsToLibResponseBody = None,
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
            temp_model = AddKeywordsToLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelStockOssCheckTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelStockOssCheckTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelStockOssCheckTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelStockOssCheckTaskResponseBody = None,
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
            temp_model = CancelStockOssCheckTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyServiceConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        service_desc: str = None,
        service_name: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.service_desc = service_desc
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_desc is not None:
            result['ServiceDesc'] = self.service_desc
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceDesc') is not None:
            self.service_desc = m.get('ServiceDesc')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CopyServiceConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyServiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyServiceConfigResponseBody = None,
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
            temp_model = CopyServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatStockOssCheckTaskRequest(TeaModel):
    def __init__(
        self,
        buckets: str = None,
        callback_id: str = None,
        distinct_history_tasks: bool = None,
        end_time: str = None,
        execute_date: int = None,
        execute_time: str = None,
        freeze: bool = None,
        freeze_high_risk_1: bool = None,
        freeze_high_risk_2: bool = None,
        freeze_medium_risk_1: bool = None,
        freeze_medium_risk_2: bool = None,
        freeze_type: str = None,
        is_inc: bool = None,
        media_type: int = None,
        prefix_filter_type: str = None,
        prefix_filters: str = None,
        priority: int = None,
        region_id: str = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_resource_type: str = None,
        scan_service: str = None,
        start_time: str = None,
        task_cycle: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.buckets = buckets
        self.callback_id = callback_id
        self.distinct_history_tasks = distinct_history_tasks
        self.end_time = end_time
        self.execute_date = execute_date
        self.execute_time = execute_time
        self.freeze = freeze
        self.freeze_high_risk_1 = freeze_high_risk_1
        self.freeze_high_risk_2 = freeze_high_risk_2
        self.freeze_medium_risk_1 = freeze_medium_risk_1
        self.freeze_medium_risk_2 = freeze_medium_risk_2
        self.freeze_type = freeze_type
        self.is_inc = is_inc
        self.media_type = media_type
        self.prefix_filter_type = prefix_filter_type
        self.prefix_filters = prefix_filters
        self.priority = priority
        self.region_id = region_id
        self.scan_limit = scan_limit
        self.scan_no_file_type = scan_no_file_type
        self.scan_resource_type = scan_resource_type
        self.scan_service = scan_service
        self.start_time = start_time
        self.task_cycle = task_cycle
        self.task_name = task_name
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.distinct_history_tasks is not None:
            result['DistinctHistoryTasks'] = self.distinct_history_tasks
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_date is not None:
            result['ExecuteDate'] = self.execute_date
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.freeze is not None:
            result['Freeze'] = self.freeze
        if self.freeze_high_risk_1 is not None:
            result['FreezeHighRisk1'] = self.freeze_high_risk_1
        if self.freeze_high_risk_2 is not None:
            result['FreezeHighRisk2'] = self.freeze_high_risk_2
        if self.freeze_medium_risk_1 is not None:
            result['FreezeMediumRisk1'] = self.freeze_medium_risk_1
        if self.freeze_medium_risk_2 is not None:
            result['FreezeMediumRisk2'] = self.freeze_medium_risk_2
        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type
        if self.is_inc is not None:
            result['IsInc'] = self.is_inc
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type
        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit
        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type
        if self.scan_resource_type is not None:
            result['ScanResourceType'] = self.scan_resource_type
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_cycle is not None:
            result['TaskCycle'] = self.task_cycle
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('DistinctHistoryTasks') is not None:
            self.distinct_history_tasks = m.get('DistinctHistoryTasks')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteDate') is not None:
            self.execute_date = m.get('ExecuteDate')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Freeze') is not None:
            self.freeze = m.get('Freeze')
        if m.get('FreezeHighRisk1') is not None:
            self.freeze_high_risk_1 = m.get('FreezeHighRisk1')
        if m.get('FreezeHighRisk2') is not None:
            self.freeze_high_risk_2 = m.get('FreezeHighRisk2')
        if m.get('FreezeMediumRisk1') is not None:
            self.freeze_medium_risk_1 = m.get('FreezeMediumRisk1')
        if m.get('FreezeMediumRisk2') is not None:
            self.freeze_medium_risk_2 = m.get('FreezeMediumRisk2')
        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')
        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')
        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')
        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')
        if m.get('ScanResourceType') is not None:
            self.scan_resource_type = m.get('ScanResourceType')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskCycle') is not None:
            self.task_cycle = m.get('TaskCycle')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreatStockOssCheckTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatStockOssCheckTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatStockOssCheckTaskResponseBody = None,
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
            temp_model = CreatStockOssCheckTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAnswerLibRequest(TeaModel):
    def __init__(
        self,
        lib_name: str = None,
        region_id: str = None,
        sample_bucket: str = None,
        sample_object: str = None,
        samples: str = None,
    ):
        self.lib_name = lib_name
        self.region_id = region_id
        self.sample_bucket = sample_bucket
        self.sample_object = sample_object
        self.samples = samples

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sample_bucket is not None:
            result['SampleBucket'] = self.sample_bucket
        if self.sample_object is not None:
            result['SampleObject'] = self.sample_object
        if self.samples is not None:
            result['Samples'] = self.samples
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SampleBucket') is not None:
            self.sample_bucket = m.get('SampleBucket')
        if m.get('SampleObject') is not None:
            self.sample_object = m.get('SampleObject')
        if m.get('Samples') is not None:
            self.samples = m.get('Samples')
        return self


class CreateAnswerLibResponseBodyResult(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_samples: List[str] = None,
        invalid_count: int = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_samples: List[str] = None,
        success_count: int = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_samples = illegal_length_samples
        self.invalid_count = invalid_count
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_samples = repeat_samples
        self.success_count = success_count
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_samples is not None:
            result['IllegalLengthSamples'] = self.illegal_length_samples
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_samples is not None:
            result['RepeatSamples'] = self.repeat_samples
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthSamples') is not None:
            self.illegal_length_samples = m.get('IllegalLengthSamples')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatSamples') is not None:
            self.repeat_samples = m.get('RepeatSamples')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateAnswerLibResponseBody(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        request_id: str = None,
        result: CreateAnswerLibResponseBodyResult = None,
        task_id: str = None,
    ):
        self.lib_id = lib_id
        self.request_id = request_id
        self.result = result
        self.task_id = task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAnswerLibResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateAnswerLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAnswerLibResponseBody = None,
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
            temp_model = CreateAnswerLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCallbackRequest(TeaModel):
    def __init__(
        self,
        crypt_type: str = None,
        name: str = None,
        region_id: str = None,
        scope: str = None,
        url: str = None,
    ):
        self.crypt_type = crypt_type
        self.name = name
        self.region_id = region_id
        self.scope = scope
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateCallbackResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCallbackResponseBody = None,
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
            temp_model = CreateCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePreCheckRequest(TeaModel):
    def __init__(
        self,
        buckets: str = None,
        distinct_history_tasks: bool = None,
        end_time: str = None,
        is_inc: bool = None,
        media_type: int = None,
        prefix_filter_type: str = None,
        prefix_filters: str = None,
        priority: int = None,
        region_id: str = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_service: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        self.buckets = buckets
        self.distinct_history_tasks = distinct_history_tasks
        self.end_time = end_time
        self.is_inc = is_inc
        self.media_type = media_type
        self.prefix_filter_type = prefix_filter_type
        self.prefix_filters = prefix_filters
        self.priority = priority
        self.region_id = region_id
        self.scan_limit = scan_limit
        self.scan_no_file_type = scan_no_file_type
        self.scan_service = scan_service
        self.start_time = start_time
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.distinct_history_tasks is not None:
            result['DistinctHistoryTasks'] = self.distinct_history_tasks
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_inc is not None:
            result['IsInc'] = self.is_inc
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type
        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit
        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DistinctHistoryTasks') is not None:
            self.distinct_history_tasks = m.get('DistinctHistoryTasks')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')
        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')
        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreatePreCheckResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, bool] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePreCheckResponseBody = None,
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
            temp_model = CreatePreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAnswerLibRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAnswerLibResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAnswerLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAnswerLibResponseBody = None,
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
            temp_model = DeleteAnswerLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAnswerSampleRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.ids = ids
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAnswerSampleResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAnswerSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAnswerSampleResponseBody = None,
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
            temp_model = DeleteAnswerSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCallbackRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCallbackResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCallbackResponseBody = None,
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
            temp_model = DeleteCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFeatureConfigRequest(TeaModel):
    def __init__(
        self,
        field: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        type: str = None,
    ):
        # Label value, customer-defined
        self.field = field
        # Region
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteFeatureConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # Return result.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message of this request.
        self.msg = msg
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFeatureConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFeatureConfigResponseBody = None,
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
            temp_model = DeleteFeatureConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesFromLibRequest(TeaModel):
    def __init__(
        self,
        image_ids: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.image_ids = image_ids
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteImagesFromLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImagesFromLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImagesFromLibResponseBody = None,
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
            temp_model = DeleteImagesFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordRequest(TeaModel):
    def __init__(
        self,
        keyword_id_list: str = None,
        keyword_ids: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.keyword_id_list = keyword_id_list
        self.keyword_ids = keyword_ids
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_id_list is not None:
            result['KeywordIdList'] = self.keyword_id_list
        if self.keyword_ids is not None:
            result['KeywordIds'] = self.keyword_ids
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordIdList') is not None:
            self.keyword_id_list = m.get('KeywordIdList')
        if m.get('KeywordIds') is not None:
            self.keyword_ids = m.get('KeywordIds')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteKeywordResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteKeywordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeywordResponseBody = None,
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
            temp_model = DeleteKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordLibRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeywordLibResponseBody = None,
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
            temp_model = DeleteKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportAnswerSampleRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExportAnswerSampleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportAnswerSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportAnswerSampleResponseBody = None,
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
            temp_model = ExportAnswerSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportCipStatsRequest(TeaModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        export_type: str = None,
        label: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        start_date: str = None,
        sub_uid: str = None,
        type: str = None,
    ):
        self.by_month = by_month
        self.end_date = end_date
        self.export_type = export_type
        self.label = label
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.start_date = start_date
        self.sub_uid = sub_uid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_month is not None:
            result['ByMonth'] = self.by_month
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.label is not None:
            result['Label'] = self.label
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ExportCipStatsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportCipStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportCipStatsResponseBody = None,
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
            temp_model = ExportCipStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportKeywordRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExportKeywordResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportKeywordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportKeywordResponseBody = None,
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
            temp_model = ExportKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportOssCheckStatRequest(TeaModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        parent_task_id: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        self.by_month = by_month
        self.end_date = end_date
        self.parent_task_id = parent_task_id
        self.region_id = region_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_month is not None:
            result['ByMonth'] = self.by_month
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportOssCheckStatResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportOssCheckStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportOssCheckStatResponseBody = None,
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
            temp_model = ExportOssCheckStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportResultShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportResultResponseBody = None,
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
            temp_model = ExportResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportScanResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: Dict[str, str] = None,
        region_id: str = None,
        resource_type: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.resource_type = resource_type
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportScanResultShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query_shrink: str = None,
        region_id: str = None,
        resource_type: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query_shrink = query_shrink
        self.region_id = region_id
        self.resource_type = resource_type
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportScanResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportScanResultResponseBody = None,
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
            temp_model = ExportScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportTextScanResultRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        query: Dict[str, str] = None,
        region_id: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.query = query
        self.region_id = region_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportTextScanResultShrinkRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        query_shrink: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.query_shrink = query_shrink
        self.region_id = region_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportTextScanResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportTextScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportTextScanResultResponseBody = None,
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
            temp_model = ExportTextScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnswerImportProgressRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAnswerImportProgressResponseBody(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_samples: List[str] = None,
        invalid_count: int = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_samples: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        task_id: str = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_samples = illegal_length_samples
        self.invalid_count = invalid_count
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_samples = repeat_samples
        self.request_id = request_id
        self.success_count = success_count
        self.task_id = task_id
        self.tips = tips
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_samples is not None:
            result['IllegalLengthSamples'] = self.illegal_length_samples
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_samples is not None:
            result['RepeatSamples'] = self.repeat_samples
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthSamples') is not None:
            self.illegal_length_samples = m.get('IllegalLengthSamples')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatSamples') is not None:
            self.repeat_samples = m.get('RepeatSamples')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAnswerImportProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAnswerImportProgressResponseBody = None,
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
            temp_model = GetAnswerImportProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBackupBucketsListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBackupBucketsListResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        region: str = None,
    ):
        self.bucket = bucket
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetBackupBucketsListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetBackupBucketsListResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetBackupBucketsListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBackupBucketsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBackupBucketsListResponseBody = None,
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
            temp_model = GetBackupBucketsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBackupConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetBackupConfigResponseBody(TeaModel):
    def __init__(
        self,
        backup_mode: int = None,
        bucket: str = None,
        enable: bool = None,
        enable_backup: bool = None,
        enable_backup_voice: bool = None,
        expire_seconds: int = None,
        gmt_modified: str = None,
        path: str = None,
        path_voice: str = None,
        region: str = None,
        request_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        uid: str = None,
    ):
        self.backup_mode = backup_mode
        self.bucket = bucket
        self.enable = enable
        self.enable_backup = enable_backup
        self.enable_backup_voice = enable_backup_voice
        self.expire_seconds = expire_seconds
        self.gmt_modified = gmt_modified
        self.path = path
        self.path_voice = path_voice
        self.region = region
        self.request_id = request_id
        self.resource_type = resource_type
        self.service_code = service_code
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.enable_backup is not None:
            result['EnableBackup'] = self.enable_backup
        if self.enable_backup_voice is not None:
            result['EnableBackupVoice'] = self.enable_backup_voice
        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.path is not None:
            result['Path'] = self.path
        if self.path_voice is not None:
            result['PathVoice'] = self.path_voice
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EnableBackup') is not None:
            self.enable_backup = m.get('EnableBackup')
        if m.get('EnableBackupVoice') is not None:
            self.enable_backup_voice = m.get('EnableBackupVoice')
        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathVoice') is not None:
            self.path_voice = m.get('PathVoice')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetBackupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBackupConfigResponseBody = None,
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
            temp_model = GetBackupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBackupStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBackupStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBackupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBackupStatusResponseBody = None,
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
            temp_model = GetBackupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketsListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBucketsListResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        region: str = None,
    ):
        self.bucket = bucket
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetBucketsListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetBucketsListResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetBucketsListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBucketsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBucketsListResponseBody = None,
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
            temp_model = GetBucketsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCipStatsRequest(TeaModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        label: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        start_date: str = None,
        sub_uid: str = None,
        type: str = None,
    ):
        self.by_month = by_month
        self.end_date = end_date
        self.label = label
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.start_date = start_date
        self.sub_uid = sub_uid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_month is not None:
            result['ByMonth'] = self.by_month
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.label is not None:
            result['Label'] = self.label
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetCipStatsResponseBodyDataLabelStatChartImageTreeChar(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCipStatsResponseBodyDataLabelStatChartTextTreeChart(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCipStatsResponseBodyDataLabelStatChartTreeChart(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCipStatsResponseBodyDataLabelStatChartY(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetCipStatsResponseBodyDataLabelStatChart(TeaModel):
    def __init__(
        self,
        image_tree_char: List[GetCipStatsResponseBodyDataLabelStatChartImageTreeChar] = None,
        service_code: str = None,
        text_tree_chart: List[GetCipStatsResponseBodyDataLabelStatChartTextTreeChart] = None,
        total_count: int = None,
        tree_chart: List[GetCipStatsResponseBodyDataLabelStatChartTreeChart] = None,
        voice_tree_chart: List[GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart] = None,
        x: List[str] = None,
        y: List[GetCipStatsResponseBodyDataLabelStatChartY] = None,
    ):
        self.image_tree_char = image_tree_char
        self.service_code = service_code
        self.text_tree_chart = text_tree_chart
        self.total_count = total_count
        self.tree_chart = tree_chart
        self.voice_tree_chart = voice_tree_chart
        self.x = x
        self.y = y

    def validate(self):
        if self.image_tree_char:
            for k in self.image_tree_char:
                if k:
                    k.validate()
        if self.text_tree_chart:
            for k in self.text_tree_chart:
                if k:
                    k.validate()
        if self.tree_chart:
            for k in self.tree_chart:
                if k:
                    k.validate()
        if self.voice_tree_chart:
            for k in self.voice_tree_chart:
                if k:
                    k.validate()
        if self.y:
            for k in self.y:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageTreeChar'] = []
        if self.image_tree_char is not None:
            for k in self.image_tree_char:
                result['ImageTreeChar'].append(k.to_map() if k else None)
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        result['TextTreeChart'] = []
        if self.text_tree_chart is not None:
            for k in self.text_tree_chart:
                result['TextTreeChart'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TreeChart'] = []
        if self.tree_chart is not None:
            for k in self.tree_chart:
                result['TreeChart'].append(k.to_map() if k else None)
        result['VoiceTreeChart'] = []
        if self.voice_tree_chart is not None:
            for k in self.voice_tree_chart:
                result['VoiceTreeChart'].append(k.to_map() if k else None)
        if self.x is not None:
            result['X'] = self.x
        result['Y'] = []
        if self.y is not None:
            for k in self.y:
                result['Y'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_tree_char = []
        if m.get('ImageTreeChar') is not None:
            for k in m.get('ImageTreeChar'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChartImageTreeChar()
                self.image_tree_char.append(temp_model.from_map(k))
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        self.text_tree_chart = []
        if m.get('TextTreeChart') is not None:
            for k in m.get('TextTreeChart'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChartTextTreeChart()
                self.text_tree_chart.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tree_chart = []
        if m.get('TreeChart') is not None:
            for k in m.get('TreeChart'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChartTreeChart()
                self.tree_chart.append(temp_model.from_map(k))
        self.voice_tree_chart = []
        if m.get('VoiceTreeChart') is not None:
            for k in m.get('VoiceTreeChart'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart()
                self.voice_tree_chart.append(temp_model.from_map(k))
        if m.get('X') is not None:
            self.x = m.get('X')
        self.y = []
        if m.get('Y') is not None:
            for k in m.get('Y'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChartY()
                self.y.append(temp_model.from_map(k))
        return self


class GetCipStatsResponseBodyDataY(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetCipStatsResponseBodyDataZ(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetCipStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        label_stat_chart: List[GetCipStatsResponseBodyDataLabelStatChart] = None,
        total_stat: Dict[str, dict] = None,
        uids: List[str] = None,
        x: List[str] = None,
        y: List[GetCipStatsResponseBodyDataY] = None,
        z: List[GetCipStatsResponseBodyDataZ] = None,
    ):
        self.label_stat_chart = label_stat_chart
        self.total_stat = total_stat
        self.uids = uids
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        if self.label_stat_chart:
            for k in self.label_stat_chart:
                if k:
                    k.validate()
        if self.y:
            for k in self.y:
                if k:
                    k.validate()
        if self.z:
            for k in self.z:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelStatChart'] = []
        if self.label_stat_chart is not None:
            for k in self.label_stat_chart:
                result['LabelStatChart'].append(k.to_map() if k else None)
        if self.total_stat is not None:
            result['TotalStat'] = self.total_stat
        if self.uids is not None:
            result['Uids'] = self.uids
        if self.x is not None:
            result['X'] = self.x
        result['Y'] = []
        if self.y is not None:
            for k in self.y:
                result['Y'].append(k.to_map() if k else None)
        result['Z'] = []
        if self.z is not None:
            for k in self.z:
                result['Z'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_stat_chart = []
        if m.get('LabelStatChart') is not None:
            for k in m.get('LabelStatChart'):
                temp_model = GetCipStatsResponseBodyDataLabelStatChart()
                self.label_stat_chart.append(temp_model.from_map(k))
        if m.get('TotalStat') is not None:
            self.total_stat = m.get('TotalStat')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        if m.get('X') is not None:
            self.x = m.get('X')
        self.y = []
        if m.get('Y') is not None:
            for k in m.get('Y'):
                temp_model = GetCipStatsResponseBodyDataY()
                self.y.append(temp_model.from_map(k))
        self.z = []
        if m.get('Z') is not None:
            for k in m.get('Z'):
                temp_model = GetCipStatsResponseBodyDataZ()
                self.z.append(temp_model.from_map(k))
        return self


class GetCipStatsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetCipStatsResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = GetCipStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCipStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCipStatsResponseBody = None,
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
            temp_model = GetCipStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteTimeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetExecuteTimeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecuteTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecuteTimeResponseBody = None,
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
            temp_model = GetExecuteTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        type: str = None,
    ):
        # Region ID
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFeatureConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        feature_conf: List[Dict[str, Any]] = None,
        resource_type: str = None,
        service_code: str = None,
        type: str = None,
        uid: str = None,
    ):
        # List of feature configurations
        self.feature_conf = feature_conf
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Type
        self.type = type
        # UID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_conf is not None:
            result['FeatureConf'] = self.feature_conf
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConf') is not None:
            self.feature_conf = m.get('FeatureConf')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetFeatureConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetFeatureConfigResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # Returned data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message for this request.
        self.msg = msg
        # ID assigned by the backend, used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = GetFeatureConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFeatureConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureConfigResponseBody = None,
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
            temp_model = GetFeatureConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageSceneLabelConfRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetImageSceneLabelConfResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[Dict[str, Any]] = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImageSceneLabelConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageSceneLabelConfResponseBody = None,
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
            temp_model = GetImageSceneLabelConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageSceneLabelListConfRequest(TeaModel):
    def __init__(
        self,
        image_service_code: str = None,
        region_id: str = None,
    ):
        self.image_service_code = image_service_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_service_code is not None:
            result['ImageServiceCode'] = self.image_service_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageServiceCode') is not None:
            self.image_service_code = m.get('ImageServiceCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetImageSceneLabelListConfResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Any] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageSceneLabelListConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageSceneLabelListConfResponseBody = None,
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
            temp_model = GetImageSceneLabelListConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobNameListRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        query: str = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.query = query
        self.region_id = region_id
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetJobNameListShrinkRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.query = query
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetJobNameListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobNameListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobNameListResponseBody = None,
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
            temp_model = GetJobNameListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordImportResultRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetKeywordImportResultResponseBodyData(TeaModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_keywords: List[str] = None,
        invalid_count: int = None,
        invalid_keywords: List[str] = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_keywords: List[str] = None,
        success_count: int = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_keywords = illegal_length_keywords
        self.invalid_count = invalid_count
        self.invalid_keywords = invalid_keywords
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_keywords = repeat_keywords
        self.success_count = success_count
        self.tips = tips
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key
        if self.illegal_length_keywords is not None:
            result['IllegalLengthKeywords'] = self.illegal_length_keywords
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count
        if self.invalid_keywords is not None:
            result['InvalidKeywords'] = self.invalid_keywords
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_keywords is not None:
            result['RepeatKeywords'] = self.repeat_keywords
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')
        if m.get('IllegalLengthKeywords') is not None:
            self.illegal_length_keywords = m.get('IllegalLengthKeywords')
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')
        if m.get('InvalidKeywords') is not None:
            self.invalid_keywords = m.get('InvalidKeywords')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatKeywords') is not None:
            self.repeat_keywords = m.get('RepeatKeywords')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetKeywordImportResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetKeywordImportResultResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetKeywordImportResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKeywordImportResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKeywordImportResultResponseBody = None,
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
            temp_model = GetKeywordImportResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordLibRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetKeywordLibResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        keyword_count: str = None,
        lib_id: str = None,
        lib_name: str = None,
        uid: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.keyword_count = keyword_count
        self.lib_id = lib_id
        self.lib_name = lib_name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.keyword_count is not None:
            result['KeywordCount'] = self.keyword_count
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('KeywordCount') is not None:
            self.keyword_count = m.get('KeywordCount')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetKeywordLibResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetKeywordLibResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKeywordLibResponseBody = None,
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
            temp_model = GetKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssCheckStatRequest(TeaModel):
    def __init__(
        self,
        by_month: bool = None,
        end_date: str = None,
        parent_task_id: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        self.by_month = by_month
        self.end_date = end_date
        self.parent_task_id = parent_task_id
        self.region_id = region_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_month is not None:
            result['ByMonth'] = self.by_month
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByMonth') is not None:
            self.by_month = m.get('ByMonth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetOssCheckStatResponseBodyBarChartY(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOssCheckStatResponseBodyBarChart(TeaModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[GetOssCheckStatResponseBodyBarChartY] = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        if self.y:
            for k in self.y:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        result['Y'] = []
        if self.y is not None:
            for k in self.y:
                result['Y'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        self.y = []
        if m.get('Y') is not None:
            for k in m.get('Y'):
                temp_model = GetOssCheckStatResponseBodyBarChartY()
                self.y.append(temp_model.from_map(k))
        return self


class GetOssCheckStatResponseBody(TeaModel):
    def __init__(
        self,
        bar_chart: GetOssCheckStatResponseBodyBarChart = None,
        request_id: str = None,
    ):
        self.bar_chart = bar_chart
        self.request_id = request_id

    def validate(self):
        if self.bar_chart:
            self.bar_chart.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bar_chart is not None:
            result['BarChart'] = self.bar_chart.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BarChart') is not None:
            temp_model = GetOssCheckStatResponseBodyBarChart()
            self.bar_chart = temp_model.from_map(m['BarChart'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssCheckStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssCheckStatResponseBody = None,
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
            temp_model = GetOssCheckStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssCheckStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOssCheckStatusResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        buy: bool = None,
        commodity_code: str = None,
        indebt: bool = None,
        ram_status: str = None,
        request_id: str = None,
        sls_status: str = None,
    ):
        # Bid。
        self.bid = bid
        self.buy = buy
        self.commodity_code = commodity_code
        self.indebt = indebt
        self.ram_status = ram_status
        self.request_id = request_id
        self.sls_status = sls_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.buy is not None:
            result['Buy'] = self.buy
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.indebt is not None:
            result['Indebt'] = self.indebt
        if self.ram_status is not None:
            result['RamStatus'] = self.ram_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Buy') is not None:
            self.buy = m.get('Buy')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Indebt') is not None:
            self.indebt = m.get('Indebt')
        if m.get('RamStatus') is not None:
            self.ram_status = m.get('RamStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        return self


class GetOssCheckStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssCheckStatusResponseBody = None,
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
            temp_model = GetOssCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScanNumRequest(TeaModel):
    def __init__(
        self,
        buckets: str = None,
        media_type: int = None,
        region_id: str = None,
    ):
        self.buckets = buckets
        self.media_type = media_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetScanNumResponseBody(TeaModel):
    def __init__(
        self,
        limit_number: int = None,
        request_id: str = None,
        scan_number: int = None,
        sum_number: int = None,
        tag: bool = None,
    ):
        self.limit_number = limit_number
        self.request_id = request_id
        self.scan_number = scan_number
        self.sum_number = sum_number
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_number is not None:
            result['ScanNumber'] = self.scan_number
        if self.sum_number is not None:
            result['SumNumber'] = self.sum_number
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanNumber') is not None:
            self.scan_number = m.get('ScanNumber')
        if m.get('SumNumber') is not None:
            self.sum_number = m.get('SumNumber')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetScanNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScanNumResponseBody = None,
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
            temp_model = GetScanNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScanResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: Dict[str, str] = None,
        region_id: str = None,
        resource_type: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.resource_type = resource_type
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetScanResultShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query_shrink: str = None,
        region_id: str = None,
        resource_type: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query_shrink = query_shrink
        self.region_id = region_id
        self.resource_type = resource_type
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetScanResultResponseBodyDataItemsResult(TeaModel):
    def __init__(
        self,
        confidence: str = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetScanResultResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        api_labels: str = None,
        api_request_time: str = None,
        api_risk_level: str = None,
        api_service: str = None,
        api_task_id: str = None,
        attack_level: str = None,
        content: str = None,
        data_id: str = None,
        end_time: str = None,
        ext_feedback: str = None,
        extra: Dict[str, Any] = None,
        frame_count: int = None,
        gmt_create: str = None,
        guard_file_urls: List[str] = None,
        guard_image_urls: List[str] = None,
        image_labels: List[Dict[str, Any]] = None,
        image_service: str = None,
        image_url: str = None,
        labels: str = None,
        malicious_file_level: str = None,
        malicious_url_level: str = None,
        manual_only: bool = None,
        no_labels: List[str] = None,
        offset: int = None,
        page_num: int = None,
        request_from: str = None,
        request_id: str = None,
        request_time: str = None,
        resource_type: str = None,
        result: List[GetScanResultResponseBodyDataItemsResult] = None,
        review_labels: str = None,
        review_risk_level: str = None,
        review_time: str = None,
        review_uid: str = None,
        reviewed: bool = None,
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        scan_result: str = None,
        score: float = None,
        sensitive_level: str = None,
        service_code: str = None,
        start_time: str = None,
        suggestion: str = None,
        task_id: str = None,
        text_labels: List[Dict[str, Any]] = None,
        thumbnail: str = None,
        time_stamp: str = None,
        url: str = None,
        voice_labels: List[Dict[str, Any]] = None,
        voice_scan_opened: bool = None,
        voice_service: str = None,
    ):
        self.api_labels = api_labels
        self.api_request_time = api_request_time
        self.api_risk_level = api_risk_level
        self.api_service = api_service
        self.api_task_id = api_task_id
        self.attack_level = attack_level
        self.content = content
        # dataId
        self.data_id = data_id
        self.end_time = end_time
        self.ext_feedback = ext_feedback
        self.extra = extra
        self.frame_count = frame_count
        self.gmt_create = gmt_create
        self.guard_file_urls = guard_file_urls
        self.guard_image_urls = guard_image_urls
        self.image_labels = image_labels
        self.image_service = image_service
        # url
        self.image_url = image_url
        self.labels = labels
        self.malicious_file_level = malicious_file_level
        self.malicious_url_level = malicious_url_level
        self.manual_only = manual_only
        self.no_labels = no_labels
        self.offset = offset
        self.page_num = page_num
        self.request_from = request_from
        self.request_id = request_id
        self.request_time = request_time
        self.resource_type = resource_type
        self.result = result
        self.review_labels = review_labels
        self.review_risk_level = review_risk_level
        self.review_time = review_time
        self.review_uid = review_uid
        self.reviewed = reviewed
        self.risk_level = risk_level
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.scan_result = scan_result
        self.score = score
        self.sensitive_level = sensitive_level
        self.service_code = service_code
        self.start_time = start_time
        self.suggestion = suggestion
        self.task_id = task_id
        self.text_labels = text_labels
        self.thumbnail = thumbnail
        self.time_stamp = time_stamp
        self.url = url
        self.voice_labels = voice_labels
        self.voice_scan_opened = voice_scan_opened
        self.voice_service = voice_service

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_labels is not None:
            result['ApiLabels'] = self.api_labels
        if self.api_request_time is not None:
            result['ApiRequestTime'] = self.api_request_time
        if self.api_risk_level is not None:
            result['ApiRiskLevel'] = self.api_risk_level
        if self.api_service is not None:
            result['ApiService'] = self.api_service
        if self.api_task_id is not None:
            result['ApiTaskId'] = self.api_task_id
        if self.attack_level is not None:
            result['AttackLevel'] = self.attack_level
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ext_feedback is not None:
            result['ExtFeedback'] = self.ext_feedback
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.guard_file_urls is not None:
            result['GuardFileUrls'] = self.guard_file_urls
        if self.guard_image_urls is not None:
            result['GuardImageUrls'] = self.guard_image_urls
        if self.image_labels is not None:
            result['ImageLabels'] = self.image_labels
        if self.image_service is not None:
            result['ImageService'] = self.image_service
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.malicious_file_level is not None:
            result['MaliciousFileLevel'] = self.malicious_file_level
        if self.malicious_url_level is not None:
            result['MaliciousUrlLevel'] = self.malicious_url_level
        if self.manual_only is not None:
            result['ManualOnly'] = self.manual_only
        if self.no_labels is not None:
            result['NoLabels'] = self.no_labels
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_from is not None:
            result['RequestFrom'] = self.request_from
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.review_labels is not None:
            result['ReviewLabels'] = self.review_labels
        if self.review_risk_level is not None:
            result['ReviewRiskLevel'] = self.review_risk_level
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.review_uid is not None:
            result['ReviewUid'] = self.review_uid
        if self.reviewed is not None:
            result['Reviewed'] = self.reviewed
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result
        if self.score is not None:
            result['Score'] = self.score
        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.text_labels is not None:
            result['TextLabels'] = self.text_labels
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.url is not None:
            result['Url'] = self.url
        if self.voice_labels is not None:
            result['VoiceLabels'] = self.voice_labels
        if self.voice_scan_opened is not None:
            result['VoiceScanOpened'] = self.voice_scan_opened
        if self.voice_service is not None:
            result['VoiceService'] = self.voice_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiLabels') is not None:
            self.api_labels = m.get('ApiLabels')
        if m.get('ApiRequestTime') is not None:
            self.api_request_time = m.get('ApiRequestTime')
        if m.get('ApiRiskLevel') is not None:
            self.api_risk_level = m.get('ApiRiskLevel')
        if m.get('ApiService') is not None:
            self.api_service = m.get('ApiService')
        if m.get('ApiTaskId') is not None:
            self.api_task_id = m.get('ApiTaskId')
        if m.get('AttackLevel') is not None:
            self.attack_level = m.get('AttackLevel')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtFeedback') is not None:
            self.ext_feedback = m.get('ExtFeedback')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GuardFileUrls') is not None:
            self.guard_file_urls = m.get('GuardFileUrls')
        if m.get('GuardImageUrls') is not None:
            self.guard_image_urls = m.get('GuardImageUrls')
        if m.get('ImageLabels') is not None:
            self.image_labels = m.get('ImageLabels')
        if m.get('ImageService') is not None:
            self.image_service = m.get('ImageService')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MaliciousFileLevel') is not None:
            self.malicious_file_level = m.get('MaliciousFileLevel')
        if m.get('MaliciousUrlLevel') is not None:
            self.malicious_url_level = m.get('MaliciousUrlLevel')
        if m.get('ManualOnly') is not None:
            self.manual_only = m.get('ManualOnly')
        if m.get('NoLabels') is not None:
            self.no_labels = m.get('NoLabels')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestFrom') is not None:
            self.request_from = m.get('RequestFrom')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetScanResultResponseBodyDataItemsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('ReviewLabels') is not None:
            self.review_labels = m.get('ReviewLabels')
        if m.get('ReviewRiskLevel') is not None:
            self.review_risk_level = m.get('ReviewRiskLevel')
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('ReviewUid') is not None:
            self.review_uid = m.get('ReviewUid')
        if m.get('Reviewed') is not None:
            self.reviewed = m.get('Reviewed')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TextLabels') is not None:
            self.text_labels = m.get('TextLabels')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VoiceLabels') is not None:
            self.voice_labels = m.get('VoiceLabels')
        if m.get('VoiceScanOpened') is not None:
            self.voice_scan_opened = m.get('VoiceScanOpened')
        if m.get('VoiceService') is not None:
            self.voice_service = m.get('VoiceService')
        return self


class GetScanResultResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[GetScanResultResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetScanResultResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetScanResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetScanResultResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            temp_model = GetScanResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScanResultResponseBody = None,
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
            temp_model = GetScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceConfRequest(TeaModel):
    def __init__(
        self,
        by_default: bool = None,
        region_id: str = None,
        resource_type: str = None,
        scene: str = None,
        service_code: str = None,
    ):
        self.by_default = by_default
        self.region_id = region_id
        self.resource_type = resource_type
        self.scene = scene
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_default is not None:
            result['ByDefault'] = self.by_default
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByDefault') is not None:
            self.by_default = m.get('ByDefault')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetServiceConfResponseBody(TeaModel):
    def __init__(
        self,
        classify: str = None,
        code: int = None,
        custom_service_conf: Dict[str, Any] = None,
        gmt_modified: str = None,
        msg: str = None,
        option: Dict[str, Any] = None,
        request_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        service_type: str = None,
        success: bool = None,
        uid: str = None,
    ):
        self.classify = classify
        self.code = code
        self.custom_service_conf = custom_service_conf
        self.gmt_modified = gmt_modified
        self.msg = msg
        self.option = option
        self.request_id = request_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.service_type = service_type
        self.success = success
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.code is not None:
            result['Code'] = self.code
        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.option is not None:
            result['Option'] = self.option
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.success is not None:
            result['Success'] = self.success
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustomServiceConf') is not None:
            self.custom_service_conf = m.get('CustomServiceConf')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetServiceConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceConfResponseBody = None,
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
            temp_model = GetServiceConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig(TeaModel):
    def __init__(
        self,
        audit_risk_levels: List[str] = None,
        callback_id: int = None,
        enable: bool = None,
        manual_service: str = None,
    ):
        self.audit_risk_levels = audit_risk_levels
        self.callback_id = callback_id
        self.enable = enable
        self.manual_service = manual_service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_risk_levels is not None:
            result['AuditRiskLevels'] = self.audit_risk_levels
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.manual_service is not None:
            result['ManualService'] = self.manual_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRiskLevels') is not None:
            self.audit_risk_levels = m.get('AuditRiskLevels')
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ManualService') is not None:
            self.manual_service = m.get('ManualService')
        return self


class GetServiceConfigResponseBodyDataCustomServiceConf(TeaModel):
    def __init__(
        self,
        keyword_filter_libs: List[str] = None,
        keyword_hit_libs: List[str] = None,
        manual_machine_config: GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig = None,
        similar_text_hit_libs: List[str] = None,
    ):
        self.keyword_filter_libs = keyword_filter_libs
        self.keyword_hit_libs = keyword_hit_libs
        self.manual_machine_config = manual_machine_config
        self.similar_text_hit_libs = similar_text_hit_libs

    def validate(self):
        if self.manual_machine_config:
            self.manual_machine_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs
        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs
        if self.manual_machine_config is not None:
            result['ManualMachineConfig'] = self.manual_machine_config.to_map()
        if self.similar_text_hit_libs is not None:
            result['SimilarTextHitLibs'] = self.similar_text_hit_libs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')
        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')
        if m.get('ManualMachineConfig') is not None:
            temp_model = GetServiceConfigResponseBodyDataCustomServiceConfManualMachineConfig()
            self.manual_machine_config = temp_model.from_map(m['ManualMachineConfig'])
        if m.get('SimilarTextHitLibs') is not None:
            self.similar_text_hit_libs = m.get('SimilarTextHitLibs')
        return self


class GetServiceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_service_conf: GetServiceConfigResponseBodyDataCustomServiceConf = None,
        gmt_modified: str = None,
        resource_type: str = None,
        service_code: str = None,
        uid: str = None,
    ):
        self.custom_service_conf = custom_service_conf
        self.gmt_modified = gmt_modified
        self.resource_type = resource_type
        self.service_code = service_code
        # UID。
        self.uid = uid

    def validate(self):
        if self.custom_service_conf:
            self.custom_service_conf.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomServiceConf') is not None:
            temp_model = GetServiceConfigResponseBodyDataCustomServiceConf()
            self.custom_service_conf = temp_model.from_map(m['CustomServiceConf'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetServiceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetServiceConfigResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetServiceConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetServiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceConfigResponseBody = None,
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
            temp_model = GetServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLabelConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetServiceLabelConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Any] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceLabelConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceLabelConfigResponseBody = None,
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
            temp_model = GetServiceLabelConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStockOssCheckTasksListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        is_inc: bool = None,
        media_type: int = None,
        page_size: int = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_time: str = None,
        task_type: str = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.is_inc = is_inc
        self.media_type = media_type
        self.page_size = page_size
        self.region_id = region_id
        self.sort = sort
        self.start_time = start_time
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_inc is not None:
            result['IsInc'] = self.is_inc
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetStockOssCheckTasksListShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        is_inc: bool = None,
        media_type: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_time: str = None,
        task_type: str = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.is_inc = is_inc
        self.media_type = media_type
        self.page_size = page_size
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_time = start_time
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_inc is not None:
            result['IsInc'] = self.is_inc
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetStockOssCheckTasksListResponseBodyItemsConfigScanServiceInfos(TeaModel):
    def __init__(
        self,
        copy_from: str = None,
        is_copy: bool = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.copy_from = copy_from
        self.is_copy = is_copy
        self.service_code = service_code
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from
        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')
        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetStockOssCheckTasksListResponseBodyItemsConfig(TeaModel):
    def __init__(
        self,
        callback_id: int = None,
        distinct_history_tasks: bool = None,
        end_time: str = None,
        execute_date: int = None,
        execute_time: str = None,
        freeze: bool = None,
        freeze_high_risk_1: bool = None,
        freeze_high_risk_2: bool = None,
        freeze_medium_risk_1: bool = None,
        freeze_medium_risk_2: bool = None,
        freeze_type: str = None,
        prefix_filter_type: str = None,
        prefix_filters: List[str] = None,
        priority: int = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_resource_type: int = None,
        scan_service: List[str] = None,
        scan_service_infos: List[GetStockOssCheckTasksListResponseBodyItemsConfigScanServiceInfos] = None,
        start_time: str = None,
        task_cycle: int = None,
    ):
        self.callback_id = callback_id
        self.distinct_history_tasks = distinct_history_tasks
        self.end_time = end_time
        self.execute_date = execute_date
        self.execute_time = execute_time
        self.freeze = freeze
        self.freeze_high_risk_1 = freeze_high_risk_1
        self.freeze_high_risk_2 = freeze_high_risk_2
        self.freeze_medium_risk_1 = freeze_medium_risk_1
        self.freeze_medium_risk_2 = freeze_medium_risk_2
        self.freeze_type = freeze_type
        self.prefix_filter_type = prefix_filter_type
        self.prefix_filters = prefix_filters
        self.priority = priority
        self.scan_limit = scan_limit
        self.scan_no_file_type = scan_no_file_type
        self.scan_resource_type = scan_resource_type
        self.scan_service = scan_service
        self.scan_service_infos = scan_service_infos
        self.start_time = start_time
        self.task_cycle = task_cycle

    def validate(self):
        if self.scan_service_infos:
            for k in self.scan_service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.distinct_history_tasks is not None:
            result['DistinctHistoryTasks'] = self.distinct_history_tasks
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_date is not None:
            result['ExecuteDate'] = self.execute_date
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.freeze is not None:
            result['Freeze'] = self.freeze
        if self.freeze_high_risk_1 is not None:
            result['FreezeHighRisk1'] = self.freeze_high_risk_1
        if self.freeze_high_risk_2 is not None:
            result['FreezeHighRisk2'] = self.freeze_high_risk_2
        if self.freeze_medium_risk_1 is not None:
            result['FreezeMediumRisk1'] = self.freeze_medium_risk_1
        if self.freeze_medium_risk_2 is not None:
            result['FreezeMediumRisk2'] = self.freeze_medium_risk_2
        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type
        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type
        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit
        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type
        if self.scan_resource_type is not None:
            result['ScanResourceType'] = self.scan_resource_type
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        result['ScanServiceInfos'] = []
        if self.scan_service_infos is not None:
            for k in self.scan_service_infos:
                result['ScanServiceInfos'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_cycle is not None:
            result['TaskCycle'] = self.task_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('DistinctHistoryTasks') is not None:
            self.distinct_history_tasks = m.get('DistinctHistoryTasks')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteDate') is not None:
            self.execute_date = m.get('ExecuteDate')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Freeze') is not None:
            self.freeze = m.get('Freeze')
        if m.get('FreezeHighRisk1') is not None:
            self.freeze_high_risk_1 = m.get('FreezeHighRisk1')
        if m.get('FreezeHighRisk2') is not None:
            self.freeze_high_risk_2 = m.get('FreezeHighRisk2')
        if m.get('FreezeMediumRisk1') is not None:
            self.freeze_medium_risk_1 = m.get('FreezeMediumRisk1')
        if m.get('FreezeMediumRisk2') is not None:
            self.freeze_medium_risk_2 = m.get('FreezeMediumRisk2')
        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')
        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')
        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')
        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')
        if m.get('ScanResourceType') is not None:
            self.scan_resource_type = m.get('ScanResourceType')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        self.scan_service_infos = []
        if m.get('ScanServiceInfos') is not None:
            for k in m.get('ScanServiceInfos'):
                temp_model = GetStockOssCheckTasksListResponseBodyItemsConfigScanServiceInfos()
                self.scan_service_infos.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskCycle') is not None:
            self.task_cycle = m.get('TaskCycle')
        return self


class GetStockOssCheckTasksListResponseBodyItems(TeaModel):
    def __init__(
        self,
        buckets: str = None,
        config: GetStockOssCheckTasksListResponseBodyItemsConfig = None,
        end_time: str = None,
        finish_num: int = None,
        is_inc: bool = None,
        last_execute_date: str = None,
        media_type: int = None,
        next_execute_date: str = None,
        object_num: int = None,
        search_num: int = None,
        start_time: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.buckets = buckets
        self.config = config
        self.end_time = end_time
        self.finish_num = finish_num
        self.is_inc = is_inc
        self.last_execute_date = last_execute_date
        self.media_type = media_type
        self.next_execute_date = next_execute_date
        self.object_num = object_num
        self.search_num = search_num
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.finish_num is not None:
            result['FinishNum'] = self.finish_num
        if self.is_inc is not None:
            result['IsInc'] = self.is_inc
        if self.last_execute_date is not None:
            result['LastExecuteDate'] = self.last_execute_date
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.next_execute_date is not None:
            result['NextExecuteDate'] = self.next_execute_date
        if self.object_num is not None:
            result['ObjectNum'] = self.object_num
        if self.search_num is not None:
            result['SearchNum'] = self.search_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            temp_model = GetStockOssCheckTasksListResponseBodyItemsConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FinishNum') is not None:
            self.finish_num = m.get('FinishNum')
        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')
        if m.get('LastExecuteDate') is not None:
            self.last_execute_date = m.get('LastExecuteDate')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('NextExecuteDate') is not None:
            self.next_execute_date = m.get('NextExecuteDate')
        if m.get('ObjectNum') is not None:
            self.object_num = m.get('ObjectNum')
        if m.get('SearchNum') is not None:
            self.search_num = m.get('SearchNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetStockOssCheckTasksListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[GetStockOssCheckTasksListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetStockOssCheckTasksListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetStockOssCheckTasksListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStockOssCheckTasksListResponseBody = None,
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
            temp_model = GetStockOssCheckTasksListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextScanResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: Dict[str, str] = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetTextScanResultShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query_shrink: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.page_size = page_size
        self.query_shrink = query_shrink
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class GetTextScanResultResponseBodyDataItemsResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetTextScanResultResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        bailian_request_id: str = None,
        content: str = None,
        ext_feedback: str = None,
        extra: Dict[str, Any] = None,
        gmt_create: str = None,
        labels: str = None,
        request_id: str = None,
        request_time: str = None,
        result: List[GetTextScanResultResponseBodyDataItemsResult] = None,
        risk_level: str = None,
        scan_result: str = None,
        score: float = None,
        service_code: str = None,
        suggestion: str = None,
        task_id: str = None,
    ):
        self.bailian_request_id = bailian_request_id
        self.content = content
        self.ext_feedback = ext_feedback
        self.extra = extra
        self.gmt_create = gmt_create
        self.labels = labels
        self.request_id = request_id
        self.request_time = request_time
        self.result = result
        self.risk_level = risk_level
        self.scan_result = scan_result
        self.score = score
        self.service_code = service_code
        self.suggestion = suggestion
        self.task_id = task_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bailian_request_id is not None:
            result['BailianRequestId'] = self.bailian_request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.ext_feedback is not None:
            result['ExtFeedback'] = self.ext_feedback
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result
        if self.score is not None:
            result['Score'] = self.score
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BailianRequestId') is not None:
            self.bailian_request_id = m.get('BailianRequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExtFeedback') is not None:
            self.ext_feedback = m.get('ExtFeedback')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTextScanResultResponseBodyDataItemsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTextScanResultResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[GetTextScanResultResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetTextScanResultResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetTextScanResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTextScanResultResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetTextScanResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTextScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextScanResultResponseBody = None,
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
            temp_model = GetTextScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadInfoRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.name = name
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        code: int = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        http_status_code: int = None,
        key: str = None,
        msg: str = None,
        name: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        success: bool = None,
    ):
        self.access_id = access_id
        self.code = code
        self.expire = expire
        self.folder = folder
        self.host = host
        self.http_status_code = http_status_code
        self.key = key
        self.msg = msg
        self.name = name
        self.policy = policy
        self.request_id = request_id
        self.signature = signature
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.code is not None:
            result['Code'] = self.code
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.key is not None:
            result['Key'] = self.key
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadInfoResponseBody = None,
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
            temp_model = GetUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserBuyStatusRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        region_id: str = None,
    ):
        self.commodity_code = commodity_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetUserBuyStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        bid: int = None,
        buy: bool = None,
        indebt: bool = None,
        tag: str = None,
    ):
        # Bid。
        self.bid = bid
        self.buy = buy
        self.indebt = indebt
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.buy is not None:
            result['Buy'] = self.buy
        if self.indebt is not None:
            result['Indebt'] = self.indebt
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Buy') is not None:
            self.buy = m.get('Buy')
        if m.get('Indebt') is not None:
            self.indebt = m.get('Indebt')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetUserBuyStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetUserBuyStatusResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetUserBuyStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserBuyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserBuyStatusResponseBody = None,
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
            temp_model = GetUserBuyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnswerLibRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAnswerLibResponseBodyData(TeaModel):
    def __init__(
        self,
        answer_count: int = None,
        gmt_modified: str = None,
        lib_id: str = None,
        lib_name: str = None,
        uid: str = None,
    ):
        self.answer_count = answer_count
        self.gmt_modified = gmt_modified
        self.lib_id = lib_id
        self.lib_name = lib_name
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_count is not None:
            result['AnswerCount'] = self.answer_count
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerCount') is not None:
            self.answer_count = m.get('AnswerCount')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListAnswerLibResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAnswerLibResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnswerLibResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAnswerLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnswerLibResponseBody = None,
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
            temp_model = ListAnswerLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallbackRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCallbackResponseBodyData(TeaModel):
    def __init__(
        self,
        crypt_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        scope: str = None,
        seed: str = None,
        uid: str = None,
        url: str = None,
    ):
        self.crypt_type = crypt_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.scope = scope
        # Seed。
        self.seed = seed
        # UID。
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListCallbackResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListCallbackResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCallbackResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCallbackResponseBody = None,
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
            temp_model = ListCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImageLibRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListImageLibResponseBodyLibList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        free_inspection: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_num: int = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        self.comment = comment
        self.free_inspection = free_inspection
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.image_num = image_num
        self.lib_id = lib_id
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.free_inspection is not None:
            result['FreeInspection'] = self.free_inspection
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_num is not None:
            result['ImageNum'] = self.image_num
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('FreeInspection') is not None:
            self.free_inspection = m.get('FreeInspection')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class ListImageLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        lib_list: List[ListImageLibResponseBodyLibList] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.lib_list = lib_list
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lib_list:
            for k in self.lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['LibList'] = []
        if self.lib_list is not None:
            for k in self.lib_list:
                result['LibList'].append(k.to_map() if k else None)
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.lib_list = []
        if m.get('LibList') is not None:
            for k in m.get('LibList'):
                temp_model = ListImageLibResponseBodyLibList()
                self.lib_list.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImageLibResponseBody = None,
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
            temp_model = ListImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesFromLibRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        img_id: str = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.img_id = img_id
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort = sort
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.img_id is not None:
            result['ImgId'] = self.img_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImgId') is not None:
            self.img_id = m.get('ImgId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ListImagesFromLibShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        img_id: str = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.img_id = img_id
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.img_id is not None:
            result['ImgId'] = self.img_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImgId') is not None:
            self.img_id = m.get('ImgId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ListImagesFromLibResponseBodyItems(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        image_id: str = None,
        image_url: str = None,
        thumbnail_url: str = None,
    ):
        self.gmt_create = gmt_create
        self.image_id = image_id
        self.image_url = image_url
        self.thumbnail_url = thumbnail_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        return self


class ListImagesFromLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        http_status_code: int = None,
        items: List[ListImagesFromLibResponseBodyItems] = None,
        msg: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.http_status_code = http_status_code
        self.items = items
        self.msg = msg
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListImagesFromLibResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesFromLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesFromLibResponseBody = None,
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
            temp_model = ListImagesFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeywordLibsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListKeywordLibsResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        keyword_count: str = None,
        lib_id: str = None,
        lib_name: str = None,
        service_codes: str = None,
        uid: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.keyword_count = keyword_count
        self.lib_id = lib_id
        self.lib_name = lib_name
        self.service_codes = service_codes
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.keyword_count is not None:
            result['KeywordCount'] = self.keyword_count
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('KeywordCount') is not None:
            self.keyword_count = m.get('KeywordCount')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListKeywordLibsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListKeywordLibsResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListKeywordLibsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListKeywordLibsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKeywordLibsResponseBody = None,
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
            temp_model = ListKeywordLibsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeywordsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        word: str = None,
    ):
        self.current_page = current_page
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort = sort
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class ListKeywordsShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
        word: str = None,
    ):
        self.current_page = current_page
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class ListKeywordsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        keyword_lib_id: str = None,
        keyword_md_5id: int = None,
        word: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.keyword_lib_id = keyword_lib_id
        self.keyword_md_5id = keyword_md_5id
        self.word = word

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
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keyword_md_5id is not None:
            result['KeywordMd5Id'] = self.keyword_md_5id
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('KeywordMd5Id') is not None:
            self.keyword_md_5id = m.get('KeywordMd5Id')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class ListKeywordsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[ListKeywordsResponseBodyDataItems] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListKeywordsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListKeywordsResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKeywordsResponseBody = None,
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
            temp_model = ListKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssCheckResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        finish_num: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
        start_date: str = None,
        status: int = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.finish_num = finish_num
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.sort = sort
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.finish_num is not None:
            result['FinishNum'] = self.finish_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FinishNum') is not None:
            self.finish_num = m.get('FinishNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOssCheckResultShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        finish_num: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
        status: int = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.finish_num = finish_num
        self.page_size = page_size
        self.query = query
        self.region_id = region_id
        self.sort_shrink = sort_shrink
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.finish_num is not None:
            result['FinishNum'] = self.finish_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FinishNum') is not None:
            self.finish_num = m.get('FinishNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOssCheckResultResponseBodyItems(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        code: str = None,
        content_type: str = None,
        copy_from: str = None,
        freeze_status: str = None,
        freeze_type: str = None,
        image_url: str = None,
        is_copy: bool = None,
        job_name: str = None,
        labels: List[str] = None,
        labels_2: List[str] = None,
        md_5: str = None,
        msg: str = None,
        object: str = None,
        risk_level: str = None,
        risk_level_0: str = None,
        risk_level_2: str = None,
        scan_result: str = None,
        service_code: str = None,
        service_name: str = None,
        task_id: str = None,
        url: str = None,
    ):
        self.bucket = bucket
        self.code = code
        self.content_type = content_type
        self.copy_from = copy_from
        self.freeze_status = freeze_status
        self.freeze_type = freeze_type
        self.image_url = image_url
        self.is_copy = is_copy
        self.job_name = job_name
        self.labels = labels
        self.labels_2 = labels_2
        self.md_5 = md_5
        self.msg = msg
        self.object = object
        self.risk_level = risk_level
        self.risk_level_0 = risk_level_0
        self.risk_level_2 = risk_level_2
        self.scan_result = scan_result
        self.service_code = service_code
        self.service_name = service_name
        self.task_id = task_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.code is not None:
            result['Code'] = self.code
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from
        if self.freeze_status is not None:
            result['FreezeStatus'] = self.freeze_status
        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.labels_2 is not None:
            result['Labels2'] = self.labels_2
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.object is not None:
            result['Object'] = self.object
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_level_0 is not None:
            result['RiskLevel0'] = self.risk_level_0
        if self.risk_level_2 is not None:
            result['RiskLevel2'] = self.risk_level_2
        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')
        if m.get('FreezeStatus') is not None:
            self.freeze_status = m.get('FreezeStatus')
        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Labels2') is not None:
            self.labels_2 = m.get('Labels2')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskLevel0') is not None:
            self.risk_level_0 = m.get('RiskLevel0')
        if m.get('RiskLevel2') is not None:
            self.risk_level_2 = m.get('RiskLevel2')
        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListOssCheckResultResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[ListOssCheckResultResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListOssCheckResultResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOssCheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOssCheckResultResponseBody = None,
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
            temp_model = ListOssCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceConfigsRequest(TeaModel):
    def __init__(
        self,
        classify: str = None,
        region_id: str = None,
        resource_type: str = None,
        use_status: str = None,
    ):
        self.classify = classify
        self.region_id = region_id
        self.resource_type = resource_type
        self.use_status = use_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.use_status is not None:
            result['UseStatus'] = self.use_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UseStatus') is not None:
            self.use_status = m.get('UseStatus')
        return self


class ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule(TeaModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule(TeaModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class ListServiceConfigsResponseBodyDataCustomServiceConfRules(TeaModel):
    def __init__(
        self,
        image_scan_rule: ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule = None,
        index: int = None,
        text_scan_rule: ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule = None,
    ):
        self.image_scan_rule = image_scan_rule
        self.index = index
        self.text_scan_rule = text_scan_rule

    def validate(self):
        if self.image_scan_rule:
            self.image_scan_rule.validate()
        if self.text_scan_rule:
            self.text_scan_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_scan_rule is not None:
            result['ImageScanRule'] = self.image_scan_rule.to_map()
        if self.index is not None:
            result['Index'] = self.index
        if self.text_scan_rule is not None:
            result['TextScanRule'] = self.text_scan_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanRule') is not None:
            temp_model = ListServiceConfigsResponseBodyDataCustomServiceConfRulesImageScanRule()
            self.image_scan_rule = temp_model.from_map(m['ImageScanRule'])
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('TextScanRule') is not None:
            temp_model = ListServiceConfigsResponseBodyDataCustomServiceConfRulesTextScanRule()
            self.text_scan_rule = temp_model.from_map(m['TextScanRule'])
        return self


class ListServiceConfigsResponseBodyDataCustomServiceConf(TeaModel):
    def __init__(
        self,
        audio_service: str = None,
        image_service: List[str] = None,
        keyword_filter_libs: List[str] = None,
        keyword_hit_libs: List[str] = None,
        rules: List[ListServiceConfigsResponseBodyDataCustomServiceConfRules] = None,
        similar_text_hit_libs: List[str] = None,
    ):
        self.audio_service = audio_service
        self.image_service = image_service
        self.keyword_filter_libs = keyword_filter_libs
        self.keyword_hit_libs = keyword_hit_libs
        self.rules = rules
        self.similar_text_hit_libs = similar_text_hit_libs

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_service is not None:
            result['AudioService'] = self.audio_service
        if self.image_service is not None:
            result['ImageService'] = self.image_service
        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs
        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.similar_text_hit_libs is not None:
            result['SimilarTextHitLibs'] = self.similar_text_hit_libs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioService') is not None:
            self.audio_service = m.get('AudioService')
        if m.get('ImageService') is not None:
            self.image_service = m.get('ImageService')
        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')
        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListServiceConfigsResponseBodyDataCustomServiceConfRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('SimilarTextHitLibs') is not None:
            self.similar_text_hit_libs = m.get('SimilarTextHitLibs')
        return self


class ListServiceConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        classify: str = None,
        copy_from: str = None,
        custom_service_conf: ListServiceConfigsResponseBodyDataCustomServiceConf = None,
        gmt_modified: str = None,
        option: Dict[str, Any] = None,
        resource_type: str = None,
        service_code: str = None,
        service_desc: str = None,
        service_name: str = None,
        service_type: str = None,
        uid: str = None,
        use_status: str = None,
    ):
        self.classify = classify
        self.copy_from = copy_from
        self.custom_service_conf = custom_service_conf
        self.gmt_modified = gmt_modified
        self.option = option
        self.resource_type = resource_type
        self.service_code = service_code
        self.service_desc = service_desc
        self.service_name = service_name
        self.service_type = service_type
        # UID。
        self.uid = uid
        self.use_status = use_status

    def validate(self):
        if self.custom_service_conf:
            self.custom_service_conf.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from
        if self.custom_service_conf is not None:
            result['CustomServiceConf'] = self.custom_service_conf.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.option is not None:
            result['Option'] = self.option
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_desc is not None:
            result['ServiceDesc'] = self.service_desc
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.use_status is not None:
            result['UseStatus'] = self.use_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')
        if m.get('CustomServiceConf') is not None:
            temp_model = ListServiceConfigsResponseBodyDataCustomServiceConf()
            self.custom_service_conf = temp_model.from_map(m['CustomServiceConf'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceDesc') is not None:
            self.service_desc = m.get('ServiceDesc')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UseStatus') is not None:
            self.use_status = m.get('UseStatus')
        return self


class ListServiceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListServiceConfigsResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListServiceConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListServiceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceConfigsResponseBody = None,
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
            temp_model = ListServiceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LlmStreamChatRequest(TeaModel):
    def __init__(
        self,
        messages: Any = None,
        temperature: float = None,
        top_p: float = None,
    ):
        self.messages = messages
        self.temperature = temperature
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.temperature is not None:
            result['Temperature'] = self.temperature
        if self.top_p is not None:
            result['TopP'] = self.top_p
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')
        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')
        return self


class LlmStreamChatResponseBodyChoicesDelta(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class LlmStreamChatResponseBodyChoices(TeaModel):
    def __init__(
        self,
        delta: LlmStreamChatResponseBodyChoicesDelta = None,
        finish_reason: str = None,
        index: int = None,
        logprobs: str = None,
    ):
        self.delta = delta
        self.finish_reason = finish_reason
        self.index = index
        self.logprobs = logprobs

    def validate(self):
        if self.delta:
            self.delta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delta is not None:
            result['Delta'] = self.delta.to_map()
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason
        if self.index is not None:
            result['Index'] = self.index
        if self.logprobs is not None:
            result['Logprobs'] = self.logprobs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delta') is not None:
            temp_model = LlmStreamChatResponseBodyChoicesDelta()
            self.delta = temp_model.from_map(m['Delta'])
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Logprobs') is not None:
            self.logprobs = m.get('Logprobs')
        return self


class LlmStreamChatResponseBodyError(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        param: str = None,
        type: str = None,
    ):
        self.code = code
        self.message = message
        self.param = param
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.param is not None:
            result['Param'] = self.param
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class LlmStreamChatResponseBody(TeaModel):
    def __init__(
        self,
        choices: List[LlmStreamChatResponseBodyChoices] = None,
        created: int = None,
        error: LlmStreamChatResponseBodyError = None,
        id: str = None,
        model: str = None,
        object: str = None,
        request_id: str = None,
        system_fingerprint: str = None,
        usage: str = None,
    ):
        self.choices = choices
        self.created = created
        self.error = error
        self.id = id
        self.model = model
        self.object = object
        self.request_id = request_id
        self.system_fingerprint = system_fingerprint
        self.usage = usage

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['Choices'].append(k.to_map() if k else None)
        if self.created is not None:
            result['Created'] = self.created
        if self.error is not None:
            result['Error'] = self.error.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.model is not None:
            result['Model'] = self.model
        if self.object is not None:
            result['Object'] = self.object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_fingerprint is not None:
            result['SystemFingerprint'] = self.system_fingerprint
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('Choices') is not None:
            for k in m.get('Choices'):
                temp_model = LlmStreamChatResponseBodyChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Error') is not None:
            temp_model = LlmStreamChatResponseBodyError()
            self.error = temp_model.from_map(m['Error'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemFingerprint') is not None:
            self.system_fingerprint = m.get('SystemFingerprint')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class LlmStreamChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LlmStreamChatResponseBody = None,
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
            temp_model = LlmStreamChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnswerLibRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.lib_name = lib_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAnswerLibResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAnswerLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAnswerLibResponseBody = None,
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
            temp_model = ModifyAnswerLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCallbackRequest(TeaModel):
    def __init__(
        self,
        crypt_type: str = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
        scope: str = None,
        url: str = None,
    ):
        self.crypt_type = crypt_type
        # This parameter is required.
        self.id = id
        self.name = name
        self.region_id = region_id
        self.scope = scope
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyCallbackResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCallbackResponseBody = None,
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
            temp_model = ModifyCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFeatureConfigRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        field: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        type: str = None,
    ):
        # Configuration, in JSON format
        self.config = config
        # Label meaning
        self.description = description
        # Label value, customer-defined
        self.field = field
        # Region
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.description is not None:
            result['Description'] = self.description
        if self.field is not None:
            result['Field'] = self.field
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyFeatureConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # Returned data
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message of this request.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyFeatureConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFeatureConfigResponseBody = None,
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
            temp_model = ModifyFeatureConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        service_desc: str = None,
        service_name: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code
        self.service_desc = service_desc
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_desc is not None:
            result['ServiceDesc'] = self.service_desc
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceDesc') is not None:
            self.service_desc = m.get('ServiceDesc')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModifyServiceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyServiceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyServiceInfoResponseBody = None,
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
            temp_model = ModifyServiceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAnswerSampleByPageRequest(TeaModel):
    def __init__(
        self,
        answer: str = None,
        current_page: int = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort: Dict[str, str] = None,
    ):
        self.answer = answer
        self.current_page = current_page
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class QueryAnswerSampleByPageShrinkRequest(TeaModel):
    def __init__(
        self,
        answer: str = None,
        current_page: int = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
    ):
        self.answer = answer
        self.current_page = current_page
        self.lib_id = lib_id
        self.page_size = page_size
        self.region_id = region_id
        self.sort_shrink = sort_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        return self


class QueryAnswerSampleByPageResponseBodyItems(TeaModel):
    def __init__(
        self,
        answer: str = None,
        gmt_create: str = None,
        id: int = None,
        lib_id: str = None,
        uid: str = None,
    ):
        self.answer = answer
        self.gmt_create = gmt_create
        self.id = id
        self.lib_id = lib_id
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryAnswerSampleByPageResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[QueryAnswerSampleByPageResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryAnswerSampleByPageResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAnswerSampleByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAnswerSampleByPageResponseBody = None,
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
            temp_model = QueryAnswerSampleByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallbackRequest(TeaModel):
    def __init__(
        self,
        check_for_oss: bool = None,
        id: int = None,
        region_id: str = None,
    ):
        self.check_for_oss = check_for_oss
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_for_oss is not None:
            result['CheckForOss'] = self.check_for_oss
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckForOss') is not None:
            self.check_for_oss = m.get('CheckForOss')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryCallbackResponseBody(TeaModel):
    def __init__(
        self,
        crypt_type: str = None,
        exists_oss_check_task: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        request_id: str = None,
        scope: str = None,
        seed: str = None,
        uid: str = None,
        url: str = None,
    ):
        self.crypt_type = crypt_type
        self.exists_oss_check_task = exists_oss_check_task
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.request_id = request_id
        self.scope = scope
        # Seed。
        self.seed = seed
        # UID。
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.exists_oss_check_task is not None:
            result['ExistsOssCheckTask'] = self.exists_oss_check_task
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('ExistsOssCheckTask') is not None:
            self.exists_oss_check_task = m.get('ExistsOssCheckTask')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallbackResponseBody = None,
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
            temp_model = QueryCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallbackByPageRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryCallbackByPageResponseBodyItems(TeaModel):
    def __init__(
        self,
        crypt_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        scope: str = None,
        seed: str = None,
        uid: str = None,
        url: str = None,
    ):
        self.crypt_type = crypt_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.scope = scope
        # Seed。
        self.seed = seed
        # UID。
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryCallbackByPageResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[QueryCallbackByPageResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryCallbackByPageResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCallbackByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallbackByPageResponseBody = None,
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
            temp_model = QueryCallbackByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupConfigRequest(TeaModel):
    def __init__(
        self,
        backup_config: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
    ):
        self.backup_config = backup_config
        self.region_id = region_id
        self.resource_type = resource_type
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_config is not None:
            result['BackupConfig'] = self.backup_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupConfig') is not None:
            self.backup_config = m.get('BackupConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class UpdateBackupConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBackupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBackupConfigResponseBody = None,
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
            temp_model = UpdateBackupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageLibRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        free_inspection: int = None,
        lib_id: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        self.comment = comment
        self.free_inspection = free_inspection
        self.lib_id = lib_id
        self.lib_name = lib_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.free_inspection is not None:
            result['FreeInspection'] = self.free_inspection
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('FreeInspection') is not None:
            self.free_inspection = m.get('FreeInspection')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateImageLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageLibResponseBody = None,
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
            temp_model = UpdateImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageLibFreeInspectionRequest(TeaModel):
    def __init__(
        self,
        config: Dict[str, int] = None,
        region_id: str = None,
    ):
        self.config = config
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateImageLibFreeInspectionShrinkRequest(TeaModel):
    def __init__(
        self,
        config_shrink: str = None,
        region_id: str = None,
    ):
        self.config_shrink = config_shrink
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateImageLibFreeInspectionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageLibFreeInspectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageLibFreeInspectionResponseBody = None,
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
            temp_model = UpdateImageLibFreeInspectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeywordLibRequest(TeaModel):
    def __init__(
        self,
        lib_id: str = None,
        lib_name: str = None,
        region_id: str = None,
    ):
        self.lib_id = lib_id
        self.lib_name = lib_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateKeywordLibResponseBody = None,
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
            temp_model = UpdateKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScanResultFeedbackRequest(TeaModel):
    def __init__(
        self,
        feedback: str = None,
        labels: str = None,
        query_request_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        risk_level: str = None,
    ):
        self.feedback = feedback
        self.labels = labels
        self.query_request_id = query_request_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class UpdateScanResultFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateScanResultFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateScanResultFeedbackResponseBody = None,
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
            temp_model = UpdateScanResultFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceConfigRequest(TeaModel):
    def __init__(
        self,
        file_config: str = None,
        keyword_filter_libs: str = None,
        keyword_hit_libs: str = None,
        manual_machine_config: str = None,
        region_id: str = None,
        resource_type: str = None,
        scene: str = None,
        scene_config: str = None,
        service_code: str = None,
        service_config: str = None,
        video_config: str = None,
    ):
        self.file_config = file_config
        self.keyword_filter_libs = keyword_filter_libs
        self.keyword_hit_libs = keyword_hit_libs
        self.manual_machine_config = manual_machine_config
        self.region_id = region_id
        self.resource_type = resource_type
        self.scene = scene
        self.scene_config = scene_config
        self.service_code = service_code
        self.service_config = service_config
        self.video_config = video_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_config is not None:
            result['FileConfig'] = self.file_config
        if self.keyword_filter_libs is not None:
            result['KeywordFilterLibs'] = self.keyword_filter_libs
        if self.keyword_hit_libs is not None:
            result['KeywordHitLibs'] = self.keyword_hit_libs
        if self.manual_machine_config is not None:
            result['ManualMachineConfig'] = self.manual_machine_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.scene_config is not None:
            result['SceneConfig'] = self.scene_config
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.video_config is not None:
            result['VideoConfig'] = self.video_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileConfig') is not None:
            self.file_config = m.get('FileConfig')
        if m.get('KeywordFilterLibs') is not None:
            self.keyword_filter_libs = m.get('KeywordFilterLibs')
        if m.get('KeywordHitLibs') is not None:
            self.keyword_hit_libs = m.get('KeywordHitLibs')
        if m.get('ManualMachineConfig') is not None:
            self.manual_machine_config = m.get('ManualMachineConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SceneConfig') is not None:
            self.scene_config = m.get('SceneConfig')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('VideoConfig') is not None:
            self.video_config = m.get('VideoConfig')
        return self


class UpdateServiceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateServiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceConfigResponseBody = None,
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
            temp_model = UpdateServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



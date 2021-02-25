# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict


class LivenessDetectRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_id: str = None,
        media_category: str = None,
        media_url: str = None,
        media_file: str = None,
    ):
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.media_category = media_category
        self.media_url = media_url
        self.media_file = media_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.media_category is not None:
            result['MediaCategory'] = self.media_category
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        if self.media_file is not None:
            result['MediaFile'] = self.media_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MediaCategory') is not None:
            self.media_category = m.get('MediaCategory')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        if m.get('MediaFile') is not None:
            self.media_file = m.get('MediaFile')
        return self


class LivenessDetectAdvanceRequest(TeaModel):
    def __init__(
        self,
        media_file_object: BinaryIO = None,
        biz_type: str = None,
        biz_id: str = None,
        media_category: str = None,
        media_url: str = None,
    ):
        self.media_file_object = media_file_object
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.media_category = media_category
        self.media_url = media_url

    def validate(self):
        self.validate_required(self.media_file_object, 'media_file_object')

    def to_map(self):
        result = dict()
        if self.media_file_object is not None:
            result['MediaFileObject'] = self.media_file_object
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.media_category is not None:
            result['MediaCategory'] = self.media_category
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaFileObject') is not None:
            self.media_file_object = m.get('MediaFileObject')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MediaCategory') is not None:
            self.media_category = m.get('MediaCategory')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        return self


class LivenessDetectResponseBodyResultObject(TeaModel):
    def __init__(
        self,
        score: float = None,
        frame_url: str = None,
        passed: str = None,
    ):
        self.score = score
        self.frame_url = frame_url
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.frame_url is not None:
            result['FrameUrl'] = self.frame_url
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('FrameUrl') is not None:
            self.frame_url = m.get('FrameUrl')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        return self


class LivenessDetectResponseBody(TeaModel):
    def __init__(
        self,
        result_object: LivenessDetectResponseBodyResultObject = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.result_object = result_object
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            temp_model = LivenessDetectResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class LivenessDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LivenessDetectResponseBody = None,
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
            temp_model = LivenessDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



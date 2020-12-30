# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict


class DetectVideoShotRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
    ):
        self.video_url = video_url
        self.async_ = async_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class DetectVideoShotAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        return self


class DetectVideoShotResponseBodyData(TeaModel):
    def __init__(
        self,
        shot_frame_ids: List[int] = None,
    ):
        self.shot_frame_ids = shot_frame_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.shot_frame_ids is not None:
            result['ShotFrameIds'] = self.shot_frame_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShotFrameIds') is not None:
            self.shot_frame_ids = m.get('ShotFrameIds')
        return self


class DetectVideoShotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DetectVideoShotResponseBodyData = None,
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
            temp_model = DetectVideoShotResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectVideoShotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectVideoShotResponseBody = None,
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
            temp_model = DetectVideoShotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoCoverRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        is_gif: bool = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.is_gif = is_gif

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.is_gif is not None:
            result['IsGif'] = self.is_gif
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('IsGif') is not None:
            self.is_gif = m.get('IsGif')
        return self


class GenerateVideoCoverAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        is_gif: bool = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.is_gif = is_gif

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.is_gif is not None:
            result['IsGif'] = self.is_gif
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('IsGif') is not None:
            self.is_gif = m.get('IsGif')
        return self


class GenerateVideoCoverResponseBodyDataOutputs(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        confidence: float = None,
    ):
        self.image_url = image_url
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class GenerateVideoCoverResponseBodyData(TeaModel):
    def __init__(
        self,
        outputs: List[GenerateVideoCoverResponseBodyDataOutputs] = None,
    ):
        self.outputs = outputs

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GenerateVideoCoverResponseBodyDataOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class GenerateVideoCoverResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GenerateVideoCoverResponseBodyData = None,
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
            temp_model = GenerateVideoCoverResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GenerateVideoCoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateVideoCoverResponseBody = None,
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
            temp_model = GenerateVideoCoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        job_id: str = None,
    ):
        self.async_ = async_
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        result: str = None,
        error_code: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.result = result
        self.error_code = error_code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseBodyData = None,
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
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncJobResultResponseBody = None,
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
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



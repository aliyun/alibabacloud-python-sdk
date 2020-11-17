# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import BinaryIO
except ImportError:
    pass


class LivenessDetectRequest(TeaModel):
    def __init__(self, biz_type=None, biz_id=None, media_category=None, media_url=None, media_file=None):
        self.biz_type = biz_type        # type: str
        self.biz_id = biz_id            # type: str
        self.media_category = media_category  # type: str
        self.media_url = media_url      # type: str
        self.media_file = media_file    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizId'] = self.biz_id
        result['MediaCategory'] = self.media_category
        result['MediaUrl'] = self.media_url
        result['MediaFile'] = self.media_file
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_id = map.get('BizId')
        self.media_category = map.get('MediaCategory')
        self.media_url = map.get('MediaUrl')
        self.media_file = map.get('MediaFile')
        return self


class LivenessDetectResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result_object=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.result_object = result_object  # type: LivenessDetectResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('ResultObject') is not None:
            temp_model = LivenessDetectResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class LivenessDetectResponseResultObject(TeaModel):
    def __init__(self, passed=None, score=None, frame_url=None):
        self.passed = passed            # type: str
        self.score = score              # type: float
        self.frame_url = frame_url      # type: str

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.score, 'score')
        self.validate_required(self.frame_url, 'frame_url')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['Score'] = self.score
        result['FrameUrl'] = self.frame_url
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.score = map.get('Score')
        self.frame_url = map.get('FrameUrl')
        return self


class LivenessDetectAdvanceRequest(TeaModel):
    def __init__(self, media_file_object=None, biz_type=None, biz_id=None, media_category=None, media_url=None):
        self.media_file_object = media_file_object  # type: BinaryIO
        self.biz_type = biz_type        # type: str
        self.biz_id = biz_id            # type: str
        self.media_category = media_category  # type: str
        self.media_url = media_url      # type: str

    def validate(self):
        self.validate_required(self.media_file_object, 'media_file_object')

    def to_map(self):
        result = {}
        result['MediaFileObject'] = self.media_file_object
        result['BizType'] = self.biz_type
        result['BizId'] = self.biz_id
        result['MediaCategory'] = self.media_category
        result['MediaUrl'] = self.media_url
        return result

    def from_map(self, map={}):
        self.media_file_object = map.get('MediaFileObject')
        self.biz_type = map.get('BizType')
        self.biz_id = map.get('BizId')
        self.media_category = map.get('MediaCategory')
        self.media_url = map.get('MediaUrl')
        return self

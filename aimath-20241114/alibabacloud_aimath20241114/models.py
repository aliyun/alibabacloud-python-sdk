# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class GenAnalysisRequest(TeaModel):
    def __init__(
        self,
        exercise_content: str = None,
    ):
        # This parameter is required.
        self.exercise_content = exercise_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exercise_content is not None:
            result['ExerciseContent'] = self.exercise_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExerciseContent') is not None:
            self.exercise_content = m.get('ExerciseContent')
        return self


class GenAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        err_code: str = None,
        err_msg: str = None,
        event_type: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.err_code = err_code
        self.err_msg = err_msg
        self.event_type = event_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenAnalysisResponseBody = None,
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
            temp_model = GenAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenStepRequest(TeaModel):
    def __init__(
        self,
        exercise_code: str = None,
    ):
        # This parameter is required.
        self.exercise_code = exercise_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exercise_code is not None:
            result['ExerciseCode'] = self.exercise_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExerciseCode') is not None:
            self.exercise_code = m.get('ExerciseCode')
        return self


class GenStepResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        err_code: str = None,
        err_msg: str = None,
        event_type: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.err_code = err_code
        self.err_msg = err_msg
        self.event_type = event_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenStepResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenStepResponseBody = None,
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
            temp_model = GenStepResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GlobalConfirmRequest(TeaModel):
    def __init__(
        self,
        exercise_code: str = None,
        tag: str = None,
    ):
        # This parameter is required.
        self.exercise_code = exercise_code
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exercise_code is not None:
            result['ExerciseCode'] = self.exercise_code
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExerciseCode') is not None:
            self.exercise_code = m.get('ExerciseCode')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GlobalConfirmResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GlobalConfirmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GlobalConfirmResponseBody = None,
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
            temp_model = GlobalConfirmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnalysisRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_code: str = None,
        exercise_code: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.content_code = content_code
        # This parameter is required.
        self.exercise_code = exercise_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_code is not None:
            result['ContentCode'] = self.content_code
        if self.exercise_code is not None:
            result['ExerciseCode'] = self.exercise_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCode') is not None:
            self.content_code = m.get('ContentCode')
        if m.get('ExerciseCode') is not None:
            self.exercise_code = m.get('ExerciseCode')
        return self


class UpdateAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAnalysisResponseBody = None,
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
            temp_model = UpdateAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStepRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_code: str = None,
        exercise_code: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.content_code = content_code
        # This parameter is required.
        self.exercise_code = exercise_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_code is not None:
            result['ContentCode'] = self.content_code
        if self.exercise_code is not None:
            result['ExerciseCode'] = self.exercise_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentCode') is not None:
            self.content_code = m.get('ContentCode')
        if m.get('ExerciseCode') is not None:
            self.exercise_code = m.get('ExerciseCode')
        return self


class UpdateStepResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.err_msg = err_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStepResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStepResponseBody = None,
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
            temp_model = UpdateStepResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


